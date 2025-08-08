#!/usr/bin/env python3
"""Test mermaid functionality directly."""


def test_mermaid():
    print("🔍 TESTING MERMAID FUNCTIONALITY DIRECTLY")
    print("=" * 50)

    try:
        print("Step 1: Test basic mermaid creation")

        # Create a simple graph to test mermaid
        from typing import TypedDict

        from langgraph.graph import StateGraph

        class SimpleState(TypedDict):
            value: str

        def node_a(state):
            return {"value": "A"}

        def node_b(state):
            return {"value": "B"}

        # Create simple graph
        graph = StateGraph(SimpleState)
        graph.add_node("A", node_a)
        graph.add_node("B", node_b)
        graph.add_edge("A", "B")
        graph.set_entry_point("A")
        graph.set_finish_point("B")

        compiled = graph.compile()
        print("✅ Simple graph created and compiled")

        print("\nStep 2: Test getting graph representation")
        graph_repr = compiled.get_graph()
        print(f"✅ Graph representation: {type(graph_repr)}")

        print("\nStep 3: Test mermaid string generation")
        mermaid_str = graph_repr.draw_mermaid()
        print(f"✅ Mermaid string generated: {len(mermaid_str)} chars")
        print(f"   First 100 chars: {mermaid_str[:100]}...")

        print("\nStep 4: Test PNG generation (this is where it might hang)")
        import time

        start = time.time()

        try:
            png_data = graph_repr.draw_mermaid_png()
            elapsed = time.time() - start
            print(f"✅ PNG generated in {elapsed:.3f}s: {len(png_data)} bytes")

            # Save it to test
            with open("test_graph.png", "wb") as f:
                f.write(png_data)
            print("✅ PNG saved to test_graph.png")

        except Exception as e:
            elapsed = time.time() - start
            print(f"❌ PNG generation failed after {elapsed:.3f}s: {e}")
            import traceback

            traceback.print_exc()

        print(f"\n🎉 Mermaid test completed!")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_mermaid()
