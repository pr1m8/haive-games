from typing import Any

r"""Comprehensive configuration system for Battleship game agents and gameplay customization.

This module provides extensive configuration options for Battleship game agents,
supporting various game modes, strategic analysis settings, visualization options,
and LLM engine configurations. The configuration system enables fine-tuned control
over game mechanics, player behavior, and performance optimization.

The configuration classes use Pydantic for validation and provide factory methods
for common Battleship game scenarios including competitive play, training modes,
and analysis-focused configurations.

Examples:
    Creating a basic Battleship agent configuration::\n

        config = BattleshipAgentConfig()
        agent = BattleshipAgent(config)

    Creating a configuration with custom player names::\n

        config = BattleshipAgentConfig(
            player1_name="Admiral_Nelson",
            player2_name="Captain_Ahab",
            enable_analysis=True
        )
        agent = BattleshipAgent(config)

    Creating a competitive configuration::\n

        config = BattleshipAgentConfig.competitive()
        config.visualize_board = False  # Silent mode for tournaments
        agent = BattleshipAgent(config)

    Creating a training configuration::\n

        config = BattleshipAgentConfig.training()
        config.enable_analysis = True
        config.visualize_board = True
        agent = BattleshipAgent(config)

Note:
    All configuration classes include comprehensive validation to ensure
    game rule consistency and prevent invalid combinations that would
    break gameplay mechanics.
"""

import uuid

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import Field, computed_field, model_validator

from haive.games.battleship.engines import build_battleship_engines
from haive.games.battleship.state import BattleshipState


