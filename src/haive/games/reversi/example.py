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
