#!/usr/bin/env python3
"""Find the EXACT point where tic tac toe example hangs."""

import signal
import sys
import time


def timeout_handler(signum, frame):
    print("\n🚨 TIMEOUT: Hung at current execution point!")
    print("🚨 This is where the hang occurs!")
    sys.exit(1)


def main():
    print("🔍 EXACT HANG POINT DEBUG")
    print("=" * 50)

    # Set timeout handler
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(20)  # 20 second timeout

    try:
        print("Step 1: Importing TicTacToeAgent...")
        from haive.games.tic_tac_toe.agent import TicTacToeAgent

        print("✅ Step 1 complete")

        print("\nStep 2: Creating TicTacToeAgent()...")
        start_time = time.time()
        agent = TicTacToeAgent()
        elapsed = time.time() - start_time
        print(f"✅ Step 2 complete in {elapsed:.3f}s")

        print("\nStep 3: Testing agent.run_game()...")
        start_time = time.time()
        print("   🚨 About to call agent.run_game() - this might be the hang point...")

        # This is probably where it hangs
        result = agent.run_game(visualize=True)

        elapsed = time.time() - start_time
        print(f"✅ Step 3 complete in {elapsed:.3f}s")
        print(f"   Result: {type(result)}")

        print("\n🎉 No hang detected - example completed successfully!")

    except KeyboardInterrupt:
        print("\n⏹️  Manually interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
    finally:
        signal.alarm(0)  # Cancel timeout


if __name__ == "__main__":
    main()
