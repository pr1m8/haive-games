"""Simple demo for testing the Monopoly game without LangGraph integration.

This script demonstrates the core functionality of the Monopoly game:
- Board setup
- Player movement
- Property purchasing
- Rent payments
- Game events

Usage:
    python simple_demo.py
"""

from rich.console import Console

from haive.games.monopoly.models import GameEvent, Property, PropertyColor, PropertyType
from haive.games.monopoly.state import MonopolyState
from haive.games.monopoly.utils import (
    calculate_rent,
    create_board,
    create_players,
    get_property_at_position,
    move_player,
    roll_dice,
)

# Setup console for pretty printing
console = Console()


def print_divider():
    """Print a divider line."""
    console.print("=" * 80, style="cyan")


def print_property(property_obj: Property):
    """Print property details."""
    if property_obj.property_type == PropertyType.SPECIAL:
        console.print(f"[bold]{property_obj.name}[/bold] (Special)")
        return

    owner_text = f"Owned by {property_obj.owner}" if property_obj.owner else "Unowned"
    color_style = property_obj.color.value

    console.print(
        f"[bold]{property_obj.name}[/bold] - [bold {color_style}]■[/bold {
            color_style
        }] - {owner_text}"
    )
    console.print(f"  Price: ${property_obj.price} | Rent: ${property_obj.rent[0]}")

    if property_obj.mortgaged:
        console.print(f"  [red]MORTGAGED[/red] for ${property_obj.mortgage_value}")
    elif property_obj.hotel:
        console.print(f"  [bold red]HOTEL[/bold red] - Rent: ${property_obj.rent[5]}")
    elif property_obj.houses > 0:
        houses = "■ " * property_obj.houses
        console.print(
            f"  [bold green]{houses}[/bold green] - Rent: ${property_obj.rent[property_obj.houses]}"
        )


def print_player_status(state: MonopolyState):
    """Print current status of all players."""
    console.print("\n[bold]Player Status:[/bold]")

    table = state.players.copy()
    # Sort so current player is first
    if state.current_player_index < len(table):
        current = table[state.current_player_index]
        table.pop(state.current_player_index)
        table.insert(0, current)

    for player in table:
        is_current = player.name == state.current_player.name
        name_style = "bold green" if is_current else "bold"

        console.print(f"[{name_style}]{player.name}[/{name_style}] - ${player.money}")

        if player.properties:
            property_text = ", ".join(player.properties)
            console.print(f"  Properties: {property_text}")

        if player.in_jail:
            console.print(f"  [red]IN JAIL[/red] (Turn {player.jail_turns}/3)")

        if player.bankrupt:
            console.print("  [red]BANKRUPT[/red]")

        # Print current position name
        position = player.position
        position_data = get_property_at_position(position)
        if position_data:
            console.print(f"  Position: {position_data['name']} ({position})")
        else:
            console.print(f"  Position: {position}")

        console.print("")


def print_recent_events(events: list[GameEvent], count: int = 5):
    """Print recent game events."""
    if not events:
        return

    recent = events[-count:]
    console.print("\n[bold]Recent Events:[/bold]")

    for event in reversed(recent):
        # Style based on event type
        if event.event_type in ["property_purchase", "rent_payment"]:
            style = "green"
        elif event.event_type in ["bankruptcy", "go_to_jail"]:
            style = "red"
        elif event.event_type == "dice_roll":
            style = "cyan"
        else:
            style = "white"

        # Money indicator
        money_indicator = ""
        if event.money_change > 0:
            money_indicator = f" [green](+${event.money_change})[/green]"
        elif event.money_change < 0:
            money_indicator = f" [red](${event.money_change})[/red]"

        console.print(
            f"• [bold]{event.player}[/bold]: [{style}]{event.description}[/{style}]{
                money_indicator
            }"
        )


