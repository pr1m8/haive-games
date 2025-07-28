"""Configurable Reversi configuration using the generic player agent system.

This module provides configurable Reversi game configurations that
replace hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.reversi.config import ReversiConfig
from haive.games.reversi.generic_engines import (
    create_generic_reversi_config_from_example,
    create_generic_reversi_engines,
    create_generic_reversi_engines_simple,
)


class ConfigurableReversiConfig(ReversiConfig):
    """Configurable Reversi configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Reversi game, providing flexibility and avoiding hardcoded models.

    Attributes:
        black_model: Model for black (can be string or LLMConfig)
        white_model: Model for white (can be string or LLMConfig)
        black_name: Name for black
        white_name: Name for white
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        visualize_game: Whether to visualize game state
        recursion_limit: Python recursion limit for game execution
    """

    black_model: Optional[str] = Field(default=None, description="Model for black")
    white_model: Optional[str] = Field(default=None, description="Model for white")
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
            self.engines = create_generic_reversi_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_reversi_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            black_model = self.black_model or "gpt-4o"
            white_model = self.white_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_reversi_engines_simple(
                black_model, white_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(black_model, white_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            black_config = self.player_configs.get("black_player")
            white_config = self.player_configs.get("white_player")

            self.black_name = (
                black_config.player_name
                if black_config and black_config.player_name
                else "Black Player"
            )
            self.white_name = (
                white_config.player_name
                if white_config and white_config.player_name
                else "White Player"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Black Player", "Claude White Player"),
            "gpt_only": ("GPT Black Player", "GPT White Player"),
            "claude_only": ("Claude Black Player", "Claude White Player"),
            "budget": ("Budget Black Player", "Budget White Player"),
            "mixed": ("Mixed Black Player", "Mixed White Player"),
            "advanced": ("Advanced Black Player", "Advanced White Player"),
        }

        if self.example_config in example_names:
            self.black_name, self.white_name = example_names[self.example_config]
        else:
            self.black_name = f"{self.example_config} Black Player"
            self.white_name = f"{self.example_config} White Player"

    def _generate_player_names_from_models(self, black_model: str, white_model: str):
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

        self.black_name = (
            getattr(self, "black_name", None)
            or f"{model_to_name(black_model)} Black Player"
        )
        self.white_name = (
            getattr(self, "white_name", None)
            or f"{model_to_name(white_model)} White Player"
        )


def create_reversi_config(
    black_model: str = "gpt-4o",
    white_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableReversiConfig:
    """Create a configurable Reversi configuration with simple model
    specifications.

    Args:
        black_model: Model for black and analyzer
        white_model: Model for white and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableReversiConfig: Configured Reversi game

    Example:
        >>> config = create_reversi_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_reversi_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_analysis=True
        ... )
    """
    return ConfigurableReversiConfig(
        black_model=black_model, white_model=white_model, **kwargs
    )


def create_reversi_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableReversiConfig:
    """Create a configurable Reversi configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableReversiConfig: Configured Reversi game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay

    Example:
        >>> config = create_reversi_config_from_example("budget", enable_analysis=False)
        >>> config = create_reversi_config_from_example("advanced", visualize_game=True)
    """
    return ConfigurableReversiConfig(example_config=example_name, **kwargs)


def create_reversi_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableReversiConfig:
    """Create a configurable Reversi configuration from detailed player
    configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableReversiConfig: Configured Reversi game

    Expected roles:
        - "black_player": Player 1 configuration
        - "white_player": Player 2 configuration
        - "black_analyzer": Player 1 analyzer configuration
        - "white_analyzef": Player 2 analyzer configuration

    Example:
        >>> player_configs = {
        ...     "black_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Strategic Black Player"
        ...     ),
        ...     "white_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Tactical White Player"
        ...     ),
        ...     "black_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Reversi Strategist"
        ...     ),
        ...     "white_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Reversi Analyst"
        ...     ),
        ... }
        >>> config = create_reversi_config_from_player_configs(player_configs)
    """
    return ConfigurableReversiConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_reversi_config(**kwargs) -> ConfigurableReversiConfig:
    """Create a budget-friendly Reversi configuration."""
    return create_reversi_config_from_example("budget", **kwargs)


def create_advanced_reversi_config(**kwargs) -> ConfigurableReversiConfig:
    """Create an advanced Reversi configuration with powerful models."""
    return create_reversi_config_from_example("advanced", **kwargs)


def create_experimental_reversi_config(**kwargs) -> ConfigurableReversiConfig:
    """Create an experimental Reversi configuration with mixed providers."""
    return create_reversi_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_reversi_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_reversi_config(enable_analysis=False),
    },
    "advanced": {
        "description": "High-performance strategic setup",
        "config": lambda: create_advanced_reversi_config(temperature=0.2),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_reversi_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableReversiConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableReversiConfig: The example configuration

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
    print("🎮 Configurable Reversi Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_reversi_config("gpt-4o", "claude-3-opus")
    print(f"   Black Player: {config1.black_name}")
    print(f"   White Player: {config1.white_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_reversi_config_from_example("advanced")
    print(f"   Black Player: {config2.black_name}")
    print(f"   White Player: {config2.white_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Custom player configs
    print("3️⃣ Custom Player Configuration:")
    player_configs = {
        "black_player": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Master Black Player", temperature=0.8
        ),
        "white_player": PlayerAgentConfig(
            llm_config="claude-3-opus",
            player_name="Expert White Player",
            temperature=0.4,
        ),
        "black_analyzer": PlayerAgentConfig(
            llm_config="gpt-4o", player_name="Strategic Command", temperature=0.2
        ),
        "white_analyzer": PlayerAgentConfig(
            llm_config="claude-3-opus", player_name="Tactical Analysis", temperature=0.2
        ),
    }
    config3 = create_reversi_config_from_player_configs(player_configs)
    print(f"   Black Player: {config3.black_name}")
    print(f"   White Player: {config3.white_name}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Reversi configurable system ready!")
