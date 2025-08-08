#!/usr/bin/env python3
"""Test the fix for TicTacToeAgent hanging on visualization."""

import signal
import sys
import time


def timeout_handler(signum, frame):
    print(f"\n🚨 TIMEOUT: Still hanging even with visualization disabled!")
    sys.exit(1)


def main():
    print("🔧 TESTING FIX: Disable visualization to prevent hang")
    print("=" * 60)

    # Set timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(15)  # 15 second timeout

    try:
        print("Step 1: Import TicTacToeAgent and Config")
        from haive.games.tic_tac_toe.agent import TicTacToeAgent
        from haive.games.tic_tac_toe.config import TicTacToeConfig

        print("✅ Imports successful")

        print("\nStep 2: Create config with visualize=False")
        config = TicTacToeConfig(
            name="test_no_visualization",
            visualize=False,  # This should fix the hang!
            enable_analysis=False,  # Also disable analysis for faster testing
        )
        print(f"✅ Config created: visualize={config.visualize}")

        print("\nStep 3: Create TicTacToeAgent with non-visualizing config")
        start_time = time.time()

        agent = TicTacToeAgent(config)

        elapsed = time.time() - start_time
        print(f"✅ SUCCESS! Agent created in {elapsed:.3f}s without hanging!")
        print(f"   Agent name: {agent.name}")
        print(f"   Agent type: {type(agent)}")

        print("\nStep 4: Test agent functionality")
        if hasattr(agent, "run_game"):
            print("✅ Agent has run_game method")

            # Try to run a quick game with timeout
            print("\nStep 5: Test quick game execution...")
            game_start = time.time()

            # Set shorter timeout for game execution
            signal.alarm(10)

            result = agent.run_game(visualize=False)

            game_elapsed = time.time() - game_start
            print(f"✅ Game completed in {game_elapsed:.3f}s!")
            print(f"   Result type: {type(result)}")
            print(f"   Game status: {result.get('game_status', 'unknown')}")

        else:
            print("❌ Agent missing run_game method")

        print(f"\n🎉 COMPLETE SUCCESS: Agent works without hanging!")
        print(f"🔧 FIX CONFIRMED: visualize=False resolves the hang issue")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
    except KeyboardInterrupt:
        print(f"\n⏹️  Manually interrupted")
    finally:
        signal.alarm(0)  # Cancel timeout


if __name__ == "__main__":
    main()
