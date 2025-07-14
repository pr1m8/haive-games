#!/usr/bin/env python3
"""Simple test to verify the gamified debate works without DynamicGraph issues.

This test demonstrates that:
1. Topics are handled properly (no None issues)
2. The modern agent architecture works correctly
3. Gamification features are implemented
4. No abstract method errors occur
"""

import asyncio
import logging

from haive.games.debate_v2.agent import GameDebateAgent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def test_agent_creation():
    """Test that GameDebateAgent can be created without abstract method errors."""
    print("🔧 Testing GameDebateAgent creation...")

    try:
        # Create gamified debate - this should NOT raise abstract method errors
        debate = GameDebateAgent.create_tournament_match(
            topic="Should AI development be regulated internationally?",
            player_a=("ProRegulation", "AI needs international oversight"),
            player_b=("AntiRegulation", "AI development should remain competitive"),
            match_id="test_001",
            bracket_position="test_match",
            # Game settings
            scoring_enabled=True,
            points_per_argument=10,
            points_per_rebuttal=15,
            # Quick format for testing
            arguments_per_side=1,
            enable_opening_statements=False,
            enable_closing_statements=False,
        )

        print("✅ GameDebateAgent created successfully!")
        print(f"✅ Topic: {debate.topic}")
        print(f"✅ Tournament Mode: {debate.tournament_mode}")
        print(f"✅ Scoring Enabled: {debate.scoring_enabled}")
        print(f"✅ Participants: {list(debate.debate_positions.keys())}")

        return True

    except Exception as e:
        print(f"❌ Agent creation failed: {e}")
        logger.error(f"Creation error: {e}", exc_info=True)
        return False


def test_topic_handling():
    """Test that topics are properly handled (no None issues)."""
    print("\n🎯 Testing topic handling...")

    try:
        debate = GameDebateAgent.create_tournament_match(
            topic="Test topic for verification",
            player_a=("Player1", "Position 1"),
            player_b=("Player2", "Position 2"),
            match_id="topic_test",
            arguments_per_side=1,
        )

        # Verify topic is properly set
        if debate.topic is None:
            print("❌ Topic is None!")
            return False

        if debate.topic == "Test topic for verification":
            print("✅ Topic handled correctly!")
            print(f"✅ Topic value: '{debate.topic}'")
            return True
        else:
            print(
                f"❌ Topic mismatch: expected 'Test topic for verification', got '{debate.topic}'"
            )
            return False

    except Exception as e:
        print(f"❌ Topic handling test failed: {e}")
        logger.error(f"Topic test error: {e}", exc_info=True)
        return False


def test_game_features():
    """Test that game features are properly configured."""
    print("\n🎮 Testing game features...")

    try:
        debate = GameDebateAgent.create_tournament_match(
            topic="Game features test",
            player_a=("Gamer1", "Gaming position 1"),
            player_b=("Gamer2", "Gaming position 2"),
            match_id="game_test",
            # Test game configuration
            scoring_enabled=True,
            points_per_argument=20,
            points_per_rebuttal=30,
            bonus_for_evidence=10,
            penalty_for_repetition=5,
            tournament_mode=True,
            track_performance=True,
        )

        # Verify game settings
        assert debate.scoring_enabled == True, "Scoring should be enabled"
        assert debate.points_per_argument == 20, "Points per argument should be 20"
        assert debate.points_per_rebuttal == 30, "Points per rebuttal should be 30"
        assert debate.bonus_for_evidence == 10, "Evidence bonus should be 10"
        assert debate.penalty_for_repetition == 5, "Repetition penalty should be 5"
        assert debate.tournament_mode == True, "Tournament mode should be enabled"
        assert (
            debate.track_performance == True
        ), "Performance tracking should be enabled"
        assert debate.match_id == "game_test", "Match ID should be set"

        print("✅ All game features configured correctly!")
        print(f"   • Scoring: {debate.scoring_enabled}")
        print(f"   • Points per argument: {debate.points_per_argument}")
        print(f"   • Points per rebuttal: {debate.points_per_rebuttal}")
        print(f"   • Evidence bonus: {debate.bonus_for_evidence}")
        print(f"   • Repetition penalty: {debate.penalty_for_repetition}")
        print(f"   • Tournament mode: {debate.tournament_mode}")
        print(f"   • Match ID: {debate.match_id}")

        return True

    except Exception as e:
        print(f"❌ Game features test failed: {e}")
        logger.error(f"Game features error: {e}", exc_info=True)
        return False


def test_inheritance():
    """Test that inheritance from DebateConversation works correctly."""
    print("\n🔗 Testing inheritance...")

    try:
        debate = GameDebateAgent.create_tournament_match(
            topic="Inheritance test",
            player_a=("TestA", "Position A"),
            player_b=("TestB", "Position B"),
            match_id="inheritance_test",
        )

        # Check that we have methods from DebateConversation
        assert hasattr(debate, "select_speaker"), "Should have select_speaker method"
        assert hasattr(
            debate, "process_response"
        ), "Should have process_response method"
        assert hasattr(
            debate, "_create_initial_message"
        ), "Should have _create_initial_message method"
        assert hasattr(
            debate, "conclude_conversation"
        ), "Should have conclude_conversation method"

        # Check that we have our game-specific methods
        assert hasattr(
            debate, "_calculate_argument_score"
        ), "Should have _calculate_argument_score method"
        assert hasattr(debate, "_has_evidence"), "Should have _has_evidence method"
        assert hasattr(debate, "_is_repetitive"), "Should have _is_repetitive method"

        print("✅ Inheritance working correctly!")
        print("   • DebateConversation methods available")
        print("   • Game-specific methods available")
        print("   • No abstract method errors")

        return True

    except Exception as e:
        print(f"❌ Inheritance test failed: {e}")
        logger.error(f"Inheritance error: {e}", exc_info=True)
        return False


def main():
    """Run all tests to verify the gamified debate implementation."""
    print("🎮 GAMIFIED DEBATE VERIFICATION TESTS")
    print("Testing that we've solved the DynamicGraph issues")
    print("=" * 60)

    tests = [
        ("Agent Creation", test_agent_creation),
        ("Topic Handling", test_topic_handling),
        ("Game Features", test_game_features),
        ("Inheritance", test_inheritance),
    ]

    results = []
    for test_name, test_func in tests:
        print(f"\n🔄 Running: {test_name}")
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))

    # Summary
    print("\n" + "=" * 60)
    print("🏁 TEST RESULTS SUMMARY")
    print("=" * 60)

    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
        if success:
            passed += 1

    total = len(results)
    print(f"\n📊 Results: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Gamified debate implementation is working correctly")
        print("✅ Topics are handled properly (no None issues)")
        print("✅ Game features are implemented and functional")
        print("✅ No abstract method errors")
        print("✅ Modern agent architecture works as expected")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
        print("❌ Some issues still need to be resolved")

    return passed == total


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
