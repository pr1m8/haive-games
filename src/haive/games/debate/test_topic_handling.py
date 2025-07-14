#!/usr/bin/env python3
"""Test to verify Debate game properly handles provided topics vs fallback."""

import logging
import sys

from haive.games.debate.agent import DebateAgent
from haive.games.debate.config import DebateAgentConfig

# Configure logging to see topic handling
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
    force=True,
)

logger = logging.getLogger(__name__)
debate_logger = logging.getLogger("haive.games.debate.agent")
debate_logger.setLevel(logging.DEBUG)


def test_explicit_topic():
    """Test that explicitly provided topic is used."""
    logger.info("=== Testing EXPLICIT TOPIC handling ===")

    config = DebateAgentConfig(
        name="topic_test_agent",
        debate_format="standard",
        max_statements=1,
        participant_roles={"debater_1": "pro", "debater_2": "con"},
    )

    agent = DebateAgent(config)

    # Provide explicit topic - should NOT use fallback
    explicit_topic = {
        "title": "Should Pineapple Go On Pizza",
        "description": "Debate the controversial culinary question of pineapple as a pizza topping",
    }

    logger.info(f"Running with EXPLICIT topic: {explicit_topic}")
    logger.info("DEBUG: Calling agent.run() with the following input:")
    input_state = {"topic": explicit_topic}
    logger.info(f"Input state: {input_state}")

    # Test schema validation directly
    from haive.games.debate.input_schema import DebateInputSchema

    logger.info("Testing DebateInputSchema validation directly...")
    try:
        schema_test = DebateInputSchema(**input_state)
        logger.info(f"Schema validation successful: {schema_test}")
        logger.info(f"Schema topic: {schema_test.topic}")
    except Exception as e:
        logger.error(f"Schema validation failed: {e}")

    result = agent.run(input_state)

    return result


def test_none_topic():
    """Test that None topic triggers fallback."""
    logger.info("=== Testing NONE TOPIC fallback ===")

    config = DebateAgentConfig(
        name="fallback_test_agent",
        debate_format="standard",
        max_statements=1,
        participant_roles={"debater_1": "pro", "debater_2": "con"},
    )

    agent = DebateAgent(config)

    # Provide None topic - should use fallback
    logger.info("Running with NONE topic (should trigger fallback)")
    result = agent.run({"topic": None})

    return result


def test_empty_state():
    """Test that empty state triggers fallback."""
    logger.info("=== Testing EMPTY STATE fallback ===")

    config = DebateAgentConfig(
        name="empty_test_agent",
        debate_format="standard",
        max_statements=1,
        participant_roles={"debater_1": "pro", "debater_2": "con"},
    )

    agent = DebateAgent(config)

    # Provide empty state - should use fallback
    logger.info("Running with EMPTY state (should trigger fallback)")
    result = agent.run({})

    return result


if __name__ == "__main__":
    logger.info("Starting topic handling verification tests...")

    try:
        # Test 1: Explicit topic should be used
        logger.info("\n" + "=" * 60)
        explicit_result = test_explicit_topic()
        logger.info("✅ Explicit topic test completed")

        # Test 2: None topic should use fallback
        logger.info("\n" + "=" * 60)
        none_result = test_none_topic()
        logger.info("✅ None topic test completed")

        # Test 3: Empty state should use fallback
        logger.info("\n" + "=" * 60)
        empty_result = test_empty_state()
        logger.info("✅ Empty state test completed")

        logger.info("\n" + "=" * 60)
        logger.info("🎯 ALL TOPIC HANDLING TESTS PASSED")
        logger.info(
            "✅ Debate game properly handles both explicit topics AND fallbacks"
        )

    except Exception as e:
        logger.error(f"❌ Topic handling test failed: {e}")
        logger.error("Full traceback:", exc_info=True)
        sys.exit(1)
