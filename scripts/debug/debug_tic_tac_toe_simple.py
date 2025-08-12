#!/usr/bin/env python3
"""Debug version of tic tac toe example - step by step with timeouts."""

import sys
import time


def print_step(step: str):
    """Print debugging step."""
    print(f"\n🐛 DEBUG: {step}")
    sys.stdout.flush()


def main():
    """Debug tic tac toe step by step."""
    print_step("Starting debug session")

    try:
        print_step("Importing TicTacToe components...")
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        print_step("✅ Imports successful")

        print_step("Testing basic state creation...")
        state = TicTacToeStateManager.initialize()
        print(f"   State created: {type(state)}")
        print(f"   Board size: {len(state.board)} x {len(state.board[0])}")
        print(f"   Available attributes: {dir(state)}")

        # Find turn-related attributes
        turn_attrs = [
            attr
            for attr in dir(state)
            if "turn" in attr.lower() or "player" in attr.lower()
        ]
        print(f"   Turn/player attributes: {turn_attrs}")

        if hasattr(state, "turn"):
            print(f"   Turn: {state.turn}")
        if hasattr(state, "current_player_name"):
            print(f"   Current player name: {state.current_player_name}")

        print_step("✅ Basic state creation successful")

        print_step("Testing move creation...")
        move = TicTacToeMove(row=1, col=1, player="X")
        print(f"   Move created: {move}")
        print_step("✅ Move creation successful")

        print_step("Testing move execution...")

        # Check available methods
        manager_methods = [
            method
            for method in dir(TicTacToeStateManager)
            if not method.startswith("_")
        ]
        print(f"   StateManager methods: {manager_methods}")

        # Try different method names
        if hasattr(TicTacToeStateManager, "apply_move"):
            new_state = TicTacToeStateManager.apply_move(state, move)
            print("   Move executed successfully with apply_move")
            print(f"   Game status: {new_state.game_status}")
        elif hasattr(TicTacToeStateManager, "make_move"):
            new_state = TicTacToeStateManager.make_move(state, move)
            print("   Move executed successfully with make_move")
        else:
            print("   No recognized move method found")
            new_state = state  # Just use original for now

        print_step("✅ Move execution successful (or skipped)")

        # Now try the agent part - use the ACTUAL TicTacToeAgent
        print_step(
            "NOW TESTING REAL TICTACTOE AGENT INITIALIZATION (this is where it might hang)..."
        )
        print(
            "   About to import TicTacToeAgent - this might hang if LLM config is missing"
        )

        try:
            from haive.games.tic_tac_toe.agent import TicTacToeAgent

            print_step("✅ TicTacToeAgent import successful")

            print_step("About to create agent (this is the likely hang point)...")
            print("   Creating TicTacToeAgent with default config...")

            # Set a timeout for agent creation
            start_time = time.time()

            print_step("Creating agent with NO CONFIG (like the example does)...")
            print("   This is probably where it hangs waiting for LLM responses...")

            # This is exactly what the example does - no config
            agent = TicTacToeAgent()

            elapsed = time.time() - start_time
            print_step(f"✅ Agent created in {elapsed:.2f}s")

            print_step("Testing agent methods...")
            agent_methods = [
                method
                for method in dir(agent)
                if not method.startswith("_") and callable(getattr(agent, method))
            ]
            print(f"   Agent methods: {agent_methods[:10]}...")

        except Exception as e:
            print_step(f"❌ TicTacToe Agent creation failed: {e}")
            print(f"   Exception type: {type(e)}")
            import traceback

            traceback.print_exc()

    except Exception as e:
        print_step(f"❌ Error in step: {e}")
        import traceback

        traceback.print_exc()

    print_step("Debug session complete")


if __name__ == "__main__":
    main()
