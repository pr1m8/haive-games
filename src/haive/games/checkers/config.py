"""Comprehensive configuration system for strategic Checkers gameplay and AI agents.

This module provides sophisticated configuration management for Checkers agents with
support for rule variations, performance optimization, and strategic AI customization.
The configuration system enables flexible game setups, from casual play to competitive
tournaments and AI research applications.

The configuration system supports:
- Complete rule customization with international variants
- Advanced AI engine configurations with strategic depth control
- Performance optimization for different gameplay scenarios
- Comprehensive validation and error handling
- Factory methods for common game configurations
- Strategic analysis parameter tuning

Examples:
    Standard American Checkers configuration::\n

        config = CheckersAgentConfig.american_checkers()
        agent = CheckersAgent(config)

    International Draughts configuration::\n

        config = CheckersAgentConfig.international_draughts()
        # 10x10 board with flying kings

    Tournament-level competitive play::\n

        config = CheckersAgentConfig.tournament()
        # Optimized for strong AI play with extended analysis

    Training configuration for AI development::\n

        config = CheckersAgentConfig.training()
        # Balanced for learning and experimentation

    Custom rule variant::\n

        config = CheckersAgentConfig(
            board_size=10,
            max_turns=200,
            allow_flying_kings=True,
            mandatory_jumps=True,
            king_promotion_row=9,
            strategic_depth=5
        )

Note:
    All configurations use Pydantic for validation and support both JSON serialization
    and integration with distributed game systems for tournament play.
"""

from typing import Any, Dict, Literal, Optional, Union

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field, computed_field, field_validator

from haive.games.checkers.engines import build_checkers_aug_llms
from haive.games.checkers.state import CheckersState


