"""Connect4 game implementation module.

This package provides a complete implementation of the Connect4 game, including:
    - Game agent with LLM-powered players
    - State management and move validation
    - Position analysis and evaluation
    - Rich UI visualization
    - Configuration and model definitions

Example:
    >>> from haive.games.connect4 import Connect4Agent, Connect4AgentConfig, Connect4UI
    >>>
    >>> # Create and configure a Connect4 agent
    >>> config = Connect4AgentConfig(enable_analysis=True)
    >>> agent = Connect4Agent(config)
    >>> ui = Connect4UI()
    >>>
    >>> # Initialize and display game state
    >>> state = Connect4State.initialize()
    >>> ui.display_state(state)
"""

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.models import (
    Connect4Analysis,
    Connect4Move,
    Connect4PlayerDecision,
)
from haive.games.connect4.state import Connect4State
from haive.games.connect4.state_manager import Connect4StateManager
from haive.games.connect4.ui import Connect4UI

__all__ = [
    "Connect4Agent",
    "Connect4AgentConfig",
    "Connect4Analysis",
    "Connect4Move",
    "Connect4PlayerDecision",
    "Connect4State",
    "Connect4StateManager",
    "Connect4UI",
]
