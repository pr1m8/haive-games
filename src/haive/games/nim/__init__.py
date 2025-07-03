"""Nim game module.

This package provides components for simulating and managing the Nim game,
including state management, LLM-based agents, configuration, and strategic analysis.
"""

from haive.games.nim.agent import NimAgent
from haive.games.nim.config import NimConfig
from haive.games.nim.engines import nim_engines
from haive.games.nim.models import NimAnalysis, NimMove
from haive.games.nim.state import NimState
from haive.games.nim.state_manager import NimStateManager

__all__ = [
    "NimAgent",
    "NimAnalysis",
    "NimConfig",
    "NimMove",
    "NimState",
    "NimStateManager",
    "nim_engines",
]
