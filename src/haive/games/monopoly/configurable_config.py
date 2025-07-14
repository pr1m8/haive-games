"""Configurable Monopoly configuration using the generic player agent system.

This module provides configurable Monopoly game configurations that replace
hardcoded LLM settings with dynamic, configurable player agents.
"""

from typing import Any, Dict, Optional

from pydantic import Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.monopoly.config import MonopolyGameAgentConfig
from haive.games.monopoly.generic_engines import (
    create_generic_monopoly_config_from_example,
    create_generic_monopoly_engines,
    create_generic_monopoly_engines_simple,
)


class ConfigurableMonopolyConfig(MonopolyGameAgentConfig):
    """Configurable Monopoly configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Monopoly game, providing flexibility and avoiding hardcoded models.

    Attributes:
        player1_model: Model for player 1 (can be string or LLMConfig)
        player2_model: Model for player 2 (can be string or LLMConfig)
        player1_name: Name for player 1
        player2_name: Name for player 2
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        enable_trading: Whether to enable property trading
        enable_building: Whether to enable house/hotel building
        recursion_limit: Python recursion limit for game execution
    """

    player1_model: Optional[str] = Field(default=None, description="Model for player 1")
    player2_model: Optional[str] = Field(default=None, description="Model for player 2")
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
            self.engines = create_generic_monopoly_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_monopoly_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            player1_model = self.player1_model or "gpt-4o"
            player2_model = self.player2_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_monopoly_engines_simple(
                player1_model, player2_model, temperature=self.temperature
            )
            self._generate_player_names_from_models(player1_model, player2_model)

    def _extract_player_names_from_configs(self):
        """Extract player names from player configurations."""
        if self.player_configs:
            player1_config = self.player_configs.get("player1_player")
            player2_config = self.player_configs.get("player2_player")

            # Set player names on the base config
            if hasattr(self, "player_names") and len(self.player_names) >= 2:
                self.player_names[0] = (
                    player1_config.player_name
                    if player1_config and player1_config.player_name
                    else "Player 1"
                )
                self.player_names[1] = (
                    player2_config.player_name
                    if player2_config and player2_config.player_name
                    else "Player 2"
                )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Mogul", "Claude Tycoon"),
            "gpt_only": ("GPT Player 1", "GPT Player 2"),
            "claude_only": ("Claude Player 1", "Claude Player 2"),
            "budget": ("Budget Investor", "Thrifty Trader"),
            "mixed": ("Mixed Mogul", "Mixed Tycoon"),
            "real_estate_moguls": ("Real Estate Mogul", "Property Baron"),
            "property_tycoons": ("Property Tycoon", "Investment King"),
        }

        if self.example_config in example_names:
            names = example_names[self.example_config]
        else:
            names = (
                f"{self.example_config} Player 1",
                f"{self.example_config} Player 2",
            )

        # Update player names in the base config
        if hasattr(self, "player_names") and len(self.player_names) >= 2:
            self.player_names[0] = names[0]
            self.player_names[1] = names[1]

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

        names = (
            f"{model_to_name(player1_model)} Mogul",
            f"{model_to_name(player2_model)} Tycoon",
        )

        # Update player names in the base config
        if hasattr(self, "player_names") and len(self.player_names) >= 2:
            self.player_names[0] = names[0]
            self.player_names[1] = names[1]


def create_monopoly_config(
    player1_model: str = "gpt-4o",
    player2_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableMonopolyConfig:
    """Create a configurable Monopoly configuration with simple model specifications.

    Args:
        player1_model: Model for player 1 and analyzer
        player2_model: Model for player 2 and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMonopolyConfig: Configured Monopoly game

    Example:
        >>> config = create_monopoly_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_monopoly_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     enable_trading=True
        ... )
    """
    return ConfigurableMonopolyConfig(
        player1_model=player1_model, player2_model=player2_model, **kwargs
    )


def create_monopoly_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableMonopolyConfig:
    """Create a configurable Monopoly configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableMonopolyConfig: Configured Monopoly game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "real_estate_moguls": High-powered models for strategic gameplay
        - "property_tycoons": Specialized for property investment

    Example:
        >>> config = create_monopoly_config_from_example("budget", enable_trading=False)
        >>> config = create_monopoly_config_from_example("real_estate_moguls", enable_building=True)
    """
    return ConfigurableMonopolyConfig(example_config=example_name, **kwargs)


def create_monopoly_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableMonopolyConfig:
    """Create a configurable Monopoly configuration from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableMonopolyConfig: Configured Monopoly game

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzer": Player 2 analyzer configuration

    Example:
        >>> player_configs = {
        ...     "player1_player": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.7,
        ...         player_name="Property Mogul"
        ...     ),
        ...     "player2_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Real Estate Tycoon"
        ...     ),
        ...     "player1_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Investment Strategist"
        ...     ),
        ...     "player2_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Market Analyst"
        ...     ),
        ... }
        >>> config = create_monopoly_config_from_player_configs(player_configs)
    """
    return ConfigurableMonopolyConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig:
    """Create a budget-friendly Monopoly configuration."""
    return create_monopoly_config_from_example("budget", **kwargs)


def create_real_estate_mogul_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig:
    """Create a real estate mogul-style Monopoly configuration with powerful models."""
    return create_monopoly_config_from_example("real_estate_moguls", **kwargs)


def create_property_tycoon_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig:
    """Create a property tycoon-style Monopoly configuration."""
    return create_monopoly_config_from_example("property_tycoons", **kwargs)


def create_experimental_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig:
    """Create an experimental Monopoly configuration with mixed providers."""
    return create_monopoly_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_monopoly_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_monopoly_config(enable_trading=False),
    },
    "real_estate_moguls": {
        "description": "High-performance real estate mogul setup",
        "config": lambda: create_real_estate_mogul_monopoly_config(temperature=0.2),
    },
    "property_tycoons": {
        "description": "Property tycoon specialized configuration",
        "config": lambda: create_property_tycoon_monopoly_config(enable_building=True),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_monopoly_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableMonopolyConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableMonopolyConfig: The example configuration

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
    print("🏠 Configurable Monopoly Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_monopoly_config("gpt-4o", "claude-3-opus")
    print(
        f"   Player 1: {config1.player_names[0] if hasattr(config1, 'player_names') and config1.player_names else 'Player 1'}"
    )
    print(
        f"   Player 2: {config1.player_names[1] if hasattr(config1, 'player_names') and len(config1.player_names) > 1 else 'Player 2'}"
    )
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_monopoly_config_from_example("real_estate_moguls")
    print(
        f"   Player 1: {config2.player_names[0] if hasattr(config2, 'player_names') and config2.player_names else 'Player 1'}"
    )
    print(
        f"   Player 2: {config2.player_names[1] if hasattr(config2, 'player_names') and len(config2.player_names) > 1 else 'Player 2'}"
    )
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Property tycoon configuration
    print("3️⃣ Property Tycoon Configuration:")
    config3 = create_property_tycoon_monopoly_config(enable_building=True)
    print(
        f"   Player 1: {config3.player_names[0] if hasattr(config3, 'player_names') and config3.player_names else 'Player 1'}"
    )
    print(
        f"   Player 2: {config3.player_names[1] if hasattr(config3, 'player_names') and len(config3.player_names) > 1 else 'Player 2'}"
    )
    print(f"   Building Enabled: {config3.enable_building}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Monopoly configurable system ready!")
