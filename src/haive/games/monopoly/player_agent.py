"""Monopoly player agent implementation.

This module provides the player agent (subgraph) for making individual
player decisions in Monopoly, including:
    - Property purchase decisions
    - Jail decisions
    - Building decisions
    - Trade negotiations

"""

import operator
import uuid
from typing import Annotated, Any

from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.messages_state import MessagesState
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END
from langgraph.types import Command
from pydantic import BaseModel, Field, computed_field

from haive.games.monopoly.engines import build_monopoly_player_aug_llms
from haive.games.monopoly.models import (
    BuildingDecision,
    JailDecision,
    PlayerActionType,
    PropertyDecision,
    TradeResponse,
)
from haive.games.monopoly.player_agent import MonopolyPlayerAgent
from haive.games.monopoly.state import MonopolyState
from haive.games.monopoly.utils import (
    create_board,
    create_players,
    get_properties_by_color,
    shuffle_cards,
)


class PlayerDecisionState(MessagesState):
    """State for player decision subgraph."""

    # Input context
    player_name: str = Field(description="Name of the player making the decision")
    # WAS STR BEFORE
    decision_type: PlayerActionType | Any = Field(description="Type of decision needed")
    game_state: MonopolyState = Field(description="Current game state")

    # Decision context
    property_name: str = Field(default="", description="Property involved in decision")
    property_price: int = Field(default=0, description="Price of property")
    player_money: int = Field(default=0, description="Player's current money")
    dice_roll: int = Field(default=0, description="Current dice roll if relevant")

    # Output
    # Was deciscion before as as dict, aand reasonoing was just a str.
    decisions: Annotated[
        list[
            PropertyDecision
            | JailDecision
            | BuildingDecision
            | TradeResponse
            | str
            | Any
        ],
        operator.add,
    ] = Field(default_factory=list, description="Player's decision")
    reasoning: Annotated[list[str], operator.add] = Field(
        default_factory=list, description="Reasoning for the decision"
    )
    error_message: str = Field(default="", description="Error message if any")

    @computed_field
    @property
    def decision(
        self,
    ) -> PropertyDecision | JailDecision | BuildingDecision | TradeResponse | str | Any:
        """Get the decision."""
        if self.decisions:
            return self.decisions[-1]
        return None


class MonopolyPlayerAgentConfig(AgentConfig):
    """Configuration for monopoly player decision agent."""

    # Override base fields
    name: str = Field(default="monopoly_player", description="Agent name")
    state_schema: type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="State schema (will be set dynamically)",
    )

    # Player agent specific engines
    engines: dict[str, AugLLMConfig] = Field(
        default_factory=dict, description="LLM engines for different decision types"
    )

    class Config:
        arbitrary_types_allowed = True


