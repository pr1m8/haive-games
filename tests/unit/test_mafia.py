"""Test script for the Mafia game implementation.

This script demonstrates the basic functionality of the Mafia game
by creating a simplified test game with minimal dependencies.
"""

import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import the necessary modules
from agent import MafiaAgent
from config import MafiaAgentConfig
from models import GamePhase, PlayerRole
from state_manager import MafiaStateManager


def test_game_initialization():
    """Test that the game can be properly initialized."""
    print("\n===== Testing Game Initialization =====")

    # Create a configuration
    config = MafiaAgentConfig.default_config(player_count=5, max_days=1)

    # Create the agent
    try:
        MafiaAgent(config)
        print("✅ Agent creation successful")
    except Exception as e:
        print(f"❌ Agent creation failed: {e}")
        return False

    # Generate player names
    player_names = [f"Player_{i+1}" for i in range(4)]
    player_names.append("Narrator")  # Add narrator as the last player

    # Initialize game state
    try:
        initial_state = MafiaStateManager.initialize(player_names)
        print("✅ State initialization successful")

        # Print role assignment for verification
        print("\nRole Assignment:")
        for player_id, role in initial_state.roles.items():
            print(f"  {player_id}: {role.value}")

        return True
    except Exception as e:
        print(f"❌ State initialization failed: {e}")
        return False


def test_game_state_operations():
    """Test basic game state operations."""
    print("\n===== Testing Game State Operations =====")

    # Create a simple test state
    player_names = ["Player_1", "Player_2", "Player_3", "Player_4", "Narrator"]

    try:
        state = MafiaStateManager.initialize(player_names)
        print("✅ State created successfully")

        # Test phase transition
        print("\nTesting phase transition...")
        initial_phase = state.game_phase
        new_state = MafiaStateManager.advance_phase(state)
        print(f"  Phase transition: {initial_phase} -> {new_state.game_phase}")

        # Test applying a move
        print("\nTesting move application...")
        from models import ActionType, MafiaAction

        # Find a mafia player
        mafia_player = None
        for player_id, role in state.roles.items():
            if role == PlayerRole.MAFIA:
                mafia_player = player_id
                break

        if mafia_player:
            # Create a kill action
            target = next(
                (
                    pid
                    for pid, role in state.roles.items()
                    if role != PlayerRole.MAFIA and pid != "Narrator"
                ),
                None,
            )

            if target:
                action = MafiaAction(
                    player_id=mafia_player,
                    action_type=ActionType.KILL,
                    target_id=target,
                    phase=GamePhase.NIGHT,
                    round_number=1,
                )

                updated_state = MafiaStateManager.apply_move(
                    new_state, mafia_player, action
                )
                print(f"  Applied kill action from {mafia_player} targeting {target}")
                print(f"  Killed at night: {updated_state.killed_at_night}")

        return True
    except Exception as e:
        print(f"❌ State operations failed: {e}")
        return False


def run_all_tests():
    """Run all tests and return overall success."""
    tests = [test_game_initialization, test_game_state_operations]

    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test_func.__name__} failed with exception: {e}")
            results.append(False)

    # Print summary
    print("\n===== Test Summary =====")
    for i, test_func in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"{status}: {test_func.__name__}")

    # Overall result
    if all(results):
        print("\n🎉 All tests passed!")
        return True
    print("\n❌ Some tests failed")
    return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
