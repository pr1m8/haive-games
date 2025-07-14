"""Example Reversi (Othello) game demonstrating the Haive Reversi implementation.

This module provides a simple example of running a Reversi game with AI players
using the Haive framework. Reversi, also known as Othello, is a strategy board
game where players flip opponent pieces by trapping them between their own pieces.

The example demonstrates:
    - Creating a Reversi agent with default configuration
    - Running a complete game with visual board display
    - AI players making strategic moves
    - Automatic piece flipping and rule enforcement
    - Winner determination based on final piece count

Usage:
    Run directly:
        $ python example.py

    Import and use:
        >>> from haive.games.reversi.agent import ReversiAgent
        >>> agent = ReversiAgent()
        >>> final_state = agent.run_game(visualize=True)

Game Rules:
    - Players take turns placing pieces on the board
    - Valid moves must flip at least one opponent piece
    - Pieces are flipped when trapped between two of your pieces
    - Game ends when no valid moves remain
    - Winner has the most pieces on the board

Example:
    >>> # Create and run a Reversi game
    >>> agent = ReversiAgent()
    >>> state = agent.run_game(visualize=True)
    >>> print(f"Winner: {state.get('winner', 'Draw')}")
"""

from haive.games.reversi.agent import ReversiAgent

# Initialize the agent
a = ReversiAgent()
a.run_game(visualize=True)
# Run the game with visualization
final_state = a.run_game(visualize=True)

# Print the winner
if final_state.get("game_status", "") == "draw":
    print("\nGame ended in a draw!")
elif final_state.get("game_status", "").endswith("_win"):
    winner_symbol = final_state["game_status"].split("_")[0]
    winner_player = (
        final_state["player_B"] if winner_symbol == "B" else final_state["player_W"]
    )
    print(
        f"\nWinner: {winner_symbol} ({'Black' if winner_symbol == 'B' else 'White'} - {winner_player})"
    )
