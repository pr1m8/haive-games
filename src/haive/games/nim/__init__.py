"""Nim game module.

This package provides components for simulating and managing the Nim game,
including state management, LLM-based agents, configuration, and strategic analysis.
"""

from .agent import NimAgent
from .config import NimConfig
from .engines import nim_engines
from .models import NimAnalysis, NimMove
from .state import NimState
from .state_manager import NimStateManager

__all__ = [
    "NimAgent",
    "NimAnalysis",
    "NimConfig",
    "NimMove",
    "NimState",
    "NimStateManager",
    "nim_engines"
]
