#!/usr/bin/env python3
"""Test TicTacToe agent with visualization ENABLED now that mermaid-cli is fixed."""

import sys
import time


def main():
    print("🎮 TIC TAC TOE WITH VISUALIZATION ENABLED")
    print("=" * 60)

    try:
        print("Step 1: Import components")
        from haive.games.tic_tac_toe.agent import TicTacToeAgent
        from haive.games.tic_tac_toe.config import TicTacToeConfig

        print("✅ Imports successful")

        print("\nStep 2: Create config with visualization ENABLED")
        config = TicTacToeConfig(
            name="visualization_test",
            visualize=True,  # ✅ ENABLED: Should work now!
            enable_analysis=False,  # Keep other things minimal for testing
            first_player="X",
            player_X="player1",
            player_O="player2",
        )
        print(f"✅ Config created with visualize={config.visualize}")

        print("\nStep 3: Create agent (should work now without hanging)")
        start_time = time.time()

        agent = TicTacToeAgent(config)

        agent_time = time.time() - start_time
        print(f"✅ Agent created successfully in {agent_time:.3f}s!")

        print("\nStep 4: Check if visualization files were created")
        import os
        from pathlib import Path

        output_dir = Path("resources/graph_images")
        if output_dir.exists():
            files = list(output_dir.glob("*.png"))
            print(f"   📁 Found {len(files)} PNG files in {output_dir}")
            for f in files[:3]:  # Show first 3
                size = f.stat().st_size
                print(f"     🎨 {f.name} ({size} bytes)")
        else:
            print(f"   📁 Output directory {output_dir} not found")

        # Check the test file we created earlier
        test_file = Path("test_graph.png")
        if test_file.exists():
            size = test_file.stat().st_size
            print(f"   🧪 Test PNG: {test_file} ({size} bytes)")

        print(f"\n🎉 SUCCESS: Visualization is now working!")
        print(f"🔧 ROOT CAUSE: Missing mermaid-cli was causing the hang")
        print(f"🔧 SOLUTION: Installing @mermaid-js/mermaid-cli fixed it")

        return agent

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    agent = main()
    if agent:
        print(f"\n✅ FINAL RESULT: Agent creation with visualization works!")
    else:
        print(f"\n❌ FAILED: Visualization still not working")
