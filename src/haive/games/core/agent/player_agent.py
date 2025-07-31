"""Configurable player agent system for games.

This module provides a flexible player agent abstraction that allows games to use
different LLM configurations for players without hardcoding them in engines.

The system supports:
- Dynamic LLM configuration per player
- Role-based agent configuration (player, analyzer, etc.)
- Easy swapping of LLMs and models
- Integration with the new LLM factory system

"""

from abc import ABC, abstractmethod
from typing import Any, Protocol

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm import LLMConfig
from haive.core.models.llm.base import (
    AnthropicLLMConfig,
    AzureLLMConfig,
    OpenAILLMConfig,
)
from pydantic import BaseModel, Field


def create_llm_config(model: str, **kwargs) -> LLMConfig:
    """Create an LLM config based on model string.

    This is a simple helper to create configs until a proper factory is available.

    """
    # Simple provider detection based on model name
    if "gpt" in model.lower() or kwargs.get("model_provider") == "openai":
        return OpenAILLMConfig(model=model, **kwargs)
    elif "claude" in model.lower() or kwargs.get("model_provider") == "anthropic":
        return AnthropicLLMConfig(model=model, **kwargs)
    elif kwargs.get("model_provider") == "azure":
        return AzureLLMConfig(model=model, **kwargs)
    else:
        # Default to OpenAI
        return OpenAILLMConfig(model=model, **kwargs)


class PlayerRole(Protocol):
    """Protocol defining the interface for player roles."""

    def get_role_name(self) -> str:
        """Get the name of this role."""
        ...

    def get_prompt_template(self) -> Any:
        """Get the prompt template for this role."""
        ...

    def get_structured_output_model(self) -> type | None:
        """Get the structured output model for this role."""
        ...


class GamePlayerRole(BaseModel):
    """Standard implementation of a player role in a game.

    This class defines a specific role that a player can take in a game, such as
    'white_player', 'black_analyzer', etc.

    """

    role_name: str = Field(description="Name of the role (e.g., 'white_player')")
    prompt_template: Any = Field(description="Prompt template for this role")
    structured_output_model: type | None = Field(
        default=None, description="Expected output model"
    )
    temperature: float | None = Field(
        default=None, description="Default temperature for this role"
    )
    description: str = Field(default="", description="Description of this role")

    class Config:
        arbitrary_types_allowed = True


class PlayerAgentConfig(BaseModel):
    """Configuration for a player agent.

    This allows specifying which LLM configuration to use for a player without
    hardcoding it in the engine definitions.

    """

    # LLM Configuration - can be string, LLMConfig, or dict
    llm_config: str | LLMConfig | dict[str, Any] = Field(
        description="LLM configuration - can be model string, LLMConfig instance, or config dict"
    )

    # Optional overrides
    temperature: float | None = Field(default=None, description="Temperature override")
    model_provider: str | None = Field(
        default=None, description="Model provider override"
    )

    # Player metadata
    player_name: str | None = Field(
        default=None, description="Human-readable player name"
    )

    class Config:
        arbitrary_types_allowed = True

    def create_llm_config(self) -> LLMConfig:
        """Create an LLMConfig instance from the configuration.

        Returns:
            LLMConfig: Configured LLM instance

        """
        if isinstance(self.llm_config, LLMConfig):
            # Already an LLMConfig, use directly
            config = self.llm_config
        elif isinstance(self.llm_config, str):
            # Model string - use factory
            config = create_llm_config(
                self.llm_config,
                temperature=self.temperature,
                model_provider=self.model_provider,
            )
        elif isinstance(self.llm_config, dict):
            # Dictionary config
            config_dict = self.llm_config.copy()
            if self.temperature is not None:
                config_dict["temperature"] = self.temperature
            if self.model_provider is not None:
                config_dict["model_provider"] = self.model_provider

            # Extract model for factory
            model = config_dict.pop("model", None)
            if not model:
                raise ValueError("Model must be specified in llm_config dict")

            config = create_llm_config(model, **config_dict)
        else:
            raise TypeError(f"Unsupported llm_config type: {type(self.llm_config)}")

        return config


