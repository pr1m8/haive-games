"""Debate game implementation module.

This package provides a complete implementation of formal debate games, including:
    - Multi-round debate structure
    - Argument presentation and rebuttal phases
    - Scoring and judging mechanisms
    - Topic selection and research phases

Example:
    >>> from haive.games.debate import DebateAgent, DebateAgentConfig
    >>> config = DebateAgentConfig()
    >>> agent = DebateAgent(config)
"""

from haive.games.debate.agent import DebateAgent
from haive.games.debate.config import DebateAgentConfig

__all__ = [
    "DebateAgent",
    "DebateAgentConfig",
]
