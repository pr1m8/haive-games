#!/usr/bin/env python3
"""Simple test to verify the gamified debate works without DynamicGraph issues.

from typing import Any
This test demonstrates that:
1. Topics are handled properly (no None issues)
2. The modern agent architecture works correctly
3. Gamification features are implemented
4. No abstract method errors occur
"""

import logging
import sys

from haive.games.debate_v2.agent import GameDebateAgent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def test_agent_creation() -> bool:
    """Test that GameDebateAgent can be created without abstract method errors."""
    try:
        # Create gamified debate - this should NOT raise abstract method errors
        GameDebateAgent.create_tournament_match(
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

        return True

    except Exception as e:
        logger.error(f"Creation error: {e}", exc_info=True)
        return False


def test_topic_handling() -> bool:
    """Test that topics are properly handled (no None issues)."""
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
            return False

        return debate.topic == "Test topic for verification"

    except Exception as e:
        logger.error(f"Topic test error: {e}", exc_info=True)
        return False


def test_game_features() -> bool:
    """Test that game features are properly configured."""
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
        assert debate.scoring_enabled is True, "Scoring should be enabled"
        assert debate.points_per_argument == 20, "Points per argument should be 20"
        assert debate.points_per_rebuttal == 30, "Points per rebuttal should be 30"
        assert debate.bonus_for_evidence == 10, "Evidence bonus should be 10"
        assert debate.penalty_for_repetition == 5, "Repetition penalty should be 5"
        assert debate.tournament_mode is True, "Tournament mode should be enabled"
        assert (
            debate.track_performance is True
        ), "Performance tracking should be enabled"
        assert debate.match_id == "game_test", "Match ID should be set"

        return True

    except Exception as e:
        logger.error(f"Game features error: {e}", exc_info=True)
        return False


def test_inheritance() -> bool:
    """Test that inheritance from DebateConversation works correctly."""
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

        return True

    except Exception as e:
        logger.error(f"Inheritance error: {e}", exc_info=True)
        return False


def main() -> Any:
    """Run all tests to verify the gamified debate implementation."""
    tests = [
        ("Agent Creation", test_agent_creation),
        ("Topic Handling", test_topic_handling),
        ("Game Features", test_game_features),
        ("Inheritance", test_inheritance),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception:
            results.append((test_name, False))

    # Summary

    passed = 0
    for test_name, success in results:
        if success:
            passed += 1

    total = len(results)

    if passed == total:
        pass
    else:
        pass

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
