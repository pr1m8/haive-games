"""Texas Hold'em Game Agent module - Main game coordinator and manager.

This module implements the core game management system for Texas Hold'em poker,
coordinating the game flow, player interactions, betting rounds, and showdowns.
It serves as the central orchestrator that manages the complete lifecycle of a
poker game from setup to completion.

Key features:
    - Complete poker game flow management with LangGraph
    - Betting round coordination and hand progression
    - Player action validation and processing
    - Pot management and chip tracking
    - Showdown evaluation and winner determination
    - Game state persistence and history tracking

The game agent creates and manages subgraph agents for each player, allowing them
to make independent decisions within the overall game context. It handles all
aspects of the game rules, ensuring proper sequencing of rounds and actions.

Example:
    >>> from haive.games.hold_em.game_agent import HoldemGameAgent
    >>> from haive.games.hold_em.config import create_default_holdem_config
    >>>
    >>> # Create a game configuration
    >>> config = create_default_holdem_config(num_players=4)
    >>>
    >>> # Initialize the game agent
    >>> agent = HoldemGameAgent(config)
    >>>
    >>> # Run the game
    >>> result = agent.app.invoke({}, debug=True)

Implementation details:
    - Enhanced player ID handling and validation
    - Robust error checking and recovery
    - Comprehensive logging for debugging
    - Fixed player lookup and identification
"""

import json
import logging
import random
import traceback
from typing import Any, Literal

from haive.core.engine.agent.agent import Agent, AgentConfig, register_agent
from haive.core.engine.aug_llm import AugLLMConfig
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command
from pydantic import Field

from haive.games.hold_em.player_agent import HoldemPlayerAgent, HoldemPlayerAgentConfig
from haive.games.hold_em.state import (
    GamePhase,
    HoldemState,
    PlayerState,
    PlayerStatus,
)

# Setup detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class HoldemGameAgentConfig(AgentConfig):
    """Configuration for the main Hold'em game agent.

    This configuration class defines the parameters for a Texas Hold'em
    game, including the number of players, blinds, starting chips, game
    limits, and player agent configurations. It encapsulates all the
    settings needed to initialize and run a complete poker game.

    The configuration serves as the blueprint for creating a
    HoldemGameAgent instance with specific game rules and player
    characteristics. It can be created directly or through helper
    functions in the config module.
    """

    state_schema: type = Field(default=HoldemState)

    # Game settings
    max_players: int = Field(default=6, description="Maximum players at table")
    small_blind: int = Field(default=10, description="Small blind amount")
    big_blind: int = Field(default=20, description="Big blind amount")
    starting_chips: int = Field(default=1000, description="Starting chips per player")
    max_hands: int = Field(default=50, description="Maximum hands to play")

    # Player configurations
    player_configs: list[HoldemPlayerAgentConfig] = Field(
        default_factory=list, description="Configurations for each player agent"
    )

    # Game engines (for dealing, evaluation, etc.)
    engines: dict[str, AugLLMConfig] = Field(
        default_factory=dict, description="Game management engines"
    )

    class Config:
        arbitrary_types_allowed = True


