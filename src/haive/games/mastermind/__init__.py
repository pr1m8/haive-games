"""Mastermind game module.

This package provides logic, configuration, state management, engine interfaces,
and an LLM-based agent for playing and analyzing Mastermind (codebreaking) games.
"""

from .agent import MastermindAgent
from .config import MastermindConfig
from .engines import mastermind_engines
from .models import ColorCode, MastermindAnalysis, MastermindGuess
from .state import MastermindState
from .state_manager import MastermindStateManager

__all__ = [
    "ColorCode",
    "MastermindAgent",
    "MastermindAnalysis",
    "MastermindConfig",
    "MastermindGuess",
    "MastermindState",
    "MastermindStateManager",
    "mastermind_engines",
]
