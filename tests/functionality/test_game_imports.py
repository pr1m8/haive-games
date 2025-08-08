#!/usr/bin/env python3
"""Test that games can be imported and initialized."""

import sys
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_game_imports():
    """Test importing and initializing various games."""
    
    games_to_test = [
        ("Nim", "haive.games.nim.state_manager", "NimStateManager"),
        ("Tic Tac Toe", "haive.games.tic_tac_toe.state_manager", "TicTacToeStateManager"),
        ("Connect4", "haive.games.connect4.state_manager", "Connect4StateManager"),
        ("Chess", "haive.games.chess.state_manager", "ChessStateManager"),
        ("Checkers", "haive.games.checkers.state_manager", "CheckersStateManager"),
        ("Reversi", "haive.games.reversi.state_manager", "ReversiStateManager"),
        ("Go", "haive.games.go.state_manager", "GoStateManager"),
        ("Battleship", "haive.games.battleship.state_manager", "BattleshipStateManager"),
    ]
    
    results = []
    
    for game_name, module_path, class_name in games_to_test:
        try:
            # Import the module
            module = __import__(module_path, fromlist=[class_name])
            
            # Get the state manager class
            state_manager = getattr(module, class_name)
            
            # Try to initialize a game state
            if hasattr(state_manager, 'initialize'):
                state = state_manager.initialize()
                print(f"✓ {game_name}: Successfully imported and initialized")
                results.append((game_name, True, None))
            else:
                print(f"⚠ {game_name}: Imported but no initialize method found")
                results.append((game_name, False, "No initialize method"))
                
        except ImportError as e:
            print(f"✗ {game_name}: Import failed - {e}")
            results.append((game_name, False, f"Import error: {e}"))
        except Exception as e:
            print(f"✗ {game_name}: Failed - {e}")
            results.append((game_name, False, str(e)))
    
    # Summary
    print("\n=== Summary ===")
    passed = sum(1 for _, success, _ in results if success)
    failed = len(results) - passed
    
    print(f"Passed: {passed}/{len(results)}")
    print(f"Failed: {failed}/{len(results)}")
    
    if failed > 0:
        print("\nFailed games:")
        for game, success, error in results:
            if not success:
                print(f"  - {game}: {error}")
    
    return passed == len(results)


def test_game_models():
    """Test importing game models."""
    print("\n=== Testing Game Models ===")
    
    models_to_test = [
        ("Nim", "haive.games.nim.models", ["NimMove", "NimState"]),
        ("Tic Tac Toe", "haive.games.tic_tac_toe.models", ["TicTacToeMove", "TicTacToeState"]),
        ("Connect4", "haive.games.connect4.models", ["Connect4Move", "Connect4State"]),
    ]
    
    for game_name, module_path, classes in models_to_test:
        try:
            module = __import__(module_path, fromlist=classes)
            missing = []
            for cls in classes:
                if not hasattr(module, cls):
                    missing.append(cls)
            
            if missing:
                print(f"⚠ {game_name}: Missing classes: {', '.join(missing)}")
            else:
                print(f"✓ {game_name}: All model classes found")
                
        except ImportError as e:
            print(f"✗ {game_name}: Import failed - {e}")


def main():
    """Run all tests."""
    print("=== Haive Games Import Tests ===\n")
    
    success = test_game_imports()
    test_game_models()
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)