def handle_property_landing(state: MonopolyState, position: int) -> list[GameEvent]:
    """Handle a player landing on a property."""
    events = []
    current_player = state.current_player

    # Get position data
    position_data = get_property_at_position(position)
    if not position_data:
        console.print(f"[red]Error: Invalid position {position}[/red]")
        return events

    property_name = position_data["name"]
    console.print(f"\n[bold]🎯 {current_player.name} landed on {property_name}[/bold]")

    # Handle special positions
    if position_data["type"] == PropertyType.SPECIAL:
        if property_name == "Income Tax":
            tax = 200
            current_player.money -= tax
            console.print(f"[red]Paid ${tax} in Income Tax[/red]")
            events.append(
                GameEvent(
                    event_type="tax_payment",
                    player=current_player.name,
                    description=f"Paid ${tax} Income Tax",
                    money_change=-tax,
                )
            )
        elif property_name == "Luxury Tax":
            tax = 75
            current_player.money -= tax
            console.print(f"[red]Paid ${tax} in Luxury Tax[/red]")
            events.append(
                GameEvent(
                    event_type="tax_payment",
                    player=current_player.name,
                    description=f"Paid ${tax} Luxury Tax",
                    money_change=-tax,
                )
            )
        elif property_name == "Go To Jail":
            current_player.position = 10  # Jail position
            current_player.in_jail = True
            console.print("[red]Go to Jail! Moving to Jail...[/red]")
            events.append(
                GameEvent(
                    event_type="go_to_jail",
                    player=current_player.name,
                    description="Sent to Jail",
                )
            )
        elif property_name in ["Chance", "Community Chest"]:
            console.print(
                f"[yellow]Draw a {property_name} card (not implemented in demo)[/yellow]"
            )
        else:
            console.print(f"[blue]On {property_name} - no action needed[/blue]")

        return events

    # Handle regular property
    property_obj = state.properties.get(property_name)

    if not property_obj:
        console.print(
            f"[red]Warning: Property '{property_name}' not found in state.[/red]"
        )
        console.print("Creating property from board data...")

        # Create property from board data
        property_obj = Property(
            name=property_name,
            position=position,
            property_type=PropertyType(position_data["type"]),
            color=PropertyColor(position_data["color"]),
            price=position_data.get("price", 0),
            rent=position_data.get("rent", [0, 0, 0, 0, 0, 0]),
            house_cost=position_data.get("house_cost", 0),
            mortgage_value=position_data.get("mortgage_value", 0),
        )

        # Add to state
        state.properties[property_name] = property_obj

        events.append(
            GameEvent(
                event_type="property_added",
                player=current_player.name,
                description=f"Property {property_name} added to game",
                property_involved=property_name,
            )
        )

    print_property(property_obj)

    # Check if property is owned
    if property_obj.owner is None:
        # Property is unowned - offer to buy
        if property_obj.price <= current_player.money:
            # In this demo, always buy if can afford
            console.print(
                f"\n[green]Buying {property_name} for ${property_obj.price}[/green]"
            )
            current_player.money -= property_obj.price
            current_player.properties.append(property_name)
            property_obj.owner = current_player.name

            events.append(
                GameEvent(
                    event_type="property_purchase",
                    player=current_player.name,
                    description=f"Purchased {property_name}",
                    money_change=-property_obj.price,
                    property_involved=property_name,
                )
            )
        else:
            console.print(
                f"\n[red]Cannot afford {property_name} (${property_obj.price})[/red]"
            )
            events.append(
                GameEvent(
                    event_type="property_pass",
                    player=current_player.name,
                    description=f"Could not afford {property_name}",
                    property_involved=property_name,
                )
            )
    elif property_obj.owner == current_player.name:
        console.print("\n[blue]You own this property - no action needed[/blue]")
    else:
        # Pay rent to owner
        owner = None
        for player in state.players:
            if player.name == property_obj.owner:
                owner = player
                break

        if not owner:
            console.print(f"[red]Error: Owner '{property_obj.owner}' not found[/red]")
            return events

        # Calculate rent
        dice_total = state.last_roll.total if state.last_roll else 0
        rent = calculate_rent(property_obj, state, dice_total)

        if rent <= 0:
            console.print(
                "\n[blue]No rent due (property mortgaged or special circumstances)[/blue]"
            )
            return events

        console.print(
            f"\n[yellow]Property owned by {owner.name} - rent: ${rent}[/yellow]"
        )

        # Pay rent
        if current_player.money >= rent:
            current_player.money -= rent
            owner.money += rent

            console.print(f"[red]Paid ${rent} in rent to {owner.name}[/red]")

            events.append(
                GameEvent(
                    event_type="rent_payment",
                    player=current_player.name,
                    description=f"Paid ${rent} rent to {owner.name}",
                    money_change=-rent,
                    property_involved=property_name,
                )
            )
        else:
            # Simplified bankruptcy
            console.print(
                f"[bold red]Cannot afford ${rent} rent - {current_player.name} goes BANKRUPT![/bold red]"
            )
            current_player.bankrupt = True

            events.append(
                GameEvent(
                    event_type="bankruptcy",
                    player=current_player.name,
                    description=f"Went bankrupt owing ${rent} rent to {owner.name}",
                    property_involved=property_name,
                )
            )

    return events


