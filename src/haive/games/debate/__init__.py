"""Debate game module for structured argumentation."""

from haive.games.debate.agent import DebateAgent
from haive.games.debate.config import DebateAgentConfig
from haive.games.debate.state import DebateState
from haive.games.debate.state_manager import DebateStateManager

__all__ = [
    "DebateAgent",
    "DebateAgentConfig",
    "DebateState",
    "DebateStateManager",
]
