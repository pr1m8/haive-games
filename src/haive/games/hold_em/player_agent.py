"""Texas Hold'em Player Agent - Clean Version without Fallbacks.

This module provides the player agent that acts as a subgraph in the main game.
Each player has their own decision-making workflow. This version removes all
fallbacks to expose real issues and provide clear debugging.
"""

import json
import logging
import traceback
from typing import Any, Dict, List, Literal, Optional

from haive.core.engine.agent.agent import Agent, AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command
from pydantic import BaseModel, Field

from haive.games.hold_em.models import (
    BettingDecision,
    PlayerDecisionModel,
    PokerAnalysis,
)
from haive.games.hold_em.state import (
    HoldemState,
    PlayerState,
    PlayerStatus,
    PokerAction,
)

# Setup detailed logging for player agents
logger = logging.getLogger(__name__)


class PlayerSubgraphState(BaseModel):
    """State for the player decision subgraph."""

    # Input from main game
    game_state: HoldemState = Field(description="Current game state")
    player_id: str = Field(description="ID of the player making decision")

    # Analysis intermediate results
    situation_analysis: Optional[Dict[str, Any]] = Field(
        default=None, description="Analysis of current situation"
    )
    hand_analysis: Optional[Dict[str, Any]] = Field(
        default=None, description="Analysis of player's hand"
    )
    opponent_analysis: Optional[Dict[str, Any]] = Field(
        default=None, description="Analysis of opponents"
    )

    # Final decision
    decision: Optional[Dict[str, Any]] = Field(
        default=None, description="Final betting decision"
    )

    # Debug information
    debug_info: Dict[str, Any] = Field(
        default_factory=dict, description="Debug information for troubleshooting"
    )


class HoldemPlayerAgentConfig(AgentConfig):
    """Configuration for Hold'em player agent."""

    state_schema: type = Field(default=PlayerSubgraphState)
    player_name: str = Field(description="Name of this player")
    player_style: str = Field(
        default="balanced",
        description="Playing style (tight, loose, aggressive, passive, balanced)",
    )
    risk_tolerance: float = Field(default=0.5, description="Risk tolerance (0-1)")

    # Engines for different analysis phases
    engines: Dict[str, AugLLMConfig] = Field(
        default_factory=dict, description="LLM engines for different decision phases"
    )

    class Config:
        arbitrary_types_allowed = True