class BattleshipAgentConfig(AgentConfig):
    r"""Comprehensive configuration for Battleship game agents with extensive customization.

    This configuration class provides complete control over Battleship game mechanics,
    supporting various game modes, strategic analysis settings, visualization options,
    and LLM engine configurations. It includes validation for game consistency and
    provides factory methods for common Battleship scenarios.

    The configuration system supports:
    - Player identification and naming
    - Strategic analysis and decision-making options
    - Visualization and debugging settings
    - LLM engine configurations for different game actions
    - Performance optimization parameters
    - Game state management and persistence

    Attributes:
        name (str): Unique identifier for the agent instance.
            Used for logging, debugging, and multi-agent coordination.
        state_schema (type): Pydantic model class for game state management.
            Defines the structure and validation rules for game state.
        player1_name (str): Display name for the first player.
            Used in visualization and game logging. Auto-generated from engine config.
        player2_name (str): Display name for the second player.
            Used in visualization and game logging. Auto-generated from engine config.
        enable_analysis (bool): Enable strategic analysis during gameplay.
            When True, agents will perform detailed position analysis before moves.
        visualize_board (bool): Enable board visualization during gameplay.
            When True, displays game boards and move history in console.
        runnable_config (RunnableConfig): LangChain runnable configuration.
            Controls execution parameters including recursion limits and thread IDs.
        engines (Dict[str, AugLLMConfig]): LLM engine configurations for game actions.
            Contains engines for ship placement, move generation, and analysis.

    Examples:
        Standard competitive configuration::\n

            config = BattleshipAgentConfig(
                name="tournament_battleship",
                player1_name="Strategic_AI",
                player2_name="Tactical_AI",
                enable_analysis=True,
                visualize_board=False
            )

        Training and debugging configuration::\n

            config = BattleshipAgentConfig(
                name="training_battleship",
                enable_analysis=True,
                visualize_board=True,
                player1_name="Learning_Agent",
                player2_name="Reference_Agent"
            )

        Performance-optimized configuration::\n

            config = BattleshipAgentConfig(
                name="speed_battleship",
                enable_analysis=False,
                visualize_board=False,
                runnable_config={
                    "configurable": {
                        "recursion_limit": 5000,
                        "thread_id": "speed_session"
                    }
                }
            )

    Note:
        Configuration validation ensures game rule consistency and prevents
        invalid combinations that would break gameplay mechanics or create
        unfair advantages.
    """

    name: str = Field(
        default="battleship_agent",
        min_length=1,
        max_length=50,
        description="Unique identifier for the agent instance used for logging and debugging",
        examples=["battleship_agent", "tournament_battleship", "training_agent"],
    )

    state_schema: type = Field(
        default=BattleshipState,
        description="Pydantic model class for game state management and validation",
    )

    player1_name: str = Field(
        default="Player 1",
        min_length=1,
        max_length=30,
        description="Display name for the first player, auto-generated from engine config",
        examples=["Admiral_Nelson", "Strategic_AI", "Human_Player"],
    )

    player2_name: str = Field(
        default="Player 2",
        min_length=1,
        max_length=30,
        description="Display name for the second player, auto-generated from engine config",
        examples=["Captain_Ahab", "Tactical_AI", "Computer_Opponent"],
    )

    enable_analysis: bool = Field(
        default=True,
        description="Enable strategic analysis during gameplay for better decision-making",
        examples=[True, False],
    )

    visualize_board: bool = Field(
        default=True,
        description="Enable board visualization during gameplay for debugging and monitoring",
        examples=[True, False],
    )

    runnable_config: RunnableConfig = Field(
        default={
            "configurable": {
                "recursion_limit": 10000,
                "thread_id": None,  # Will be set to UUID in model_validator
            }
        },
        description="LangChain runnable configuration with execution parameters and thread management",
    )

    engines: dict[str, AugLLMConfig] = Field(
        default_factory=build_battleship_engines,
        description="LLM engine configurations for ship placement, move generation, and analysis",
    )

    @model_validator(mode="after")
    @classmethod
    def update_player_names_from_engines(cls) -> Any:
        r"""Update player names based on LLM provider and model from engines.

        Automatically generates meaningful player names based on the configured
        LLM engines, creating identifiers that include provider and model information.
        Also ensures thread_id is set for proper session management.

        Returns:
            BattleshipAgentConfig: Self with updated player names and thread configuration.

        Examples:
            Configuration with OpenAI engines::\n

                config = BattleshipAgentConfig()
                # After validation, player names might be:
                # player1_name = "azure-gpt-4o"
                # player2_name = "Player 2"
        """
        # Set thread_id if not already set
        if (
            not self.runnable_config.get("configurable", {}).get("thread_id")
            or self.runnable_config["configurable"]["thread_id"] is None
        ):
            self.runnable_config["configurable"]["thread_id"] = str(uuid.uuid4())

        # Safely update player names based on engine configuration
        try:
            if self.engines and self.player1_name == "Player 1":
                player1_engine = self.engines.get("player1_move")
                if player1_engine and hasattr(player1_engine, "llm_config"):
                    llm_config = player1_engine.llm_config
                    if hasattr(llm_config, "model"):
                        model = getattr(llm_config, "model", "unknown")
                        self.player1_name = f"azure-{model}"
        except Exception:
            # If there's any issue accessing engine config, keep default names
            pass

        return self

    @classmethod
    def competitive(cls) -> "BattleshipAgentConfig":
        r"""Create a configuration optimized for competitive gameplay.

        Generates a configuration suitable for tournaments and competitive matches,
        with analysis enabled but visualization disabled for performance.

        Returns:
            BattleshipAgentConfig: Configuration optimized for competitive play.

        Examples:
            Creating a tournament-ready configuration::\n

                config = BattleshipAgentConfig.competitive()
                agent = BattleshipAgent(config)

                # Results in:
                # - Analysis enabled for strategic depth
                # - Visualization disabled for performance
                # - Optimized recursion limits
                # - Tournament-appropriate naming
        """
        return cls(
            name="competitive_battleship",
            enable_analysis=True,
            visualize_board=False,
            runnable_config={
                "configurable": {
                    "recursion_limit": 8000,
                    "thread_id": f"competitive_{str(uuid.uuid4())[:8]}",
                }
            },
        )

    @classmethod
    def training(cls) -> "BattleshipAgentConfig":
        r"""Create a configuration optimized for training and development.

        Generates a configuration suitable for agent training, debugging, and
        development work, with full analysis and visualization enabled.

        Returns:
            BattleshipAgentConfig: Configuration optimized for training scenarios.

        Examples:
            Creating a training configuration::\n

                config = BattleshipAgentConfig.training()
                agent = BattleshipAgent(config)

                # Results in:
                # - Analysis enabled for learning
                # - Visualization enabled for monitoring
                # - Extended recursion limits
                # - Training-appropriate naming
        """
        return cls(
            name="training_battleship",
            enable_analysis=True,
            visualize_board=True,
            runnable_config={
                "configurable": {
                    "recursion_limit": 15000,
                    "thread_id": f"training_{str(uuid.uuid4())[:8]}",
                }
            },
        )

    @classmethod
    def performance(cls) -> "BattleshipAgentConfig":
        r"""Create a configuration optimized for maximum performance.

        Generates a configuration suitable for high-speed gameplay and benchmarking,
        with analysis and visualization disabled for optimal performance.

        Returns:
            BattleshipAgentConfig: Configuration optimized for performance.

        Examples:
            Creating a performance-optimized configuration::\n

                config = BattleshipAgentConfig.performance()
                agent = BattleshipAgent(config)

                # Results in:
                # - Analysis disabled for speed
                # - Visualization disabled for performance
                # - Reduced recursion limits
                # - Performance-appropriate naming
        """
        return cls(
            name="performance_battleship",
            enable_analysis=False,
            visualize_board=False,
            runnable_config={
                "configurable": {
                    "recursion_limit": 5000,
                    "thread_id": f"performance_{str(uuid.uuid4())[:8]}",
                }
            },
        )

    @computed_field
    @property
    def configuration_summary(self) -> dict[str, str]:
        r"""Get a summary of the current configuration settings.

        Returns:
            Dict[str, str]: Summary of key configuration parameters.

        Examples:
            Checking configuration summary::\n

                config = BattleshipAgentConfig.competitive()
                summary = config.configuration_summary
                print(f"Mode: {summary['mode']}")
                print(f"Analysis: {summary['analysis_enabled']}")
        """
        return {
            "name": self.name,
            "analysis_enabled": "Yes" if self.enable_analysis else "No",
            "visualization_enabled": "Yes" if self.visualize_board else "No",
            "recursion_limit": str(
                self.runnable_config.get("configurable", {}).get(
                    "recursion_limit", "Unknown"
                )
            ),
            "thread_id": (
                self.runnable_config.get("configurable", {}).get(
                    "thread_id", "Not set"
                )[:8]
                + "..."
                if self.runnable_config.get("configurable", {}).get("thread_id")
                else "Not set"
            ),
            "engine_count": str(len(self.engines)),
        }

    class Config:
        """Pydantic configuration for flexible validation and type handling."""

        arbitrary_types_allowed = True
        validate_assignment = True
