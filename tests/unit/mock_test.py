"""Minimal test script for Mafia game with mocked dependencies.

This script tests the basic functionality of the Mafia game state
management without requiring full framework integration.
"""

import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import directly from local files to avoid framework dependencies
from models import ActionType, GamePhase, MafiaAction, PlayerRole, PlayerState
from state import MafiaGameState


# Simple test to verify the imports and basic model functionality
def test_models():
    """Test basic model creation and functionality."""
    print("\n===== Testing Models =====")

    try:
        # Create a player state
        player_state = PlayerState(
            player_id="Player_1", role=PlayerRole.VILLAGER, is_alive=True
        )
        print(
            f"✅ Created player state: {player_state.player_id}, Role: {player_state.role}, Alive: {player_state.is_alive}"
        )

        # Create an action
        action = MafiaAction(
            player_id="Player_2",
            action_type=ActionType.VOTE,
            target_id="Player_1",
            phase=GamePhase.DAY_VOTING,
            round_number=1,
        )
        print(f"✅ Created action: {action.player_id} voted for {action.target_id}")

        # Test string representation
        print(f"  Action string: {action!s}")

        return True
    except Exception as e:
        print(f"❌ Model tests failed: {e}")
        return False


def test_game_state():
    """Test game state creation and basic operations."""
    print("\n===== Testing Game State =====")

    try:
        # Create a minimal game state
        state = MafiaGameState(
            players=["Player_1", "Player_2", "Narrator"],
            roles={
                "Player_1": PlayerRole.VILLAGER,
                "Player_2": PlayerRole.MAFIA,
                "Narrator": PlayerRole.NARRATOR,
            },
            player_states={
                "Player_1": PlayerState(player_id="Player_1", role=PlayerRole.VILLAGER),
                "Player_2": PlayerState(player_id="Player_2", role=PlayerRole.MAFIA),
                "Narrator": PlayerState(player_id="Narrator", role=PlayerRole.NARRATOR),
            },
            game_phase=GamePhase.SETUP,
            day_number=0,
            round_number=0,
            alive_mafia_count=1,
            alive_village_count=1,
        )
        print("✅ Created game state")

        # Test adding announcements
        state.add_public_announcement("Game is starting!")
        print(f"✅ Added announcement: {state.public_announcements[-1]}")

        # Test updating alive counts
        state.update_alive_counts()
        print(
            f"✅ Updated alive counts - Mafia: {state.alive_mafia_count}, Village: {state.alive_village_count}"
        )

        # Test logging an action
        action = MafiaAction(
            player_id="Player_2",
            action_type=ActionType.KILL,
            target_id="Player_1",
            phase=GamePhase.NIGHT,
            round_number=1,
        )
        state.log_action(action)
        print(f"✅ Logged action: {state.action_history[-1]}")

        return True
    except Exception as e:
        print(f"❌ Game state tests failed: {e}")
        return False


def run_tests():
    """Run all test functions."""
    test_functions = [test_models, test_game_state]
    results = []

    for test_func in test_functions:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test_func.__name__} failed with exception: {e}")
            results.append(False)

    # Print summary
    print("\n===== Test Summary =====")
    for i, test_func in enumerate(test_functions):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"{status}: {test_func.__name__}")

    if all(results):
        print("\n🎉 All tests passed!")
        return True
    print("\n❌ Some tests failed")
    return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
