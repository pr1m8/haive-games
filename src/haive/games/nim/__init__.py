"""Nim Game Module - Mathematical Strategy Game Implementation.

This package provides comprehensive components for simulating and managing the mathematical
game of Nim, including state management, LLM-based agents, strategic analysis, and
perfect play algorithms. The implementation supports multiple game variants and provides
educational tools for understanding game theory and optimal play strategies.

The Nim game is a fundamental example in combinatorial game theory, demonstrating
concepts such as:
- Nim-sum calculation using XOR operations
- P-positions and N-positions (Sprague-Grundy theorem)
- Perfect information games with optimal strategies
- Misère variants and endgame analysis
- Multi-pile strategic considerations

Key Components:
    NimAgent: LLM-based agent with strategic analysis capabilities
    NimStateManager: Complete game state management and rule enforcement
    NimConfig: Flexible configuration for various game modes and settings
    NimAnalysis: Mathematical analysis of positions with strategic recommendations
    NimMove: Comprehensive move representation with reasoning
    NimState: Core game state with validation and serialization

Game Variants Supported:
    - Standard Nim: Last player to move wins
    - Misère Nim: Last player to move loses
    - Fibonacci Nim: Restricted move counts
    - Kayles: Splitting moves allowed
    - Subtraction Game: Limited stone removal options

Educational Features:
    - Step-by-step strategic analysis
    - Binary arithmetic demonstrations
    - Game theory concept explanations
    - Optimal play algorithm illustrations
    - Mathematical proof presentations

Examples:
    Basic game setup::

        from haive.games.nim import NimAgent, NimConfig

        # Create standard Nim game
        config = NimConfig(pile_sizes=[3, 5, 7], misere_mode=False)
        agent = NimAgent(config=config)
        result = agent.run_game()

    Strategic analysis::

        from haive.games.nim import NimStateManager

        # Analyze position
        manager = NimStateManager()
        manager.initialize_game([4, 6, 8])
        analysis = manager.analyze_position()

        print(f"Nim-sum: {analysis.nim_sum}")
        print(f"Strategy: {analysis.winning_strategy}")
        print(f"Optimal move: {analysis.recommended_move}")

    Misère variant::

        from haive.games.nim import NimConfig, NimAgent

        # Misère Nim (last player loses)
        config = NimConfig(
            pile_sizes=[2, 3, 4],
            misere_mode=True,
            enable_analysis=True
        )
        agent = NimAgent(config=config)
        result = agent.run_game()

Version: 2.0.0
License: Same as Haive framework
Maintainer: Haive Development Team
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

# Core game components
from haive.games.nim.agent import NimAgent
from haive.games.nim.config import NimConfig

# Engine and strategy components
from haive.games.nim.engines import nim_engines

# Data models and analysis
from haive.games.nim.models import (  # NimPosition,  # TODO: This class doesn't exist - needs to be implemented; MoveQuality,  # TODO: Check if this exists; AnalysisDepth,  # TODO: Check if this exists
    NimAnalysis,
    NimMove,
    NimVariant,
    PositionType,
)
from haive.games.nim.state import NimState
from haive.games.nim.state_manager import NimStateManager

# UI components (optional)
try:
    from haive.games.nim.ui import RICH_AVAILABLE, NimUI

    _UI_AVAILABLE = True
except ImportError:
    _UI_AVAILABLE = False
    NimUI = None
    RICH_AVAILABLE = False

# Type aliases for better API documentation
PileConfiguration = List[int]
GameResult = Dict[str, Any]
AnalysisResult = Dict[str, Union[int, str, bool, List[Any]]]

# Version information
__version__ = "2.0.0"
__author__ = "Haive Development Team"
__license__ = "Same as Haive framework"

# Public API exports
__all__ = [
    # Core Classes
    "NimAgent",
    "NimConfig",
    "NimState",
    "NimStateManager",
    # Data Models
    "NimAnalysis",
    "NimMove",
    "NimVariant",
    # "NimPosition",  # TODO: Not implemented
    # Enums and Types
    "PositionType",
    # "MoveQuality",  # TODO: Check if exists
    # "AnalysisDepth",  # TODO: Check if exists
    # Engine Components
    "nim_engines",
    # UI Components (conditional)
    "NimUI",
    "RICH_AVAILABLE",
    # Type Aliases
    "PileConfiguration",
    "GameResult",
    "AnalysisResult",
    # Utility Functions
    "create_standard_game",
    "create_misere_game",
    "analyze_position",
    "calculate_nim_sum",
    "find_optimal_move",
    # Version Info
    "__version__",
    "__author__",
    "__license__",
]

# Conditional exports based on availability
if _UI_AVAILABLE:
    __all__.extend(["NimUI", "RICH_AVAILABLE"])


# Utility functions for common operations
def create_standard_game(
    pile_sizes: PileConfiguration = [3, 5, 7],
    enable_analysis: bool = True,
    visualize: bool = False,
) -> NimAgent:
    """Create a standard Nim game with default configuration.

    Args:
        pile_sizes: Initial pile sizes for the game
        enable_analysis: Whether to enable strategic analysis
        visualize: Whether to enable visualization

    Returns:
        Configured NimAgent ready for gameplay

    Example:
        >>> agent = create_standard_game([4, 6, 8])
        >>> result = agent.run_game()
    """
    config = NimConfig(
        pile_sizes=pile_sizes,
        misere_mode=False,
        enable_analysis=enable_analysis,
        visualize=visualize,
    )
    return NimAgent(config=config)


def create_misere_game(
    pile_sizes: PileConfiguration = [2, 3, 4],
    enable_analysis: bool = True,
    visualize: bool = False,
) -> NimAgent:
    """Create a misère Nim game (last player loses).

    Args:
        pile_sizes: Initial pile sizes for the game
        enable_analysis: Whether to enable strategic analysis
        visualize: Whether to enable visualization

    Returns:
        Configured NimAgent for misère gameplay

    Example:
        >>> agent = create_misere_game([1, 2, 3])
        >>> result = agent.run_game()
    """
    config = NimConfig(
        pile_sizes=pile_sizes,
        misere_mode=True,
        enable_analysis=enable_analysis,
        visualize=visualize,
    )
    return NimAgent(config=config)


def analyze_position(
    pile_sizes: PileConfiguration, misere_mode: bool = False
) -> NimAnalysis:
    """Analyze a Nim position and provide strategic recommendations.

    Args:
        pile_sizes: Current pile sizes to analyze
        misere_mode: Whether to use misère rules

    Returns:
        Comprehensive analysis of the position

    Example:
        >>> analysis = analyze_position([3, 5, 7])
        >>> print(f"Nim-sum: {analysis.nim_sum}")
        >>> print(f"Evaluation: {analysis.position_evaluation}")
    """
    manager = NimStateManager()
    config = NimConfig(pile_sizes=pile_sizes, misere_mode=misere_mode)
    manager.initialize_game(pile_sizes)
    return manager.analyze_position()


def calculate_nim_sum(pile_sizes: PileConfiguration) -> int:
    """Calculate the nim-sum (XOR) of pile sizes.

    Args:
        pile_sizes: List of pile sizes

    Returns:
        Nim-sum as integer

    Example:
        >>> nim_sum = calculate_nim_sum([3, 5, 7])
        >>> print(f"Nim-sum: {nim_sum}")  # Output: 1
    """
    import functools
    import operator

    return functools.reduce(operator.xor, pile_sizes, 0)


def find_optimal_move(
    pile_sizes: PileConfiguration, misere_mode: bool = False
) -> Optional[NimMove]:
    """Find the optimal move for a given position.

    Args:
        pile_sizes: Current pile sizes
        misere_mode: Whether to use misère rules

    Returns:
        Optimal move or None if no winning move exists

    Example:
        >>> move = find_optimal_move([3, 5, 7])
        >>> if move:
        ...     print(f"Take {move.stones_taken} from pile {move.pile_index}")
    """
    manager = NimStateManager()
    config = NimConfig(pile_sizes=pile_sizes, misere_mode=misere_mode)
    manager.initialize_game(pile_sizes)

    try:
        return manager.find_optimal_move()
    except Exception:
        return None


# Module-level constants
DEFAULT_PILE_SIZES: PileConfiguration = [3, 5, 7]
CLASSIC_PILE_SIZES: PileConfiguration = [3, 5, 7]
SIMPLE_PILE_SIZES: PileConfiguration = [1, 2, 3]
COMPLEX_PILE_SIZES: PileConfiguration = [4, 6, 8, 10]

# Game theory constants
LOSING_POSITION_NIMSUM = 0
WINNING_POSITION_NIMSUM_MIN = 1

# Performance constants
MAX_RECOMMENDED_PILES = 20
MAX_RECOMMENDED_PILE_SIZE = 1000

# Import validation
if TYPE_CHECKING:
    # Import type checking only
    from haive.games.nim.configurable_config import ConfigurableNimConfig
    from haive.games.nim.generic_engines import GenericNimEngine
    from haive.games.nim.standalone_game import StandaloneNimGame
