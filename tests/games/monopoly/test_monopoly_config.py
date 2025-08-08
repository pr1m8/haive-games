#!/usr/bin/env python3
"""Test script for MonopolyAgentConfig validation"""

from pathlib import Path
import sys

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from haive.games.monopoly.config import MonopolyAgentConfig


def main():
    """Test MonopolyAgentConfig instantiation."""
    try:
        print("Creating default MonopolyAgentConfig...")
        config = MonopolyAgentConfig()
        print("Success! MonopolyAgentConfig created.")
        print(f"Number of engines: {len(config.engines)}")

        # Test MonopolyAgent creation
        from haive.games.monopoly.agent import MonopolyAgent

        MonopolyAgent(config=config)
        print("Success! MonopolyAgent created.")

        return 0
    except Exception as e:
        print(f"Error: {e!s}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