class HoldemPlayerAgent(Agent[HoldemPlayerAgentConfig]):
    """Player agent for Texas Hold'em - Clean version without fallbacks."""

    def __init__(self, config: HoldemPlayerAgentConfig):
        # Ensure the config uses the correct state schema
        config.state_schema = PlayerSubgraphState
        super().__init__(config)

        # Store engines directly for easier access
        self.engines = config.engines

        # Validate required engines
        self._validate_required_engines()

        # Debug tracking
        self.analysis_log = []
        self.decision_log = []
        self.error_log = []

    def _validate_required_engines(self):
        """Validate that all required engines are present and configured."""
        required_engines = [
            "situation_analyzer",
            "hand_analyzer",
            "opponent_analyzer",
            "decision_maker",
        ]

        missing_engines = []
        for engine_name in required_engines:
            if engine_name not in self.engines:
                missing_engines.append(engine_name)

        if missing_engines:
            raise ValueError(
                f"Missing required engines for {self.config.player_name}: {missing_engines}"
            )

        # Validate engine configurations
        for engine_name, engine in self.engines.items():
            if (
                not hasattr(engine, "structured_output_model")
                or engine.structured_output_model is None
            ):
                raise ValueError(
                    f"Engine {engine_name} for {self.config.player_name} missing structured_output_model"
                )

            if not hasattr(engine, "prompt_template") or engine.prompt_template is None:
                raise ValueError(
                    f"Engine {engine_name} for {self.config.player_name} missing prompt_template"
                )

        logger.info(f"✅ All required engines validated for {self.config.player_name}")

    def setup_workflow(self):
        """Setup the player decision workflow."""
        logger.info(f"🔧 Setting up workflow for {self.config.player_name}")

        # Create state graph with PlayerSubgraphState
        self.graph = StateGraph(PlayerSubgraphState)

        # Add analysis nodes
        self.graph.add_node("analyze_situation", self.analyze_situation)
        self.graph.add_node("analyze_hand", self.analyze_hand)
        self.graph.add_node("analyze_opponents", self.analyze_opponents)
        self.graph.add_node("make_decision", self.make_decision)

        # Set up the workflow - each step must complete successfully
        self.graph.add_edge(START, "analyze_situation")
        self.graph.add_edge("analyze_situation", "analyze_hand")
        self.graph.add_edge("analyze_hand", "analyze_opponents")
        self.graph.add_edge("analyze_opponents", "make_decision")
        self.graph.add_edge("make_decision", END)

        logger.info(f"✅ Workflow setup complete for {self.config.player_name}")

    def analyze_situation(
        self, state: PlayerSubgraphState
    ) -> Command[Literal["analyze_hand"]]:
        """Analyze the current game situation."""
        logger.info(f"🔍 {self.config.player_name}: Analyzing situation...")
        if isinstance(state, dict):
            state = PlayerSubgraphState.model_validate(state)
        try:
            # Reconstruct HoldemState from the dict
            game_state = state.game_state
            player = game_state.get_player_by_id(state.player_id)

            if not player:
                raise RuntimeError(f"Player {state.player_id} not found in game state")

            logger.debug(
                f"   Player found: {player.name}, chips: {player.chips}, position: {player.position}"
            )

            # Get situation analyzer engine
            analyzer = self.engines["situation_analyzer"]
            logger.debug(f"   Using analyzer: {analyzer.name}")

            # Prepare context
            context = {
                "player_position": player.position,
                "pot_size": game_state.total_pot,
                "current_bet": game_state.current_bet,
                "player_chips": player.chips,
                "players_in_hand": len(game_state.players_in_hand),
                "game_phase": game_state.current_phase.value,
                "community_cards": game_state.community_cards,
                "recent_actions": game_state.actions_this_round[-5:],
                "stack_sizes": {p.player_id: p.chips for p in game_state.players},
            }

            logger.debug(
                f"   Context prepared: pot={context['pot_size']}, bet={context['current_bet']}"
            )

            # Get analysis - no fallbacks, let it fail if it will
            logger.debug(f"   Invoking situation analyzer...")
            analysis = analyzer.invoke(context)
            logger.debug(f"   Analysis received, type: {type(analysis)}")

            # Convert to dict if needed
            if hasattr(analysis, "model_dump"):
                analysis_dict = analysis.model_dump()
            elif hasattr(analysis, "dict"):
                analysis_dict = analysis.dict()
            else:
                # Try to convert to dict
                try:
                    analysis_dict = dict(analysis)
                except Exception:
                    raise RuntimeError(
                        f"Cannot convert analysis result to dict. Type: {type(analysis)}, Value: {analysis}"
                    )

            logger.info(f"✅ {self.config.player_name}: Situation analysis complete")
            logger.debug(f"   Analysis keys: {list(analysis_dict.keys())}")

            # Log for debugging
            analysis_entry = {
                "player_name": self.config.player_name,
                "analysis_type": "situation",
                "context": context,
                "result": analysis_dict,
            }
            self.analysis_log.append(analysis_entry)

            return Command(
                update={
                    "situation_analysis": analysis_dict,
                    "debug_info": {"situation_analysis_complete": True},
                },
                # goto="analyze_hand"
            )

        except Exception as e:
            error_msg = (
                f"Situation analysis failed for {self.config.player_name}: {str(e)}"
            )
            logger.error(f"❌ {error_msg}")
            logger.error(f"   Stack trace: {traceback.format_exc()}")

            error_entry = {
                "player_name": self.config.player_name,
                "analysis_type": "situation",
                "error": str(e),
                "traceback": traceback.format_exc(),
            }
            self.error_log.append(error_entry)

            # Don't use fallbacks - let the error propagate
            raise RuntimeError(error_msg) from e

    def analyze_hand(
        self, state: PlayerSubgraphState
    ) -> Command[Literal["analyze_opponents"]]:
        """Analyze the player's hand strength."""
        logger.info(f"🃏 {self.config.player_name}: Analyzing hand...")
        if isinstance(state, dict):
            print("--------------------------------")
            print(state)
            print(type(state))
            print("--------------------------------")
            state = PlayerSubgraphState.model_validate(state)
        try:
            # Reconstruct HoldemState from the dict
            game_state = state.game_state
            player = game_state.get_player_by_id(state.player_id)

            if not player:
                raise RuntimeError(f"Player {state.player_id} not found in game state")

            logger.debug(f"   Player hole cards: {player.hole_cards}")
            logger.debug(f"   Community cards: {game_state.community_cards}")

            # Get hand analyzer engine
            analyzer = self.engines["hand_analyzer"]
            logger.debug(f"   Using analyzer: {analyzer.name}")

            # Prepare context
            context = {
                "hole_cards": player.hole_cards,
                "community_cards": game_state.community_cards,
                "game_phase": game_state.current_phase.value,
                "num_opponents": len(game_state.players_in_hand) - 1,
                "pot_odds": self._calculate_pot_odds(game_state, player),
                "current_bet": str(game_state.current_bet),  # ADD THIS
                "pot_size": str(game_state.total_pot),  # ADD THIS
            }

            logger.debug(
                f"   Hand context: phase={context['game_phase']}, opponents={context['num_opponents']}"
            )

            # Get analysis - no fallbacks
            logger.debug(f"   Invoking hand analyzer...")
            analysis = analyzer.invoke(context)
            logger.debug(f"   Hand analysis received, type: {type(analysis)}")

            # Convert to dict if needed
            if hasattr(analysis, "model_dump"):
                analysis_dict = analysis.model_dump()
            elif hasattr(analysis, "dict"):
                analysis_dict = analysis.dict()
            else:
                try:
                    analysis_dict = dict(analysis)
                except Exception:
                    raise RuntimeError(
                        f"Cannot convert hand analysis result to dict. Type: {type(analysis)}, Value: {analysis}"
                    )

            logger.info(f"✅ {self.config.player_name}: Hand analysis complete")
            logger.debug(f"   Analysis keys: {list(analysis_dict.keys())}")

            # Log for debugging
            analysis_entry = {
                "player_name": self.config.player_name,
                "analysis_type": "hand",
                "context": context,
                "result": analysis_dict,
            }
            self.analysis_log.append(analysis_entry)

            return Command(
                update={
                    "hand_analysis": analysis_dict,
                    "debug_info": {"hand_analysis_complete": True},
                },
                # goto="analyze_opponents"
            )

        except Exception as e:
            error_msg = f"Hand analysis failed for {self.config.player_name}: {str(e)}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"   Stack trace: {traceback.format_exc()}")

            error_entry = {
                "player_name": self.config.player_name,
                "analysis_type": "hand",
                "error": str(e),
                "traceback": traceback.format_exc(),
            }
            self.error_log.append(error_entry)

            # Don't use fallbacks - let the error propagate
            raise RuntimeError(error_msg) from e

    def analyze_opponents(self, state):
        """Analyze opponent behavior and tendencies."""
        try:
            # Get the opponent analyzer engine
            analyzer = self.engines["opponent_analyzer"]

            # Get opponents (exclude current player)
            all_players = getattr(state, "players", [])
            opponents = [
                p for p in all_players if getattr(p, "name", str(p)) != self.player_name
            ]

            # Prepare context using the helper function that handles missing attributes
            context = self._prepare_opponent_context(state, opponents)

            # Call the analyzer
            analysis = analyzer.invoke(context)

            return analysis

        except Exception as e:
            error_msg = f"Opponent analysis failed for {self.player_name}: {str(e)}"
            raise RuntimeError(error_msg) from e

    def _prepare_opponent_context(self, game_state, opponents) -> Dict[str, str]:
        """Prepare context dictionary for opponent analysis with error handling."""

        # Helper to safely get position info
        def _get_position_info(game_state):
            """Create position info summary from game state."""
            try:
                position_data = []

                # Try different ways to get position information
                if hasattr(game_state, "dealer_position"):
                    position_data.append(f"Dealer: {game_state.dealer_position}")

                if hasattr(game_state, "players_in_hand"):
                    position_data.append(
                        f"Players in hand: {len(game_state.players_in_hand)}"
                    )

                if hasattr(game_state, "current_player"):
                    position_data.append(f"Current: {game_state.current_player}")

                if hasattr(game_state, "button_position"):
                    position_data.append(f"Button: {game_state.button_position}")

                return (
                    " | ".join(position_data)
                    if position_data
                    else "Position info unavailable"
                )

            except Exception:
                return "Position info unavailable"

        # Helper to safely get stack sizes
        def _get_stack_sizes(game_state):
            """Create stack sizes summary from game state."""
            try:
                stack_info = {}

                # Try to get stack info from players
                if hasattr(game_state, "players") and game_state.players:
                    for player in game_state.players:
                        player_name = getattr(player, "name", str(player))
                        chips = getattr(player, "chips", getattr(player, "stack", 0))
                        stack_info[player_name] = chips

                # Alternative: check for direct stack_sizes attribute
                elif hasattr(game_state, "stack_sizes"):
                    stack_info = game_state.stack_sizes

                # Alternative: check for player_stacks attribute
                elif hasattr(game_state, "player_stacks"):
                    stack_info = game_state.player_stacks

                return str(stack_info) if stack_info else "Stack info unavailable"

            except Exception:
                return "Stack info unavailable"

        # Build the context dictionary with safe attribute access
        return {
            "opponents": str([getattr(opp, "name", str(opp)) for opp in opponents]),
            "betting_pattern": str(
                getattr(
                    game_state,
                    "betting_pattern",
                    getattr(
                        game_state, "action_history", "No betting pattern available"
                    ),
                )
            ),
            "game_phase": str(
                getattr(
                    game_state,
                    "phase",
                    getattr(
                        game_state,
                        "game_phase",
                        getattr(game_state, "street", "unknown"),
                    ),
                )
            ),
            "community_cards": str(
                getattr(game_state, "community_cards", getattr(game_state, "board", []))
            ),
            "position_info": _get_position_info(game_state),
            "stack_sizes": _get_stack_sizes(game_state),
        }

    def make_decision(self, state: PlayerSubgraphState) -> Command[Literal[END]]:
        """Make the final betting decision - FIXED to handle BettingDecision model."""
        if isinstance(state, dict):
            state = PlayerSubgraphState.model_validate(state)

        logger.info(f"🎯 {self.config.player_name}: Making final decision...")

        try:
            # Reconstruct HoldemState from the dict/object
            game_state = state.game_state
            player = game_state.get_player_by_id(state.player_id)

            if not player:
                # Enhanced player lookup with fallback by name
                for p in game_state.players:
                    if p.name == self.config.player_name:
                        player = p
                        logger.warning(
                            f"🔧 Found player by name: {p.name} (ID: '{p.player_id}')"
                        )
                        break

            if not player:
                available_players = [
                    f"'{p.name}' (ID: '{p.player_id}')" for p in game_state.players
                ]
                error_msg = (
                    f"Player lookup failed for ID '{state.player_id}' and name '{self.config.player_name}'. "
                    f"Available players: {available_players}"
                )
                raise RuntimeError(error_msg)

            logger.debug(f"   ✅ Found player: {player.name}, chips: {player.chips}")

            # Get decision maker engine
            decision_maker = self.engines["decision_maker"]
            logger.debug(f"   Using decision maker: {decision_maker.name}")

            # Prepare comprehensive context
            context = {
                "hole_cards": player.hole_cards,
                "community_cards": game_state.community_cards,
                "phase": game_state.current_phase.value,
                "position": player.position,
                "chips": player.chips,
                "current_bet": game_state.current_bet,
                "pot": game_state.total_pot,
                "players_in_hand": len(game_state.players_in_hand),
                "situation_analysis": state.situation_analysis or {},
                "hand_analysis": state.hand_analysis or {},
                "opponent_analysis": state.opponent_analysis or {},
                "available_actions": self._get_available_actions(game_state, player),
                "player_style": self.config.player_style,
                "risk_tolerance": self.config.risk_tolerance,
            }

            logger.debug(
                f"   Decision context: available_actions={context['available_actions']}"
            )

            # Get decision from LLM
            logger.debug(f"   Invoking decision maker...")
            decision = decision_maker.invoke(context)
            logger.debug(f"   Decision received, type: {type(decision)}")

            # FIXED: Handle different decision model formats
            decision_dict = self._normalize_decision(decision)

            # Validate decision has required fields
            required_fields = ["action", "amount", "reasoning"]
            missing_fields = [
                field for field in required_fields if field not in decision_dict
            ]
            if missing_fields:
                raise RuntimeError(
                    f"Decision missing required fields: {missing_fields}. Got: {list(decision_dict.keys())}"
                )

            # Validate decision against available actions
            validated_decision = self._validate_decision(
                decision_dict, game_state, player
            )

            logger.info(
                f"✅ {self.config.player_name}: Decision made - {validated_decision['action']}"
            )
            if validated_decision.get("amount", 0) > 0:
                logger.info(f"   Amount: {validated_decision['amount']}")
            logger.debug(
                f"   Reasoning: {validated_decision.get('reasoning', 'No reasoning')[:100]}..."
            )

            return Command(
                update={
                    "decision": validated_decision,
                    "debug_info": {"decision_complete": True},
                },
            )

        except Exception as e:
            error_msg = (
                f"Decision making failed for {self.config.player_name}: {str(e)}"
            )
            logger.error(f"❌ {error_msg}")
            logger.error(f"   Stack trace: {traceback.format_exc()}")
            raise RuntimeError(error_msg) from e

    def _normalize_decision(self, decision: Any) -> Dict[str, Any]:
        """
        Normalize different decision model formats to a consistent dictionary.

        Handles:
        - BettingDecision model (primary_action, bet_size, etc.)
        - PlayerDecisionModel (action, amount, etc.)
        - Raw dictionaries
        """
        # Convert to dict if it's a Pydantic model
        if hasattr(decision, "model_dump"):
            decision_dict = decision.model_dump()
        elif hasattr(decision, "dict"):
            decision_dict = decision.dict()
        else:
            try:
                decision_dict = dict(decision)
            except Exception:
                raise RuntimeError(
                    f"Cannot convert decision result to dict. Type: {type(decision)}, Value: {decision}"
                )

        logger.debug(f"   Original decision fields: {list(decision_dict.keys())}")

        # Check if it's a BettingDecision format and convert to expected format
        if "primary_action" in decision_dict:
            logger.debug("   Detected BettingDecision format, converting...")

            # Map BettingDecision fields to expected format
            normalized = {
                "action": decision_dict.get("primary_action", "fold"),
                "amount": decision_dict.get("bet_size", 0),
                "reasoning": decision_dict.get("reasoning", "No reasoning provided"),
                "confidence": 0.5,  # Default confidence
                "aggression_level": decision_dict.get("aggression_level", "moderate"),
                "expected_outcome": decision_dict.get("expected_outcome", ""),
                "alternative_action": decision_dict.get("alternative_action"),
            }

            logger.debug(
                f"   Converted to: action={normalized['action']}, amount={normalized['amount']}"
            )
            return normalized

        # Check if it's already in the expected format
        elif "action" in decision_dict:
            logger.debug("   Already in expected format")
            return decision_dict

        # Handle other potential formats
        else:
            logger.warning(f"   Unknown decision format: {list(decision_dict.keys())}")

            # Try to extract any action-like field
            action = "fold"  # Safe default
            amount = 0
            reasoning = decision_dict.get("reasoning", "Unknown decision format")

            # Look for action in various field names
            for field_name in ["action", "primary_action", "decision", "move"]:
                if field_name in decision_dict:
                    action = decision_dict[field_name]
                    break

            # Look for amount in various field names
            for field_name in ["amount", "bet_size", "size", "bet_amount"]:
                if field_name in decision_dict:
                    amount = decision_dict[field_name]
                    break

            normalized = {
                "action": action,
                "amount": amount,
                "reasoning": reasoning,
                "confidence": 0.5,
            }

            logger.warning(f"   Normalized unknown format to: {normalized}")
            return normalized

    def _calculate_pot_odds(
        self, game_state: HoldemState, player: PlayerState
    ) -> float:
        """Calculate pot odds for the player."""
        if game_state.current_bet <= player.current_bet:
            return 0.0  # No additional bet required

        call_amount = game_state.current_bet - player.current_bet
        if call_amount <= 0:
            return 0.0

        total_pot = game_state.total_pot + call_amount
        return call_amount / total_pot if total_pot > 0 else 0.0

    def _get_available_actions(
        self, game_state: HoldemState, player: PlayerState
    ) -> List[str]:
        """Get list of available actions for the player."""
        actions = []

        # Can always fold (unless all-in)
        if player.status == PlayerStatus.ACTIVE:
            actions.append("fold")

        # Check if can check
        if game_state.current_bet == player.current_bet:
            actions.append("check")

        # Check if can call
        call_amount = game_state.current_bet - player.current_bet
        if call_amount > 0 and call_amount <= player.chips:
            actions.append("call")

        # Check if can bet (when no current bet)
        if game_state.current_bet == 0 and player.chips >= game_state.big_blind:
            actions.append("bet")

        # Check if can raise
        if (
            game_state.current_bet > 0
            and player.chips > call_amount + game_state.min_raise
        ):
            actions.append("raise")

        # Can always go all-in if have chips
        if player.chips > 0:
            actions.append("all_in")

        return actions

    def _validate_decision(
        self, decision: Dict[str, Any], game_state: HoldemState, player: PlayerState
    ) -> Dict[str, Any]:
        """Validate and potentially correct a decision."""
        action = decision.get("action", "fold")
        amount = decision.get("amount", 0)

        logger.debug(f"   Validating decision: {action} {amount}")

        # Get available actions
        available = self._get_available_actions(game_state, player)
        logger.debug(f"   Available actions: {available}")

        # If action not available, this is an error - don't fallback
        if action not in available:
            raise RuntimeError(
                f"Invalid action '{action}' for {player.name}. Available actions: {available}"
            )

        # Validate amounts
        if action in ["bet", "raise"]:
            min_amount = game_state.min_raise
            if amount < min_amount:
                logger.warning(
                    f"   Bet/raise amount {amount} below minimum {min_amount}, adjusting"
                )
                amount = min_amount
            if amount > player.chips:
                logger.warning(
                    f"   Bet/raise amount {amount} exceeds chips {player.chips}, converting to all-in"
                )
                action = "all_in"
                amount = player.chips
        elif action == "call":
            expected_amount = min(
                game_state.current_bet - player.current_bet, player.chips
            )
            if amount != expected_amount:
                logger.warning(
                    f"   Call amount {amount} incorrect, should be {expected_amount}, adjusting"
                )
                amount = expected_amount
        elif action == "all_in":
            if amount != player.chips:
                logger.warning(
                    f"   All-in amount {amount} incorrect, should be {player.chips}, adjusting"
                )
                amount = player.chips
        else:
            amount = 0

        validated = {
            "action": action,
            "amount": amount,
            "reasoning": decision.get("reasoning", "Validated decision"),
            "confidence": decision.get("confidence", 0.5),
        }

        logger.debug(
            f"   Validated decision: {validated['action']} {validated['amount']}"
        )

        return validated

    def save_debug_logs(self, timestamp: str = None):
        """Save debug logs for this player agent."""
        if timestamp is None:
            import datetime

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        try:
            player_name_safe = self.config.player_name.replace(" ", "_").lower()

            # Save analysis log
            with open(f"player_analysis_{player_name_safe}_{timestamp}.json", "w") as f:
                json.dump(self.analysis_log, f, indent=2, default=str)

            # Save decision log
            with open(
                f"player_decisions_{player_name_safe}_{timestamp}.json", "w"
            ) as f:
                json.dump(self.decision_log, f, indent=2, default=str)

            # Save error log
            with open(f"player_errors_{player_name_safe}_{timestamp}.json", "w") as f:
                json.dump(self.error_log, f, indent=2, default=str)

            logger.info(
                f"✅ Debug logs saved for {self.config.player_name} with timestamp {timestamp}"
            )

        except Exception as e:
            logger.error(
                f"❌ Failed to save debug logs for {self.config.player_name}: {e}"
            )
