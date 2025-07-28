"""Configurable Checkers configuration using the generic player agent system.

This module provides configurable Checkers game configurations that
replace hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional

from pydantic import Field

from haive.games.checkers.config import CheckersAgentConfig
from haive.games.checkers.generic_engines import (
    create_generic_checkers_config_from_example,
    create_generic_checkers_engines,
    create_generic_checkers_engines_simple,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class ConfigurableCheckersConfig(CheckersAgentConfig):
    """Configurable Checkers configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Checkers game, providing flexibility and avoiding hardcoded models.

    Attributes:
        red_model: Model for red player (can be string or LLMConfig)
        black_model: Model for black player (can be string or LLMConfig)
        red_player_name: Name for the red player
        black_player_name: Name for the black player
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        max_moves: Maximum number of moves before draw
        enable_analysis: Whether to enable position analysis
        recursion_limit: Python recursion limit for game execution
    """

    red_model: Optional[str] = Field(default=None, description="Model for red player")
    black_model: Optional[str] = Field(
        default=None, description="Model for black player"
    )
    red_player_name: Optional[str] = Field(
        default=None, description="Name for red player"
    )
    black_player_name: Optional[str] = Field(
        default=None, description="Name for black player"
    )
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
    max_moves: int = Field(default=100, description="Maximum moves before draw")
    enable_analysis: bool = Field(default=True, description="Enable position analysis")
    recursion_limit: int = Field(default=500, description="Python recursion limit")

    def model_post_init(self, __context: Any) -> None:
        """Initialize engines after model creation."""
        super().model_post_init(__context)

        # Create engines based on configuration method
        if self.player_configs:
            # Method 1: Use detailed player configurations
            self.engines = create_generic_checkers_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_checkers_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            red_model = self.red_model or "gpt-4o"
            black_model = self.black_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_checkers_engines_simple(
                red_model, black_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(red_model, black_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            red_config = self.player_configs.get("red_player")
            black_config = self.player_configs.get("black_player")

            self.red_player_name = (
                red_config.player_name
                if red_config and red_config.player_name
                else "Red Player"
            )
            self.black_player_name = (
                black_config.player_name
                if black_config and black_config.player_name
                else "Black Player"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Red", "Claude Black"),
            "gpt_only": ("GPT Red", "GPT Black"),
            "claude_only": ("Claude Red", "Claude Black"),
            "budget": ("Budget Red", "Budget Black"),
            "mixed": ("Mixed Red", "Mixed Black"),
            "checkers_masters": ("Master Red", "Master Black"),
        }

        if self.example_config in example_names:
            self.red_player_name, self.black_player_name = example_names[
                self.example_config
            ]
        else:
            self.red_player_name = f"{self.example_config} Red"
            self.black_player_name = f"{self.example_config} Black"

    def _generate_player_names_from_models(self, red_model: str, black_model: str):
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

        self.red_player_name = self.red_player_name or f"{model_to_name(red_model)} Red"
        self.black_player_name = (
            self.black_player_name or f"{model_to_name(black_model)} Black"
        )


def create_checkers_config(
    red_model: str = "gpt-4o", black_model: str = "claude-3-5-sonnet-20240620", **kwargs
) -> ConfigurableCheckersConfig:
    """Create a configurable Checkers configuration with simple model
    specifications.

    Args:
        red_model: Model for red player and analyzer
        black_model: Model for black player and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableCheckersConfig: Configured Checkers game

    Example:
        >>> config = create_checkers_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_checkers_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     max_moves=150
        ... )
    """
    return ConfigurableCheckersConfig(
        red_model=red_model, black_model=black_model, **kwargs
    )


def create_checkers_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableCheckersConfig:
    """Create a configurable Checkers configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableCheckersConfig: Configured Checkers game

    Available examples:
        - "gpt_vs_claude": GPT-4 vs Claude
        - "gpt_only": GPT-4 for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "checkers_masters": High-powered models for competitive play

    Example:
        >>> config = create_checkers_config_from_example("budget", max_moves=80)
        >>> config = create_checkers_config_from_example("gpt_vs_claude", enable_analysis=False)
    """
    return ConfigurableCheckersConfig(example_config=example_name, **kwargs)


def create_checkers_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableCheckersConfig:
    """Create a configurable Checkers configuration from detailed player
    configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableCheckersConfig: Configured Checkers game

    Expected roles:
        - "red_player": Red player configuration
        - "black_player": Black player configuration
        - "red_analyzer": Red analyzer configuration
        - "black_analyzer": Black analyzer configuration

    Example:
        >>> player_configs = {
        ...     "red_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Aggressive Red"
        ...     ),
        ...     "black_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Strategic Black"
        ...     ),
        ...     "red_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Red Analyst"
        ...     ),
        ...     "black_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Black Analyst"
        ...     ),
        ... }
        >>> config = create_checkers_config_from_player_configs(player_configs)
    """
    return ConfigurableCheckersConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_checkers_config(**kwargs) -> ConfigurableCheckersConfig:
    """Create a budget-friendly Checkers configuration."""
    return create_checkers_config_from_example("budget", **kwargs)


def create_competitive_checkers_config(**kwargs) -> ConfigurableCheckersConfig:
    """Create a competitive Checkers configuration with powerful models."""
    return create_checkers_config_from_example("checkers_masters", **kwargs)


def create_experimental_checkers_config(**kwargs) -> ConfigurableCheckersConfig:
    """Create an experimental Checkers configuration with mixed providers."""
    return create_checkers_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_checkers_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_checkers_config(max_moves=80),
    },
    "competitive": {
        "description": "High-performance competitive setup",
        "config": lambda: create_competitive_checkers_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_checkers_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableCheckersConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableCheckersConfig: The example configuration

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
    print("🔴 Configurable Checkers Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_checkers_config("gpt-4o", "claude-3-opus")
    print(f"   Red: {config1.red_player_name}")
    print(f"   Black: {config1.black_player_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_checkers_config_from_example("budget")
    print(f"   Red: {config2.red_player_name}")
    print(f"   Black: {config2.black_player_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "red_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="The Red Baron", temperature=0.8
        ),
        "black_player": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Black Knight", temperature=0.4
        ),
        "red_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Red Strategist", temperature=0.2
        ),
        "black_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Black Tactician", temperature=0.2
        ),
    }
    config3 = create_checkers_config_from_player_configs(player_configs)
    print(f"   Red: {config3.red_player_name}")
    print(f"   Black: {config3.black_player_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Checkers configurable system ready!")
