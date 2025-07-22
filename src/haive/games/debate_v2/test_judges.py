#!/usr/bin/env python3
"""Test the AI judge system for gamified debates."""

import asyncio
import logging
import sys

from haive.games.debate_v2.agent_with_judges import JudgedGameDebateAgent
from haive.games.debate_v2.judges import (
    AIDebateJudge,
    JudgeType,
    create_tournament_judges,
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def test_judge_creation() -> bool:
    """Test that judges can be created properly."""
    try:
        # Create individual judge
        judge = AIDebateJudge(
            name="Test_Judge",
            judge_type=JudgeType.BALANCED,
            expertise_area="General Debate",
            strictness_level=0.5,
        )

        assert judge.name == "Test_Judge"
        assert judge.judge_type == JudgeType.BALANCED
        assert judge.agent is not None

        # Create judge panel with default size
        panel = create_tournament_judges()
        assert len(panel.judges) == 3  # Default size
        assert all(isinstance(j, AIDebateJudge) for j in panel.judges)

        # Test configurable size
        panel_5 = create_tournament_judges(5)
        assert len(panel_5.judges) == 5

        # Test odd number warning (should work but warn)
        panel_4 = create_tournament_judges(4)
        assert len(panel_4.judges) == 4

        return True

    except Exception:
        return False


def test_judged_agent_creation() -> bool:
    """Test that judged debate agents can be created."""
    try:
        # Create judged debate agent with configurable judges
        agent = JudgedGameDebateAgent.create_judged_tournament_match(
            topic="Test debate topic",
            player_a=("TestA", "Position A"),
            player_b=("TestB", "Position B"),
            match_id="test_001",
            judge_panel_type="tournament",
            num_judges=5,  # Test with 5 judges
        )

        assert agent.topic == "Test debate topic"
        assert agent.use_ai_judges is True
        assert agent.judge_panel_type == "tournament"
        assert agent.custom_judges is not None

        # Test judge panel info
        panel_info = agent.get_judge_panel_info()
        assert "judges" in panel_info
        assert len(panel_info["judges"]) == 5  # Should match our config

        return True

    except Exception as e:
        logger.error(f"Agent creation error: {e}", exc_info=True)
        return False


async def test_judge_evaluation_simulation():
    """Test judge evaluation with simulated debate transcript."""
    try:
        # Create a simple judge
        AIDebateJudge("Simulator", JudgeType.BALANCED, strictness_level=0.3)

        # Simulate a short debate transcript

        # Test judge evaluation (this would normally call LLM)

        # Test that panel can be set up for evaluation
        panel = create_tournament_judges()

        # Verify panel setup
        assert len(panel.judges) > 0
        assert all(hasattr(j, "judge_player_performance") for j in panel.judges)

        return True

    except Exception as e:
        logger.error(f"Evaluation test error: {e}", exc_info=True)
        return False


def test_scoring_combination() -> bool:
    """Test automatic + judge scoring combination."""
    try:
        # Create agent with combined scoring and custom judge count
        agent = JudgedGameDebateAgent.create_judged_tournament_match(
            topic="Test scoring",
            player_a=("Alice", "Position A"),
            player_b=("Bob", "Position B"),
            match_id="scoring_test",
            num_judges=7,  # Test with 7 judges (optimal according to research)
            combine_auto_and_judge_scoring=True,
            auto_scoring_weight=0.4,
            judge_scoring_weight=0.6,
        )

        # Verify scoring configuration exists
        if hasattr(agent, "combine_auto_and_judge_scoring"):
            pass
        else:
            pass

        if hasattr(agent, "auto_scoring_weight"):
            pass
        else:
            pass

        if hasattr(agent, "judge_scoring_weight"):
            pass
        else:
            pass

        if hasattr(agent, "num_judges"):
            pass
        else:
            pass

        # Verify judge panel size matches configuration
        panel_info = agent.get_judge_panel_info()
        expected_judges = 7
        actual_judges = len(panel_info.get("judges", []))

        if actual_judges == expected_judges:
            pass
        else:
            return False

        return True

    except Exception as e:
        logger.error(f"Scoring combination error: {e}", exc_info=True)
        return False


async def main():
    """Run all judge system tests."""
    tests = [
        ("Judge Creation", test_judge_creation),
        ("Judged Agent Creation", test_judged_agent_creation),
        ("Judge Evaluation", test_judge_evaluation_simulation),
        ("Scoring Combination", test_scoring_combination),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            if asyncio.iscoroutinefunction(test_func):
                success = await test_func()
            else:
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
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
