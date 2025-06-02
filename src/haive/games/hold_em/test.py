#!/usr/bin/env python3
"""Test runner for Texas Hold'em game.

This script sets up and runs a Texas Hold'em game with the Rich UI.
"""

import argparse
import sys
from typing import Optional

try:
    from haive.games.hold_em.config import (
        create_cash_game_config,
        create_default_holdem_config,
        create_heads_up_config,
        create_tournament_config,
    )
    from haive.games.hold_em.game_agent import HoldemGameAgent
    from haive.games.hold_em.ui import HoldemRichUI
except ImportError as e:
    print(f"Error importing Haive modules: {e}")
    print("Make sure you have the Haive framework installed and available.")
    sys.exit(1)


def run_default_game():
    """Run a default 4-player Hold'em game."""
    print("🃏 Starting default Texas Hold'em game...")
    print("   4 players, 1000 starting chips, 10/20 blinds")

    config = create_default_holdem_config(
        num_players=4, starting_chips=1000, small_blind=10, big_blind=20
    )

    agent = HoldemGameAgent(config)
    ui = HoldemRichUI()
    ui.run(agent, delay=1.5)


def run_heads_up_game():
    """Run a heads-up (2 player) game."""
    print("🃏 Starting heads-up Texas Hold'em game...")
    print("   2 players, 1000 starting chips, 10/20 blinds")

    config = create_heads_up_config(
        player1_name="Alice", player2_name="Bob", starting_chips=1000, big_blind=20
    )

    agent = HoldemGameAgent(config)
    ui = HoldemRichUI()
    ui.run(agent, delay=1.0)  # Faster for heads-up


def run_tournament_game():
    """Run a tournament-style game."""
    print("🃏 Starting tournament Texas Hold'em game...")
    print("   6 players, 1500 starting chips, escalating blinds")

    config = create_tournament_config(num_players=6, starting_chips=1500)

    agent = HoldemGameAgent(config)
    ui = HoldemRichUI()
    ui.run(agent, delay=2.0)


def run_cash_game():
    """Run a cash game."""
    print("🃏 Starting cash game Texas Hold'em...")
    print("   6 players, 2000 starting chips, 25/50 blinds")

    config = create_cash_game_config(num_players=6, big_blind=50, max_buy_in=2000)

    agent = HoldemGameAgent(config)
    ui = HoldemRichUI()
    ui.run(agent, delay=2.0)


def run_custom_game(
    num_players: int = 4,
    starting_chips: int = 1000,
    big_blind: int = 20,
    max_hands: int = 100,
):
    """Run a custom configured game."""
    print(f"🃏 Starting custom Texas Hold'em game...")
    print(f"   {num_players} players, {starting_chips} starting chips")
    print(f"   {big_blind//2}/{big_blind} blinds, max {max_hands} hands")

    config = create_default_holdem_config(
        num_players=num_players,
        starting_chips=starting_chips,
        small_blind=big_blind // 2,
        big_blind=big_blind,
    )
    config.max_hands = max_hands

    agent = HoldemGameAgent(config)
    ui = HoldemRichUI()
    ui.run(agent, delay=1.5)


def print_game_types():
    """Print available game types."""
    print("\n🃏 Available Texas Hold'em Game Types:")
    print("   default    - 4 players, standard settings")
    print("   heads-up   - 2 players, aggressive play")
    print("   tournament - 6 players, escalating blinds")
    print("   cash       - 6 players, deep stacks")
    print("   custom     - Customizable settings")
    print("\nUse --help for more options.")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Texas Hold'em Game Runner with Rich UI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_holdem.py                    # Run default game
  python test_holdem.py heads-up           # Run heads-up game  
  python test_holdem.py tournament         # Run tournament
  python test_holdem.py custom --players 6 --chips 2000 --bb 50
        """,
    )

    parser.add_argument(
        "game_type",
        nargs="?",
        default="default",
        choices=["default", "heads-up", "tournament", "cash", "custom"],
        help="Type of game to run",
    )

    # Custom game options
    parser.add_argument(
        "--players",
        "-p",
        type=int,
        default=4,
        choices=range(2, 9),
        help="Number of players (2-8, default: 4)",
    )

    parser.add_argument(
        "--chips",
        "-c",
        type=int,
        default=1000,
        help="Starting chips per player (default: 1000)",
    )

    parser.add_argument(
        "--bb",
        "--big-blind",
        type=int,
        default=20,
        help="Big blind amount (default: 20)",
    )

    parser.add_argument(
        "--hands", type=int, default=100, help="Maximum hands to play (default: 100)"
    )

    parser.add_argument(
        "--list-types", "-l", action="store_true", help="List available game types"
    )

    args = parser.parse_args()

    if args.list_types:
        print_game_types()
        return

    try:
        if args.game_type == "default":
            run_default_game()
        elif args.game_type == "heads-up":
            run_heads_up_game()
        elif args.game_type == "tournament":
            run_tournament_game()
        elif args.game_type == "cash":
            run_cash_game()
        elif args.game_type == "custom":
            run_custom_game(
                num_players=args.players,
                starting_chips=args.chips,
                big_blind=args.bb,
                max_hands=args.hands,
            )

    except KeyboardInterrupt:
        print("\n\n🛑 Game interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running game: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()


# Additional utility functions for testing individual components


def test_state_creation():
    """Test state creation and validation."""
    from haive.games.hold_em.state import HoldemState, PlayerState
    from haive.games.hold_em.utils import create_standard_deck, shuffle_deck

    print("Testing state creation...")

    players = [
        PlayerState(player_id="alice", name="Alice", chips=1000, position=0),
        PlayerState(player_id="bob", name="Bob", chips=1000, position=1),
    ]

    state = HoldemState(
        game_id="test",
        players=players,
        deck=shuffle_deck(create_standard_deck()),
        small_blind=10,
        big_blind=20,
    )

    print(f"✅ Created state with {len(state.players)} players")
    print(f"✅ Deck has {len(state.deck)} cards")
    print(f"✅ Total pot: {state.total_pot}")


def test_hand_evaluation():
    """Test hand evaluation functions."""
    from haive.games.holdem.utils import evaluate_hand_simple

    print("Testing hand evaluation...")

    # Test cases
    test_hands = [
        (["Ah", "Kh"], ["Qh", "Jh", "Th"], "Royal Flush"),
        (["As", "Ad"], ["Ac", "Ah", "2s"], "Four Aces"),
        (["7h", "8h"], ["9h", "Th", "Jh"], "Straight Flush"),
        (["2c", "3d"], ["4s", "5h", "6c"], "Straight"),
    ]

    for hole_cards, community_cards, expected in test_hands:
        result = evaluate_hand_simple(hole_cards, community_cards)
        print(f"✅ {hole_cards} + {community_cards} = {result['description']}")


def test_ui_components():
    """Test UI components without running full game."""
    print("Testing UI components...")

    ui = HoldemRichUI()

    # Test with empty state
    header = ui.render_header()
    footer = ui.render_footer()

    print("✅ UI components render without errors")


if __name__ == "__main__":
    # If run with special arguments, run tests
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_state_creation()
        test_hand_evaluation()
        test_ui_components()
    else:
        main()
