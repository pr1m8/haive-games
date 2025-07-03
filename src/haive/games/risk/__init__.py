"""Risk game module.

This package provides components for simulating and managing the Risk game,
including state management, territory control, armies, attack mechanics,
LLM-based agents, configuration, and strategic analysis.
"""

from haive.games.risk.agent import RiskAgent
from haive.games.risk.config import RiskConfig
from haive.games.risk.engines import risk_engines
from haive.games.risk.models import (
    Card,
    Continent,
    Player,
    RiskAnalysis,
    RiskMove,
    Territory,
)
from haive.games.risk.state import RiskState
from haive.games.risk.state_manager import RiskStateManager

__all__ = [
    "Card",
    "Continent",
    "Player",
    "RiskAgent",
    "RiskAnalysis",
    "RiskConfig",
    "RiskMove",
    "RiskState",
    "RiskStateManager",
    "Territory",
    "risk_engines",
]
