"""Run a Monopoly game with the fixed UI.

This script demonstrates how to run a Monopoly game with the fixed UI.
"""

import logging

from haive.games.monopoly.config import MonopolyGameAgentConfig
from haive.games.monopoly.main_agent import MonopolyAgent
from haive.games.monopoly.ui_fixed import MonopolyRichUI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Run a Monopoly game with the fixed UI."""
    logger.info("Starting Monopoly game...")

    # Create configuration with more explicit settings
    config = MonopolyGameAgentConfig(
        name="monopoly_demo",
        player_names=["Alice", "Bob", "Charlie", "Diana"],
        max_turns=50,  # Shorter for testing
        enable_trading=False,
        enable_building=False,
        enable_auctions=False,
        # Set higher recursion limit to avoid errors
        runnable_config={
            "configurable": {"recursion_limit": 500, "thread_id": "monopoly_game_demo"}
        },
    )

    # Create the agent
    agent = MonopolyAgent(config)

    # Create the UI and run the game
    ui = MonopolyRichUI()
    ui.run(agent, delay=1.0)


if __name__ == "__main__":
    main()
