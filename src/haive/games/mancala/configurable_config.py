"""Configurable Mancala configuration using the generic player agent system.

This module provides configurable Mancala game configurations that
replace hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.mancala.config import MancalaConfig
from haive.games.mancala.generic_engines import (
    create_generic_mancala_config_from_example,
    create_generic_mancala_engines,
    create_generic_mancala_engines_simple,
)


class ConfigurableMancalaConfig(MancalaConfig):
    """Configurable Mancala configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Mancala game, providing flexibility and avoiding hardcoded models.

    Attributes:
        player1_model: Model for player1 (can be string or LLMConfig)
        player2_model: Model for player2 (can be string or LLMConfig)
        player1_name: Name for player1
        player2_name: Name for player2
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution
    """

    player1_model: Optional[str] = Field(default=None, description="Model for player1")
    player2_model: Optional[str] = Field(default=None, description="Model for player2")
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
            self.engines = create_generic_mancala_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_mancala_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            player1_model = self.player1_model or "gpt-4o"
            player2_model = self.player2_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_mancala_engines_simple(
                player1_model, player2_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(player1_model, player2_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            player1_config = self.player_configs.get("player1_player")
            player2_config = self.player_configs.get("player2_player")

            self.player1_name = (
                player1_config.player_name
                if player1_config and player1_config.player_name
                else "Mancala Player"
            )
            self.player2_name = (
                player2_config.player_name
                if player2_config and player2_config.player_name
                else "Mancala Expert"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Mancala Player", "Claude Mancala Expert"),
            "gpt_only": ("GPT Mancala Player", "GPT Mancala Expert"),
            "claude_only": ("Claude Mancala Player", "Claude Mancala Expert"),
            "budget": ("Budget Mancala Player", "Budget Mancala Expert"),
            "mixed": ("Mixed Mancala Player", "Mixed Mancala Expert"),
            "advanced": ("Advanced Mancala Player", "Advanced Mancala Expert"),
        }

        if self.example_config in example_names:
            self.player1_name, self.player2_name = example_names[self.example_config]
        else:
            self.player1_name = f"{self.example_config} Mancala Player"
            self.player2_name = f"{self.example_config} Mancala Expert"

    def _generate_player_names_from_models(
        self, player1_model: str, player2_model: str
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

        self.player1_name = (
            getattr(self, "player1_name", None)
            or f"{model_to_name(player1_model)} Mancala Player"
        )
        self.player2_name = (
            getattr(self, "player2_name", None)
            or f"{model_to_name(player2_model)} Mancala Expert"
        )


def create_mancala_config(
    player1_model: str = "gpt-4o",
    player2_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableMancalaConfig:
    """Create a configurable Mancala configuration with simple model
    specifications.

    Args:
        player1_model: Model for player1 and analyzer
        player2_model: Model for player2 and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMancalaConfig: Configured Mancala game

    Example:
        >>> config = create_mancala_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_mancala_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )
    """
    return ConfigurableMancalaConfig(
        player1_model=player1_model, player2_model=player2_model, **kwargs
    )


def create_mancala_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableMancalaConfig:
    """Create a configurable Mancala configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableMancalaConfig: Configured Mancala game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Example:
        >>> config = create_mancala_config_from_example("budget", enable_analysis=False)
        >>> config = create_mancala_config_from_example("advanced", visualize_game=True)
    """
    return ConfigurableMancalaConfig(example_config=example_name, **kwargs)


def create_mancala_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableMancalaConfig:
    """Create a configurable Mancala configuration from detailed player
    configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMancalaConfig: Configured Mancala game

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzef": Player 2 analyzer configuration

    Example:
        >>> player_configs = {
        ...     "player1_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Mancala Player"
        ...     ),
        ...     "player2_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical Mancala Expert"
        ...     ),
        ...     "player1_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Mancala Strategist"
        ...     ),
        ...     "player2_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Mancala Analyst"
        ...     ),
        ... }
        >>> config = create_mancala_config_from_player_configs(player_configs)
    """
    return ConfigurableMancalaConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_mancala_config(**kwargs) -> ConfigurableMancalaConfig:
    """Create a budget-friendly Mancala configuration."""
    return create_mancala_config_from_example("budget", **kwargs)


def create_advanced_mancala_config(**kwargs) -> ConfigurableMancalaConfig:
    """Create an advanced Mancala configuration with powerful models."""
    return create_mancala_config_from_example("advanced", **kwargs)


def create_experimental_mancala_config(**kwargs) -> ConfigurableMancalaConfig:
    """Create an experimental Mancala configuration with mixed providers."""
    return create_mancala_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_mancala_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_mancala_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_mancala_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_mancala_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableMancalaConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableMancalaConfig: The example configuration

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
    print("🎮 Configurable Mancala Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_mancala_config("gpt-4o", "claude-3-opus")
    print(f"   Mancala Player: {config1.player1_name}")
    print(f"   Mancala Expert: {config1.player2_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_mancala_config_from_example("advanced")
    print(f"   Mancala Player: {config2.player1_name}")
    print(f"   Mancala Expert: {config2.player2_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "player1_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Mancala Player", temperature=0.8
        ),
        "player2_player": PlayerAgentConfig(
            llm_config="claude-3-opus",
            player_name="Expert Mancala Expert",
            temperature=0.4,
        ),
        "player1_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "player2_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_mancala_config_from_player_configs(player_configs)
    print(f"   Mancala Player: {config3.player1_name}")
    print(f"   Mancala Expert: {config3.player2_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Mancala configurable system ready!")
