"""Configurable Among Us configuration using the generic player agent system.

This module provides configurable Among Us game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.

"""

from typing import Any

from pydantic import Field

from haive.games.among_us.config import AmongUsConfig
from haive.games.among_us.generic_engines import (
    create_generic_among_us_config_from_example,
    create_generic_among_us_engines,
    create_generic_among_us_engines_simple,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class ConfigurableAmongUsConfig(AmongUsConfig):
    """Configurable Among Us configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Among Us game, providing flexibility and avoiding hardcoded models.

    Attributes:
        crewmate_model: Model for crewmate players (can be string or LLMConfig)
        impostor_model: Model for impostor players (can be string or LLMConfig)
        crewmate_player_name: Name for the crewmate players
        impostor_player_name: Name for the impostor players
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        max_rounds: Maximum number of rounds before game ends
        enable_analysis: Whether to enable game state analysis
        recursion_limit: Python recursion limit for game execution

    """

    crewmate_model: str | None = Field(
        default=None, description="Model for crewmate players"
    )
    impostor_model: str | None = Field(
        default=None, description="Model for impostor players"
    )
    crewmate_player_name: str | None = Field(
        default=None, description="Name for crewmate players"
    )
    impostor_player_name: str | None = Field(
        default=None, description="Name for impostor players"
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
    max_rounds: int = Field(default=50, description="Maximum rounds before game ends")
    enable_analysis: bool = Field(
        default=True, description="Enable game state analysis"
    )
    recursion_limit: int = Field(default=800, description="Python recursion limit")

    def model_post_init(self, __context: Any) -> None:
        """Initialize engines after model creation."""
        super().model_post_init(__context)

        # Create engines based on configuration method
        if self.player_configs:
            # Method 1: Use detailed player configurations
            self.engines = create_generic_among_us_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_among_us_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            crewmate_model = self.crewmate_model or "gpt-4o"
            impostor_model = self.impostor_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_among_us_engines_simple(
                crewmate_model, impostor_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(crewmate_model, impostor_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            crewmate_config = self.player_configs.get("crewmate_player")
            impostor_config = self.player_configs.get("impostor_player")

            self.crewmate_player_name = (
                crewmate_config.player_name
                if crewmate_config and crewmate_config.player_name
                else "Crewmate"
            )
            self.impostor_player_name = (
                impostor_config.player_name
                if impostor_config and impostor_config.player_name
                else "Impostor"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Crewmate", "Claude Impostor"),
            "gpt_only": ("GPT Crewmate", "GPT Impostor"),
            "claude_only": ("Claude Crewmate", "Claude Impostor"),
            "budget": ("Budget Crewmate", "Budget Impostor"),
            "mixed": ("Mixed Crewmate", "Mixed Impostor"),
            "detective_vs_mastermind": ("Detective", "Mastermind"),
        }

        if self.example_config in example_names:
            self.crewmate_player_name, self.impostor_player_name = example_names[
                self.example_config
            ]
        else:
            self.crewmate_player_name = f"{self.example_config} Crewmate"
            self.impostor_player_name = f"{self.example_config} Impostor"

    def _generate_player_names_from_models(
        self, crewmate_model: str, impostor_model: str
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

        self.crewmate_player_name = (
            self.crewmate_player_name or f"{model_to_name(crewmate_model)} Crewmate"
        )
        self.impostor_player_name = (
            self.impostor_player_name or f"{model_to_name(impostor_model)} Impostor"
        )


def create_among_us_config(
    crewmate_model: str = "gpt-4o",
    impostor_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableAmongUsConfig:
    """Create a configurable Among Us configuration with simple model specifications.

    Args:
        crewmate_model: Model for crewmate players and analyzers
        impostor_model: Model for impostor players and analyzers
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableAmongUsConfig: Configured Among Us game

    Examples:
        >>> config = create_among_us_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_among_us_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     max_rounds=75
        ... )

    """
    return ConfigurableAmongUsConfig(
        crewmate_model=crewmate_model, impostor_model=impostor_model, **kwargs
    )


def create_among_us_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableAmongUsConfig:
    """Create a configurable Among Us configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableAmongUsConfig: Configured Among Us game

    Available examples:
        - "gpt_vs_claude": GPT crewmate vs Claude impostor
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "detective_vs_mastermind": High-powered models for intense gameplay

    Examples:
        >>> config = create_among_us_config_from_example("budget", max_rounds=40)
        >>> config = create_among_us_config_from_example("detective_vs_mastermind", enable_analysis=False)

    """
    return ConfigurableAmongUsConfig(example_config=example_name, **kwargs)


def create_among_us_config_from_player_configs(
    player_configs: dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableAmongUsConfig:
    """Create a configurable Among Us configuration from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableAmongUsConfig: Configured Among Us game

    Expected roles:
        - "crewmate_player": Crewmate player configuration
        - "impostor_player": Impostor player configuration
        - "crewmate_analyzer": Crewmate analyzer configuration
        - "impostor_analyzer": Impostor analyzer configuration

    Examples:
        >>> player_configs = {
        ...     "crewmate_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Detective Crewmate"
        ...     ),
        ...     "impostor_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Stealth Impostor"
        ...     ),
        ...     "crewmate_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Crew Analyst"
        ...     ),
        ...     "impostor_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Impostor Strategist"
        ...     ),
        ... }
        >>> config = create_among_us_config_from_player_configs(player_configs)

    """
    return ConfigurableAmongUsConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_among_us_config(**kwargs) -> ConfigurableAmongUsConfig:
    """Create a budget-friendly Among Us configuration."""
    return create_among_us_config_from_example("budget", **kwargs)


def create_detective_among_us_config(**kwargs) -> ConfigurableAmongUsConfig:
    """Create a detective-style Among Us configuration with powerful models."""
    return create_among_us_config_from_example("detective_vs_mastermind", **kwargs)


def create_experimental_among_us_config(**kwargs) -> ConfigurableAmongUsConfig:
    """Create an experimental Among Us configuration with mixed providers."""
    return create_among_us_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_among_us_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_among_us_config(max_rounds=40),
    },
    "detective": {
        "description": "High-performance detective vs mastermind setup",
        "config": lambda: create_detective_among_us_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_among_us_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableAmongUsConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableAmongUsConfig: The example configuration

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
    print("🕵️ Configurable Among Us Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_among_us_config("gpt-4o", "claude-3-opus")
    print(f"   Crewmate: {config1.crewmate_player_name}")
    print(f"   Impostor: {config1.impostor_player_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_among_us_config_from_example("detective_vs_mastermind")
    print(f"   Crewmate: {config2.crewmate_player_name}")
    print(f"   Impostor: {config2.impostor_player_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "crewmate_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Sherlock Holmes", temperature=0.8
        ),
        "impostor_player": PlayerAgentConfig(
            llm_config="claude-3-opus",
            player_name="Professor Moriarty",
            temperature=0.4,
        ),
        "crewmate_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Watson", temperature=0.2
        ),
        "impostor_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus",
            player_name="Criminal Mastermind",
            temperature=0.2,
        ),
    }
    config3 = create_among_us_config_from_player_configs(player_configs)
    print(f"   Crewmate: {config3.crewmate_player_name}")
    print(f"   Impostor: {config3.impostor_player_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Among Us configurable system ready!")
