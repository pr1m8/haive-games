"""Fixed Monopoly game agent implementation.

This module provides the corrected main game agent for orchestrating a Monopoly game,
with proper handling of BaseModel objects from LangGraph instead of dictionaries.
"""

from typing import Any

from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.engine.agent.config import AgentConfig
from langgraph.graph import END
from langgraph.types import Command
from pydantic import BaseModel, Field

from haive.games.monopoly.models import GameEvent, PlayerActionType
from haive.games.monopoly.state import MonopolyState
from haive.games.monopoly.utils import (
    check_game_end,
    get_property_at_position,
    move_player,
    roll_dice,
)


class MonopolyGameAgentConfig(AgentConfig):
    """Configuration for monopoly game agent."""

    name: str = Field(default="monopoly_game", description="Agent name")
    player_names: list[str] = Field(description="Names of players in the game")
    max_turns: int = Field(default=1000, description="Maximum turns before ending game")
    enable_trading: bool = Field(default=False, description="Enable trade negotiations")
    state_schema: type[BaseModel] = Field(
        default=MonopolyState, description="The state schema for the game"
    )
    # Reference to player agent (will be set externally)
    player_agent: Any = Field(default=None, description="Player decision agent")

    class Config:
        arbitrary_types_allowed = True


@register_agent(MonopolyGameAgentConfig)
class MonopolyGameAgent(Agent[MonopolyGameAgentConfig]):
    """Main game agent for orchestrating Monopoly."""

    def __init__(self, config: MonopolyGameAgentConfig):
        """Initialize the game agent."""
        super().__init__(config)
        self.player_agent = config.player_agent

    def setup_workflow(self) -> None:
        """Set up the main game workflow."""
        # Add core game nodes
        self.graph.add_node("start_turn", self.start_turn)
        self.graph.add_node("roll_dice", self.roll_dice_node)
        self.graph.add_node("move_player", self.move_player_node)
        self.graph.add_node("handle_landing", self.handle_landing)
        self.graph.add_node("check_doubles", self.check_doubles)
        self.graph.add_node("end_turn", self.end_turn)
        self.graph.add_node("check_game_end", self.check_game_end_node)

        # Set up the main flow
        self.graph.set_entry_point("start_turn")

        # Linear flow for most of the turn
        self.graph.add_edge("start_turn", "roll_dice")
        self.graph.add_edge("roll_dice", "move_player")
        self.graph.add_edge("move_player", "handle_landing")
        self.graph.add_edge("handle_landing", "check_doubles")

        # Conditional routing from doubles check
        self.graph.add_conditional_edges(
            "check_doubles",
            self.route_after_doubles,
            {
                "continue_turn": "roll_dice",  # Roll again for doubles
                "go_to_jail": "end_turn",  # Three doubles = jail
                "end_turn": "end_turn",  # Normal end turn
            },
        )

        # End turn processing
        self.graph.add_edge("end_turn", "check_game_end")

        # Game end routing
        self.graph.add_conditional_edges(
            "check_game_end",
            self.route_game_end,
            {
                "continue": "start_turn",  # Next player's turn
                "finished": END,  # Game over
            },
        )

    def start_turn(self, state: MonopolyState | BaseModel | dict[str, Any]) -> Command:
        """Start a player's turn."""
        # CRITICAL FIX: Handle BaseModel objects properly
        monopoly_state = state
        current_player = monopoly_state.current_player

        # Reset doubles count if starting new turn
        if not monopoly_state.doubles_rolled:
            current_player.doubles_count = 0

        # Add turn start event
        event = GameEvent(
            event_type="turn_start",
            player=current_player.name,
            description=f"{current_player.name} starts their turn",
        )

        return Command(
            update={
                "game_events": [event],  # Will be reduced with existing events
                "game_status": "playing",
            }
        )

    def roll_dice_node(
        self, state: MonopolyState | BaseModel | dict[str, Any]
    ) -> Command:
        """Roll dice for the current player."""
        monopoly_state = MonopolyState.from_state_object(state)
        current_player = monopoly_state.current_player

        # Check if player is in jail
        if current_player.in_jail:
            return self.handle_jail_turn(monopoly_state)

        # Roll dice
        dice_roll = roll_dice()

        # Track doubles
        is_doubles = dice_roll.is_doubles
        if is_doubles:
            current_player.doubles_count += 1

        # Add dice roll event
        event = GameEvent(
            event_type="dice_roll",
            player=current_player.name,
            description=f"Rolled {dice_roll.die1} and {dice_roll.die2}",
            details={"dice_roll": dice_roll.model_dump()},
        )

        return Command(
            update={
                "last_roll": dice_roll.model_dump(),
                "doubles_rolled": is_doubles,
                "game_events": [event],
            }
        )

    def move_player_node(
        self, state: MonopolyState | BaseModel | dict[str, Any]
    ) -> Command:
        """Move the current player based on dice roll."""
        monopoly_state = MonopolyState.from_state_object(state)
        current_player = monopoly_state.current_player
        dice_roll = monopoly_state.last_roll

        if not dice_roll:
            return Command(update={"error_message": "No dice roll found"})

        # Move player
        old_position = current_player.position
        new_position, passed_go = move_player(current_player, dice_roll)

        # Handle passing GO
        money_gained = 0
        if passed_go:
            money_gained = 200
            current_player.money += money_gained

        # Add movement event
        event = GameEvent(
            event_type="player_move",
            player=current_player.name,
            description=f"Moved from position {old_position} to {new_position}",
            money_change=money_gained,
            details={
                "old_position": old_position,
                "new_position": new_position,
                "passed_go": passed_go,
            },
        )

        # Create event update
        event_update = {"game_events": [event]}

        # Check if players list is valid before trying to update
        if monopoly_state.players and 0 <= monopoly_state.current_player_index < len(
            monopoly_state.players
        ):
            # Update the player in the players list using safe update_player method
            updated_state = monopoly_state.update_player(
                monopoly_state.current_player_index, current_player
            )
            event_update["players"] = updated_state.players
        # Handle the empty players list case
        # Initialize players list if needed
        elif not monopoly_state.players:
            event_update["players"] = [current_player]

        return Command(update=event_update)

    def handle_landing(
        self, state: MonopolyState | BaseModel | dict[str, Any]
    ) -> Command:
        """Handle the player landing on a space."""
        if isinstance(state, dict):
            state = MonopolyState.model_validate(state)

        monopoly_state = state
        current_player = monopoly_state.current_player

        position_data = get_property_at_position(current_player.position)
        if not position_data:
            return Command(
                update={"error_message": f"Invalid position: {current_player.position}"}
            )

        position_name = position_data["name"]

        # Handle different types of spaces
        if position_data["type"] == "special":
            return self.handle_special_space(monopoly_state, position_name)
        return self.handle_property_space(monopoly_state, position_name)

    def handle_special_space(self, state: MonopolyState, space_name: str) -> Command:
        """Handle landing on special spaces like GO, Jail, etc."""
        current_player = state.current_player
        events = []
        money_change = 0

        if space_name == "Income Tax":
            # Pay $200 or 10% of net worth (choose $200 for simplicity)
            tax_amount = 200
            current_player.money -= tax_amount
            money_change = -tax_amount

            events.append(
                GameEvent(
                    event_type="tax_payment",
                    player=current_player.name,
                    description="Paid income tax",
                    money_change=money_change,
                )
            )

        elif space_name == "Luxury Tax":
            tax_amount = 75
            current_player.money -= tax_amount
            money_change = -tax_amount

            events.append(
                GameEvent(
                    event_type="tax_payment",
                    player=current_player.name,
                    description="Paid luxury tax",
                    money_change=money_change,
                )
            )

        elif space_name == "Go To Jail":
            current_player.position = 10  # Jail position
            current_player.in_jail = True
            current_player.jail_turns = 0
            current_player.doubles_count = 0  # Reset doubles when going to jail

            events.append(
                GameEvent(
                    event_type="go_to_jail",
                    player=current_player.name,
                    description="Sent to jail",
                )
            )

        elif space_name in ["Chance", "Community Chest"]:
            # For now, just log the card draw
            # In a full implementation, this would draw and execute cards

            events.append(
                GameEvent(
                    event_type="card_draw",
                    player=current_player.name,
                    description=f"Drew {space_name} card",
                )
            )

        else:
            # Free Parking, visiting Jail, etc. - no action needed
            pass

        # Update player in the players list
        updated_players = state.players.copy()
        updated_players[state.current_player_index] = current_player

        return Command(update={"players": updated_players, "game_events": events})

    def handle_property_space(
        self, state: MonopolyState, property_name: str
    ) -> Command:
        """Handle landing on a property space."""
        current_player = state.current_player
        property_obj = state.get_property_by_name(property_name)

        if not property_obj:
            # Handle the case where property isn't found - log error but don't crash

            # Try to get property info from utils.BOARD_PROPERTIES
            from haive.games.monopoly.utils import BOARD_PROPERTIES

            position = current_player.position
            position_data = BOARD_PROPERTIES.get(position)

            if position_data and position_data["name"] == property_name:
                # Create the property on the fly based on board data
                from haive.games.monopoly.models import (
                    Property,
                    PropertyColor,
                    PropertyType,
                )

                property_obj = Property(
                    name=position_data["name"],
                    position=position,
                    property_type=PropertyType(position_data["type"]),
                    color=PropertyColor(position_data["color"]),
                    price=position_data.get("price", 0),
                    rent=position_data.get("rent", [0, 0, 0, 0, 0, 0]),
                    house_cost=position_data.get("house_cost", 0),
                    mortgage_value=position_data.get("mortgage_value", 0),
                )

                # Add to the state and continue
                updated_properties = state.properties.copy()
                updated_properties[property_name] = property_obj

                # Return event that adds the property to state
                return Command(
                    update={
                        "properties": updated_properties,
                        "game_events": [
                            GameEvent(
                                event_type="property_added",
                                player=current_player.name,
                                description=f"Property {property_name} added to game",
                                property_involved=property_name,
                            )
                        ],
                    }
                )
            # If we can't recover, return error but don't crash the game
            return Command(
                update={
                    "game_events": [
                        GameEvent(
                            event_type="property_error",
                            player=current_player.name,
                            description=f"Unable to find property: {property_name}",
                        )
                    ]
                }
            )

        # Check if property is owned
        if property_obj.owner is None:
            # Property is unowned - offer to buy
            return self.offer_property_purchase(state, property_obj)
        if property_obj.owner == current_player.name:
            # Player owns the property - no action needed
            return Command(update={})
        # Property is owned by another player - pay rent
        return self.pay_rent(state, property_obj)

    def offer_property_purchase(self, state: MonopolyState, property_obj) -> Command:
        """Offer property purchase to current player."""
        current_player = state.current_player

        # Create decision input for player agent
        decision_input = {
            "player_name": current_player.name,
            "decision_type": "property",
            "game_state": state.to_dict(),
            "property_name": property_obj.name,
            "property_price": property_obj.price,
            "player_money": current_player.money,
            "messages": state.messages if hasattr(state, "messages") else [],
        }
        # decision_input = self.player_agent/
        # Get decision from player agent
        # print(f"Player agent: {self.player_agent}")
        # print(f"Player agent app: {self.player_agent.app}")
        # print(f"Decision input: {decision_input}")
        # print(f"Input type: {type(decision_input)}")
        # print(f"Player agent app input: {self.player_agent.app.input_schema.mode}")
        # print(f"Player agent app output: {self.player_agent.app.output_schema}")
        if self.player_agent and hasattr(self.player_agent, "app"):
            decision_result = self.player_agent.run(decision_input)
            decision = decision_result.get("decision", {})
            decision_result.get("reasoning", "No reasoning provided")
        else:
            # Fallback decision
            decision = {"action": PlayerActionType.PASS_PROPERTY.value}

        action = decision.get("action", PlayerActionType.PASS_PROPERTY.value)

        events = []
        updated_players = state.players.copy()
        updated_properties = state.properties.copy()

        if action == PlayerActionType.BUY_PROPERTY.value:
            if current_player.can_afford(property_obj.price):
                # Buy the property
                current_player.money -= property_obj.price
                current_player.properties.append(property_obj.name)
                property_obj.owner = current_player.name

                events.append(
                    GameEvent(
                        event_type="property_purchase",
                        player=current_player.name,
                        description=f"Purchased {property_obj.name}",
                        money_change=-property_obj.price,
                        property_involved=property_obj.name,
                    )
                )

                # Update collections
                updated_players[state.current_player_index] = current_player
                updated_properties[property_obj.name] = property_obj

            else:
                events.append(
                    GameEvent(
                        event_type="purchase_failed",
                        player=current_player.name,
                        description=f"Could not afford {property_obj.name}",
                    )
                )
        else:
            # Pass on property - could trigger auction in full implementation
            events.append(
                GameEvent(
                    event_type="property_passed",
                    player=current_player.name,
                    description=f"Passed on {property_obj.name}",
                    property_involved=property_obj.name,
                )
            )

        return Command(
            update={
                "players": updated_players,
                "properties": updated_properties,
                "game_events": events,
            }
        )

    def pay_rent(self, state: MonopolyState, property_obj) -> Command:
        """Handle rent payment."""
        current_player = state.current_player
        owner = state.get_player_by_name(property_obj.owner)

        if not owner or owner.bankrupt:
            return Command(update={})

        # Calculate rent
        dice_total = state.last_roll.total if state.last_roll else 0
        rent_amount = state.get_rent_amount(property_obj.name, dice_total)

        if rent_amount <= 0:
            return Command(update={})

        events = []
        updated_players = state.players.copy()

        # Pay rent
        if current_player.can_afford(rent_amount):
            current_player.money -= rent_amount
            owner.money += rent_amount

            events.append(
                GameEvent(
                    event_type="rent_payment",
                    player=current_player.name,
                    description=f"Paid ${rent_amount} rent to {owner.name}",
                    money_change=-rent_amount,
                    property_involved=property_obj.name,
                    details={"recipient": owner.name, "rent_amount": rent_amount},
                )
            )

            # Update both players
            updated_players[state.current_player_index] = current_player
            for i, player in enumerate(updated_players):
                if player.name == owner.name:
                    updated_players[i] = owner
                    break
        else:
            # Player cannot afford rent - simplified bankruptcy
            current_player.bankrupt = True

            events.append(
                GameEvent(
                    event_type="bankruptcy",
                    player=current_player.name,
                    description=f"Went bankrupt owing ${rent_amount} rent",
                    property_involved=property_obj.name,
                )
            )

            updated_players[state.current_player_index] = current_player

        return Command(update={"players": updated_players, "game_events": events})

    def check_doubles(
        self, state: MonopolyState | BaseModel | dict[str, Any]
    ) -> Command:
        """Check if doubles were rolled and handle accordingly."""
        # No additional processing needed here - just pass through
        return Command(update={})

    def route_after_doubles(
        self, state: MonopolyState | BaseModel | dict[str, Any]
    ) -> str:
        """Route based on doubles status."""
        monopoly_state = MonopolyState.from_state_object(state)
        current_player = monopoly_state.current_player

        # Check for three doubles in a row
        if current_player.doubles_count >= 3:
            return "go_to_jail"

        # Check if doubles were rolled
        if monopoly_state.doubles_rolled and current_player.doubles_count < 3:
            return "continue_turn"

        return "end_turn"

    def end_turn(self, state: MonopolyState | BaseModel | dict[str, Any]) -> Command:
        """End the current player's turn."""
        monopoly_state = MonopolyState.from_state_object(state)
        current_player = monopoly_state.current_player

        events = []
        updated_players = monopoly_state.players.copy()

        # Handle three doubles = jail
        if current_player.doubles_count >= 3:
            current_player.position = 10  # Jail
            current_player.in_jail = True
            current_player.jail_turns = 0

            events.append(
                GameEvent(
                    event_type="go_to_jail",
                    player=current_player.name,
                    description="Sent to jail for rolling three doubles",
                )
            )

            updated_players[monopoly_state.current_player_index] = current_player

        # Reset doubles for next turn if not continuing
        if not monopoly_state.doubles_rolled or current_player.doubles_count >= 3:
            current_player.doubles_count = 0
            doubles_rolled = False

            # Move to next player
            monopoly_state.next_player()
        else:
            doubles_rolled = monopoly_state.doubles_rolled

        return Command(
            update={
                "players": updated_players,
                "current_player_index": monopoly_state.current_player_index,
                "turn_number": monopoly_state.turn_number,
                "round_number": monopoly_state.round_number,
                "doubles_rolled": doubles_rolled,
                "game_events": events,
            }
        )

    def check_game_end_node(
        self, state: MonopolyState | BaseModel | dict[str, Any]
    ) -> Command:
        """Check if the game should end."""
        monopoly_state = MonopolyState.from_state_object(state)

        # Check for game end conditions
        game_ended, winner = check_game_end(monopoly_state)

        if game_ended:
            return Command(update={"game_status": "finished", "winner": winner})

        # Check turn limit
        if monopoly_state.turn_number >= self.config.max_turns:

            # Determine winner by net worth
            best_player = None
            best_worth = -1

            for player in monopoly_state.active_players:
                net_worth = player.net_worth(monopoly_state.properties)
                if net_worth > best_worth:
                    best_worth = net_worth
                    best_player = player.name

            return Command(update={"game_status": "finished", "winner": best_player})

        return Command(update={})

    def route_game_end(self, state: MonopolyState | BaseModel | dict[str, Any]) -> str:
        """Route based on game end status."""
        monopoly_state = MonopolyState.from_state_object(state)

        if monopoly_state.game_status == "finished":
            return "finished"

        return "continue"

    def handle_jail_turn(self, state: MonopolyState) -> Command:
        """Handle a turn when player is in jail."""
        current_player = state.current_player

        # Create decision input for player agent
        decision_input = {
            "player_name": current_player.name,
            "decision_type": "jail",
            "game_state": state.to_dict(),
            "player_money": current_player.money,
        }

        # Get decision from player agent
        if self.player_agent and hasattr(self.player_agent, "app"):
            decision_result = self.player_agent.app.invoke(decision_input)
            decision = decision_result.get("decision", {})
        else:
            decision = {"action": PlayerActionType.ROLL_FOR_JAIL.value}

        action = decision.get("action", PlayerActionType.ROLL_FOR_JAIL.value)

        events = []
        updated_players = state.players.copy()

        if action == PlayerActionType.PAY_JAIL_FINE.value:
            if current_player.can_afford(50):
                current_player.money -= 50
                current_player.in_jail = False
                current_player.jail_turns = 0

                events.append(
                    GameEvent(
                        event_type="jail_fine_paid",
                        player=current_player.name,
                        description="Paid fine to get out of jail",
                        money_change=-50,
                    )
                )

                # Now roll dice normally
                dice_roll = roll_dice()

                updated_players[state.current_player_index] = current_player

                return Command(
                    update={
                        "players": updated_players,
                        "last_roll": dice_roll.model_dump(),
                        "game_events": events,
                    }
                )

        elif action == PlayerActionType.USE_JAIL_CARD.value:
            if current_player.jail_cards > 0:
                current_player.jail_cards -= 1
                current_player.in_jail = False
                current_player.jail_turns = 0

                events.append(
                    GameEvent(
                        event_type="jail_card_used",
                        player=current_player.name,
                        description="Used Get Out of Jail Free card",
                    )
                )

                # Now roll dice normally
                dice_roll = roll_dice()

                updated_players[state.current_player_index] = current_player

                return Command(
                    update={
                        "players": updated_players,
                        "last_roll": dice_roll.model_dump(),
                        "game_events": events,
                    }
                )

        # Default: Roll for jail (or if other options failed)
        dice_roll = roll_dice()

        if dice_roll.is_doubles:
            # Doubles gets you out
            current_player.in_jail = False
            current_player.jail_turns = 0

            events.append(
                GameEvent(
                    event_type="jail_doubles_escape",
                    player=current_player.name,
                    description="Rolled doubles to escape jail",
                )
            )
        else:
            # Stay in jail
            current_player.jail_turns += 1

            if current_player.jail_turns >= 3:
                # Must pay fine after 3 turns
                if current_player.can_afford(50):
                    current_player.money -= 50
                    current_player.in_jail = False
                    current_player.jail_turns = 0

                    events.append(
                        GameEvent(
                            event_type="jail_forced_payment",
                            player=current_player.name,
                            description="Forced to pay fine after 3 turns in jail",
                            money_change=-50,
                        )
                    )
                else:
                    # Can't afford fine - bankruptcy (simplified)
                    current_player.bankrupt = True

                    events.append(
                        GameEvent(
                            event_type="bankruptcy",
                            player=current_player.name,
                            description="Went bankrupt in jail",
                        )
                    )
            else:

                events.append(
                    GameEvent(
                        event_type="jail_stay",
                        player=current_player.name,
                        description=f"Stays in jail (turn {current_player.jail_turns}/3)",
                    )
                )

        updated_players[state.current_player_index] = current_player

        return Command(
            update={
                "players": updated_players,
                "last_roll": dice_roll.model_dump(),
                "doubles_rolled": False,  # Jail rolls don't count for doubles streak
                "game_events": events,
            }
        )
