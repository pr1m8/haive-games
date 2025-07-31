"""Example usage of the Monopoly agent.

This example demonstrates how to run a Monopoly game with AI agents.
The game will use the Rich UI to display the game state.

Usage:
    python example.py

"""

import logging

from haive.games.monopoly.config import MonopolyGameAgentConfig
from haive.games.monopoly.main_agent import MonopolyAgent
from haive.games.monopoly.ui_fixed import MonopolyRichUI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Run the example Monopoly game with AI agents."""
    logger.info("Starting Monopoly game with AI agents")

    # Create configuration with AI agents
    config = MonopolyGameAgentConfig(
        name="monopoly_example",
        player_names=["Alice", "Bob", "Charlie", "Diana"],
        max_turns=50,  # Limit turns for demo
        enable_trading=True,
        enable_building=True,
        enable_auctions=True,
        # Set higher recursion limit to avoid errors
        runnable_config={
            "configurable": {"recursion_limit": 500, "thread_id": "monopoly_example"}
        },
    )

    # Create the agent
    agent = MonopolyAgent(config)

    # Create the UI and run the game
    ui = MonopolyRichUI()
    logger.info("Starting Monopoly game with Rich UI...")
    ui.run(agent, delay=1.0)


if __name__ == "__main__":
    main()
