#!/usr/bin/env python3
"""Test tic tac toe example with the visualization fix applied."""

import time


def main():
    print("🎮 TIC TAC TOE EXAMPLE - WITH VISUALIZATION FIX")
    print("=" * 60)

    try:
        print("Step 1: Import components")
        from haive.games.tic_tac_toe.agent import TicTacToeAgent
        from haive.games.tic_tac_toe.config import TicTacToeConfig

        print("✅ Imports successful")

        print("\nStep 2: Create config with visualization disabled")
        config = TicTacToeConfig(
            name="fixed_example",
            visualize=False,  # FIX: Disable visualization to prevent hang
            enable_analysis=True,  # Keep analysis for interesting gameplay
            first_player="X",
            player_X="player1",  # Fixed: Must be "player1" or "player2"
            player_O="player2",  # Fixed: Must be "player1" or "player2"
        )
        print(f"✅ Config created: {config.name}")

        print("\nStep 3: Create agent (should be fast now)")
        start_time = time.time()
        agent = TicTacToeAgent(config)
        agent_time = time.time() - start_time
        print(f"✅ Agent created in {agent_time:.3f}s")

        print("\nStep 4: Run actual game with real LLMs")
        print("   🤖 This will make real LLM API calls...")
        game_start = time.time()

        # Run the actual game - this should work now!
        result = agent.run_game(visualize=False)  # Also disable runtime visualization

        game_time = time.time() - game_start
        print(f"✅ Game completed in {game_time:.3f}s!")

        print("\nStep 5: Analyze results")
        print(f"   Result type: {type(result)}")

        if isinstance(result, dict):
            game_status = result.get("game_status", "unknown")
            move_count = len(result.get("move_history", []))
            winner = result.get("winner", "none")

            print(f"   Game status: {game_status}")
            print(f"   Total moves: {move_count}")
            print(f"   Winner: {winner}")

            if "move_history" in result:
                print("   Move history:")
                for i, move in enumerate(
                    result["move_history"][:3]
                ):  # Show first 3 moves
                    print(f"     {i+1}. {move}")
                if move_count > 3:
                    print(f"     ... and {move_count-3} more moves")

        print("\n🎉 SUCCESS: Tic Tac Toe example runs without hanging!")
        print(f"💡 Total execution time: {(agent_time + game_time):.3f}s")

        return result

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n📊 FINAL RESULT: {result.get('game_status', 'unknown')}")
    else:
        print("\n❌ FAILED: No result returned")
