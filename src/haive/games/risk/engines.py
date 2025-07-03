"""Risk game engines.

This module defines engine configurations for the Risk game,
including state management, analysis, and strategic planning.
"""

from typing import Any

from haive.games.risk.config import RiskConfig


def risk_engines(config: RiskConfig | None = None) -> dict[str, Any]:
    """Create a set of engines for the Risk game.

    Args:
        config: Optional configuration for the Risk game.
            If not provided, default configuration will be used.

    Returns:
        A dictionary of engine configurations for the Risk game.
    """
    # Use default config if none provided
    if config is None:
        config = RiskConfig.classic()

    # Define engines for Risk game
    engines = {
        "state_manager": {
            "type": "RiskStateManager",
            "config": {"risk_config": config.dict()},
        },
        "agent": {"type": "RiskAgent", "config": {"strategy": "balanced"}},
        "analysis": {"type": "RiskAnalysis", "config": {}},
    }

    return engines
