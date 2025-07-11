"""Connect4 game implementation module.

This package provides a complete implementation of the Connect4 game, including:
    - Game agent with LLM-powered players and strategic reasoning
    - State management and move validation with gravity mechanics
    - Position analysis and threat detection
    - Rich UI visualization with animations
    - Configuration and model definitions with type safety
    - Comprehensive examples and testing utilities

The Connect4 module demonstrates advanced game AI capabilities with:
    - Strategic position evaluation
    - Multi-directional threat detection (horizontal, vertical, diagonal)
    - Center control analysis and strategic positioning
    - Pattern recognition for winning combinations
    - Performance optimization for high-throughput scenarios

Example:
    Basic usage:
        >>> from haive.games.connect4 import Connect4Agent, Connect4AgentConfig, Connect4UI
        >>> from haive.games.connect4.state_manager import Connect4StateManager
        >>>
        >>> # Create and configure a Connect4 agent
        >>> config = Connect4AgentConfig(enable_analysis=True)
        >>> agent = Connect4Agent(config)
        >>> ui = Connect4UI()
        >>>
        >>> # Initialize and display game state
        >>> state = Connect4StateManager.initialize()
        >>> ui.display_state(state)
        >>>
        >>> # Create and apply moves
        >>> from haive.games.connect4.models import Connect4Move
        >>> move = Connect4Move(column=3, explanation="Control center")
        >>> new_state = Connect4StateManager.apply_move(state, move)
        >>> ui.display_state(new_state)

    Advanced usage with analysis:
        >>> from haive.games.connect4.models import Connect4Analysis
        >>>
        >>> # Create position analysis
        >>> analysis = Connect4Analysis(
        ...     position_score=0.5,
        ...     center_control=8,
        ...     threats={"winning_moves": [3], "blocking_moves": [2]},
        ...     suggested_columns=[3, 2, 4],
        ...     winning_chances=75
        ... )
        >>> print(f"Position strength: {analysis.position_score}")
        >>> print(f"Winning chances: {analysis.winning_chances}%")

    Rich UI demonstration:
        >>> # Run game with beautiful interface
        >>> for step in agent.app.stream(state.model_dump(), debug=False):
        ...     ui.display_state(step)
        ...     if step.get("game_status") != "ongoing":
        ...         ui.show_game_over(step.get("winner"))
        ...         break
"""

from typing import TYPE_CHECKING

# Core game components
from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig

# Game models and data structures
from haive.games.connect4.models import (
    Connect4Analysis,
    Connect4Move,
    Connect4PlayerDecision,
)
from haive.games.connect4.state import Connect4State
from haive.games.connect4.state_manager import Connect4StateManager
from haive.games.connect4.ui import Connect4UI

# Type checking imports for better IDE support
if TYPE_CHECKING:
    from haive.games.connect4.engines import Connect4Engine
    from haive.games.connect4.factory import Connect4Factory

# Version information
__version__ = "1.0.0"

# Public API exports
__all__ = [
    # Core classes
    "Connect4Agent",
    "Connect4AgentConfig",
    "Connect4State",
    "Connect4StateManager",
    "Connect4UI",
    # Data models
    "Connect4Analysis",
    "Connect4Move",
    "Connect4PlayerDecision",
    # Module metadata
    "__version__",
]

# Module-level constants
BOARD_ROWS = 6
BOARD_COLUMNS = 7
MAX_MOVES = 42
DEFAULT_PLAYER_COLORS = ["red", "yellow"]
WIN_LENGTH = 4


# Quick access functions for common operations
def create_game(
    enable_analysis: bool = True, max_moves: int = MAX_MOVES
) -> Connect4Agent:
    """Create a Connect4 game with default configuration.

    Args:
        enable_analysis: Whether to enable position analysis
        max_moves: Maximum number of moves allowed

    Returns:
        Connect4Agent: Configured game agent

    Example:
        >>> game = create_game(enable_analysis=True)
        >>> # Game ready to play
    """
    config = Connect4AgentConfig(
        name="default_connect4",
        enable_analysis=enable_analysis,
        max_moves=max_moves,
        should_visualize_graph=False,
    )
    return Connect4Agent(config)


def create_ui() -> Connect4UI:
    """Create a Connect4 UI with default settings.

    Returns:
        Connect4UI: Configured UI instance

    Example:
        >>> ui = create_ui()
        >>> state = Connect4StateManager.initialize()
        >>> ui.display_state(state)
    """
    return Connect4UI()


def initialize_game() -> Connect4State:
    """Initialize a new Connect4 game state.

    Returns:
        Connect4State: Initial game state

    Example:
        >>> state = initialize_game()
        >>> assert state.turn == "red"
        >>> assert state.game_status == "ongoing"
    """
    return Connect4StateManager.initialize()


# Add convenience functions to __all__
__all__.extend(
    [
        "create_game",
        "create_ui",
        "initialize_game",
        "BOARD_ROWS",
        "BOARD_COLUMNS",
        "MAX_MOVES",
        "DEFAULT_PLAYER_COLORS",
        "WIN_LENGTH",
    ]
)
