"""Example script for running a full Checkers game with LLM agents.

This script demonstrates how to create and run a checkers game with
LLM-powered agents, using the default configuration settings.

The example shows:
    - How to initialize a checkers agent
    - How to run a complete game with default parameters
    - Basic usage of the CheckersAgent API

To run this example:
    python -m haive.games.checkers.example

Example Output:
    Game starts with initial board setup
    LLM agents alternate moves until game conclusion
    Final game state and winner displayed
"""

from haive.games.checkers.agent import CheckersAgent, CheckersAgentConfig
from haive.games.checkers.state import CheckersState


def run_example_game():
    """Run a complete checkers game with default configuration.

    Creates a checkers agent with default configuration and runs a full game
    with visualization enabled. This demonstrates the basic usage pattern for
    the checkers module.

    Returns:
        None

    Examples:
        >>> run_example_game()
        # Game visualization and progress will display in terminal
    """
    # Initialize a checkers agent with default configuration
    agent = CheckersAgent(CheckersAgentConfig())

    # Run a complete game with default parameters
    agent.run_game()


if __name__ == "__main__":
    run_example_game()
