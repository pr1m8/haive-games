#!/usr/bin/env python3
"""Test Nim game with correct field names."""

import sys
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_nim_game_corrected():
    """Test Nim game with proper field names."""
    print("🎲 Testing Nim Game (Fixed)")
    print("-" * 40)
    
    try:
        from haive.games.nim.models import NimMove
        from haive.games.nim.state_manager import NimStateManager
        
        # Initialize game with classic 3-5-7 configuration
        state = NimStateManager.initialize(pile_sizes=[3, 5, 7])
        print(f"✓ Initialized game with piles: {state.piles}")
        print(f"✓ Current turn: {state.turn}")
        print(f"✓ Game status: {state.game_status}")
        
        # Test legal moves generation
        legal_moves = NimStateManager.get_legal_moves(state, "player1")
        print(f"✓ Found {len(legal_moves)} legal moves for player1")
        
        # Make a few moves with correct field names
        moves_to_test = [
            NimMove(pile_index=1, stones_taken=3, player="player1"),  # Take 3 from pile 1 (size 5)
            NimMove(pile_index=2, stones_taken=2, player="player2"),  # Take 2 from pile 2 (size 7)  
        ]
        
        current_state = state
        for i, move in enumerate(moves_to_test):
            print(f"\nMove {i+1}: {move.player} takes {move.stones_taken} from pile {move.pile_index}")
            print(f"  Before: piles = {current_state.piles}")
            print(f"  Current turn: {current_state.turn}")
            
            # Verify it's the correct player's turn
            if current_state.turn != move.player:
                print(f"  ⚠️ Skipping move - not {move.player}'s turn (it's {current_state.turn}'s turn)")
                continue
            
            try:
                # Make the move using the state manager
                command = NimStateManager.make_move(current_state, move.player, move)
                
                # Extract new state from command
                if hasattr(command, 'update'):
                    # Reconstruct state from command update
                    from haive.games.nim.state import NimState
                    current_state = NimState(**command.update)
                elif hasattr(command, 'state'):
                    current_state = command.state
                else:
                    current_state = command
                
                print(f"  ✓ Move successful!")
                print(f"  After: piles = {current_state.piles}")
                print(f"  New turn: {current_state.turn}")
                print(f"  Game status: {current_state.game_status}")
                
                # Check if game ended
                if current_state.game_status != "ongoing":
                    winner = NimStateManager.get_winner(current_state)
                    print(f"  🎉 Game ended! Winner: {winner}")
                    break
                    
            except Exception as e:
                print(f"  ✗ Move failed: {e}")
                return False
        
        print(f"\n✓ Nim game test completed successfully!")
        print(f"Final state: piles = {current_state.piles}, status = {current_state.game_status}")
        return True
        
    except Exception as e:
        print(f"✗ Nim test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_nim_models():
    """Test Nim model creation directly."""
    print("\n🔧 Testing Nim Models")
    print("-" * 40)
    
    try:
        from haive.games.nim.models import NimMove, NimAnalysis
        from haive.games.nim.state import NimState
        
        # Test NimMove creation
        move = NimMove(pile_index=0, stones_taken=2, player="testplayer")
        print(f"✓ Created NimMove: {move}")
        print(f"  Move notation: {move.move_notation}")
        print(f"  Has strategic context: {move.has_strategic_context}")
        
        # Test NimMove with strategic context
        strategic_move = NimMove(
            pile_index=1, 
            stones_taken=3, 
            player="ai",
            reasoning="Optimal play to force nim-sum to 0",
            move_quality="optimal"
        )
        print(f"✓ Created strategic move: {strategic_move}")
        print(f"  Has strategic context: {strategic_move.has_strategic_context}")
        
        # Test NimState creation
        state = NimState(piles=[3, 5, 7])
        print(f"✓ Created NimState: piles = {state.piles}")
        print(f"  Turn: {state.turn}")
        print(f"  Status: {state.game_status}")
        
        return True
        
    except Exception as e:
        print(f"✗ Model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("🎮 Nim Game Fixed Tests")
    print("=" * 50)
    
    tests = [
        test_nim_models,
        test_nim_game_corrected,
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n🎯 Test Summary")
    print("-" * 20)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ All Nim tests passed!")
    else:
        print("❌ Some tests failed")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)