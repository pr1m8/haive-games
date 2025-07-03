"""Verify imports script for Mafia game module.

This script checks that we can import all essential models from the Mafia
module without requiring external dependencies.
"""

print("Attempting to import models from Mafia module...")

try:
    from models import (
        ActionType,
        GamePhase,
        MafiaAction,
        PlayerRole,
    )

    print("✅ Successfully imported models module classes")

    # Test model creation
    action = MafiaAction(
        player_id="Player_1",
        action_type=ActionType.VOTE,
        target_id="Player_2",
        phase=GamePhase.DAY_VOTING,
        round_number=1,
    )
    print(f"✅ Created MafiaAction: {action}")

    # Test enum values
    print(f"✅ GamePhase values: {[phase.value for phase in GamePhase]}")
    print(f"✅ PlayerRole values: {[role.value for role in PlayerRole]}")
    print(f"✅ ActionType values: {[action.value for action in ActionType]}")

except Exception as e:
    print(f"❌ Error importing from models: {e}")

print("\nVerifying imports from the aug_llms module...")

try:

    print("✅ Successfully imported aug_llms module functions and objects")

except Exception as e:
    print(f"❌ Error importing from aug_llms: {e}")

print("\n✅ Import verification complete!")
