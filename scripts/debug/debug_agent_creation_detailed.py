#!/usr/bin/env python3
"""Debug TicTacToeAgent creation step by step to find the exact hanging point."""

import signal
import sys
import time
import traceback


def timeout_handler(signum, frame):
    print("\n🚨 TIMEOUT: Hung at this exact line!")
    print("Stack trace at hang point:")
    traceback.print_stack(frame)
    sys.exit(1)


def debug_step(step_name):
    print(f"🔍 {step_name}")
    sys.stdout.flush()
    time.sleep(0.1)  # Small delay to ensure output appears


def main():
    print("🛠️  DETAILED AGENT CREATION DEBUG")
    print("=" * 60)

    # Set timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(30)  # 30 second timeout

    try:
        debug_step("Step 1: Importing TicTacToeAgent class")
        from haive.games.tic_tac_toe.agent import TicTacToeAgent

        debug_step("✅ Import successful")

        debug_step("Step 2: Checking TicTacToeAgent.__init__ method")
        init_method = TicTacToeAgent.__init__
        debug_step(f"✅ __init__ method found: {init_method}")

        debug_step("Step 3: About to call TicTacToeAgent() constructor")
        debug_step("   This is where the hang occurs...")

        start_time = time.time()

        # Try to debug what happens inside __init__
        debug_step("Step 3.1: Calling TicTacToeAgent() now...")

        # This is where it hangs - let's see if we can catch it
        agent = TicTacToeAgent()

        elapsed = time.time() - start_time
        debug_step(f"✅ Agent created successfully in {elapsed:.3f}s!")
        debug_step(f"   Agent type: {type(agent)}")
        debug_step(f"   Agent name: {getattr(agent, 'name', 'unknown')}")

        debug_step("Step 4: Testing basic agent methods")
        if hasattr(agent, "run_game"):
            debug_step("✅ Agent has run_game method")
        else:
            debug_step("❌ Agent missing run_game method")

        print("\n🎉 SUCCESS: Agent creation completed without hanging!")

    except Exception as e:
        debug_step(f"❌ Exception during agent creation: {e}")
        debug_step(f"   Exception type: {type(e)}")
        traceback.print_exc()
    except KeyboardInterrupt:
        debug_step("⏹️  Manually interrupted")
    finally:
        signal.alarm(0)  # Cancel timeout


if __name__ == "__main__":
    main()
