"""Haive Games Package - AI-powered implementations of classic and modern games.

This package provides a comprehensive collection of game implementations that
demonstrate AI agent capabilities in structured, rule-based environments.
Each game is built with the Haive framework and includes AI agents, game logic,
state management, and user interfaces.

The games serve multiple purposes:
1. Demonstration of AI agent capabilities in game environments
2. Benchmarking and testing of different AI strategies
3. Educational examples of game theory and AI decision-making
4. Entertainment and interactive experiences

Available Games:

Strategy Games:
    - Clue (Cluedo): Classic mystery deduction game with AI detectives
    - Checkers: Traditional board game with strategic AI opponents
    - Chess: Classic chess with various AI difficulty levels
    - Go: Ancient strategy game with modern AI implementations

Card Games:
    - Poker: Texas Hold'em with probabilistic reasoning agents
    - Blackjack: Card counting and strategy optimization
    - Uno: Multi-player card game with rule-based AI

Party Games:
    - Among Us: Social deduction game with AI imposters and crewmates
    - Werewolf/Mafia: Social deduction with natural language reasoning

Each game implementation includes:
- Complete game logic and rule enforcement
- Multiple AI agent types with different strategies
- State management and history tracking
- Rich logging and debugging capabilities
- Extensible configuration options
- Performance monitoring and analytics

Usage:
    ```python
    from haive.games.clue import ClueGame
    from haive.games.checkers import CheckersGame
    from haive.games.poker import PokerGame

    # Create a Clue game with AI players
    clue_game = ClueGame(
        players=["Detective AI", "Logical Agent", "Random Player"],
        ai_difficulty="medium"
    )

    # Run the game
    result = await clue_game.play()
    print(f"Winner: {result.winner}")

    # Create a checkers match
    checkers = CheckersGame(
        player1="Minimax Agent",
        player2="Monte Carlo Agent"
    )

    winner = await checkers.play_match()
    ```

Architecture:
    Each game follows a consistent architecture pattern:
    - Game Controller: Manages game flow and rules
    - State Manager: Tracks game state and history
    - AI Agents: Different AI strategies and personalities
    - UI Components: Visual representation and interaction
    - Configuration: Customizable game settings

The games are designed to be:
- Modular and extensible
- Educational and demonstrative
- Performance-optimized for AI testing
- Compatible with various AI backends
- Suitable for research and development

For detailed information about each game, see the individual game modules
and their respective documentation.
"""

import logging

# Configure logging - reduce verbosity from underlying libraries
logging.getLogger("haive.core.models.llm.base").setLevel(logging.ERROR)
logging.getLogger("haive.core.engine.aug_llm").setLevel(logging.ERROR)
logging.getLogger("openai").setLevel(logging.ERROR)
logging.getLogger("langchain").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Set up games-specific logger with appropriate level for game events
games_logger = logging.getLogger("haive.games")
games_logger.setLevel(logging.INFO)

__version__ = "0.1.0"

# Import commonly used game components
try:
    from haive.games.checkers import CheckersGame
    from haive.games.clue import ClueGame

    GAMES_AVAILABLE = True
except ImportError:
    # Graceful degradation if specific games aren't available
    GAMES_AVAILABLE = False
    games_logger.warning("Some game modules not available")

__all__ = [
    "__version__",
    "games_logger",
]

if GAMES_AVAILABLE:
    __all__.extend(["CheckersGame", "ClueGame"])
