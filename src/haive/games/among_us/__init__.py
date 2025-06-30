"""Among Us game implementation module.

This package provides a complete implementation of the Among Us social deduction game, including:
    - Game agent with LLM-powered players
    - State management for crew and impostor roles
    - Task completion and voting mechanics
    - Emergency meetings and discussion phases

Example:
    >>> from haive.games.among_us import AmongUsAgent, AmongUsAgentConfig
    >>> config = AmongUsAgentConfig()
    >>> agent = AmongUsAgent(config)
"""

from haive.games.among_us.agent import AmongUsAgent
from haive.games.among_us.config import AmongUsAgentConfig
from haive.games.among_us.state import AmongUsState
from haive.games.among_us.state_manager import AmongUsStateManagerMixin

__all__ = [
    "AmongUsAgent",
    "AmongUsAgentConfig",
    "AmongUsState",
    "AmongUsStateManagerMixin",
]
