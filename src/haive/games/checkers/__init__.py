"""Checkers Game Module - Strategic Board Game Implementation with AI Analysis.

This package provides a comprehensive implementation of the classic Checkers game
(also known as Draughts) with advanced AI analysis, strategic decision-making,
and multi-level gameplay using the Haive framework.

The Checkers game demonstrates fundamental strategic concepts including tactical
combinations, positional play, and endgame technique. The implementation supports
standard American Checkers rules with mandatory jumps and king promotion.

Key Components:
    CheckersAgent: Main game controller with LLM-powered gameplay
    CheckersAgentConfig: Flexible configuration for various game modes
    CheckersStateManager: Complete game state management and rule enforcement
    CheckersAnalysis: Strategic analysis and position evaluation
    CheckersMove: Comprehensive move representation with validation
    CheckersState: Core game state with move history and validation

Game Features:
    - Standard 8x8 American Checkers rules
    - Mandatory jump captures with multiple jump sequences
    - King promotion at board edges
    - Advanced AI analysis with strategic reasoning
    - Rich terminal UI with visualization
    - Tournament play capabilities
    - Educational mode with move explanations
    - Performance optimization options

Strategic Concepts:
    - Tactical combinations (forks, pins, skewers)
    - Positional play and center control
    - King vs. men endgame technique
    - Opposition principles and tempo usage
    - Sacrifice patterns for advantage

Examples:
    Basic game setup::

        from haive.games.checkers import CheckersAgent, CheckersAgentConfig

        # Create standard Checkers game
        config = CheckersAgentConfig()
        agent = CheckersAgent(config)
        result = agent.run_game(visualize=True)

    Strategic analysis::

        from haive.games.checkers import CheckersStateManager

        # Analyze position
        manager = CheckersStateManager()
        state = manager.initialize_game()
        analysis = manager.analyze_position(state, "player1")

        print(f"Material: {analysis.material_advantage}")
        print(f"Position: {analysis.positional_evaluation}")
        print(f"Best move: {analysis.best_move}")

    Tournament play::

        from haive.core.engine.aug_llm import AugLLMConfig

        # Tournament configuration
        config = CheckersAgentConfig(
            aug_llm_configs={
                "player1": AugLLMConfig(temperature=0.3),  # Defensive
                "player2": AugLLMConfig(temperature=0.9)   # Aggressive
            },
            max_turns=200,
            show_analysis=True
        )
        agent = CheckersAgent(config)

        # Run tournament games
        results = []
        for game in range(10):
            result = agent.run_game(visualize=False)
            results.append(result)

Version: 2.0.0
License: Same as Haive framework
Maintainer: Haive Development Team
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

# Core game components
from haive.games.checkers.agent import CheckersAgent
from haive.games.checkers.config import CheckersAgentConfig

# Data models and analysis
from haive.games.checkers.models import (
    CheckersAnalysis,
    CheckersMove,
    CheckersPlayerDecision,
)
from haive.games.checkers.state import CheckersState
from haive.games.checkers.state_manager import CheckersStateManager

# Engine components
try:
    from haive.games.checkers.engines import checkers_engines

    _ENGINES_AVAILABLE = True
except ImportError:
    _ENGINES_AVAILABLE = False
    checkers_engines = None

# UI components (optional)
try:
    from haive.games.checkers.ui import CheckersUI

    _UI_AVAILABLE = True
except ImportError:
    _UI_AVAILABLE = False
    CheckersUI = None

# Type aliases for better API documentation
BoardPosition = List[List[str]]
GameResult = Dict[str, Any]
MoveHistory = List[CheckersMove]
AnalysisResult = Dict[str, Union[str, int, bool, List[Any]]]
PlayerConfiguration = Dict[str, Any]

# Version information
__version__ = "2.0.0"
__author__ = "Haive Development Team"
__license__ = "Same as Haive framework"

# Public API exports
__all__ = [
    # Core Classes
    "CheckersAgent",
    "CheckersAgentConfig",
    "CheckersState",
    "CheckersStateManager",
    # Data Models
    "CheckersAnalysis",
    "CheckersMove",
    "CheckersPlayerDecision",
    # Engine Components (conditional)
    "checkers_engines",
    # UI Components (conditional)
    "CheckersUI",
    # Type Aliases
    "BoardPosition",
    "GameResult",
    "MoveHistory",
    "AnalysisResult",
    "PlayerConfiguration",
    # Utility Functions
    "create_standard_game",
    "create_tournament_game",
    "create_educational_game",
    "analyze_board_position",
    "validate_checkers_move",
    "format_game_result",
    # Version Info
    "__version__",
    "__author__",
    "__license__",
]

# Conditional exports based on availability
if _ENGINES_AVAILABLE:
    __all__.extend(["checkers_engines"])

if _UI_AVAILABLE:
    __all__.extend(["CheckersUI"])


# Utility functions for common operations
def create_standard_game(
    show_analysis: bool = True, visualize: bool = True, max_turns: int = 200
) -> CheckersAgent:
    """Create a standard Checkers game with default configuration.

    Args:
        show_analysis: Whether to enable position analysis
        visualize: Whether to enable game visualization
        max_turns: Maximum number of turns allowed

    Returns:
        Configured CheckersAgent ready for gameplay

    Example:
        >>> agent = create_standard_game(show_analysis=True)
        >>> result = agent.run_game()
    """
    config = CheckersAgentConfig(
        max_turns=max_turns,
        show_analysis=show_analysis,
        ui_enabled=visualize,
        move_timeout=30,
        analysis_depth=2,
    )
    return CheckersAgent(config)


def create_tournament_game(
    player1_style: str = "balanced",
    player2_style: str = "balanced",
    fast_mode: bool = True,
) -> CheckersAgent:
    """Create a Checkers game optimized for tournament play.

    Args:
        player1_style: Playing style for player 1 ("aggressive", "defensive", "balanced")
        player2_style: Playing style for player 2 ("aggressive", "defensive", "balanced")
        fast_mode: Whether to optimize for speed over analysis depth

    Returns:
        Configured CheckersAgent for tournament gameplay

    Example:
        >>> agent = create_tournament_game("aggressive", "defensive")
        >>> result = agent.run_game(visualize=False)
    """
    from haive.core.engine.aug_llm import AugLLMConfig

    style_configs = {
        "aggressive": {
            "temperature": 0.9,
            "system_message": "You are an aggressive checkers player who seeks tactical combinations.",
        },
        "defensive": {
            "temperature": 0.3,
            "system_message": "You are a defensive checkers player who prioritizes piece safety.",
        },
        "balanced": {
            "temperature": 0.7,
            "system_message": "You are a balanced checkers player with strategic awareness.",
        },
    }

    config = CheckersAgentConfig(
        aug_llm_configs={
            "player1": AugLLMConfig(
                model="gpt-4",
                temperature=style_configs[player1_style]["temperature"],
                system_message=style_configs[player1_style]["system_message"],
            ),
            "player2": AugLLMConfig(
                model="gpt-4",
                temperature=style_configs[player2_style]["temperature"],
                system_message=style_configs[player2_style]["system_message"],
            ),
        },
        max_turns=150 if fast_mode else 250,
        show_analysis=not fast_mode,
        ui_enabled=False,
        move_timeout=10 if fast_mode else 30,
        analysis_depth=1 if fast_mode else 2,
    )
    return CheckersAgent(config)


def create_educational_game(
    enable_explanations: bool = True, slower_pace: bool = True
) -> CheckersAgent:
    """Create a Checkers game optimized for educational purposes.

    Args:
        enable_explanations: Whether to enable detailed move explanations
        slower_pace: Whether to allow more time for analysis and explanations

    Returns:
        Configured CheckersAgent for educational gameplay

    Example:
        >>> agent = create_educational_game(enable_explanations=True)
        >>> result = agent.run_game(visualize=True)
    """
    from haive.core.engine.aug_llm import AugLLMConfig

    config = CheckersAgentConfig(
        aug_llm_configs={
            "player1": AugLLMConfig(
                model="gpt-4",
                temperature=0.5,
                system_message="You are a checkers teacher who explains moves clearly with educational reasoning.",
            ),
            "player2": AugLLMConfig(
                model="gpt-4",
                temperature=0.5,
                system_message="You are a checkers instructor who demonstrates good technique and explains strategic concepts.",
            ),
            "analyzer": AugLLMConfig(
                model="gpt-4",
                temperature=0.1,
                system_message="You are a checkers coach who provides detailed educational analysis.",
            ),
        },
        max_turns=100,  # Shorter games for educational focus
        show_analysis=enable_explanations,
        ui_enabled=True,
        move_timeout=60 if slower_pace else 30,
        analysis_depth=3 if enable_explanations else 2,
    )
    return CheckersAgent(config)


def analyze_board_position(
    board_position: BoardPosition, current_player: str = "player1"
) -> CheckersAnalysis:
    """Analyze a Checkers board position and provide strategic insights.

    Args:
        board_position: 8x8 board representation
        current_player: Player to analyze for ("player1" or "player2")

    Returns:
        Comprehensive analysis of the position

    Example:
        >>> manager = CheckersStateManager()
        >>> state = manager.initialize_game()
        >>> analysis = analyze_board_position(state.board, "player1")
        >>> print(f"Best move: {analysis.best_move}")
    """
    manager = CheckersStateManager()

    # Create state from board position
    state = CheckersState(
        board=board_position,
        current_player=current_player,
        move_history=[],
        game_over=False,
        winner=None,
        kings={},
    )

    return manager.analyze_position(state, current_player)


def validate_checkers_move(
    board_position: BoardPosition, player: str, move: str
) -> bool:
    """Validate if a checkers move is legal for the given position.

    Args:
        board_position: 8x8 board representation
        player: Player attempting the move
        move: Move in algebraic notation (e.g., "22-18")

    Returns:
        True if move is valid, False otherwise

    Example:
        >>> manager = CheckersStateManager()
        >>> state = manager.initialize_game()
        >>> is_valid = validate_checkers_move(state.board, "player1", "22-18")
        >>> print(f"Move valid: {is_valid}")
    """
    manager = CheckersStateManager()

    # Create state from board position
    state = CheckersState(
        board=board_position,
        current_player=player,
        move_history=[],
        game_over=False,
        winner=None,
        kings={},
    )

    return manager.validate_move(state, player, move)


def format_game_result(result: GameResult) -> str:
    """Format a game result dictionary into a readable string.

    Args:
        result: Game result dictionary from CheckersAgent.run_game()

    Returns:
        Formatted string describing the game outcome

    Example:
        >>> agent = create_standard_game()
        >>> result = agent.run_game()
        >>> summary = format_game_result(result)
        >>> print(summary)
    """
    winner = result.get("winner", "Draw")
    turns = result.get("turn_count", "Unknown")
    duration = result.get("duration", "Unknown")

    if winner == "Draw":
        return f"Game ended in a draw after {turns} turns ({duration})"
    else:
        return f"{winner} won after {turns} turns ({duration})"


# Module-level constants for common configurations
DEFAULT_GAME_CONFIG = {
    "max_turns": 200,
    "show_analysis": True,
    "ui_enabled": True,
    "move_timeout": 30,
    "analysis_depth": 2,
}

TOURNAMENT_CONFIG = {
    "max_turns": 150,
    "show_analysis": False,
    "ui_enabled": False,
    "move_timeout": 10,
    "analysis_depth": 1,
}

EDUCATIONAL_CONFIG = {
    "max_turns": 100,
    "show_analysis": True,
    "ui_enabled": True,
    "move_timeout": 60,
    "analysis_depth": 3,
}

# Performance constants
MAX_RECOMMENDED_TURNS = 300
MIN_MOVE_TIMEOUT = 5
MAX_ANALYSIS_DEPTH = 5

# Game state constants
BOARD_SIZE = 8
INITIAL_PIECES_PER_PLAYER = 12
KING_ROWS = {"player1": 0, "player2": 7}

# Import validation
if TYPE_CHECKING:
    # Import type checking only
    from haive.games.checkers.configurable_config import ConfigurableCheckersConfig
    from haive.games.checkers.generic_engines import GenericCheckersEngine
    from haive.games.checkers.standalone_game import StandaloneCheckersGame
