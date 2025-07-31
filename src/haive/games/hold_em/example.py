#!/usr/bin/env python3
"""Example usage of the Texas Hold'em poker implementation.

This example script demonstrates how to:
    - Create and configure a Texas Hold'em game
    - Set up player agents with different playing styles
    - Run a complete game with the Rich UI
    - Access and analyze game results

Run this script directly to see a Hold'em game in action.

"""

import argparse
import logging
import traceback

from haive.games.hold_em import HoldemGameAgent, HoldemGameAgentConfig
from haive.games.hold_em.aug_llms import get_complete_llm_suite
from haive.games.hold_em.config import (
    create_cash_game_config,
    create_default_holdem_config,
    create_heads_up_config,
    create_tournament_config,
)
from haive.games.hold_em.player_agent import HoldemPlayerAgentConfig
from haive.games.hold_em.state import HoldemState
from haive.games.hold_em.ui import HoldemRichUI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("holdem_example")


def create_custom_game(
    player_names: list[str],
    player_styles: list[str] | None = None,
    starting_chips: int = 1000,
    small_blind: int = 10,
    big_blind: int = 20,
    max_hands: int = 50,
) -> HoldemGameAgent:
    """Create a custom Hold'em game with specified players and settings.

    Args:
        player_names: List of player names
        player_styles: Optional list of player styles (defaults to "balanced" for all)
        starting_chips: Starting chips per player
        small_blind: Small blind amount
        big_blind: Big blind amount
        max_hands: Maximum hands to play

    Returns:
        HoldemGameAgent: Configured game agent ready to run

    """
    if player_styles is None:
        player_styles = ["balanced"] * len(player_names)

    # Ensure player_styles is the same length as player_names
    if len(player_styles) != len(player_names):
        player_styles = player_styles[: len(player_names)]
        player_styles.extend(["balanced"] * (len(player_names) - len(player_styles)))

    logger.info(f"Creating custom game with {len(player_names)} players")
    logger.info(f"Player lineup: {', '.join(player_names)}")
    logger.info(f"Styles: {', '.join(player_styles)}")
    logger.info(f"Starting chips: {starting_chips}, Blinds: {small_blind}/{big_blind}")

    # Create player configurations
    player_configs = []
    for i, (name, style) in enumerate(zip(player_names, player_styles, strict=False)):
        logger.info(f"Setting up {name} ({style} style)")

        # Create specialized LLMs for this player
        player_engines = get_complete_llm_suite(style)
        logger.info(f"Created {len(player_engines)} specialized engines for {name}")

        # Create player config
        player_config = HoldemPlayerAgentConfig(
            name=f"player_{name.lower()}",
            player_name=name,
            player_style=style,
            risk_tolerance=0.3 + (i * 0.1),  # Vary risk tolerance
            engines=player_engines,
            state_schema=HoldemState,
        )
        player_configs.append(player_config)
        logger.info(f"Added player: {name} ({style})")

    # Create main game configuration
    game_config = HoldemGameAgentConfig(
        name="custom_holdem_game",
        state_schema=HoldemState,
        max_players=len(player_names),
        small_blind=small_blind,
        big_blind=big_blind,
        starting_chips=starting_chips,
        max_hands=max_hands,
        player_configs=player_configs,
    )

    # Create the game agent
    agent = HoldemGameAgent(game_config)
    logger.info("Game agent created successfully")

    return agent


def run_example_game(game_type: str = "default", delay: float = 1.5):
    """Run an example Hold'em game with the specified configuration.

    Args:
        game_type: Type of game to run ("default", "heads-up", "tournament", "cash", "custom")
        delay: Delay between UI updates (seconds)

    """
    try:
        if game_type == "default":
            logger.info("Running default Hold'em game")
            config = create_default_holdem_config(
                num_players=4, starting_chips=1000, small_blind=10, big_blind=20
            )
            agent = HoldemGameAgent(config)

        elif game_type == "heads-up":
            logger.info("Running heads-up Hold'em game")
            config = create_heads_up_config(
                player1_name="Alice",
                player2_name="Bob",
                starting_chips=1000,
                big_blind=20,
            )
            agent = HoldemGameAgent(config)

        elif game_type == "tournament":
            logger.info("Running tournament Hold'em game")
            config = create_tournament_config(num_players=6, starting_chips=1500)
            agent = HoldemGameAgent(config)

        elif game_type == "cash":
            logger.info("Running cash game Hold'em")
            config = create_cash_game_config(
                num_players=6, big_blind=20, max_buy_in=2000
            )
            agent = HoldemGameAgent(config)

        elif game_type == "custom":
            logger.info("Running custom Hold'em game")
            player_names = ["Alice", "Bob", "Charlie", "Diana"]
            player_styles = ["tight", "loose", "aggressive", "balanced"]
            agent = create_custom_game(
                player_names=player_names,
                player_styles=player_styles,
                starting_chips=1000,
                small_blind=10,
                big_blind=20,
            )

        else:
            logger.error(f"Unknown game type: {game_type}")
            return

        # Run the game with the Rich UI
        ui = HoldemRichUI()
        logger.info("Starting game with Rich UI")
        ui.run(agent, delay=delay)
        logger.info("Game completed")

    except Exception as e:
        logger.error(f"Error running game: {e}")

        logger.error(traceback.format_exc())


def analyze_game_results(agent: HoldemGameAgent):
    """Analyze the results of a completed game.

    Args:
        agent: The game agent after running a game

    """
    # Access the final state
    if not hasattr(agent, "app") or not hasattr(agent.app, "last_state"):
        logger.error("No game results available for analysis")
        return

    final_state = agent.app.last_state
    if not final_state:
        logger.error("No final state available")
        return

    # Print game summary
    logger.info("\n=== GAME SUMMARY ===")
    logger.info(f"Hands played: {final_state.hand_number - 1}")
    logger.info(f"Final pot: {final_state.total_pot}")

    # Player results
    logger.info("\n=== PLAYER RESULTS ===")
    for player in final_state.players:
        logger.info(
            f"{player.name}: {player.chips} chips, Status: {player.status.value}"
        )

    # Hand history
    if final_state.hand_history:
        logger.info("\n=== HAND HISTORY ===")
        for _i, hand in enumerate(final_state.hand_history[-5:]):  # Last 5 hands
            winner_name = "Unknown"
            for player in final_state.players:
                if player.player_id == hand.get("winner"):
                    winner_name = player.name
                    break
            logger.info(
                f"Hand #{hand.get('hand_number')}: {winner_name} won {
                    hand.get('pot_size')
                } chips"
            )


def main():
    """Main entry point with command line argument handling."""
    parser = argparse.ArgumentParser(
        description="Texas Hold'em Example Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python example.py                   # Run default game
  python example.py --type heads-up   # Run heads-up game
  python example.py --type tournament # Run tournament
  python example.py --type custom     # Run custom game
        """,
    )

    parser.add_argument(
        "--type",
        "-t",
        default="default",
        choices=["default", "heads-up", "tournament", "cash", "custom"],
        help="Type of game to run",
    )

    parser.add_argument(
        "--delay",
        "-d",
        type=float,
        default=1.5,
        help="Delay between UI updates (seconds)",
    )

    parser.add_argument(
        "--analyze",
        "-a",
        action="store_true",
        help="Analyze game results after completion",
    )

    args = parser.parse_args()

    # Run the specified game
    run_example_game(args.type, args.delay)


if __name__ == "__main__":
    # Run a quick heads-up game for testing
    print("Running quick Hold'em heads-up game example...")
    run_example_game("heads-up", delay=0.1)
    print("\nExample completed!")