@register_agent(HoldemGameAgentConfig)
class HoldemGameAgent(Agent[HoldemGameAgentConfig]):
    """Main Texas Hold'em game agent that coordinates the complete poker game.

    This agent manages the entire lifecycle of a Texas Hold'em poker game,
    implementing all game rules, betting rounds, player actions, and hand evaluations.
    It creates and coordinates player subgraphs, manages the central game state,
    and ensures proper game flow from initial setup through the final showdown.

    The game progresses through the standard Texas Hold'em phases:
    1. Setup hand and post blinds
    2. Deal hole cards and run preflop betting
    3. Deal flop (3 community cards) and run flop betting
    4. Deal turn (4th community card) and run turn betting
    5. Deal river (5th community card) and run river betting
    6. Showdown evaluation and pot distribution
    7. Proceed to next hand or end game

    Between betting rounds, the agent routes the game flow based on the current
    state, handling special cases like all players folded or all-in situations.

    This version includes enhanced debugging capabilities, robust player ID handling,
    and comprehensive error recovery mechanisms.
    """

    def __init__(self, config: HoldemGameAgentConfig):
        super().__init__(config)

        # Debug tracking
        self.decision_log = []
        self.invocation_log = []
        self.error_log = []

        # Create player subgraph agents
        self.player_agents = {}
        self.setup_player_agents()

    def setup_player_agents(self):
        """Set up player subgraph agents with detailed logging.

        This method initializes a HoldemPlayerAgent instance for each player in the game
        based on the player configurations. It creates the independent decision-making
        subgraphs that will be invoked during betting rounds. The method includes
        comprehensive error handling and logging to ensure all agents are properly created.

        The player agents are stored in a dictionary keyed by player name for later
        retrieval during decision-making phases.

        Raises:
            RuntimeError: If any required player agent cannot be created successfully
        """
        logger.info(f"🎭 Setting up {len(self.config.player_configs)} player agents...")

        for player_config in self.config.player_configs:
            try:
                logger.info(f"Creating agent for {player_config.player_name}")
                player_agent = HoldemPlayerAgent(player_config)
                self.player_agents[player_config.player_name] = player_agent
                logger.info(
                    f"✅ Successfully created agent for {player_config.player_name}"
                )

                # Log agent configuration
                self.log_agent_config(player_config)

            except Exception as e:
                logger.error(
                    f"❌ Failed to create agent for {player_config.player_name}: {e}"
                )
                logger.error(traceback.format_exc())
                raise RuntimeError(
                    f"Failed to create required player agent for {player_config.player_name}: {e}"
                )

    def log_agent_config(self, player_config: HoldemPlayerAgentConfig):
        """Log detailed player agent configuration for debugging purposes.

        This method creates a structured representation of a player agent's configuration
        and logs it for debugging. It includes information about the player's style,
        risk tolerance, engines, and engine details such as models and output formats.

        Args:
            player_config (HoldemPlayerAgentConfig): The player configuration to log

        Returns:
            None: The configuration is logged to the logger
        """
        config_info = {
            "player_name": player_config.player_name,
            "player_style": player_config.player_style,
            "risk_tolerance": player_config.risk_tolerance,
            "engines": list(player_config.engines.keys()),
            "engine_details": {},
        }

        for engine_name, engine in player_config.engines.items():
            config_info["engine_details"][engine_name] = {
                "name": engine.name,
                "model": getattr(engine.llm_config, "model", "unknown"),
                "structured_output_model": (
                    engine.structured_output_model.__name__
                    if engine.structured_output_model
                    else None
                ),
                "force_tool_choice": engine.force_tool_choice,
            }

        logger.info(f"Player config: {json.dumps(config_info, indent=2)}")

    def setup_workflow(self):
        """Setup the main game workflow graph with all nodes and transitions.

        This method configures the complete LangGraph workflow for the poker game,
        defining all game phases, decision points, and conditional routing logic.
        It establishes the core game flow including:

        1. Game setup nodes: setup_hand, post_blinds, deal_hole_cards
        2. Betting round nodes: preflop_betting, flop_betting, turn_betting, river_betting
        3. Card dealing nodes: deal_flop, deal_turn, deal_river
        4. Game conclusion nodes: showdown, award_pot, check_game_end
        5. Player decision node: Invokes player subgraphs for decisions

        The graph includes conditional edges to route game flow based on the current
        state, such as proceeding to the next betting round or directly to showdown
        when appropriate. This creates a complete state machine for poker game flow.
        """
        logger.info("🔧 Setting up game workflow...")

        # Create state graph
        self.graph = StateGraph(self.config.state_schema)

        # Game setup and management nodes
        self.graph.add_node("setup_hand", self.setup_hand)
        self.graph.add_node("post_blinds", self.post_blinds)
        self.graph.add_node("deal_hole_cards", self.deal_hole_cards)

        # Betting round nodes
        self.graph.add_node("preflop_betting", self.preflop_betting)
        self.graph.add_node("deal_flop", self.deal_flop)
        self.graph.add_node("flop_betting", self.flop_betting)
        self.graph.add_node("deal_turn", self.deal_turn)
        self.graph.add_node("turn_betting", self.turn_betting)
        self.graph.add_node("deal_river", self.deal_river)
        self.graph.add_node("river_betting", self.river_betting)

        # Game conclusion
        self.graph.add_node("showdown", self.showdown)
        self.graph.add_node("award_pot", self.award_pot)
        self.graph.add_node("check_game_end", self.check_game_end)

        # Player decision node (this will call subgraphs)
        self.graph.add_node("player_decision", self.get_player_decision)

        # Set up the main flow
        self.graph.add_edge(START, "setup_hand")

        # Hand setup flow
        self.graph.add_edge("setup_hand", "post_blinds")
        self.graph.add_edge("post_blinds", "deal_hole_cards")
        self.graph.add_edge("deal_hole_cards", "preflop_betting")

        # Betting rounds with conditional routing
        self.graph.add_conditional_edges(
            "preflop_betting",
            self.route_after_betting,
            {
                "deal_flop": "deal_flop",
                "showdown": "showdown",
                "award_pot": "award_pot",
                "player_decision": "player_decision",
            },
        )

        self.graph.add_edge("deal_flop", "flop_betting")
        self.graph.add_conditional_edges(
            "flop_betting",
            self.route_after_betting,
            {
                "deal_turn": "deal_turn",
                "showdown": "showdown",
                "award_pot": "award_pot",
                "player_decision": "player_decision",
            },
        )

        self.graph.add_edge("deal_turn", "turn_betting")
        self.graph.add_conditional_edges(
            "turn_betting",
            self.route_after_betting,
            {
                "deal_river": "deal_river",
                "showdown": "showdown",
                "award_pot": "award_pot",
                "player_decision": "player_decision",
            },
        )

        self.graph.add_edge("deal_river", "river_betting")
        self.graph.add_conditional_edges(
            "river_betting",
            self.route_after_betting,
            {
                "showdown": "showdown",
                "award_pot": "award_pot",
                "player_decision": "player_decision",
            },
        )

        # End game flow
        self.graph.add_edge("showdown", "award_pot")
        self.graph.add_edge("award_pot", "check_game_end")

        self.graph.add_conditional_edges(
            "check_game_end",
            self.route_game_continuation,
            {"setup_hand": "setup_hand", "END": END},
        )

        logger.info("✅ Game workflow setup complete")

    def setup_hand(self, state: HoldemState) -> Command[Literal["post_blinds"]]:
        """Setup a new poker hand by initializing deck and player states.

        This node initializes a new hand by creating and shuffling a deck,
        resetting player states, advancing the dealer position, and setting up
        player positions around the table. It prepares all the necessary state
        for starting a new hand of poker.

        Args:
            state (HoldemState): The current game state

        Returns:
            Command: State update with new deck, reset community cards, pot, etc.

        Raises:
            RuntimeError: If hand setup fails due to errors
        """
        logger.info(f"\n🃏 Setting up hand #{state.hand_number}")

        try:
            # Create new deck
            deck = self._create_deck()
            random.shuffle(deck)
            logger.debug(f"Created and shuffled deck: {len(deck)} cards")

            # Reset player states for new hand
            for player in state.players:
                player.hole_cards = []
                player.current_bet = 0
                player.total_bet = 0
                player.actions_this_hand = []
                if player.status != PlayerStatus.OUT:
                    player.status = PlayerStatus.ACTIVE

            # Advance dealer position
            new_dealer_position = (state.dealer_position + 1) % len(state.players)
            logger.debug(f"New dealer position: {new_dealer_position}")

            # Set positions
            self._set_player_positions(state, new_dealer_position)

            logger.info(f"✅ Hand #{state.hand_number} setup complete")

            return Command(
                update={
                    "deck": deck,
                    "community_cards": [],
                    "burned_cards": [],
                    "pot": 0,
                    "side_pots": [],
                    "current_bet": 0,
                    "min_raise": state.big_blind,
                    "current_phase": GamePhase.PREFLOP,
                    "actions_this_round": [],
                    "betting_round_complete": False,
                    "winner": None,
                    "error_message": None,
                    "dealer_position": new_dealer_position,
                }
            )

        except Exception as e:
            logger.error(f"❌ Hand setup error: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Hand setup failed: {e!s}")

    def post_blinds(self, state: HoldemState) -> Command[Literal["deal_hole_cards"]]:
        """Post small and big blinds to start the betting.

        This node identifies the small blind and big blind players based on
        their positions, collects the blind amounts from them, and adds these
        amounts to the pot. If a player doesn't have enough chips for their blind,
        they go all-in with their remaining chips.

        Args:
            state (HoldemState): The current game state

        Returns:
            Command: State update with updated pot, player chips, and actions

        Raises:
            RuntimeError: If blind players cannot be found or posting fails
        """
        logger.info("💰 Posting blinds...")

        try:
            # Find blind positions
            small_blind_player = None
            big_blind_player = None

            for player in state.players:
                if player.is_small_blind:
                    small_blind_player = player
                elif player.is_big_blind:
                    big_blind_player = player

            if not small_blind_player or not big_blind_player:
                raise RuntimeError("Could not find blind players")

            logger.debug(
                f"Small blind: {small_blind_player.name}, Big blind: {big_blind_player.name}"
            )

            # Post blinds
            small_blind_amount = min(state.small_blind, small_blind_player.chips)
            big_blind_amount = min(state.big_blind, big_blind_player.chips)

            small_blind_player.chips -= small_blind_amount
            small_blind_player.current_bet = small_blind_amount
            small_blind_player.total_bet = small_blind_amount

            big_blind_player.chips -= big_blind_amount
            big_blind_player.current_bet = big_blind_amount
            big_blind_player.total_bet = big_blind_amount

            # Set all-in if necessary
            if small_blind_player.chips == 0:
                small_blind_player.status = PlayerStatus.ALL_IN
                logger.debug(f"{small_blind_player.name} is all-in on small blind")
            if big_blind_player.chips == 0:
                big_blind_player.status = PlayerStatus.ALL_IN
                logger.debug(f"{big_blind_player.name} is all-in on big blind")

            pot = small_blind_amount + big_blind_amount
            current_bet = big_blind_amount

            # Record actions
            actions = [
                {
                    "player_id": small_blind_player.player_id,
                    "action": "post_small_blind",
                    "amount": small_blind_amount,
                    "phase": "preflop",
                },
                {
                    "player_id": big_blind_player.player_id,
                    "action": "post_big_blind",
                    "amount": big_blind_amount,
                    "phase": "preflop",
                },
            ]

            logger.info(
                f"💰 Blinds posted: SB {small_blind_amount}, BB {big_blind_amount}, Pot: {pot}"
            )

            return Command(
                update={
                    "pot": pot,
                    "current_bet": current_bet,
                    "actions_this_round": actions,
                }
            )

        except Exception as e:
            logger.error(f"❌ Posting blinds error: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Posting blinds failed: {e!s}")

    def deal_hole_cards(
        self, state: HoldemState
    ) -> Command[Literal["preflop_betting"]]:
        """Deal two hole cards to each active player in the game.

        This node deals two private cards to each active player from the deck,
        and determines the first player to act in the preflop betting round.
        For standard games, the first player to act is the one after the big blind.

        Args:
            state (HoldemState): The current game state

        Returns:
            Command: State update with updated deck, player hole cards, and
                     the index of the first player to act

        Raises:
            RuntimeError: If there aren't enough cards or dealing fails
        """
        logger.info("🎴 Dealing hole cards...")

        try:
            deck = state.deck.copy()
            cards_dealt = 0

            # Deal 2 cards to each active player
            for player in state.players:
                if player.status in [PlayerStatus.ACTIVE, PlayerStatus.ALL_IN]:
                    if len(deck) >= 2:
                        player.hole_cards = [deck.pop(), deck.pop()]
                        cards_dealt += 2
                        logger.debug(f"Dealt {player.hole_cards} to {player.name}")
                    else:
                        raise RuntimeError(f"Not enough cards to deal to {player.name}")

            logger.info(
                f"🎴 Dealt hole cards to {len([p for p in state.players if p.hole_cards])} players ({cards_dealt} cards)"
            )

            # Set first player to act (after big blind)
            big_blind_pos = next(
                (i for i, p in enumerate(state.players) if p.is_big_blind), 0
            )
            first_to_act = (big_blind_pos + 1) % len(state.players)

            # Find next active player
            attempts = 0
            while (
                attempts < len(state.players)
                and state.players[first_to_act].status != PlayerStatus.ACTIVE
            ):
                first_to_act = (first_to_act + 1) % len(state.players)
                attempts += 1

            logger.debug(
                f"First to act: {state.players[first_to_act].name} (position {first_to_act})"
            )

            return Command(update={"deck": deck, "current_player_index": first_to_act})

        except Exception as e:
            logger.error(f"❌ Dealing hole cards error: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Dealing hole cards failed: {e!s}")

    def get_player_decision(self, state: HoldemState) -> Command:
        """Get decision from current player using their subgraph agent.

        This is a critical node that invokes the current player's subgraph agent
        to get their poker decision (fold, check, call, bet, raise, or all-in).
        The method performs extensive validation of player IDs and provides detailed
        debugging information to track the decision process.

        The workflow:
        1. Identifies the current player and validates their player_id
        2. Prepares input for the player's subgraph agent
        3. Invokes the player agent with the game state and player ID
        4. Receives the decision and applies it to the game state

        Enhanced debug features include:
        - Comprehensive player ID validation and repair
        - Detailed logging of decision context and results
        - Error tracking with comprehensive context

        Args:
            state (HoldemState): The current game state

        Returns:
            Command: State update based on the player's action

        Raises:
            RuntimeError: If player lookup fails or decision-making fails
        """
        # Ensure we have proper state object
        if isinstance(state, dict):
            state = HoldemState.model_validate(state)

        # Enhanced logging for state debugging
        logger.info("\n🔍 DEBUGGING PLAYER DECISION:")
        logger.info(f"   State type: {type(state)}")
        logger.info(f"   Current player index: {state.current_player_index}")
        logger.info(f"   Total players: {len(state.players)}")

        # Log all players and their IDs
        logger.info("   All players:")
        for i, player in enumerate(state.players):
            logger.info(
                f"     [{i}] Name: '{player.name}', ID: '{player.player_id}', Status: {player.status}"
            )

        # Get current player with better error handling
        current_player = state.current_player

        if not current_player:
            logger.warning(
                "⚠️ No current player found - attempting to find next active player"
            )
            # Try to find any active player
            for i, player in enumerate(state.players):
                if player.status == PlayerStatus.ACTIVE:
                    logger.info(f"🔧 Found active player: {player.name} at index {i}")
                    state.current_player_index = i
                    current_player = player
                    break

            if not current_player:
                logger.error("❌ No active players found!")
                return self._advance_or_complete_betting(state)

        # ENHANCED: Validate player_id and fix if necessary
        logger.info("🎯 Current player details:")
        logger.info(f"   Name: '{current_player.name}'")
        logger.info(f"   Original ID: '{current_player.player_id}'")
        logger.info(f"   Position: {current_player.position}")
        logger.info(f"   Status: {current_player.status}")
        logger.info(f"   Chips: {current_player.chips}")

        # CRITICAL FIX: Validate and fix player_id
        if not current_player.player_id or current_player.player_id.strip() == "":
            logger.error(
                f"❌ Current player {current_player.name} has empty player_id!"
            )

            # Try multiple strategies to fix the player_id
            fixed_player_id = None

            # Strategy 1: Use position-based ID
            position_based_id = f"player_{current_player.position}"
            logger.warning(
                f"🔧 Strategy 1: Trying position-based ID: '{position_based_id}'"
            )

            # Strategy 2: Find the player in player_configs by name
            for i, player_config in enumerate(self.config.player_configs):
                if player_config.player_name == current_player.name:
                    config_based_id = f"player_{i}"
                    logger.warning(
                        f"🔧 Strategy 2: Found in config at index {i}, ID: '{config_based_id}'"
                    )
                    fixed_player_id = config_based_id
                    break

            # Strategy 3: Use the position-based ID as fallback
            if not fixed_player_id:
                fixed_player_id = position_based_id

            logger.warning(f"🔧 Applying fix: setting player_id to '{fixed_player_id}'")
            current_player.player_id = fixed_player_id

            # Update the player in the state as well
            for i, player in enumerate(state.players):
                if player.name == current_player.name:
                    state.players[i].player_id = fixed_player_id
                    logger.info(f"✅ Updated player_id in state for {player.name}")
                    break

        # Final validation
        if not current_player.player_id or current_player.player_id.strip() == "":
            error_msg = f"Failed to fix empty player_id for {current_player.name}"
            logger.error(f"❌ {error_msg}")
            raise RuntimeError(error_msg)

        logger.info(f"✅ Final player_id: '{current_player.player_id}'")

        # Log decision context
        logger.info(
            f"🎯 Getting decision from {current_player.name} (ID: {current_player.player_id})"
        )
        logger.info(f"   Position: {current_player.position}")
        logger.info(f"   Chips: {current_player.chips}")
        logger.info(f"   Current bet: {current_player.current_bet}")
        logger.info(
            f"   To call: {max(0, state.current_bet - current_player.current_bet)}"
        )
        logger.info(f"   Hole cards: {current_player.hole_cards}")

        # Get the player agent
        player_agent = self.player_agents.get(current_player.name)
        if not player_agent:
            error_msg = f"No player agent found for {current_player.name}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"   Available agents: {list(self.player_agents.keys())}")
            raise RuntimeError(error_msg)

        try:
            # Prepare input for player subgraph
            game_state_dict = state.model_dump()

            # CRITICAL: Ensure player_id is properly set in the input
            player_input = {
                "game_state": game_state_dict,
                "player_id": current_player.player_id,  # This should now be valid
            }

            # Final validation of the input
            if not player_input["player_id"] or player_input["player_id"].strip() == "":
                raise RuntimeError(
                    f"Player ID is still empty for {current_player.name} after all fixes"
                )

            # Enhanced logging of invocation details
            invocation_details = {
                "player_name": current_player.name,
                "player_id": current_player.player_id,
                "hand_number": state.hand_number,
                "phase": state.current_phase.value,
                "pot": state.total_pot,
                "current_bet": state.current_bet,
                "player_chips": current_player.chips,
                "hole_cards": current_player.hole_cards,
                "community_cards": state.community_cards,
                "players_in_hand": [p.name for p in state.players_in_hand],
                "input_validation": {
                    "game_state_keys": (
                        list(game_state_dict.keys()) if game_state_dict else []
                    ),
                    "player_id_length": len(player_input["player_id"]),
                    "player_id_valid": bool(player_input["player_id"].strip()),
                },
            }

            logger.info(f"🤖 Invoking player agent for {current_player.name}")
            logger.debug(
                f"Invocation details: {json.dumps(invocation_details, indent=2, default=str)}"
            )

            self.invocation_log.append(invocation_details)

            # Invoke with enhanced error handling
            logger.info("🔄 About to invoke player agent...")
            player_result = player_agent.app.invoke(player_input, debug=True)
            logger.info("✅ Player agent returned successfully")

            # Rest of the method remains the same...
            # [Continue with existing result processing logic]

            if not isinstance(player_result, dict):
                error_msg = (
                    f"Unexpected result type from player agent: {type(player_result)}"
                )
                logger.error(f"❌ {error_msg}")
                raise RuntimeError(error_msg)

            decision = player_result.get("decision")

            if not decision:
                error_msg = f"No decision in result from {current_player.name}"
                logger.error(f"❌ {error_msg}")
                logger.error(f"Full result: {player_result}")
                raise RuntimeError(error_msg)

            # Log the decision
            decision_details = {
                "player_name": current_player.name,
                "hand_number": state.hand_number,
                "phase": state.current_phase.value,
                "decision": decision,
                "game_context": {
                    "pot": state.total_pot,
                    "current_bet": state.current_bet,
                    "call_amount": max(
                        0, state.current_bet - current_player.current_bet
                    ),
                    "player_chips": current_player.chips,
                },
            }

            logger.info(
                f"🎯 {current_player.name} decision: {decision.get('action', 'unknown')}"
            )
            if decision.get("amount", 0) > 0:
                logger.info(f"   Amount: {decision['amount']}")
            reasoning = decision.get("reasoning", "No reasoning provided")
            logger.info(
                f"   Reasoning: {reasoning[:100]}{'...' if len(reasoning) > 100 else ''}"
            )

            self.decision_log.append(decision_details)

            # Apply the action
            return self._apply_player_action(state, current_player, decision)

        except Exception as e:
            error_details = {
                "player_name": current_player.name,
                "player_id": current_player.player_id,
                "error": str(e),
                "traceback": traceback.format_exc(),
                "hand_number": state.hand_number,
                "phase": state.current_phase.value,
                "debug_context": {
                    "state_type": str(type(state)),
                    "current_player_index": state.current_player_index,
                    "total_players": len(state.players),
                    "player_agents_available": list(self.player_agents.keys()),
                },
            }

            logger.error(
                f"❌ Critical error in get_player_decision for {current_player.name}: {e!s}"
            )
            logger.error(f"   Stack trace: {traceback.format_exc()}")

            self.error_log.append(error_details)

            # Re-raise the error with enhanced context
            raise RuntimeError(
                f"Player decision failed for {current_player.name}: {e!s}"
            )

    def _apply_player_action(
        self, state: HoldemState, player: PlayerState, decision: dict[str, Any]
    ) -> Command:
        """Apply a player's action to the game state and update chips and pot.

        This method processes a player's poker decision, updating the game state
        according to the chosen action (fold, check, call, bet, raise, or all-in).
        It modifies player chips, current bets, pot size, and player status as needed.

        The method also handles edge cases like:
        - Forcing call when player tries to check but there's a bet
        - Forcing fold when player can't meet the minimum call amount
        - Converting raise to all-in when player has insufficient chips
        - Treating unknown actions as fold for safety

        Args:
            state (HoldemState): The current game state
            player (PlayerState): The player making the action
            decision (Dict[str, Any]): The decision from the player agent

        Returns:
            Command: Game state update with the action applied and next player set

        Raises:
            RuntimeError: If action application fails due to errors
        """
        action = decision.get("action", "fold")
        amount = decision.get("amount", 0)

        logger.info(f"   🔧 Applying action: {action} {amount if amount > 0 else ''}")

        try:
            # Record the action
            action_record = {
                "player_id": player.player_id,
                "action": action,
                "amount": amount,
                "phase": state.current_phase.value,
                "reasoning": decision.get("reasoning", ""),
            }

            # Apply the action logic
            if action == "fold":
                player.status = PlayerStatus.FOLDED
                logger.info(f"   ✋ {player.name} folds")

            elif action == "check":
                if state.current_bet > player.current_bet:
                    # Can't check if there's a bet to call
                    call_amount = state.current_bet - player.current_bet
                    if call_amount <= player.chips:
                        # Force call
                        action = "call"
                        amount = call_amount
                        action_record["action"] = "call"
                        action_record["amount"] = amount
                        self._apply_call(player, state, call_amount)
                        logger.info(
                            f"   ☎️ {player.name} calls {call_amount} (forced from check)"
                        )
                    else:
                        # Force fold
                        player.status = PlayerStatus.FOLDED
                        action_record["action"] = "fold"
                        action_record["amount"] = 0
                        logger.info(f"   ✋ {player.name} folds (forced from check)")
                else:
                    logger.info(f"   ✅ {player.name} checks")

            elif action == "call":
                call_amount = min(
                    amount, state.current_bet - player.current_bet, player.chips
                )
                self._apply_call(player, state, call_amount)
                action_record["amount"] = call_amount
                if player.chips == 0:
                    player.status = PlayerStatus.ALL_IN
                    logger.info(f"   ☎️ {player.name} calls {call_amount} (ALL-IN)")
                else:
                    logger.info(f"   ☎️ {player.name} calls {call_amount}")

            elif action == "bet":
                if state.current_bet > 0:
                    # Already a bet, this should be a raise
                    action = "raise"
                    action_record["action"] = "raise"

                bet_amount = min(amount, player.chips)
                self._apply_bet_raise(player, state, bet_amount)
                action_record["amount"] = bet_amount

                if player.chips == 0:
                    player.status = PlayerStatus.ALL_IN
                    logger.info(f"   💰 {player.name} bets {bet_amount} (ALL-IN)")
                else:
                    logger.info(f"   💰 {player.name} bets {bet_amount}")

            elif action == "raise":
                # Calculate total amount needed
                call_amount = state.current_bet - player.current_bet
                raise_amount = max(0, amount - call_amount)
                total_amount = call_amount + raise_amount

                if total_amount > player.chips:
                    total_amount = player.chips
                    action = "all_in"
                    action_record["action"] = "all_in"

                self._apply_bet_raise(player, state, total_amount)
                action_record["amount"] = total_amount

                if player.chips == 0:
                    player.status = PlayerStatus.ALL_IN
                    logger.info(
                        f"   ⬆️ {player.name} raises to {player.current_bet} (ALL-IN)"
                    )
                else:
                    logger.info(f"   ⬆️ {player.name} raises to {player.current_bet}")

            elif action == "all_in":
                all_in_amount = player.chips
                self._apply_bet_raise(player, state, all_in_amount)
                player.status = PlayerStatus.ALL_IN
                action_record["amount"] = all_in_amount
                logger.info(f"   🚀 {player.name} goes ALL-IN for {all_in_amount}")

            else:
                logger.warning(f"⚠️ Unknown action: {action}, treating as fold")
                player.status = PlayerStatus.FOLDED
                action_record["action"] = "fold"
                action_record["amount"] = 0

            # Add action to player's hand history
            player.actions_this_hand.append(action_record)

            # Log current game state after action
            logger.info("   📊 Game state after action:")
            logger.info(f"      Pot: {state.total_pot}")
            logger.info(f"      Current bet: {state.current_bet}")
            logger.info(f"      Players in hand: {len(state.players_in_hand)}")
            logger.info(
                f"      Active players: {len([p for p in state.players_in_hand if p.status == PlayerStatus.ACTIVE])}"
            )

            # Advance to next player or complete betting
            return self._advance_or_complete_betting_with_action(state, action_record)

        except Exception as e:
            logger.error(f"❌ Error applying action: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Applying action failed: {e!s}")

    # Helper methods (keeping the existing implementations)
    def _create_deck(self) -> list[str]:
        """Create a standard 52-card deck."""
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        suits = ["h", "d", "c", "s"]
        return [f"{rank}{suit}" for rank in ranks for suit in suits]

    def _set_player_positions(self, state: HoldemState, dealer_pos: int):
        """Set player positions for the hand."""
        num_players = len(state.players)

        # Reset position flags
        for player in state.players:
            player.is_dealer = False
            player.is_small_blind = False
            player.is_big_blind = False

        # Set dealer
        state.players[dealer_pos].is_dealer = True

        # Set blinds
        if num_players == 2:
            # Heads up: dealer is small blind
            state.players[dealer_pos].is_small_blind = True
            state.players[(dealer_pos + 1) % num_players].is_big_blind = True
        else:
            # Normal: small blind after dealer, big blind after small
            state.players[(dealer_pos + 1) % num_players].is_small_blind = True
            state.players[(dealer_pos + 2) % num_players].is_big_blind = True

    def _apply_call(self, player: PlayerState, state: HoldemState, call_amount: int):
        """Apply a call action."""
        player.chips -= call_amount
        player.current_bet += call_amount
        player.total_bet += call_amount
        state.pot += call_amount

    def _apply_bet_raise(
        self, player: PlayerState, state: HoldemState, bet_amount: int
    ):
        """Apply a bet or raise action."""
        player.chips -= bet_amount
        player.current_bet += bet_amount
        player.total_bet += bet_amount
        state.pot += bet_amount
        state.current_bet = player.current_bet
        state.min_raise = bet_amount

    def _advance_or_complete_betting_with_action(
        self, state: HoldemState, action_record: dict[str, Any]
    ) -> Command:
        """Advance betting after applying an action."""
        # Check if betting is complete
        if state.is_betting_complete():
            logger.info("   ✅ Betting round complete")
            return Command(
                update={
                    "actions_this_round": [action_record],
                    "last_action": action_record,
                    "betting_round_complete": True,
                }
            )

        # Advance to next player
        next_player_index = state.advance_to_next_player()
        if next_player_index is None:
            next_player_index = state.current_player_index

        next_player = state.players[next_player_index]
        logger.info(f"   ➡️ Next to act: {next_player.name}")

        return Command(
            update={
                "actions_this_round": [action_record],
                "last_action": action_record,
                "current_player_index": next_player_index,
            }
        )

    def _advance_or_complete_betting(self, state: HoldemState) -> Command:
        """Advance to next player or complete betting round."""
        # Advance to next player
        next_player_index = state.advance_to_next_player()

        if next_player_index is None or state.is_betting_complete():
            # Betting complete
            return Command(update={"betting_round_complete": True})
        # Continue with next player
        return Command(update={"current_player_index": next_player_index})

    # Rest of the methods (abbreviated for space but same as original)
    def preflop_betting(self, state: HoldemState) -> Command:
        """Handle preflop betting round."""
        logger.info("🎲 Preflop betting round")
        return self._handle_betting_round(state, "preflop")

    def flop_betting(self, state: HoldemState) -> Command:
        """Handle flop betting round."""
        logger.info("🎲 Flop betting round")
        return self._handle_betting_round(state, "flop")

    def turn_betting(self, state: HoldemState) -> Command:
        """Handle turn betting round."""
        logger.info("🎲 Turn betting round")
        return self._handle_betting_round(state, "turn")

    def river_betting(self, state: HoldemState) -> Command:
        """Handle river betting round."""
        logger.info("🎲 River betting round")
        return self._handle_betting_round(state, "river")

    def _handle_betting_round(self, state: HoldemState, round_name: str) -> Command:
        """Handle a betting round."""
        # Check if betting is complete
        if state.is_betting_complete():
            logger.info(f"   ✅ {round_name} betting complete")
            return Command(update={"betting_round_complete": True})

        # Get current player
        current_player = state.current_player
        if not current_player:
            logger.warning(f"   ⚠️ No current player in {round_name} betting")
            return Command(update={"betting_round_complete": True})

        # Route to player decision
        return Command()

    def deal_flop(self, state: HoldemState) -> Command[Literal["flop_betting"]]:
        """Deal the flop (3 community cards)."""
        return self._deal_community_cards(state, 3, GamePhase.FLOP, "flop_betting")

    def deal_turn(self, state: HoldemState) -> Command[Literal["turn_betting"]]:
        """Deal the turn (4th community card)."""
        return self._deal_community_cards(state, 1, GamePhase.TURN, "turn_betting")

    def deal_river(self, state: HoldemState) -> Command[Literal["river_betting"]]:
        """Deal the river (5th community card)."""
        return self._deal_community_cards(state, 1, GamePhase.RIVER, "river_betting")

    def _deal_community_cards(
        self, state: HoldemState, num_cards: int, phase: GamePhase, next_node: str
    ) -> Command:
        """Deal community cards to the board, with burn card.

        This helper method handles dealing community cards for the flop, turn, or river.
        It burns one card first (discards it face down), then deals the specified number
        of cards to the board. It also resets betting for the new round and determines
        the first player to act.

        Args:
            state (HoldemState): The current game state
            num_cards (int): Number of cards to deal (3 for flop, 1 for turn/river)
            phase (GamePhase): The new game phase to set
            next_node (str): The next node to transition to

        Returns:
            Command: State update with new community cards, game phase, and
                     reset betting information

        Raises:
            RuntimeError: If card dealing fails
        """
        try:
            deck = state.deck.copy()
            community_cards = state.community_cards.copy()
            burned_cards = state.burned_cards.copy()

            # Burn a card
            if deck:
                burned_cards.append(deck.pop())

            # Deal community cards
            new_cards = []
            for _ in range(num_cards):
                if deck:
                    card = deck.pop()
                    community_cards.append(card)
                    new_cards.append(card)

            logger.info(f"🎴 Dealt {num_cards} community cards: {new_cards}")
            logger.info(f"   Board: {community_cards}")

            # Reset betting for new round
            for player in state.players:
                player.current_bet = 0

            # First to act is first active player after dealer
            dealer_pos = state.dealer_position
            first_to_act = (dealer_pos + 1) % len(state.players)

            # Find next active player
            attempts = 0
            while (
                attempts < len(state.players)
                and state.players[first_to_act].status != PlayerStatus.ACTIVE
            ):
                first_to_act = (first_to_act + 1) % len(state.players)
                attempts += 1

            logger.debug(f"First to act: {state.players[first_to_act].name}")

            return Command(
                update={
                    "deck": deck,
                    "community_cards": community_cards,
                    "burned_cards": burned_cards,
                    "current_phase": phase,
                    "current_bet": 0,
                    "current_player_index": first_to_act,
                    "actions_this_round": [],
                    "betting_round_complete": False,
                }
            )

        except Exception as e:
            logger.error(f"❌ Dealing community cards error: {e}")
            raise RuntimeError(f"Dealing community cards failed: {e!s}")

    def showdown(self, state: HoldemState) -> Command[Literal["award_pot"]]:
        """Handle showdown - evaluate player hands and determine the winner.

        This node evaluates the hand of each player still in the game (not folded)
        and determines the winner based on hand strength. In case only one player
        remains, that player automatically wins. Otherwise, all qualifying hands
        are compared to find the strongest.

        The current implementation uses a simplified hand evaluation algorithm,
        which would be replaced by a more sophisticated poker hand evaluator
        in a production version.

        Args:
            state (HoldemState): The current game state

        Returns:
            Command: State update with the winner's player ID

        Raises:
            RuntimeError: If showdown evaluation fails
        """
        logger.info("🏆 Showdown!")

        try:
            players_in_showdown = [
                p
                for p in state.players_in_hand
                if p.status in [PlayerStatus.ACTIVE, PlayerStatus.ALL_IN]
            ]

            logger.info(f"Players in showdown: {[p.name for p in players_in_showdown]}")

            if len(players_in_showdown) <= 1:
                winner = players_in_showdown[0] if players_in_showdown else None
                winner_id = winner.player_id if winner else None
                logger.info(
                    f"🏆 Winner by elimination: {winner.name if winner else 'None'}"
                )
                return Command(update={"winner": winner_id})

            # Simple hand evaluation (placeholder)
            hand_rankings = []
            for player in players_in_showdown:
                hand_strength = self._evaluate_hand_simple(
                    player.hole_cards, state.community_cards
                )
                hand_rankings.append((player, hand_strength))
                logger.info(f"   {player.name}: {player.hole_cards} = {hand_strength}")

            # Sort by hand strength (higher is better)
            hand_rankings.sort(key=lambda x: x[1], reverse=True)
            winner = hand_rankings[0][0]

            logger.info(f"🏆 Showdown winner: {winner.name}")

            return Command(update={"winner": winner.player_id})

        except Exception as e:
            logger.error(f"❌ Showdown error: {e}")
            raise RuntimeError(f"Showdown failed: {e!s}")

    def award_pot(self, state: HoldemState) -> Command[Literal["check_game_end"]]:
        """Award the pot to the winner and record hand history.

        This node adds the pot to the winner's chip stack and records the completed
        hand in the game history. If no winner is explicitly determined (e.g., from
        showdown), it finds the last remaining player as the winner.

        The hand history is recorded with details about the hand number, winner,
        pot size, community cards, and betting actions for later analysis.

        Args:
            state (HoldemState): The current game state

        Returns:
            Command: State update with winner's updated chips and hand history,
                     and incremented hand number

        Raises:
            RuntimeError: If pot awarding fails
        """
        logger.info("💰 Awarding pot...")

        try:
            winner_id = state.winner
            if not winner_id:
                # Find last remaining player
                players_in_hand = state.players_in_hand
                if players_in_hand:
                    winner_id = players_in_hand[0].player_id

            if winner_id:
                winner = state.get_player_by_id(winner_id)
                if winner:
                    winner.chips += state.total_pot
                    logger.info(
                        f"💰 {winner.name} wins {state.total_pot} chips (now has {winner.chips})"
                    )

            # Record hand in history
            hand_record = {
                "hand_number": state.hand_number,
                "winner": winner_id,
                "pot_size": state.total_pot,
                "community_cards": state.community_cards,
                "actions": state.actions_this_round,
            }

            return Command(
                update={
                    "hand_history": [hand_record],
                    "hand_number": state.hand_number + 1,
                }
            )

        except Exception as e:
            logger.error(f"❌ Awarding pot error: {e}")
            raise RuntimeError(f"Awarding pot failed: {e!s}")

    def check_game_end(self, state: HoldemState) -> Command:
        """Check if the game should end."""
        try:
            # Check win conditions
            players_with_chips = [p for p in state.players if p.chips > 0]

            if len(players_with_chips) <= 1:
                logger.info("🎉 Game over - only one player remaining!")
                self._save_debug_logs()
                return Command(update={"game_over": True})

            if state.hand_number > self.config.max_hands:
                logger.info(
                    f"🕐 Game over - max hands ({self.config.max_hands}) reached!"
                )
                self._save_debug_logs()
                return Command(update={"game_over": True})

            # Continue to next hand
            logger.info(f"▶️ Continuing to hand #{state.hand_number}")
            return Command()

        except Exception as e:
            logger.error(f"❌ Game end check error: {e}")
            raise RuntimeError(f"Game end check failed: {e!s}")

    def route_after_betting(self, state: HoldemState) -> str:
        """Route game flow after a betting round completes.

        This conditional routing method determines where the game should proceed
        after a betting round. The routing logic considers:

        1. If only one player remains (others folded) -> award_pot
        2. If betting is not complete -> player_decision (continue betting)
        3. If only one active player (rest all-in) -> showdown
        4. Otherwise, proceed to next game phase based on current phase:
           - Preflop -> deal_flop
           - Flop -> deal_turn
           - Turn -> deal_river
           - River -> showdown

        Args:
            state (HoldemState): The current game state

        Returns:
            str: The name of the next node to route to
        """
        try:
            players_in_hand = [
                p for p in state.players_in_hand if p.status != PlayerStatus.FOLDED
            ]
            if len(players_in_hand) <= 1:
                logger.info("   → Routing to award_pot (≤1 player remaining)")
                return "award_pot"

            if not state.is_betting_complete():
                logger.info("   → Routing to player_decision (betting not complete)")
                return "player_decision"

            # Check if all remaining players are all-in
            active_players = [
                p for p in players_in_hand if p.status == PlayerStatus.ACTIVE
            ]
            if len(active_players) <= 1:
                logger.info("   → Routing to showdown (≤1 active player)")
                return "showdown"

            # Continue to next phase
            if state.current_phase == GamePhase.PREFLOP:
                logger.info("   → Routing to deal_flop")
                return "deal_flop"
            if state.current_phase == GamePhase.FLOP:
                logger.info("   → Routing to deal_turn")
                return "deal_turn"
            if state.current_phase == GamePhase.TURN:
                logger.info("   → Routing to deal_river")
                return "deal_river"
            logger.info("   → Routing to showdown")
            return "showdown"
        except Exception as e:
            logger.error(f"❌ Routing error: {e}")
            return "award_pot"

    def route_game_continuation(self, state: HoldemState) -> str:
        """Route game continuation."""
        try:
            if state.game_over:
                return "END"
            return "setup_hand"
        except Exception:
            return "END"

    def _evaluate_hand_simple(
        self, hole_cards: list[str], community_cards: list[str]
    ) -> float:
        """Simple hand evaluation method (placeholder for production
        evaluator).

        This is a simplified poker hand evaluator that assigns a score based
        primarily on high card values. In a production system, this would be
        replaced with a proper poker hand evaluator that correctly ranks hands
        according to standard poker rules.

        Args:
            hole_cards (List[str]): Player's private hole cards
            community_cards (List[str]): Shared community cards

        Returns:
            float: A score representing hand strength (higher is better)
        """
        all_cards = hole_cards + community_cards
        if not all_cards:
            return 0.0

        # Very simple evaluation - just count high cards
        score = 0
        for card in all_cards:
            if card[0] in ["A", "K", "Q", "J", "T"]:
                score += 10
            elif card[0].isdigit():
                score += int(card[0])

        return score

    def _save_debug_logs(self):
        """Save debug logs to files."""
        try:
            import datetime
            import json

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            # Save decision log
            with open(f"decision_log_{timestamp}.json", "w") as f:
                json.dump(self.decision_log, f, indent=2, default=str)

            # Save invocation log
            with open(f"invocation_log_{timestamp}.json", "w") as f:
                json.dump(self.invocation_log, f, indent=2, default=str)

            # Save error log
            with open(f"error_log_{timestamp}.json", "w") as f:
                json.dump(self.error_log, f, indent=2, default=str)

            logger.info(f"✅ Debug logs saved with timestamp {timestamp}")

        except Exception as e:
            logger.error(f"❌ Failed to save debug logs: {e}")
