"""Mastermind game module.

This package provides logic, configuration, state management, engine interfaces,
and an LLM-based agent for playing and analyzing Mastermind (codebreaking) games.
"""

from haive.games.mastermind.agent import MastermindAgent
from haive.games.mastermind.config import MastermindConfig
from haive.games.mastermind.engines import mastermind_engines
from haive.games.mastermind.models import ColorCode, MastermindAnalysis, MastermindGuess
from haive.games.mastermind.state import MastermindState
from haive.games.mastermind.state_manager import MastermindStateManager

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