class PlayerAgentFactory:
    """Factory for creating configurable player agents.

    This factory creates AugLLMConfig instances for game roles using configurable player
    agents instead of hardcoded LLM configurations.

    """

    @staticmethod
    def create_player_engine(
        role: GamePlayerRole, agent_config: PlayerAgentConfig, **kwargs
    ) -> AugLLMConfig:
        """Create an AugLLMConfig for a player role.

        Args:
            role: The game role definition
            agent_config: The player agent configuration
            **kwargs: Additional parameters for AugLLMConfig

        Returns:
            AugLLMConfig: Configured engine for the role

        """
        # Get LLM config from agent
        llm_config = agent_config.create_llm_config()

        # Use role temperature if agent doesn't specify one
        temperature = agent_config.temperature or role.temperature

        return AugLLMConfig(
            name=role.role_name,
            llm_config=llm_config,
            prompt_template=role.prompt_template,
            structured_output_model=role.structured_output_model,
            temperature=temperature,
            description=role.description,
            **kwargs,
        )

    @staticmethod
    def create_engines_from_player_configs(
        roles: dict[str, GamePlayerRole], player_configs: dict[str, PlayerAgentConfig]
    ) -> dict[str, AugLLMConfig]:
        """Create a complete set of engines from role definitions and player configs.

        Args:
            roles: Dictionary of role name to role definition
            player_configs: Dictionary of role name to player agent config

        Returns:
            Dict[str, AugLLMConfig]: Dictionary of engines

        Example:
            >>> roles = {
            ...     "white_player": GamePlayerRole(
            ...         role_name="white_player",
            ...         prompt_template=white_move_prompt,
            ...         structured_output_model=ChessPlayerDecision
            ...     )
            ... }
            >>> configs = {
            ...     "white_player": PlayerAgentConfig(llm_config="gpt-4")
            ... }
            >>> engines = PlayerAgentFactory.create_engines_from_player_configs(roles, configs)

        """
        engines = {}

        for role_name, role in roles.items():
            if role_name in player_configs:
                agent_config = player_configs[role_name]
                engines[role_name] = PlayerAgentFactory.create_player_engine(
                    role, agent_config
                )
            else:
                raise ValueError(f"No player config provided for role: {role_name}")

        return engines


class ConfigurableGameAgent(ABC):
    """Abstract base for game agents with configurable players.

    This class provides the interface for game agents that support configurable player
    agents instead of hardcoded engines.

    """

    @abstractmethod
    def get_role_definitions(self) -> dict[str, GamePlayerRole]:
        """Get the role definitions for this game.

        Returns:
            Dict[str, GamePlayerRole]: Dictionary of role name to role definition

        """

    @abstractmethod
    def create_engines_from_player_configs(
        self, player_configs: dict[str, PlayerAgentConfig]
    ) -> dict[str, AugLLMConfig]:
        """Create engines from player configurations.

        Args:
            player_configs: Dictionary of role name to player agent config

        Returns:
            Dict[str, AugLLMConfig]: Dictionary of engines

        """
        roles = self.get_role_definitions()
        return PlayerAgentFactory.create_engines_from_player_configs(
            roles, player_configs
        )


# Convenience functions for common configurations


def create_player_config(
    model: str | LLMConfig,
    temperature: float | None = None,
    player_name: str | None = None,
    **kwargs,
) -> PlayerAgentConfig:
    """Create a player agent configuration.

    Args:
        model: Model string, LLMConfig instance, or config dict
        temperature: Temperature setting
        player_name: Human-readable name for the player
        **kwargs: Additional configuration parameters

    Returns:
        PlayerAgentConfig: Configured player agent

    Examples:
        >>> config = create_player_config("gpt-4", temperature=0.7)
        >>> config = create_player_config("anthropic:claude-3-opus")
        >>> config = create_player_config({"model": "gpt-4", "provider": "openai"})

    """
    return PlayerAgentConfig(
        llm_config=model, temperature=temperature, player_name=player_name, **kwargs
    )


def create_simple_player_configs(
    white_model: str | LLMConfig = "gpt-4",
    black_model: str | LLMConfig = "claude-3-opus",
    temperature: float | None = None,
    **kwargs,
) -> dict[str, PlayerAgentConfig]:
    """Create simple player configurations for two-player games.

    Args:
        white_model: Model for white/first player
        black_model: Model for black/second player
        temperature: Temperature for both players
        **kwargs: Additional configuration parameters

    Returns:
        Dict[str, PlayerAgentConfig]: Player configurations

    Example:
        >>> configs = create_simple_player_configs("gpt-4", "claude-3-opus", temperature=0.7)
        >>> # Creates configs for white_player, black_player, white_analyzer, black_analyzer

    """
    base_config = {"temperature": temperature, **kwargs}

    return {
        "white_player": create_player_config(
            white_model, player_name="White", **base_config
        ),
        "black_player": create_player_config(
            black_model, player_name="Black", **base_config
        ),
        "white_analyzer": create_player_config(
            white_model, player_name="White Analyzer", **base_config
        ),
        "black_analyzer": create_player_config(
            black_model, player_name="Black Analyzer", **base_config
        ),
    }
