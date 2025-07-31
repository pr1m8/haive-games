"""Example usage of the Risk agent.

This example demonstrates how to run a Risk game with AI agents.

Usage:
    python example.py

"""

import logging

from haive.games.risk.agent import RiskAgent
from haive.games.risk.models import MoveType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Run example Risk game scenarios with AI agents."""
    logger.info("Starting Risk game example with AI agents")

    # Create a basic Risk agent
    agent = RiskAgent(
        name="General_AI",
        strategy="balanced",
        risk_tolerance=0.6,
        diplomatic_stance="neutral",
    )

    logger.info(f"Created Risk agent: {agent.name}")
    logger.info(f"Strategy: {agent.strategy}")
    logger.info(f"Risk tolerance: {agent.risk_tolerance}")

    # Example 1: Analyze position
    logger.info("\n=== Example 1: Position Analysis ===")
    try:
        analysis = agent.analyze_position()
        logger.info(f"Controlled territories: {analysis.controlled_territories}")
        logger.info(f"Army strength: {analysis.total_armies}")
        logger.info(f"Strategic assessment: {analysis.strategic_assessment}")
    except Exception as e:
        logger.info(f"Position analysis requires game state: {e}")

    # Example 2: Get strategic move
    logger.info("\n=== Example 2: Strategic Move ===")
    try:
        move = agent.get_move()
        if move.move_type == MoveType.ATTACK:
            logger.info(f"Attack from {move.from_territory} to {move.to_territory}")
        elif move.move_type == MoveType.PLACE_ARMIES:
            logger.info(f"Place {move.armies} armies in {move.to_territory}")
        elif move.move_type == MoveType.FORTIFY:
            logger.info(f"Fortify {move.from_territory} to {move.to_territory}")
    except Exception as e:
        logger.info(f"Move generation requires game state: {e}")

    # Example 3: Create agent with different strategies
    logger.info("\n=== Example 3: Different Agent Strategies ===")

    aggressive_agent = RiskAgent(
        name="Napoleon",
        strategy="aggressive",
        risk_tolerance=0.9,
        diplomatic_stance="aggressive",
    )
    logger.info(
        f"Aggressive agent: {aggressive_agent.name} (tolerance: {
            aggressive_agent.risk_tolerance
        })"
    )

    defensive_agent = RiskAgent(
        name="Defender",
        strategy="defensive",
        risk_tolerance=0.3,
        diplomatic_stance="cooperative",
    )
    logger.info(
        f"Defensive agent: {defensive_agent.name} (tolerance: {
            defensive_agent.risk_tolerance
        })"
    )

    logger.info("\n=== Risk Game Example Complete ===")
    logger.info("Note: Full gameplay requires proper game state initialization")
    logger.info("See the Risk game documentation for complete integration examples")


if __name__ == "__main__":
    main()