class CheckersAgentConfig(AgentConfig):
    """Advanced configuration system for Checkers agents with comprehensive rule support.

    This class provides complete configuration management for Checkers gameplay,
    supporting multiple rule variants, strategic AI customization, and performance
    optimization. The configuration system enables flexible game setups from
    casual play to competitive tournaments and AI research applications.

    The configuration supports:
    - International rule variants (American, International, Russian, Brazilian)
    - Advanced AI strategy parameters with depth control
    - Performance optimization for different scenarios
    - Comprehensive validation and error handling
    - Factory methods for common configurations
    - Strategic analysis parameter tuning

    Attributes:
        board_size (int): Size of the checkers board (8 for American, 10 for International).
            Determines the game complexity and strategy depth.
        max_turns (int): Maximum number of turns before declaring a draw.
            Prevents infinite games and ensures reasonable game duration.
        allow_flying_kings (bool): Whether kings can move any distance along diagonals.
            True for International Draughts, False for American Checkers.
        mandatory_jumps (bool): Whether jumps are mandatory when available.
            Core rule that significantly affects strategy and gameplay.
        king_promotion_row (int): Row where pieces promote to kings.
            Typically board_size-1 for the opponent's back rank.
        strategic_depth (int): Analysis depth for AI strategic planning.
            Higher values provide stronger play but slower decision-making.
        time_per_move (float): Maximum time allowed per move in seconds.
            Prevents excessive computation and ensures game flow.
        enable_endgame_tables (bool): Whether to use endgame tablebase lookup.
            Provides perfect play in endgame positions when available.
        analysis_threads (int): Number of threads for position analysis.
            Enables parallel processing for faster strategic evaluation.
        memory_limit_mb (int): Memory limit for position evaluation in MB.
            Prevents excessive memory usage during deep analysis.
        state_schema (type[BaseModel]): State schema for the checkers game.
            Pydantic model defining the game state structure.
        engines (Dict[str, AugLLMConfig]): LLM configurations for players and analyzers.
            Mapping of engine names to their configuration objects.
        runnable_config (RunnableConfig): Runtime configuration for the agent.
            LangGraph configuration including recursion limits and threading.

    Examples:
        Standard American Checkers configuration::\n

            config = CheckersAgentConfig.american_checkers()
            assert config.board_size == 8
            assert config.allow_flying_kings == False
            assert config.mandatory_jumps == True

        International Draughts configuration::\n

            config = CheckersAgentConfig.international_draughts()
            assert config.board_size == 10
            assert config.allow_flying_kings == True
            assert config.strategic_depth == 6

        Tournament-level competitive play::\n

            config = CheckersAgentConfig.tournament()
            assert config.strategic_depth == 8
            assert config.time_per_move == 30.0
            assert config.enable_endgame_tables == True

        Custom configuration with validation::\n

            config = CheckersAgentConfig(
                board_size=12,  # Custom board size
                max_turns=300,
                allow_flying_kings=True,
                strategic_depth=4,
                time_per_move=15.0
            )
            # Automatic validation ensures king_promotion_row = 11

        Training configuration for AI development::\n

            config = CheckersAgentConfig.training()
            assert config.strategic_depth == 3  # Faster for experimentation
            assert config.memory_limit_mb == 512  # Reasonable resource usage

        Performance-optimized configuration::\n

            config = CheckersAgentConfig.performance()
            assert config.analysis_threads == 4
            assert config.memory_limit_mb == 1024
            assert config.enable_endgame_tables == True

    Note:
        All configurations use Pydantic for validation and support both JSON
        serialization and integration with distributed tournament systems.
    """

    board_size: int = Field(
        default=8,
        ge=6,
        le=12,
        description="Size of the checkers board (6-12, typically 8 for American or 10 for International)",
        examples=[8, 10, 12],
    )

    max_turns: int = Field(
        default=100,
        ge=20,
        le=500,
        description="Maximum number of turns before declaring a draw (20-500)",
        examples=[100, 150, 200, 300],
    )

    allow_flying_kings: bool = Field(
        default=False,
        description="Whether kings can move any distance along diagonals (True for International Draughts)",
        examples=[True, False],
    )

    mandatory_jumps: bool = Field(
        default=True,
        description="Whether jumps are mandatory when available (core gameplay rule)",
        examples=[True, False],
    )

    king_promotion_row: Optional[int] = Field(
        default=None,
        ge=0,
        description="Row where pieces promote to kings (auto-calculated from board_size if not specified)",
        examples=[7, 9, 11],
    )

    strategic_depth: int = Field(
        default=4,
        ge=1,
        le=10,
        description="Analysis depth for AI strategic planning (1-10, higher is stronger but slower)",
        examples=[3, 4, 5, 6, 8],
    )

    time_per_move: float = Field(
        default=10.0,
        ge=1.0,
        le=120.0,
        description="Maximum time allowed per move in seconds (1-120)",
        examples=[5.0, 10.0, 15.0, 30.0, 60.0],
    )

    enable_endgame_tables: bool = Field(
        default=False,
        description="Whether to use endgame tablebase lookup for perfect endgame play",
        examples=[True, False],
    )

    analysis_threads: int = Field(
        default=1,
        ge=1,
        le=8,
        description="Number of threads for position analysis (1-8 for parallel processing)",
        examples=[1, 2, 4, 8],
    )

    memory_limit_mb: int = Field(
        default=256,
        ge=64,
        le=2048,
        description="Memory limit for position evaluation in MB (64-2048)",
        examples=[128, 256, 512, 1024],
    )

    state_schema: type[BaseModel] = Field(
        default=CheckersState,
        description="State schema for the checkers game (Pydantic model)",
    )

    engines: Dict[str, AugLLMConfig] = Field(
        default_factory=build_checkers_aug_llms,
        description="LLM configurations for players and analyzers",
    )

    runnable_config: RunnableConfig = Field(
        default={"configurable": {"recursion_limit": 2000}},
        description="Runtime configuration for the agent including recursion limits",
    )

    @field_validator("king_promotion_row")
    @classmethod
    def validate_king_promotion_row(cls, v: Optional[int], values) -> int:
        """Validate and auto-calculate king promotion row.

        Args:
            v (Optional[int]): The specified king promotion row.
            values: Other field values for validation context.

        Returns:
            int: The validated king promotion row.

        Raises:
            ValueError: If promotion row is invalid for the board size.
        """
        board_size = values.get("board_size", 8)
        if v is None:
            return board_size - 1

        if not (0 <= v < board_size):
            raise ValueError(f"King promotion row must be between 0 and {board_size-1}")

        return v

    @computed_field
    @property
    def total_squares(self) -> int:
        """Calculate total number of squares on the board.

        Returns:
            int: Total number of squares (board_size * board_size).
        """
        return self.board_size * self.board_size

    @computed_field
    @property
    def playable_squares(self) -> int:
        """Calculate number of playable (dark) squares on the board.

        Returns:
            int: Number of playable squares (half of total squares).
        """
        return self.total_squares // 2

    @computed_field
    @property
    def pieces_per_player(self) -> int:
        """Calculate number of pieces per player at game start.

        Returns:
            int: Number of pieces each player starts with.
        """
        # Typically 3 rows of pieces for each player
        return (self.board_size // 2 - 1) * (self.board_size // 2)

    @computed_field
    @property
    def game_variant(self) -> str:
        """Determine the game variant based on configuration.

        Returns:
            str: Game variant name (American, International, Custom).
        """
        if self.board_size == 8 and not self.allow_flying_kings:
            return "American Checkers"
        elif self.board_size == 10 and self.allow_flying_kings:
            return "International Draughts"
        else:
            return "Custom Variant"

    @computed_field
    @property
    def performance_profile(self) -> Dict[str, Union[str, int, float]]:
        """Generate performance profile based on configuration.

        Returns:
            Dict[str, Union[str, int, float]]: Performance characteristics.
        """
        complexity_score = (
            self.board_size
            * self.strategic_depth
            * (2 if self.allow_flying_kings else 1)
        )

        if complexity_score < 100:
            performance_level = "Fast"
        elif complexity_score < 300:
            performance_level = "Balanced"
        else:
            performance_level = "Deep"

        return {
            "complexity_score": complexity_score,
            "performance_level": performance_level,
            "estimated_time_per_move": self.time_per_move,
            "memory_usage": self.memory_limit_mb,
            "parallel_processing": self.analysis_threads > 1,
        }

    @classmethod
    def american_checkers(cls) -> "CheckersAgentConfig":
        """Create configuration for standard American Checkers.

        Standard American Checkers features:
        - 8x8 board with 64 squares
        - 12 pieces per player
        - Kings move one square diagonally
        - Mandatory jumps when available
        - Pieces promote on the back rank

        Returns:
            CheckersAgentConfig: Configuration for American Checkers.

        Examples:
            Creating American Checkers game::\n

                config = CheckersAgentConfig.american_checkers()
                agent = CheckersAgent(config)
                result = agent.run_game()

            Verifying American Checkers rules::\n

                config = CheckersAgentConfig.american_checkers()
                assert config.board_size == 8
                assert config.allow_flying_kings == False
                assert config.mandatory_jumps == True
                assert config.pieces_per_player == 12
        """
        return cls(
            name="american_checkers",
            board_size=8,
            max_turns=100,
            allow_flying_kings=False,
            mandatory_jumps=True,
            strategic_depth=4,
            time_per_move=10.0,
            enable_endgame_tables=False,
            analysis_threads=1,
            memory_limit_mb=256,
        )

    @classmethod
    def international_draughts(cls) -> "CheckersAgentConfig":
        """Create configuration for International Draughts (10x10).

        International Draughts features:
        - 10x10 board with 100 squares
        - 20 pieces per player
        - Flying kings with unlimited diagonal movement
        - Mandatory jumps with maximum capture rule
        - More complex strategic gameplay

        Returns:
            CheckersAgentConfig: Configuration for International Draughts.

        Examples:
            Creating International Draughts game::\n

                config = CheckersAgentConfig.international_draughts()
                agent = CheckersAgent(config)
                result = agent.run_game()

            Verifying International rules::\n

                config = CheckersAgentConfig.international_draughts()
                assert config.board_size == 10
                assert config.allow_flying_kings == True
                assert config.pieces_per_player == 20
                assert config.strategic_depth == 6
        """
        return cls(
            name="international_draughts",
            board_size=10,
            max_turns=150,
            allow_flying_kings=True,
            mandatory_jumps=True,
            strategic_depth=6,
            time_per_move=15.0,
            enable_endgame_tables=True,
            analysis_threads=2,
            memory_limit_mb=512,
        )

    @classmethod
    def tournament(cls) -> "CheckersAgentConfig":
        """Create configuration optimized for tournament play.

        Tournament configuration features:
        - Extended analysis depth for strong play
        - Endgame tablebase support
        - Optimized time controls
        - Enhanced memory allocation
        - Parallel processing support

        Returns:
            CheckersAgentConfig: Configuration optimized for competitive tournament play.

        Examples:
            Setting up tournament game::\n

                config = CheckersAgentConfig.tournament()
                agent = CheckersAgent(config)
                # Strong AI play suitable for competitions

            Tournament characteristics::\n

                config = CheckersAgentConfig.tournament()
                assert config.strategic_depth == 8
                assert config.enable_endgame_tables == True
                assert config.time_per_move == 30.0
                assert config.analysis_threads == 4
        """
        return cls(
            name="tournament_checkers",
            board_size=8,
            max_turns=200,
            allow_flying_kings=False,
            mandatory_jumps=True,
            strategic_depth=8,
            time_per_move=30.0,
            enable_endgame_tables=True,
            analysis_threads=4,
            memory_limit_mb=1024,
        )

    @classmethod
    def training(cls) -> "CheckersAgentConfig":
        """Create configuration optimized for AI training and experimentation.

        Training configuration features:
        - Balanced depth for learning
        - Reasonable resource usage
        - Faster move generation
        - Suitable for iterative improvement
        - Good for experimentation

        Returns:
            CheckersAgentConfig: Configuration optimized for AI training and development.

        Examples:
            Setting up training environment::\n

                config = CheckersAgentConfig.training()
                agent = CheckersAgent(config)
                # Balanced for learning and experimentation

            Training characteristics::\n

                config = CheckersAgentConfig.training()
                assert config.strategic_depth == 3
                assert config.time_per_move == 5.0
                assert config.memory_limit_mb == 256
                assert config.max_turns == 100
        """
        return cls(
            name="training_checkers",
            board_size=8,
            max_turns=100,
            allow_flying_kings=False,
            mandatory_jumps=True,
            strategic_depth=3,
            time_per_move=5.0,
            enable_endgame_tables=False,
            analysis_threads=2,
            memory_limit_mb=256,
        )

    @classmethod
    def performance(cls) -> "CheckersAgentConfig":
        """Create configuration optimized for maximum performance.

        Performance configuration features:
        - Maximum parallel processing
        - Extended memory allocation
        - Optimized analysis depth
        - Endgame tablebase support
        - Balanced for speed and strength

        Returns:
            CheckersAgentConfig: Configuration optimized for maximum performance.

        Examples:
            Setting up high-performance game::\n

                config = CheckersAgentConfig.performance()
                agent = CheckersAgent(config)
                # Optimized for speed and strength

            Performance characteristics::\n

                config = CheckersAgentConfig.performance()
                assert config.analysis_threads == 4
                assert config.memory_limit_mb == 1024
                assert config.enable_endgame_tables == True
                assert config.strategic_depth == 6
        """
        return cls(
            name="performance_checkers",
            board_size=8,
            max_turns=150,
            allow_flying_kings=False,
            mandatory_jumps=True,
            strategic_depth=6,
            time_per_move=15.0,
            enable_endgame_tables=True,
            analysis_threads=4,
            memory_limit_mb=1024,
        )

    @classmethod
    def default(cls) -> "CheckersAgentConfig":
        """Create a default configuration for checkers.

        Creates a configuration with standard American Checkers rules:
        - 8x8 board with 64 squares
        - 100 max turns for reasonable game length
        - Mandatory jumps following traditional rules
        - Standard kings (no flying kings)
        - Balanced strategic depth

        Returns:
            CheckersAgentConfig: Default configuration for checkers.

        Examples:
            Creating default game::\n

                config = CheckersAgentConfig.default()
                agent = CheckersAgent(config)
                result = agent.run_game()

            Verifying default settings::\n

                config = CheckersAgentConfig.default()
                assert config.board_size == 8
                assert config.mandatory_jumps == True
                assert config.strategic_depth == 4
                assert config.game_variant == "American Checkers"
        """
        return cls.american_checkers()

    model_config = {"arbitrary_types_allowed": True}
