#!/usr/bin/env python3
"""Debug WHY visualization is breaking during agent initialization."""

import signal
import sys
import time
import traceback


def timeout_handler(signum, frame):
    print("\n🚨 TIMEOUT: Visualization is hanging!")
    print("Stack trace at hang point:")
    traceback.print_stack(frame)
    sys.exit(1)


def main():
    print("🔍 DEBUGGING VISUALIZATION HANG ISSUE")
    print("=" * 60)

    # Set timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(45)  # 45 second timeout

    try:
        print("Step 1: Import components")
        from haive.games.tic_tac_toe.agent import TicTacToeAgent
        from haive.games.tic_tac_toe.config import TicTacToeConfig

        print("✅ Imports successful")

        print("\nStep 2: Create config WITH visualization enabled")
        config = TicTacToeConfig(
            name="debug_visualization",
            visualize=True,  # Enable visualization to trigger the hang
            enable_analysis=False,  # Keep other things minimal
        )
        print(f"✅ Config created with visualize={config.visualize}")

        print("\nStep 3: Start agent creation and monitor where it hangs...")
        print("   This should hang during self.visualize_graph()")

        # Monitor what happens during creation
        start_time = time.time()

        print("   🔍 About to call TicTacToeAgent(config)...")
        print("   🔍 Expected hang: self.visualize_graph() -> draw_mermaid_png()")

        agent = TicTacToeAgent(config)

        elapsed = time.time() - start_time
        print(f"✅ UNEXPECTED: Agent created successfully in {elapsed:.3f}s!")
        print("   This means visualization worked - let's check what's different")

        # Check if visualization files were created
        print("\nStep 4: Check if visualization files were created")
        from pathlib import Path

        # Check output directories
        output_dir = Path("resources/graph_images")
        if output_dir.exists():
            files = list(output_dir.glob("*"))
            print(f"   📁 Found {len(files)} files in {output_dir}")
            for f in files[:5]:  # Show first 5 files
                print(f"     📄 {f.name}")
        else:
            print(f"   📁 Output directory {output_dir} does not exist")

        # Check if visualization actually worked
        if hasattr(agent, "app"):
            print("   ✅ Agent has app attribute")
            try:
                graph = agent.app.get_graph()
                print(f"   ✅ Graph retrieved successfully: {type(graph)}")

                # Try to get the graph drawing methods
                methods = [
                    m
                    for m in dir(graph)
                    if "draw" in m.lower() or "mermaid" in m.lower()
                ]
                print(f"   🎨 Available drawing methods: {methods}")

                # Test the problematic method
                print("   🔍 Testing draw_mermaid_png() method...")
                start_png = time.time()

                png_data = graph.draw_mermaid_png()

                png_elapsed = time.time() - start_png
                print(f"   ✅ draw_mermaid_png() completed in {png_elapsed:.3f}s")
                print(f"   📊 PNG data size: {len(png_data) if png_data else 0} bytes")

            except Exception as e:
                print(f"   ❌ Graph drawing failed: {e}")
                print("   🔍 This might be the actual hang cause:")
                traceback.print_exc()

        print("\n🎉 Visualization debug completed successfully!")

    except Exception as e:
        print(f"\n❌ Error during visualization debug: {e}")
        print(f"   Exception type: {type(e)}")
        traceback.print_exc()
    except KeyboardInterrupt:
        print("\n⏹️  Manually interrupted")
    finally:
        signal.alarm(0)  # Cancel timeout


if __name__ == "__main__":
    main()
