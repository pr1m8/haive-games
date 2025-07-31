"""Configurable Mafia configuration using the generic player agent system.

This module provides configurable Mafia game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.

"""

from typing import Any

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.mafia.config import MafiaConfig
from haive.games.mafia.generic_engines import (
    create_generic_mafia_config_from_example,
    create_generic_mafia_engines,
    create_generic_mafia_engines_simple,
)


class ConfigurableMafiaConfig(MafiaConfig):
    """Configurable Mafia configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Mafia game, providing flexibility and avoiding hardcoded models.

    Attributes:
        mafia_model: Model for mafia (can be string or LLMConfig)
        town_model: Model for town (can be string or LLMConfig)
        mafia_name: Name for mafia
        town_name: Name for town
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution

    """

    mafia_model: str | None = Field(default=None, description="Model for mafia")
    town_model: str | None = Field(default=None, description="Model for town")
    example_config: str | None = Field(
        default=None, description="Example configuration name"
    )
    player_configs: dict[str, PlayerAgentConfig] | None = Field(
        default=None, description="Detailed player configurations"
    )

    # Game configuration
    temperature: float = Field(
        default=0.3, description="Temperature for LLM generation"
    )
    recursion_limit: int = Field(default=500, description="Python recursion limit")

    def model_post_init(self, __context: Any) -> None:
        """Initialize engines after model creation."""
        super().model_post_init(__context)

        # Create engines based on configuration method
        if self.player_configs:
            # Method 1: Use detailed player configurations
            self.engines = create_generic_mafia_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_mafia_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            mafia_model = self.mafia_model or "gpt-4o"
            town_model = self.town_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_mafia_engines_simple(
                mafia_model, town_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(mafia_model, town_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            mafia_config = self.player_configs.get("mafia_player")
            town_config = self.player_configs.get("town_player")

            self.mafia_name = (
                mafia_config.player_name
                if mafia_config and mafia_config.player_name
                else "Mafia"
            )
            self.town_name = (
                town_config.player_name
                if town_config and town_config.player_name
                else "Town"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Mafia", "Claude Town"),
            "gpt_only": ("GPT Mafia", "GPT Town"),
            "claude_only": ("Claude Mafia", "Claude Town"),
            "budget": ("Budget Mafia", "Budget Town"),
            "mixed": ("Mixed Mafia", "Mixed Town"),
            "advanced": ("Advanced Mafia", "Advanced Town"),
        }

        if self.example_config in example_names:
            self.mafia_name, self.town_name = example_names[self.example_config]
        else:
            self.mafia_name = f"{self.example_config} Mafia"
            self.town_name = f"{self.example_config} Town"

    def _generate_player_names_from_models(self, mafia_model: str, town_model: str):
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

        self.mafia_name = (
            getattr(self, "mafia_name", None) or f"{model_to_name(mafia_model)} Mafia"
        )
        self.town_name = (
            getattr(self, "town_name", None) or f"{model_to_name(town_model)} Town"
        )


def create_mafia_config(
    mafia_model: str = "gpt-4o",
    town_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableMafiaConfig:
    """Create a configurable Mafia configuration with simple model specifications.

    Args:
        mafia_model: Model for mafia and analyzer
        town_model: Model for town and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMafiaConfig: Configured Mafia game

    Example:
        >>> config = create_mafia_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_mafia_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )

    """
    return ConfigurableMafiaConfig(
        mafia_model=mafia_model, town_model=town_model, **kwargs
    )


def create_mafia_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableMafiaConfig:
    """Create a configurable Mafia configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableMafiaConfig: Configured Mafia game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Example:
        >>> config = create_mafia_config_from_example("budget", enable_analysis=False)
        >>> config = create_mafia_config_from_example("advanced", visualize_game=True)

    """
    return ConfigurableMafiaConfig(example_config=example_name, **kwargs)


def create_mafia_config_from_player_configs(
    player_configs: dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableMafiaConfig:
    """Create a configurable Mafia configuration from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMafiaConfig: Configured Mafia game

    Expected roles:
        - "mafia_player": Player 1 configuration
        - "town_player": Player 2 configuration
        - "mafia_analyzer": Player 1 analyzer configuration
        - "town_analyzer": Player 2 analyzer configuration

    Example:
        >>> player_configs = {
        ...     "mafia_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Mafia"
        ...     ),
        ...     "town_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical Town"
        ...     ),
        ...     "mafia_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Mafia Strategist"
        ...     ),
        ...     "town_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Mafia Analyst"
        ...     ),
        ... }
        >>> config = create_mafia_config_from_player_configs(player_configs)

    """
    return ConfigurableMafiaConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_mafia_config(**kwargs) -> ConfigurableMafiaConfig:
    """Create a budget-friendly Mafia configuration."""
    return create_mafia_config_from_example("budget", **kwargs)


def create_advanced_mafia_config(**kwargs) -> ConfigurableMafiaConfig:
    """Create an advanced Mafia configuration with powerful models."""
    return create_mafia_config_from_example("advanced", **kwargs)


def create_experimental_mafia_config(**kwargs) -> ConfigurableMafiaConfig:
    """Create an experimental Mafia configuration with mixed providers."""
    return create_mafia_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_mafia_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_mafia_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_mafia_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_mafia_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableMafiaConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableMafiaConfig: The example configuration

    Raises:
        ValueError: If the example name is not found

    """
    if name not in EXAMPLE_CONFIGURATIONS:
        available = ", ".join(EXAMPLE_CONFIGURATIONS.keys())
        raise ValueError(f"Unknown example '{name}'. Available: {available}")

    return EXAMPLE_CONFIGURATIONS[name]["config"]()


def list_example_configurations() -> dict[str, str]:
    """List all available example configurations.

    Returns:
        Dict[str, str]: Mapping of configuration names to descriptions

    """
    return {
        name: config["description"] for name, config in EXAMPLE_CONFIGURATIONS.items()
    }


if __name__ == "__main__":
    # Demo the configurable system
    print("🎮 Configurable Mafia Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_mafia_config("gpt-4o", "claude-3-opus")
    print(f"   Mafia: {config1.mafia_name}")
    print(f"   Town: {config1.town_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_mafia_config_from_example("advanced")
    print(f"   Mafia: {config2.mafia_name}")
    print(f"   Town: {config2.town_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "mafia_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Mafia", temperature=0.8
        ),
        "town_player": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Expert Town", temperature=0.4
        ),
        "mafia_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "town_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_mafia_config_from_player_configs(player_configs)
    print(f"   Mafia: {config3.mafia_name}")
    print(f"   Town: {config3.town_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Mafia configurable system ready!")