class MonopolyGameAgentConfig(AgentConfig):
    """Configuration class for monopoly game agents.

    This class defines the configuration parameters for monopoly agents, including:
        - Game settings (players, turn limits)
        - Player decision configurations
        - Board and game state initialization

    Attributes:
        state_schema (type): The state schema for the game
        player_names (List[str]): Names of players in the game
        max_turns (int): Maximum turns before ending game
        enable_trading (bool): Whether to enable trade negotiations
        enable_building (bool): Whether to enable house/hotel building

    """

    # Override base agent config fields
    name: str = Field(default="monopoly_game", description="Agent name")
    state_schema: type[BaseModel] = Field(
        default=MonopolyState, description="The state schema for the game"
    )

    # Game settings
    player_names: list[str] = Field(
        default=["Alice", "Bob", "Charlie", "Diana"],
        description="Names of players in the game",
    )

    max_turns: int = Field(
        default=1000, description="Maximum number of turns before forcing game end"
    )

    enable_trading: bool = Field(
        default=False,
        description="Whether to enable trade negotiations between players",
    )

    enable_building: bool = Field(
        default=False, description="Whether to enable house/hotel building"
    )

    enable_auctions: bool = Field(
        default=False, description="Whether to enable property auctions"
    )

    # Visualization settings
    should_visualize_graph: bool = Field(
        default=True, description="Whether to visualize the game workflow graph"
    )

    # Player agent configuration - using composition instead of direct
    # reference
    player_agent_config: MonopolyPlayerAgentConfig = Field(
        default_factory=lambda: MonopolyPlayerAgentConfig(name="monopoly_player_agent"),
        description="Configuration for player decision agent",
    )

    # Runtime configuration
    runnable_config: RunnableConfig = Field(
        default_factory=lambda: RunnableConfigManager.create(
            thread_id=str(uuid.uuid4()), recursion_limit=500
        ),
        description="Runtime configuration for the game",
    )

    def create_initial_state(self) -> MonopolyState:
        """Create the initial game state with all required fields and proper
        validation.
        """
        # Create board and players
        properties = create_board()
        players = create_players(self.player_names)

        # Shuffle cards
        chance_cards, community_chest_cards = shuffle_cards()

        # Validate we have players
        if not players:
            raise ValueError(
                "No players were created - check player_names configuration"
            )

        # Create initial state with ALL required fields including messages
        initial_state = MonopolyState(
            players=players,
            properties=properties,
            current_player_index=0,  # Always start with first player
            turn_number=1,
            round_number=1,
            game_status="waiting",
            chance_cards=chance_cards,
            community_chest_cards=community_chest_cards,
            game_events=[],
            messages=[],  # CRITICAL FIX: Include empty messages list for schema compatibility
        )

        # Validate the initial state
        issues = initial_state.validate_state_consistency()
        if issues:
            raise ValueError(f"Initial state validation failed: {issues}")

        return initial_state

    def create_player_agent(self) -> Any:
        """Create the player decision agent."""
        # Import here to avoid circular dependency

        # Set up the engines for the player agent
        if not self.player_agent_config.engines:
            self.player_agent_config.engines = build_monopoly_player_aug_llms()

        # Create and return the player agent
        return MonopolyPlayerAgent(self.player_agent_config)

    def setup_player_agent_engines(self) -> None:
        """Set up the engines for the player agent if not already configured."""
        if not self.player_agent_config.engines:
            self.player_agent_config.engines = build_monopoly_player_aug_llms()

    class Config:
        """Pydantic configuration class."""

        arbitrary_types_allowed = True


