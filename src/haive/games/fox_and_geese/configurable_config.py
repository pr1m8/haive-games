"""Configurable FoxAndGeese configuration using the generic player agent system.

This module provides configurable FoxAndGeese game configurations that replace
hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.generic_engines import (
    create_generic_fox_and_geese_config_from_example,
    create_generic_fox_and_geese_engines,
    create_generic_fox_and_geese_engines_simple,
)


class ConfigurableFoxAndGeeseConfig(FoxAndGeeseConfig):
    """Configurable FoxAndGeese configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the FoxAndGeese game, providing flexibility and avoiding hardcoded models.

    Attributes:
        fox_model: Model for fox (can be string or LLMConfig)
        geese_model: Model for geese (can be string or LLMConfig)
        fox_name: Name for fox
        geese_name: Name for geese
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution
    """

    fox_model: Optional[str] = Field(default=None, description="Model for fox")
    geese_model: Optional[str] = Field(default=None, description="Model for geese")
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
    recursion_limit: int = Field(default=500, description="Python recursion limit")

    def model_post_init(self, __context: Any) -> None:
        """Initialize engines after model creation."""
        super().model_post_init(__context)

        # Create engines based on configuration method
        if self.player_configs:
            # Method 1: Use detailed player configurations
            self.engines = create_generic_fox_and_geese_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_fox_and_geese_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            fox_model = self.fox_model or "gpt-4o"
            geese_model = self.geese_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_fox_and_geese_engines_simple(
                fox_model, geese_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(fox_model, geese_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            fox_config = self.player_configs.get("fox_player")
            geese_config = self.player_configs.get("geese_player")

            self.fox_name = (
                fox_config.player_name
                if fox_config and fox_config.player_name
                else "Fox"
            )
            self.geese_name = (
                geese_config.player_name
                if geese_config and geese_config.player_name
                else "Geese"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Fox", "Claude Geese"),
            "gpt_only": ("GPT Fox", "GPT Geese"),
            "claude_only": ("Claude Fox", "Claude Geese"),
            "budget": ("Budget Fox", "Budget Geese"),
            "mixed": ("Mixed Fox", "Mixed Geese"),
            "advanced": ("Advanced Fox", "Advanced Geese"),
        }

        if self.example_config in example_names:
            self.fox_name, self.geese_name = example_names[self.example_config]
        else:
            self.fox_name = f"{self.example_config} Fox"
            self.geese_name = f"{self.example_config} Geese"

    def _generate_player_names_from_models(self, fox_model: str, geese_model: str):
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

        self.fox_name = (
            getattr(self, "fox_name", None) or f"{model_to_name(fox_model)} Fox"
        )
        self.geese_name = (
            getattr(self, "geese_name", None) or f"{model_to_name(geese_model)} Geese"
        )


def create_fox_and_geese_config(
    fox_model: str = "gpt-4o", geese_model: str = "claude-3-5-sonnet-20240620", **kwargs
) -> ConfigurableFoxAndGeeseConfig:
    """Create a configurable FoxAndGeese configuration with simple model specifications.

    Args:
        fox_model: Model for fox and analyzer
        geese_model: Model for geese and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableFoxAndGeeseConfig: Configured FoxAndGeese game

    Example:
        >>> config = create_fox_and_geese_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_fox_and_geese_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )
    """
    return ConfigurableFoxAndGeeseConfig(
        fox_model=fox_model, geese_model=geese_model, **kwargs
    )


def create_fox_and_geese_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableFoxAndGeeseConfig:
    """Create a configurable FoxAndGeese configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableFoxAndGeeseConfig: Configured FoxAndGeese game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Example:
        >>> config = create_fox_and_geese_config_from_example("budget", enable_analysis=False)
        >>> config = create_fox_and_geese_config_from_example("advanced", visualize_game=True)
    """
    return ConfigurableFoxAndGeeseConfig(example_config=example_name, **kwargs)


def create_fox_and_geese_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableFoxAndGeeseConfig:
    """Create a configurable FoxAndGeese configuration from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableFoxAndGeeseConfig: Configured FoxAndGeese game

    Expected roles:
        - "fox_player": Player 1 configuration
        - "geese_player": Player 2 configuration
        - "fox_analyzer": Player 1 analyzer configuration
        - "geese_analyzer": Player 2 analyzer configuration

    Example:
        >>> player_configs = {
        ...     "fox_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Fox"
        ...     ),
        ...     "geese_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical Geese"
        ...     ),
        ...     "fox_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="FoxAndGeese Strategist"
        ...     ),
        ...     "geese_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="FoxAndGeese Analyst"
        ...     ),
        ... }
        >>> config = create_fox_and_geese_config_from_player_configs(player_configs)
    """
    return ConfigurableFoxAndGeeseConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_fox_and_geese_config(**kwargs) -> ConfigurableFoxAndGeeseConfig:
    """Create a budget-friendly FoxAndGeese configuration."""
    return create_fox_and_geese_config_from_example("budget", **kwargs)


def create_advanced_fox_and_geese_config(**kwargs) -> ConfigurableFoxAndGeeseConfig:
    """Create an advanced FoxAndGeese configuration with powerful models."""
    return create_fox_and_geese_config_from_example("advanced", **kwargs)


def create_experimental_fox_and_geese_config(**kwargs) -> ConfigurableFoxAndGeeseConfig:
    """Create an experimental FoxAndGeese configuration with mixed providers."""
    return create_fox_and_geese_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_fox_and_geese_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_fox_and_geese_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_fox_and_geese_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_fox_and_geese_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableFoxAndGeeseConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableFoxAndGeeseConfig: The example configuration

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
    print("🎮 Configurable FoxAndGeese Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_fox_and_geese_config("gpt-4o", "claude-3-opus")
    print(f"   Fox: {config1.fox_name}")
    print(f"   Geese: {config1.geese_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_fox_and_geese_config_from_example("advanced")
    print(f"   Fox: {config2.fox_name}")
    print(f"   Geese: {config2.geese_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "fox_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Fox", temperature=0.8
        ),
        "geese_player": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Expert Geese", temperature=0.4
        ),
        "fox_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "geese_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_fox_and_geese_config_from_player_configs(player_configs)
    print(f"   Fox: {config3.fox_name}")
    print(f"   Geese: {config3.geese_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ FoxAndGeese configurable system ready!")
