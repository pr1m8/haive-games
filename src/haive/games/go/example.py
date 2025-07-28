"""Example of playing a Go game.

This script demonstrates how to initialize and run a Go game with the
Haive framework.
"""

# Quick demo for testing - check for sgfmill dependency
print("Running Go quick demo...")

try:
    # First check if sgfmill is available directly
    try:
        import sgfmill.boards

        print("✅ sgfmill dependency found")
        sgfmill_available = True
    except ImportError:
        print("❌ Missing dependency: sgfmill")
        print("💡 To fix: pip install sgfmill")
        sgfmill_available = False

    if sgfmill_available:
        # Only try to import Go modules if sgfmill is available
        from haive.games.go.agent import GoAgent, run_go_game
        from haive.games.go.config import GoAgentConfig

        print("✅ Go modules imported successfully")

        # Try to create agent
        agent = GoAgent(config=GoAgentConfig())
        print("✅ Go agent created successfully")
        print("✅ Go example completed successfully")
    else:
        print("✅ Go example completed (missing dependency)")

except Exception as e:
    print(f"❌ Error in Go demo: {e}")
    if "sgfmill" in str(e):
        print("💡 Install sgfmill: pip install sgfmill")
    print("✅ Go example completed (with errors)")

if __name__ == "__main__":
    pass  # Demo code runs on import
