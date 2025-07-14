"""Base configuration classes for configurable games.

This module provides the foundation for creating flexible game configurations
that support multiple LLM providers and configuration modes.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional

from haive.core.engine.agent.agent import AgentConfig


# Note: create_llm_config doesn't exist - using placeholder
def create_llm_config(model: str, **kwargs):
    """Placeholder function until core factory is available."""
    from haive.core.models.llm.base import OpenAILLMConfig

    return OpenAILLMConfig(model=model, **kwargs)


from pydantic import BaseModel, Field, model_validator

from haive.games.core.agent.player_agent import PlayerAgentConfig


class ConfigMode(str, Enum):
    """Configuration mode for game setup."""

    LEGACY = "legacy"  # Use hardcoded engines (backward compatibility)
    SIMPLE = "simple"  # Use simple model strings
    EXAMPLE = "example"  # Use predefined example configurations
    ADVANCED = "advanced"  # Use full PlayerAgentConfig objects
    AUTO = "auto"  # Automatically determine based on provided fields


class GamePlayerRole(BaseModel):
    """Definition of a player role in a game."""

    name: str = Field(description="Internal name for the role (e.g., 'white_player')")
    display_name: str = Field(description="Display name for the role (e.g., 'White')")
    is_analyzer: bool = Field(
        default=False, description="Whether this is an analyzer role"
    )
    default_model: str = Field(
        default="gpt-3.5-turbo", description="Default model for this role"
    )


class BaseGameConfig(AgentConfig, ABC):
    """Base configuration for all configurable games.

    This class provides a unified configuration system that supports:
    - Legacy hardcoded engines (backward compatibility)
    - Simple model string configuration
    - Example-based configuration
    - Advanced PlayerAgentConfig configuration

    Games should extend this class and implement the required abstract methods.
    """

    # Configuration mode
    config_mode: ConfigMode = Field(
        default=ConfigMode.AUTO, description="Configuration mode to use"
    )

    # Legacy mode
    use_legacy_engines: bool = Field(
        default=False, description="Use hardcoded engines for backward compatibility"
    )

    # Simple mode - games override with specific fields like white_model, red_model, etc.
    player1_model: Optional[str] = Field(default=None, description="Model for player 1")
    player2_model: Optional[str] = Field(default=None, description="Model for player 2")

    # Example mode
    example_config: Optional[str] = Field(
        default=None, description="Name of predefined example configuration"
    )

    # Advanced mode
    player_configs: Optional[Dict[str, PlayerAgentConfig]] = Field(
        default=None, description="Detailed player configurations"
    )

    # Common game settings
    temperature: float = Field(
        default=0.7, description="Temperature for LLM generation"
    )
    enable_analysis: bool = Field(default=True, description="Enable position analysis")
    recursion_limit: int = Field(default=500, description="Python recursion limit")

    @abstractmethod
    def get_role_definitions(self) -> Dict[str, GamePlayerRole]:
        """Define the player roles for this game.

        Returns:
            Dictionary mapping role names to GamePlayerRole definitions

        Example:
            {
                "white_player": GamePlayerRole(name="white_player", display_name="White"),
                "black_player": GamePlayerRole(name="black_player", display_name="Black"),
                "white_analyzer": GamePlayerRole(name="white_analyzer", display_name="White Analyst", is_analyzer=True),
                "black_analyzer": GamePlayerRole(name="black_analyzer", display_name="Black Analyst", is_analyzer=True),
            }
        """
        pass

    @abstractmethod
    def get_example_configs(self) -> Dict[str, Dict[str, Any]]:
        """Define available example configurations.

        Returns:
            Dictionary mapping example names to configuration parameters

        Example:
            {
                "gpt_vs_claude": {
                    "player1_model": "gpt-4",
                    "player2_model": "claude-3-opus",
                    "temperature": 0.7
                },
                "budget": {
                    "player1_model": "gpt-3.5-turbo",
                    "player2_model": "gpt-3.5-turbo",
                    "temperature": 0.5
                }
            }
        """
        pass

    @abstractmethod
    def build_legacy_engines(self) -> List[Any]:
        """Build legacy hardcoded engines for backward compatibility.

        Returns:
            List of game engines using hardcoded LLM configurations
        """
        pass

    @abstractmethod
    def create_engines_from_player_configs(
        self, player_configs: Dict[str, PlayerAgentConfig]
    ) -> List[Any]:
        """Create engines from detailed player configurations.

        Args:
            player_configs: Dictionary mapping role names to PlayerAgentConfig

        Returns:
            List of configured game engines
        """
        pass

    def determine_config_mode(self) -> ConfigMode:
        """Automatically determine configuration mode based on provided fields."""
        if self.config_mode != ConfigMode.AUTO:
            return self.config_mode

        if self.use_legacy_engines:
            return ConfigMode.LEGACY
        elif self.player_configs:
            return ConfigMode.ADVANCED
        elif self.example_config:
            return ConfigMode.EXAMPLE
        else:
            return ConfigMode.SIMPLE

    def create_simple_player_configs(self) -> Dict[str, PlayerAgentConfig]:
        """Create player configs from simple model strings.

        This method should be overridden by games that use different
        field names (e.g., white_model/black_model instead of player1_model/player2_model).
        """
        roles = self.get_role_definitions()
        configs = {}

        # Map simple model strings to player configs
        for role_name, role_def in roles.items():
            if "player1" in role_name and self.player1_model:
                model = self.player1_model
            elif "player2" in role_name and self.player2_model:
                model = self.player2_model
            else:
                model = role_def.default_model

            configs[role_name] = PlayerAgentConfig(
                llm_config=model,
                temperature=self.temperature,
                player_name=role_def.display_name,
            )

        return configs

    def create_example_player_configs(
        self, example_name: str
    ) -> Dict[str, PlayerAgentConfig]:
        """Create player configs from example configuration."""
        examples = self.get_example_configs()

        if example_name not in examples:
            available = ", ".join(examples.keys())
            raise ValueError(
                f"Unknown example '{example_name}'. Available: {available}"
            )

        example = examples[example_name]

        # Update fields from example
        for key, value in example.items():
            if hasattr(self, key):
                setattr(self, key, value)

        # Create configs using simple mode
        return self.create_simple_player_configs()

    @model_validator(mode="after")
    def configure_engines(self) -> "BaseGameConfig":
        """Configure engines based on the determined mode."""
        mode = self.determine_config_mode()

        if mode == ConfigMode.LEGACY:
            self.engines = self.build_legacy_engines()

        elif mode == ConfigMode.ADVANCED:
            if not self.player_configs:
                raise ValueError("player_configs required for advanced mode")
            self.engines = self.create_engines_from_player_configs(self.player_configs)

        elif mode == ConfigMode.EXAMPLE:
            if not self.example_config:
                raise ValueError("example_config required for example mode")
            player_configs = self.create_example_player_configs(self.example_config)
            self.engines = self.create_engines_from_player_configs(player_configs)

        else:  # SIMPLE mode
            player_configs = self.create_simple_player_configs()
            self.engines = self.create_engines_from_player_configs(player_configs)

        return self

    def get_player_names(self) -> Dict[str, str]:
        """Get display names for all players."""
        roles = self.get_role_definitions()
        return {
            role_name: role_def.display_name
            for role_name, role_def in roles.items()
            if not role_def.is_analyzer
        }


# Convenience functions for creating configurations


def create_simple_config(
    config_class: type[BaseGameConfig], player1_model: str, player2_model: str, **kwargs
) -> BaseGameConfig:
    """Create a simple game configuration with model strings.

    Args:
        config_class: The game's configuration class
        player1_model: Model for player 1
        player2_model: Model for player 2
        **kwargs: Additional configuration parameters

    Returns:
        Configured game instance
    """
    return config_class(
        config_mode=ConfigMode.SIMPLE,
        player1_model=player1_model,
        player2_model=player2_model,
        **kwargs,
    )


def create_example_config(
    config_class: type[BaseGameConfig], example_name: str, **kwargs
) -> BaseGameConfig:
    """Create a game configuration from a predefined example.

    Args:
        config_class: The game's configuration class
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        Configured game instance
    """
    return config_class(
        config_mode=ConfigMode.EXAMPLE, example_config=example_name, **kwargs
    )


def create_advanced_config(
    config_class: type[BaseGameConfig],
    player_configs: Dict[str, PlayerAgentConfig],
    **kwargs,
) -> BaseGameConfig:
    """Create a game configuration with detailed player configs.

    Args:
        config_class: The game's configuration class
        player_configs: Dictionary mapping role names to PlayerAgentConfig
        **kwargs: Additional configuration parameters

    Returns:
        Configured game instance
    """
    return config_class(
        config_mode=ConfigMode.ADVANCED, player_configs=player_configs, **kwargs
    )
