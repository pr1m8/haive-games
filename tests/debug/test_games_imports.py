#!/usr/bin/env python3
"""Test imports and basic functionality of all games including BS, Among Us, Debate, Monopoly, and Risk."""

import sys
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_bs_game():
    """Test BS (Bullshit) card game imports and initialization."""
    print("\n🃏 Testing BS (Bullshit) Card Game...")
    try:
        # Test imports
        from haive.games.cards.standard.bs import (
            BSStateManager,
            BullshitStateManager,
        )

        print("✅ BS imports successful")

        # Test initialization
        state = BullshitStateManager.initialize_game(num_players=4)
        print(f"✅ BS game initialized with {len(state.players)} players")

        # Verify alias works
        state2 = BSStateManager.initialize_game(num_players=3)
        print(f"✅ BSStateManager alias works ({len(state2.players)} players)")

        return True

    except Exception as e:
        print(f"❌ BS game error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_among_us_game():
    """Test Among Us game imports and initialization."""
    print("\n🚀 Testing Among Us...")
    try:
        # Test imports
        from haive.games.among_us import (
            AmongUsStateManagerMixin,
        )

        print("✅ Among Us imports successful")

        # Test initialization
        state = AmongUsStateManagerMixin.initialize(
            player_names=["Alice", "Bob", "Charlie", "David", "Eve"],
            map_name="skeld",
            num_impostors=1,
        )
        print(f"✅ Among Us initialized with {len(state.players)} players")

        return True

    except Exception as e:
        print(f"❌ Among Us error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_debate_game():
    """Test Debate game imports."""
    print("\n💬 Testing Debate...")
    try:
        # Test imports
        from haive.games.debate.models import Topic
        from haive.games.debate.state_manager import DebateStateManager

        print("✅ Debate imports successful")

        # Test initialization
        topic = Topic(
            title="AI Safety Should Be Prioritized",
            description="Debate on the importance of AI safety measures",
        )
        state = DebateStateManager.initialize(
            player_names=["Alice", "Bob"], topic=topic
        )
        print(f"✅ Debate initialized with topic: {state.topic.title}")

        return True

    except Exception as e:
        print(f"❌ Debate error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_monopoly_game():
    """Test Monopoly game imports."""
    print("\n🎩 Testing Monopoly...")
    try:
        # Test imports
        from haive.games.monopoly.config import MonopolyGameAgentConfig

        print("✅ Monopoly imports successful")

        # Test configuration
        config = MonopolyGameAgentConfig(
            player_names=["Alice", "Bob", "Charlie", "David"]
        )
        print(f"✅ Monopoly config created with {len(config.player_names)} players")

        return True

    except Exception as e:
        print(f"❌ Monopoly error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_risk_game():
    """Test Risk game imports."""
    print("\n⚔️ Testing Risk...")
    try:
        # Test imports
        from haive.games.risk.state_manager import RiskStateManager

        print("✅ Risk imports successful")

        # Test initialization
        manager = RiskStateManager.initialize(player_names=["Alice", "Bob", "Charlie"])
        print(f"✅ Risk initialized with {len(manager.state.players)} players")

        return True

    except Exception as e:
        print(f"❌ Risk error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_core_games():
    """Test the core 8 games."""
    print("\n🎮 Testing Core Games...")

    results = []

    # Test Nim
    try:
        from haive.games.nim.state_manager import NimStateManager

        state = NimStateManager.initialize(pile_sizes=[3, 5, 7])
        print("✅ Nim working")
        results.append(("Nim", True))
    except Exception as e:
        print(f"❌ Nim error: {e}")
        results.append(("Nim", False))

    # Test Tic Tac Toe
    try:
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        state = TicTacToeStateManager.initialize()
        print("✅ Tic Tac Toe working")
        results.append(("Tic Tac Toe", True))
    except Exception as e:
        print(f"❌ Tic Tac Toe error: {e}")
        results.append(("Tic Tac Toe", False))

    # Test Connect4
    try:
        from haive.games.connect4.state_manager import Connect4StateManager

        state = Connect4StateManager.initialize()
        print("✅ Connect4 working")
        results.append(("Connect4", True))
    except Exception as e:
        print(f"❌ Connect4 error: {e}")
        results.append(("Connect4", False))

    # Test Chess
    try:
        from haive.games.chess.state_manager import ChessGameStateManager

        state = ChessGameStateManager.initialize()
        print("✅ Chess working")
        results.append(("Chess", True))
    except Exception as e:
        print(f"❌ Chess error: {e}")
        results.append(("Chess", False))

    # Test Checkers
    try:
        from haive.games.checkers.state_manager import CheckersStateManager

        state = CheckersStateManager.initialize()
        print("✅ Checkers working")
        results.append(("Checkers", True))
    except Exception as e:
        print(f"❌ Checkers error: {e}")
        results.append(("Checkers", False))

    # Test Reversi
    try:
        from haive.games.reversi.state_manager import ReversiStateManager

        state = ReversiStateManager.initialize()
        print("✅ Reversi working")
        results.append(("Reversi", True))
    except Exception as e:
        print(f"❌ Reversi error: {e}")
        results.append(("Reversi", False))

    # Test Battleship
    try:
        from haive.games.battleship.state_manager import BattleshipStateManager

        state = BattleshipStateManager.initialize()
        print("✅ Battleship working")
        results.append(("Battleship", True))
    except Exception as e:
        print(f"❌ Battleship error: {e}")
        results.append(("Battleship", False))

    # Test Go
    try:
        from haive.games.go.state_manager import GoGameStateManager

        state = GoGameStateManager.initialize(board_size=19)
        print("✅ Go working")
        results.append(("Go", True))
    except Exception as e:
        print(f"❌ Go error: {e}")
        results.append(("Go", False))

    return results


def main():
    """Run all game import tests."""
    print("🎮 HAIVE GAMES - Import and Initialization Test")
    print("=" * 60)

    all_results = []

    # Test requested games
    requested_games = [
        ("BS (Bullshit)", test_bs_game),
        ("Among Us", test_among_us_game),
        ("Debate", test_debate_game),
        ("Monopoly", test_monopoly_game),
        ("Risk", test_risk_game),
    ]

    print("\n📋 Testing Requested Games:")
    print("-" * 60)

    for game_name, test_func in requested_games:
        success = test_func()
        all_results.append((game_name, success))

    # Test core games
    print("\n📋 Testing Core Games:")
    print("-" * 60)

    core_results = test_core_games()
    all_results.extend(core_results)

    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    working_count = sum(1 for _, success in all_results if success)
    total_count = len(all_results)

    print(f"\n✅ Working: {working_count}/{total_count}")
    print(f"❌ Failed: {total_count - working_count}/{total_count}")
    print(f"📈 Success Rate: {working_count/total_count*100:.1f}%")

    print("\n📝 Detailed Results:")
    for game_name, success in all_results:
        status = "✅" if success else "❌"
        print(f"  {status} {game_name}")

    if working_count == total_count:
        print("\n🎉 PERFECT! All games import and initialize successfully!")
    elif working_count >= total_count * 0.8:
        print("\n👍 EXCELLENT! Most games are working!")
    else:
        print("\n⚠️ Some games need attention.")

    # Example file locations
    print("\n📁 Example Files:")
    print("  - BS: src/haive/games/cards/standard/bs/example.py")
    print("  - Among Us: src/haive/games/among_us/example.py")
    print("  - Debate: src/haive/games/debate/example.py")
    print("  - Monopoly: src/haive/games/monopoly/example.py")
    print("  - Risk: src/haive/games/risk/example.py")

    return working_count == total_count


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
