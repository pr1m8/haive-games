"""Configurable Tic-Tac-Toe configuration using the generic player agent
system.

This module provides configurable Tic-Tac-Toe game configurations that
replace hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.generic_engines import (
    create_generic_ttt_config_from_example,
    create_generic_ttt_engines,
    create_generic_ttt_engines_simple,
)


class ConfigurableTicTacToeConfig(TicTacToeConfig):
    """Configurable Tic-Tac-Toe configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Tic-Tac-Toe game, providing flexibility and avoiding hardcoded models.

    Attributes:
        x_model: Model for X player (can be string or LLMConfig)
        o_model: Model for O player (can be string or LLMConfig)
        x_player_name: Name for the X player
        o_player_name: Name for the O player
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        max_moves: Maximum number of moves before draw
        enable_analysis: Whether to enable position analysis
        recursion_limit: Python recursion limit for game execution
    """

    x_model: Optional[str] = Field(default=None, description="Model for X player")
    o_model: Optional[str] = Field(default=None, description="Model for O player")
    x_player_name: Optional[str] = Field(default=None, description="Name for X player")
    o_player_name: Optional[str] = Field(default=None, description="Name for O player")
    example_config: Optional[str] = Field(
        default=None, description="Example configuration name"
    )
    player_configs: Optional[Dict[str, PlayerAgentConfig]] = Field(
        default=None, description="Detailed player configurations"
    )

    # Game configuration
    temperature: float = Field(
        default=0.3, description="Temperature for LLM generation"
    )
    max_moves: int = Field(
        default=9, description="Maximum moves (should be 9 for Tic-Tac-Toe)"
    )
    enable_analysis: bool = Field(default=True, description="Enable position analysis")
    recursion_limit: int = Field(default=300, description="Python recursion limit")

    def model_post_init(self, __context: Any) -> None:
        """Initialize engines after model creation."""
        super().model_post_init(__context)

        # Create engines based on configuration method
        if self.player_configs:
            # Method 1: Use detailed player configurations
            self.engines = create_generic_ttt_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_ttt_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            x_model = self.x_model or "gpt-4o"
            o_model = self.o_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_ttt_engines_simple(
                x_model, o_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(x_model, o_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            x_config = self.player_configs.get("X_player")
            o_config = self.player_configs.get("O_player")

            self.x_player_name = (
                x_config.player_name
                if x_config and x_config.player_name
                else "X Player"
            )
            self.o_player_name = (
                o_config.player_name
                if o_config and o_config.player_name
                else "O Player"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT X", "Claude O"),
            "gpt_only": ("GPT X", "GPT O"),
            "claude_only": ("Claude X", "Claude O"),
            "budget": ("Budget X", "Budget O"),
            "mixed": ("Mixed X", "Mixed O"),
        }

        if self.example_config in example_names:
            self.x_player_name, self.o_player_name = example_names[self.example_config]
        else:
            self.x_player_name = f"{self.example_config} X"
            self.o_player_name = f"{self.example_config} O"

    def _generate_player_names_from_models(self, x_model: str, o_model: str):
        """Generate player names based on model names."""

        def model_to_name(model: str) -> str:
            if "gpt" in model.lower():
                return "GPT"
            elif "claude" in model.lower():
                return "Claude"
            elif "gemini" in model.lower():
                return "Gemini"
            elif "llama" in model.lower():
                return "Llama"
            else:
                # Extract provider or model name
                if ":" in model:
                    return model.split(":")[0].title()
                return model.split("-")[0].title()

        self.x_player_name = self.x_player_name or f"{model_to_name(x_model)} X"
        self.o_player_name = self.o_player_name or f"{model_to_name(o_model)} O"


def create_ttt_config(
    x_model: str = "gpt-4o", o_model: str = "claude-3-5-sonnet-20240620", **kwargs
) -> ConfigurableTicTacToeConfig:
    """Create a configurable Tic-Tac-Toe configuration with simple model
    specifications.

    Args:
        x_model: Model for X player and analyzer
        o_model: Model for O player and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableTicTacToeConfig: Configured Tic-Tac-Toe game

    Example:
        >>> config = create_ttt_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_ttt_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     max_moves=9
        ... )
    """
    return ConfigurableTicTacToeConfig(x_model=x_model, o_model=o_model, **kwargs)


def create_ttt_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableTicTacToeConfig:
    """Create a configurable Tic-Tac-Toe configuration from a predefined
    example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableTicTacToeConfig: Configured Tic-Tac-Toe game

    Available examples:
        - "gpt_vs_claude": GPT-4 vs Claude
        - "gpt_only": GPT-4 for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role

    Example:
        >>> config = create_ttt_config_from_example("budget", max_moves=9)
        >>> config = create_ttt_config_from_example("gpt_vs_claude", enable_analysis=False)
    """
    return ConfigurableTicTacToeConfig(example_config=example_name, **kwargs)


def create_ttt_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableTicTacToeConfig:
    """Create a configurable Tic-Tac-Toe configuration from detailed player
    configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableTicTacToeConfig: Configured Tic-Tac-Toe game

    Expected roles:
        - "X_player": X player configuration
        - "O_player": O player configuration
        - "X_analyzer": X analyzer configuration
        - "O_analyzer": O analyzer configuration

    Example:
        >>> player_configs = {
        ...     "X_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic X"
        ...     ),
        ...     "O_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical O"
        ...     ),
        ...     "X_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="X Analyst"
        ...     ),
        ...     "O_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="O Analyst"
        ...     ),
        ... }
        >>> config = create_ttt_config_from_player_configs(player_configs)
    """
    return ConfigurableTicTacToeConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig:
    """Create a budget-friendly Tic-Tac-Toe configuration."""
    return create_ttt_config_from_example("budget", **kwargs)


def create_quick_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig:
    """Create a quick Tic-Tac-Toe configuration with fast models."""
    return create_ttt_config("gpt-3.5-turbo", "claude-3-haiku", **kwargs)


def create_experimental_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig:
    """Create an experimental Tic-Tac-Toe configuration with mixed
    providers."""
    return create_ttt_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_ttt_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_ttt_config(),
    },
    "quick": {
        "description": "Fast execution with lighter models",
        "config": lambda: create_quick_ttt_config(),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_ttt_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableTicTacToeConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableTicTacToeConfig: The example configuration

    Raises:
        ValueError: If the example name is not found
    """
    if name not in EXAMPLE_CONFIGURATIONS:
        available = ", ".join(EXAMPLE_CONFIGURATIONS.keys())
        raise ValueError(f"Unknown example '{name}'. Available: {available}")

    return EXAMPLE_CONFIGURATIONS[name]["config"]()


def list_example_configurations() -> Dict[str, str]:
    """List all available example configurations.

    Returns:
        Dict[str, str]: Mapping of configuration names to descriptions
    """
    return {
        name: config["description"] for name, config in EXAMPLE_CONFIGURATIONS.items()
    }


if __name__ == "__main__":
    # Demo the configurable system
    print("⭕ Configurable Tic-Tac-Toe Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_ttt_config("gpt-4o", "claude-3-opus")
    print(f"   X: {config1.x_player_name}")
    print(f"   O: {config1.o_player_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_ttt_config_from_example("budget")
    print(f"   X: {config2.x_player_name}")
    print(f"   O: {config2.o_player_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "X_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Tic-Tac Master X", temperature=0.8
        ),
        "O_player": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Strategic O", temperature=0.4
        ),
        "X_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="X Strategist", temperature=0.2
        ),
        "O_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="O Tactician", temperature=0.2
        ),
    }
    config3 = create_ttt_config_from_player_configs(player_configs)
    print(f"   X: {config3.x_player_name}")
    print(f"   O: {config3.o_player_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Tic-Tac-Toe configurable system ready!")
