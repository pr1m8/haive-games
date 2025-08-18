"""Configurable Mastermind configuration using the generic player agent system.

This module provides configurable Mastermind game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.

"""

from typing import Any

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.mastermind.config import MastermindConfig
from haive.games.mastermind.generic_engines import (
    create_generic_mastermind_config_from_example,
    create_generic_mastermind_engines,
    create_generic_mastermind_engines_simple,
)


class ConfigurableMastermindConfig(MastermindConfig):
    """Configurable Mastermind configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Mastermind game, providing flexibility and avoiding hardcoded models.

    Attributes:
        codemaker_model: Model for codemaker (can be string or LLMConfig)
        codebreaker_model: Model for codebreaker (can be string or LLMConfig)
        codemaker_name: Name for codemaker
        codebreaker_name: Name for codebreaker
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution

    """

    codemaker_model: str | None = Field(default=None, description="Model for codemaker")
    codebreaker_model: str | None = Field(
        default=None, description="Model for codebreaker"
    )
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
            self.engines = create_generic_mastermind_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_mastermind_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            codemaker_model = self.codemaker_model or "gpt-4o"
            codebreaker_model = self.codebreaker_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_mastermind_engines_simple(
                codemaker_model, codebreaker_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(codemaker_model, codebreaker_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            codemaker_config = self.player_configs.get("codemaker_player")
            codebreaker_config = self.player_configs.get("codebreaker_player")

            self.codemaker_name = (
                codemaker_config.player_name
                if codemaker_config and codemaker_config.player_name
                else "Codemaker"
            )
            self.codebreaker_name = (
                codebreaker_config.player_name
                if codebreaker_config and codebreaker_config.player_name
                else "Codebreaker"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Codemaker", "Claude Codebreaker"),
            "gpt_only": ("GPT Codemaker", "GPT Codebreaker"),
            "claude_only": ("Claude Codemaker", "Claude Codebreaker"),
            "budget": ("Budget Codemaker", "Budget Codebreaker"),
            "mixed": ("Mixed Codemaker", "Mixed Codebreaker"),
            "advanced": ("Advanced Codemaker", "Advanced Codebreaker"),
        }

        if self.example_config in example_names:
            self.codemaker_name, self.codebreaker_name = example_names[
                self.example_config
            ]
        else:
            self.codemaker_name = f"{self.example_config} Codemaker"
            self.codebreaker_name = f"{self.example_config} Codebreaker"

    def _generate_player_names_from_models(
        self, codemaker_model: str, codebreaker_model: str
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

        self.codemaker_name = (
            getattr(self, "codemaker_name", None)
            or f"{model_to_name(codemaker_model)} Codemaker"
        )
        self.codebreaker_name = (
            getattr(self, "codebreaker_name", None)
            or f"{model_to_name(codebreaker_model)} Codebreaker"
        )


def create_mastermind_config(
    codemaker_model: str = "gpt-4o",
    codebreaker_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableMastermindConfig:
    """Create a configurable Mastermind configuration with simple model specifications.

    Args:
        codemaker_model: Model for codemaker and analyzer
        codebreaker_model: Model for codebreaker and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMastermindConfig: Configured Mastermind game

    Examples:
        >>> config = create_mastermind_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_mastermind_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )

    """
    return ConfigurableMastermindConfig(
        codemaker_model=codemaker_model, codebreaker_model=codebreaker_model, **kwargs
    )


def create_mastermind_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableMastermindConfig:
    """Create a configurable Mastermind configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableMastermindConfig: Configured Mastermind game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Examples:
        >>> config = create_mastermind_config_from_example("budget", enable_analysis=False)
        >>> config = create_mastermind_config_from_example("advanced", visualize_game=True)

    """
    return ConfigurableMastermindConfig(example_config=example_name, **kwargs)


def create_mastermind_config_from_player_configs(
    player_configs: dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableMastermindConfig:
    """Create a configurable Mastermind configuration from detailed player.
    configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMastermindConfig: Configured Mastermind game

    Expected roles:
        - "codemaker_player": Player 1 configuration
        - "codebreaker_player": Player 2 configuration
        - "codemaker_analyzer": Player 1 analyzer configuration
        - "codebreaker_analyzer": Player 2 analyzer configuration

    Examples:
        >>> player_configs = {
        ...     "codemaker_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Codemaker"
        ...     ),
        ...     "codebreaker_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical Codebreaker"
        ...     ),
        ...     "codemaker_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Mastermind Strategist"
        ...     ),
        ...     "codebreaker_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Mastermind Analyst"
        ...     ),
        ... }
        >>> config = create_mastermind_config_from_player_configs(player_configs)

    """
    return ConfigurableMastermindConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_mastermind_config(**kwargs) -> ConfigurableMastermindConfig:
    """Create a budget-friendly Mastermind configuration."""
    return create_mastermind_config_from_example("budget", **kwargs)


def create_advanced_mastermind_config(**kwargs) -> ConfigurableMastermindConfig:
    """Create an advanced Mastermind configuration with powerful models."""
    return create_mastermind_config_from_example("advanced", **kwargs)


def create_experimental_mastermind_config(**kwargs) -> ConfigurableMastermindConfig:
    """Create an experimental Mastermind configuration with mixed providers."""
    return create_mastermind_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_mastermind_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_mastermind_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_mastermind_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_mastermind_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableMastermindConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableMastermindConfig: The example configuration

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
    print("🎮 Configurable Mastermind Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_mastermind_config("gpt-4o", "claude-3-opus")
    print(f"   Codemaker: {config1.codemaker_name}")
    print(f"   Codebreaker: {config1.codebreaker_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_mastermind_config_from_example("advanced")
    print(f"   Codemaker: {config2.codemaker_name}")
    print(f"   Codebreaker: {config2.codebreaker_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "codemaker_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Codemaker", temperature=0.8
        ),
        "codebreaker_player": PlayerAgentConfig(
            llm_config="claude-3-opus",
            player_name="Expert Codebreaker",
            temperature=0.4,
        ),
        "codemaker_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "codebreaker_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_mastermind_config_from_player_configs(player_configs)
    print(f"   Codemaker: {config3.codemaker_name}")
    print(f"   Codebreaker: {config3.codebreaker_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Mastermind configurable system ready!")
