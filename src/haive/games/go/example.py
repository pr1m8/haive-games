"""Example of playing a Go game.

This script demonstrates how to initialize and run a Go game
with the Haive framework.
"""

from haive.games.go.agent import GoAgent, run_go_game
from haive.games.go.config import GoAgentConfig

# Run the game
if __name__ == "__main__":
    run_go_game(agent=GoAgent(config=GoAgentConfig()))