@register_agent(MonopolyPlayerAgentConfig)
class MonopolyPlayerAgent(Agent[MonopolyPlayerAgentConfig]):
    """Player agent for making individual decisions in Monopoly."""

    def __init__(self, config: MonopolyPlayerAgentConfig):
        """Initialize the player agent."""
        super().__init__(config)
        self.engines = {}

        # Set up engines
        for key, engine_config in config.engines.items():
            self.engines[key] = engine_config.create_runnable()

            if self.engines[key] is None:
                raise ValueError(f"Failed to create engine for {key}")

    def setup_workflow(self) -> None:
        """Set up the player decision workflow."""
        # Add decision nodes
        self.graph.add_node("route_decision", self.route_decision)
        self.graph.add_node("make_property_decision", self.make_property_decision)
        self.graph.add_node("make_jail_decision", self.make_jail_decision)
        self.graph.add_node("make_building_decision", self.make_building_decision)
        self.graph.add_node("make_trade_decision", self.make_trade_decision)

        # Set up routing
        self.graph.set_entry_point("route_decision")

        # Add conditional edges from router
        self.graph.add_conditional_edges(
            "route_decision",
            self.get_decision_route,
            {
                "property": "make_property_decision",
                "jail": "make_jail_decision",
                "building": "make_building_decision",
                "trade": "make_trade_decision",
                "end": END,
            },
        )

        # All decision nodes go to END
        for node in [
            "make_property_decision",
            "make_jail_decision",
            "make_building_decision",
            "make_trade_decision",
        ]:
            self.graph.add_edge(node, END)

    def route_decision(self, state: BaseModel) -> Command:
        """Route to appropriate decision node based on decision type."""
        if isinstance(state, dict):
            # Debug: Print the raw state dict

            # Map simplified decision types to PlayerActionType values
            decision_type_mapping = {
                # Default to buy for property decisions
                "property": PlayerActionType.BUY_PROPERTY.value,
                "jail": PlayerActionType.PAY_JAIL_FINE.value,  # Default to pay fine for jail
                "building": "building",  # Keep as is
                "trade": PlayerActionType.TRADE_OFFER.value,  # Default to offer for trade
            }

            # If we have a simplified type, map it
            if (
                "decision_type" in state
                and state["decision_type"] in decision_type_mapping
            ):
                state["decision_type"] = decision_type_mapping[state["decision_type"]]

            decision_state = PlayerDecisionState.model_validate(state)
        else:
            decision_state = state

        # Map PlayerActionType values back to simple route names
        route_mapping = {
            PlayerActionType.BUY_PROPERTY.value: "property",
            PlayerActionType.PASS_PROPERTY.value: "property",
            PlayerActionType.PAY_JAIL_FINE.value: "jail",
            PlayerActionType.ROLL_FOR_JAIL.value: "jail",
            PlayerActionType.USE_JAIL_CARD.value: "jail",
            PlayerActionType.BUILD_HOUSE.value: "building",
            PlayerActionType.BUILD_HOTEL.value: "building",
            PlayerActionType.TRADE_OFFER.value: "trade",
            PlayerActionType.TRADE_ACCEPT.value: "trade",
            PlayerActionType.TRADE_DECLINE.value: "trade",
        }

        # Get the simplified route from the mapping
        route = route_mapping.get(decision_state.decision_type, None)

        if not route:
            return Command(
                update={
                    "error_message": f"Invalid decision type: {decision_state.decision_type}",
                    "decisions": [{"action": "error"}],
                }
            )

        return Command(update={})

    def get_decision_route(self, state: BaseModel) -> str:
        """Get the route for the decision."""
        if isinstance(state, dict):
            state = PlayerDecisionState.model_validate(state)
        decision_state = PlayerDecisionState.model_validate(state)

        if decision_state.error_message:
            return "end"

        return decision_state.decision_type

    def make_property_decision(self, state: BaseModel) -> Command:
        """Make a property purchase decision."""
        if isinstance(state, dict):
            state = PlayerDecisionState.model_validate(state)
        decision_state = PlayerDecisionState.model_validate(state)

        # Get the decision engine
        decision_engine = self.engines.get("property_decision")
        if not decision_engine:
            return Command(
                update={
                    "error_message": "Missing property decision engine",
                    "decision": {"action": "pass"},
                }
            )

        try:
            # Prepare context for the LLM
            context = self._prepare_property_context(decision_state)

            # Get decision from LLM
            decision_result = decision_engine.invoke(context)

            # Extract decision
            if hasattr(decision_result, "model_dump"):
                decision_dict = decision_result.model_dump()
            elif hasattr(decision_result, "dict"):
                decision_dict = decision_result.dict()
            else:
                decision_dict = dict(decision_result)

            return Command(
                update={
                    "decision": decision_dict,
                    "reasoning": decision_dict.get("reasoning", ""),
                }
            )

        except Exception as e:
            error_msg = f"Error making property decision: {e!s}"
            return Command(
                update={
                    "error_message": error_msg,
                    "decision": {"action": PlayerActionType.PASS_PROPERTY.value},
                }
            )

    def make_jail_decision(self, state: BaseModel) -> Command:
        """Make a jail-related decision."""
        if isinstance(state, dict):
            state = PlayerDecisionState.model_validate(state)
        decision_state = PlayerDecisionState.model_validate(state)

        # Get the decision engine
        decision_engine = self.engines.get("jail_decision")
        if not decision_engine:
            return Command(
                update={
                    "error_message": "Missing jail decision engine",
                    "decision": {"action": PlayerActionType.ROLL_FOR_JAIL.value},
                }
            )

        try:
            # Prepare context for the LLM
            context = self._prepare_jail_context(decision_state)

            # Get decision from LLM
            decision_result = decision_engine.invoke(context)

            # Extract decision
            if hasattr(decision_result, "model_dump"):
                decision_dict = decision_result.model_dump()
            elif hasattr(decision_result, "dict"):
                decision_dict = decision_result.dict()
            else:
                decision_dict = dict(decision_result)

            return Command(
                update={
                    "decision": decision_dict,
                    "reasoning": decision_dict.get("reasoning", ""),
                }
            )

        except Exception as e:
            error_msg = f"Error making jail decision: {e!s}"
            return Command(
                update={
                    "error_message": error_msg,
                    "decision": {"action": PlayerActionType.ROLL_FOR_JAIL.value},
                }
            )

    def make_building_decision(self, state: BaseModel) -> Command:
        """Make a building decision."""
        if isinstance(state, dict):
            state = PlayerDecisionState.model_validate(state)
        PlayerDecisionState.model_validate(state)

        # For now, return no building decision
        # This would be expanded with proper building logic
        return Command(
            update={
                "decision": {"action": "no_building"},
                "reasoning": "Building decisions not implemented yet",
            }
        )

    def make_trade_decision(self, state: BaseModel) -> Command:
        """Make a trade decision."""
        if isinstance(state, dict):
            state = PlayerDecisionState.model_validate(state)
        PlayerDecisionState.model_validate(state)

        # For now, return decline trade decision
        # This would be expanded with proper trade logic
        return Command(
            update={
                "decision": {"action": PlayerActionType.TRADE_DECLINE.value},
                "reasoning": "Trade decisions not implemented yet",
            }
        )

    def _prepare_property_context(
        self, decision_state: PlayerDecisionState
    ) -> dict[str, Any]:
        """Prepare context for property decision."""
        if isinstance(decision_state.game_state, dict):
            game_state = MonopolyState.model_validate(decision_state.game_state)
        else:
            game_state = decision_state.game_state
        player = game_state.get_player_by_name(decision_state.player_name)
        property_obj = game_state.get_property_by_name(decision_state.property_name)

        # Calculate affordability
        can_afford = (
            player.can_afford(decision_state.property_price) if player else False
        )

        # Get owned properties
        owned_properties = []
        if player:
            owned_props = game_state.get_properties_owned_by_player(player.name)
            owned_properties = [prop.name for prop in owned_props]

        # Check for color group completion potential
        color_group_info = ""
        if property_obj:
            color_props = get_properties_by_color(property_obj.color)
            owned_in_group = [prop for prop in owned_properties if prop in color_props]
            color_group_info = f"Color group {property_obj.color.value}: {
                len(owned_in_group)
            }/{len(color_props)} owned"

        return {
            "player_name": decision_state.player_name,
            "property_name": decision_state.property_name,
            "property_price": decision_state.property_price,
            "property_type": (
                property_obj.property_type.value if property_obj else "unknown"
            ),
            "property_color": property_obj.color.value if property_obj else "unknown",
            "current_money": player.money if player else 0,
            "can_afford": can_afford,
            "owned_properties": owned_properties,
            "color_group_info": color_group_info,
            "turn_number": game_state.turn_number,
            "other_players": [
                p.name
                for p in game_state.active_players
                if p.name != decision_state.player_name
            ],
        }

    def _prepare_jail_context(
        self, decision_state: PlayerDecisionState
    ) -> dict[str, Any]:
        """Prepare context for jail decision."""
        game_state = MonopolyState(**decision_state.game_state)
        player = game_state.get_player_by_name(decision_state.player_name)

        return {
            "player_name": decision_state.player_name,
            "current_money": player.money if player else 0,
            "jail_turns": player.jail_turns if player else 0,
            "has_jail_cards": (player.jail_cards > 0) if player else False,
            "can_afford_fine": player.can_afford(50) if player else False,
            "turn_number": game_state.turn_number,
        }
