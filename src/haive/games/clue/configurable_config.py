"""Configurable Clue configuration using the generic player agent system.

This module provides configurable Clue game configurations that replace
hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional

from pydantic import Field

from haive.games.clue.config import ClueConfig
from haive.games.clue.generic_engines import (
    create_generic_clue_config_from_example,
    create_generic_clue_engines,
    create_generic_clue_engines_simple,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class ConfigurableClueConfig(ClueConfig):
    """Configurable Clue configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Clue game, providing flexibility and avoiding hardcoded models.

    Attributes:
        detective_model: Model for detective (can be string or LLMConfig)
        suspect_model: Model for suspect (can be string or LLMConfig)
        detective_name: Name for detective
        suspect_name: Name for suspect
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution
    """

    detective_model: Optional[str] = Field(
        default=None, description="Model for detective"
    )
    suspect_model: Optional[str] = Field(default=None, description="Model for suspect")
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
            self.engines = create_generic_clue_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_clue_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            detective_model = self.detective_model or "gpt-4o"
            suspect_model = self.suspect_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_clue_engines_simple(
                detective_model, suspect_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(detective_model, suspect_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            detective_config = self.player_configs.get("detective_player")
            suspect_config = self.player_configs.get("suspect_player")

            self.detective_name = (
                detective_config.player_name
                if detective_config and detective_config.player_name
                else "Detective"
            )
            self.suspect_name = (
                suspect_config.player_name
                if suspect_config and suspect_config.player_name
                else "Suspect"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Detective", "Claude Suspect"),
            "gpt_only": ("GPT Detective", "GPT Suspect"),
            "claude_only": ("Claude Detective", "Claude Suspect"),
            "budget": ("Budget Detective", "Budget Suspect"),
            "mixed": ("Mixed Detective", "Mixed Suspect"),
            "advanced": ("Advanced Detective", "Advanced Suspect"),
        }

        if self.example_config in example_names:
            self.detective_name, self.suspect_name = example_names[self.example_config]
        else:
            self.detective_name = f"{self.example_config} Detective"
            self.suspect_name = f"{self.example_config} Suspect"

    def _generate_player_names_from_models(
        self, detective_model: str, suspect_model: str
    ):
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

        self.detective_name = (
            getattr(self, "detective_name", None)
            or f"{model_to_name(detective_model)} Detective"
        )
        self.suspect_name = (
            getattr(self, "suspect_name", None)
            or f"{model_to_name(suspect_model)} Suspect"
        )


def create_clue_config(
    detective_model: str = "gpt-4o",
    suspect_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableClueConfig:
    """Create a configurable Clue configuration with simple model
    specifications.

    Args:
        detective_model: Model for detective and analyzer
        suspect_model: Model for suspect and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableClueConfig: Configured Clue game

    Example:
        >>> config = create_clue_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_clue_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )
    """
    return ConfigurableClueConfig(
        detective_model=detective_model, suspect_model=suspect_model, **kwargs
    )


def create_clue_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableClueConfig:
    """Create a configurable Clue configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableClueConfig: Configured Clue game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Example:
        >>> config = create_clue_config_from_example("budget", enable_analysis=False)
        >>> config = create_clue_config_from_example("advanced", visualize_game=True)
    """
    return ConfigurableClueConfig(example_config=example_name, **kwargs)


def create_clue_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableClueConfig:
    """Create a configurable Clue configuration from detailed player
    configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableClueConfig: Configured Clue game

    Expected roles:
        - "detective_player": Player 1 configuration
        - "suspect_player": Player 2 configuration
        - "detective_analyzer": Player 1 analyzer configuration
        - "suspect_analyzer": Player 2 analyzer configuration

    Example:
        >>> player_configs = {
        ...     "detective_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Detective"
        ...     ),
        ...     "suspect_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical Suspect"
        ...     ),
        ...     "detective_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Clue Strategist"
        ...     ),
        ...     "suspect_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Clue Analyst"
        ...     ),
        ... }
        >>> config = create_clue_config_from_player_configs(player_configs)
    """
    return ConfigurableClueConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_clue_config(**kwargs) -> ConfigurableClueConfig:
    """Create a budget-friendly Clue configuration."""
    return create_clue_config_from_example("budget", **kwargs)


def create_advanced_clue_config(**kwargs) -> ConfigurableClueConfig:
    """Create an advanced Clue configuration with powerful models."""
    return create_clue_config_from_example("advanced", **kwargs)


def create_experimental_clue_config(**kwargs) -> ConfigurableClueConfig:
    """Create an experimental Clue configuration with mixed providers."""
    return create_clue_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_clue_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_clue_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_clue_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_clue_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableClueConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableClueConfig: The example configuration

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
    print("🎮 Configurable Clue Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_clue_config("gpt-4o", "claude-3-opus")
    print(f"   Detective: {config1.detective_name}")
    print(f"   Suspect: {config1.suspect_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_clue_config_from_example("advanced")
    print(f"   Detective: {config2.detective_name}")
    print(f"   Suspect: {config2.suspect_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "detective_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Detective", temperature=0.8
        ),
        "suspect_player": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Expert Suspect", temperature=0.4
        ),
        "detective_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "suspect_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_clue_config_from_player_configs(player_configs)
    print(f"   Detective: {config3.detective_name}")
    print(f"   Suspect: {config3.suspect_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Clue configurable system ready!")