def run_demo(turns: int = 20):
    """Run a simple Monopoly game demo."""
    # Initialize game state
    players = create_players(["Alice", "Bob", "Charlie"])
    properties = create_board()

    # Ensure Vermont Avenue exists in properties
    if "Vermont Avenue" not in properties:
        # Get position 8 (Vermont Avenue)
        vermont_data = get_property_at_position(8)
        if vermont_data:
            properties["Vermont Avenue"] = Property(
                name="Vermont Avenue",
                position=8,
                property_type=PropertyType.STREET,
                color=PropertyColor.LIGHT_BLUE,
                price=100,
                rent=[6, 30, 90, 270, 400, 550],
                house_cost=50,
                mortgage_value=50,
            )

    state = MonopolyState(
        players=players,
        properties=properties,
        current_player_index=0,
        turn_number=1,
        game_events=[],
    )

    console.print("[bold green]🎮 MONOPOLY DEMO[/bold green]")
    console.print("A simplified demonstration of the Monopoly game\n")

    # Show initial state
    print_player_status(state)

    # Game loop
    for turn in range(1, turns + 1):
        if len(state.active_players) <= 1:
            console.print("[bold red]Game over - only one player remains![/bold red]")
            break

        current_player = state.current_player

        if current_player.bankrupt:
            console.print(
                f"[red]{current_player.name} is bankrupt - skipping turn[/red]"
            )
            state.next_player()
            continue

        print_divider()
        console.print(f"[bold]Turn {turn}: {current_player.name}'s turn[/bold]")

        # Roll dice
        dice = roll_dice()
        state.last_roll = dice

        console.print(
            f"\n🎲 [bold]{current_player.name}[/bold] rolls: {dice.die1} + {dice.die2} = {dice.total}"
        )
        state.game_events.append(
            GameEvent(
                event_type="dice_roll",
                player=current_player.name,
                description=f"Rolled {dice.die1} and {dice.die2} for {dice.total}",
                details={"dice": [dice.die1, dice.die2]},
            )
        )

        # Handle jail
        if current_player.in_jail:
            if dice.is_doubles:
                current_player.in_jail = False
                console.print("[green]Rolled doubles! Out of jail![/green]")
                state.game_events.append(
                    GameEvent(
                        event_type="jail_release",
                        player=current_player.name,
                        description="Got out of jail by rolling doubles",
                    )
                )
            else:
                current_player.jail_turns += 1
                if current_player.jail_turns >= 3:
                    # Must pay to get out after 3 turns
                    if current_player.money >= 50:
                        current_player.money -= 50
                        current_player.in_jail = False
                        console.print(
                            "[yellow]Paid $50 to get out of jail after 3 turns[/yellow]"
                        )
                        state.game_events.append(
                            GameEvent(
                                event_type="jail_release",
                                player=current_player.name,
                                description="Paid $50 to get out of jail after 3 turns",
                                money_change=-50,
                            )
                        )
                    else:
                        # Simplified bankruptcy
                        console.print(
                            "[bold red]Cannot afford jail fine - goes BANKRUPT![/bold red]"
                        )
                        current_player.bankrupt = True
                        state.game_events.append(
                            GameEvent(
                                event_type="bankruptcy",
                                player=current_player.name,
                                description="Went bankrupt unable to pay jail fine",
                            )
                        )
                        state.next_player()
                        continue
                else:
                    console.print(
                        f"[red]Stays in jail (turn {current_player.jail_turns}/3)[/red]"
                    )
                    state.game_events.append(
                        GameEvent(
                            event_type="jail_stay",
                            player=current_player.name,
                            description=f"Stays in jail (turn {
                                current_player.jail_turns
                            }/3)",
                        )
                    )
                    state.next_player()
                    continue

        # Move player
        old_position = current_player.position
        new_position, passed_go = move_player(current_player, dice)

        console.print(f"\n🚶 Moves from {old_position} to {new_position}")

        # Handle passing GO
        if passed_go:
            current_player.money += 200
            console.print("[green]Passed GO! Collect $200[/green]")
            state.game_events.append(
                GameEvent(
                    event_type="pass_go",
                    player=current_player.name,
                    description="Passed GO and collected $200",
                    money_change=200,
                )
            )

        # Handle landing on property
        events = handle_property_landing(state, new_position)
        state.game_events.extend(events)

        # Print recent events and status
        print_recent_events(state.game_events)
        print_player_status(state)

        # Next player
        state.next_player()

        # Wait for user to continue
        input("\nPress Enter for next turn...")

    # Game summary
    print_divider()
    console.print("[bold green]🏁 Game Summary[/bold green]")

    # Determine winner
    active_players = state.active_players
    if len(active_players) == 1:
        winner = active_players[0]
        console.print(
            f"[bold green]Winner: {winner.name} with ${winner.money}[/bold green]"
        )
    else:
        # Find player with highest net worth
        best_player = None
        best_worth = -1

        for player in active_players:
            net_worth = player.net_worth(state.properties)
            if net_worth > best_worth:
                best_worth = net_worth
                best_player = player

        if best_player:
            console.print(
                f"[bold green]Highest net worth: {best_player.name} with ${
                    best_worth
                }[/bold green]"
            )

    # Print final player status
    print_player_status(state)

    # Print statistics
    property_owners = {}
    for prop_name, prop in state.properties.items():
        if prop.owner:
            if prop.owner not in property_owners:
                property_owners[prop.owner] = []
            property_owners[prop.owner].append(prop_name)

    console.print("\n[bold]Property Ownership:[/bold]")
    for owner, props in property_owners.items():
        console.print(f"[bold]{owner}[/bold]: {len(props)} properties")
        for prop in props:
            color = state.properties[prop].color.value
            console.print(f"  [{color}]■[/{color}] {prop}")


if __name__ == "__main__":
    run_demo(20)
