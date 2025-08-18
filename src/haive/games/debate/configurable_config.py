"""Configurable Debate configuration using the generic player agent system.

This module provides configurable Debate game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.

"""

from typing import Any

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.debate.config import DebateAgentConfig
from haive.games.debate.generic_engines import (
    create_generic_debate_config_from_example,
    create_generic_debate_engines,
    create_generic_debate_engines_simple,
)


class ConfigurableDebateConfig(DebateAgentConfig):
    """Configurable Debate configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Debate game, providing flexibility and avoiding hardcoded models.

    Attributes:
        debater1_model: Model for debater1 (can be string or LLMConfig)
        debater2_model: Model for debater2 (can be string or LLMConfig)
        debater1_name: Name for debater1
        debater2_name: Name for debater2
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution

    """

    debater1_model: str | None = Field(default=None, description="Model for debater1")
    debater2_model: str | None = Field(default=None, description="Model for debater2")
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
            self.engines = create_generic_debate_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_debate_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            debater1_model = self.debater1_model or "gpt-4o"
            debater2_model = self.debater2_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_debate_engines_simple(
                debater1_model, debater2_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(debater1_model, debater2_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            debater1_config = self.player_configs.get("debater1_player")
            debater2_config = self.player_configs.get("debater2_player")

            self.debater1_name = (
                debater1_config.player_name
                if debater1_config and debater1_config.player_name
                else "Debater A"
            )
            self.debater2_name = (
                debater2_config.player_name
                if debater2_config and debater2_config.player_name
                else "Debater B"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Debater A", "Claude Debater B"),
            "gpt_only": ("GPT Debater A", "GPT Debater B"),
            "claude_only": ("Claude Debater A", "Claude Debater B"),
            "budget": ("Budget Debater A", "Budget Debater B"),
            "mixed": ("Mixed Debater A", "Mixed Debater B"),
            "advanced": ("Advanced Debater A", "Advanced Debater B"),
        }

        if self.example_config in example_names:
            self.debater1_name, self.debater2_name = example_names[self.example_config]
        else:
            self.debater1_name = f"{self.example_config} Debater A"
            self.debater2_name = f"{self.example_config} Debater B"

    def _generate_player_names_from_models(
        self, debater1_model: str, debater2_model: str
    ):
        """Generate player names based on model names."""

        def model_to_name(model: str) -> str:
            """Model To Name.

Args:
    model: [TODO: Add description]

Returns:
    [TODO: Add return description]
"""
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

        self.debater1_name = (
            getattr(self, "debater1_name", None)
            or f"{model_to_name(debater1_model)} Debater A"
        )
        self.debater2_name = (
            getattr(self, "debater2_name", None)
            or f"{model_to_name(debater2_model)} Debater B"
        )


def create_debate_config(
    debater1_model: str = "gpt-4o",
    debater2_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableDebateConfig:
    """Create a configurable Debate configuration with simple model specifications.

    Args:
        debater1_model: Model for debater1 and analyzer
        debater2_model: Model for debater2 and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableDebateConfig: Configured Debate game

    Examples:
        >>> config = create_debate_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_debate_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )

    """
    return ConfigurableDebateConfig(
        debater1_model=debater1_model, debater2_model=debater2_model, **kwargs
    )


def create_debate_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableDebateConfig:
    """Create a configurable Debate configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableDebateConfig: Configured Debate game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Examples:
        >>> config = create_debate_config_from_example("budget", enable_analysis=False)
        >>> config = create_debate_config_from_example("advanced", visualize_game=True)

    """
    return ConfigurableDebateConfig(example_config=example_name, **kwargs)


def create_debate_config_from_player_configs(
    player_configs: dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableDebateConfig:
    """Create a configurable Debate configuration from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableDebateConfig: Configured Debate game

    Expected roles:
        - "debater1_player": Player 1 configuration
        - "debater2_player": Player 2 configuration
        - "debater1_analyzer": Player 1 analyzer configuration
        - "debater2_analyzer": Player 2 analyzer configuration

    Examples:
        >>> player_configs = {
        ...     "debater1_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Debater A"
        ...     ),
        ...     "debater2_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical Debater B"
        ...     ),
        ...     "debater1_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Debate Strategist"
        ...     ),
        ...     "debater2_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Debate Analyst"
        ...     ),
        ... }
        >>> config = create_debate_config_from_player_configs(player_configs)

    """
    return ConfigurableDebateConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_debate_config(**kwargs) -> ConfigurableDebateConfig:
    """Create a budget-friendly Debate configuration."""
    return create_debate_config_from_example("budget", **kwargs)


def create_advanced_debate_config(**kwargs) -> ConfigurableDebateConfig:
    """Create an advanced Debate configuration with powerful models."""
    return create_debate_config_from_example("advanced", **kwargs)


def create_experimental_debate_config(**kwargs) -> ConfigurableDebateConfig:
    """Create an experimental Debate configuration with mixed providers."""
    return create_debate_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_debate_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_debate_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_debate_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_debate_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableDebateConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableDebateConfig: The example configuration

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
    print("🎮 Configurable Debate Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_debate_config("gpt-4o", "claude-3-opus")
    print(f"   Debater A: {config1.debater1_name}")
    print(f"   Debater B: {config1.debater2_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_debate_config_from_example("advanced")
    print(f"   Debater A: {config2.debater1_name}")
    print(f"   Debater B: {config2.debater2_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "debater1_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Debater A", temperature=0.8
        ),
        "debater2_player": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Expert Debater B", temperature=0.4
        ),
        "debater1_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "debater2_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_debate_config_from_player_configs(player_configs)
    print(f"   Debater A: {config3.debater1_name}")
    print(f"   Debater B: {config3.debater2_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Debate configurable system ready!")
