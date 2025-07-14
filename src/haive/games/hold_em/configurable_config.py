"""Configurable Hold'em configuration using the generic player agent system.

This module provides configurable Texas Hold'em game configurations that replace
hardcoded LLM settings with dynamic, configurable player agents.
"""

<<<<<<< Updated upstream
from typing import Any, Dict, Optional, Union

=======
import logging
from typing import Any, Dict, Optional

>>>>>>> Stashed changes

from pydantic import BaseModel, Field

from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.hold_em.config import HoldemGameAgentConfig
from haive.games.hold_em.generic_engines import (
    create_generic_holdem_config_from_example,
    create_generic_holdem_engines,
    create_generic_holdem_engines_simple,
)

logger = logging.getLogger(__name__)


class ConfigurableHoldemConfig(HoldemGameAgentConfig):
    """Configurable Hold'em configuration with dynamic LLM selection.

    This configuration allows users to specify different LLMs for different
    roles in the Texas Hold'em game, providing flexibility and avoiding hardcoded models.

    Attributes:
        player1_model: Model for player 1 (can be string or LLMConfig)
        player2_model: Model for player 2 (can be string or LLMConfig)
        player1_name: Name for player 1
        player2_name: Name for player 2
        example_config: Optional example configuration name
        player_configs: Optional detailed player configurations
        temperature: Temperature for LLM generation
        enable_analysis: Whether to enable strategic analysis
        heads_up_mode: Whether this is heads-up play
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
        default=0.4, description="Temperature for LLM generation"
    )
    heads_up_mode: bool = Field(
        default=False, description="Whether this is heads-up play"
    )
    recursion_limit: int = Field(default=500, description="Python recursion limit")

    def model_post_init(self, __context: Any) -> None:
        """Initialize engines after model creation."""
        super().model_post_init(__context)

        # Create engines based on configuration method
        if self.player_configs:
            # Method 1: Use detailed player configurations
            self.engines = create_generic_holdem_engines(self.player_configs)
            self._extract_player_names_from_configs()

        elif self.example_config:
            # Method 2: Use example configuration
            self.engines = create_generic_holdem_config_from_example(
                self.example_config, temperature=self.temperature
            )
            self._generate_player_names_from_example()

        else:
            # Method 3: Use simple model specifications (default)
            player1_model = self.player1_model or "gpt-4o"
            player2_model = self.player2_model or "claude-3-5-sonnet-20240620"

            self.engines = create_generic_holdem_engines_simple(
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
                else "Player 1"
            )
            self.player2_name = (
                player2_config.player_name
                if player2_config and player2_config.player_name
                else "Player 2"
            )

    def _generate_player_names_from_example(self):
        """Generate player names based on example configuration."""
        example_names = {
            "gpt_vs_claude": ("GPT Pro", "Claude Shark"),
            "gpt_only": ("GPT Player 1", "GPT Player 2"),
            "claude_only": ("Claude Player 1", "Claude Player 2"),
            "budget": ("Budget Player 1", "Budget Player 2"),
            "mixed": ("Mixed Player 1", "Mixed Player 2"),
            "poker_pros": ("Poker Pro", "High Roller"),
            "heads_up": ("Heads-Up Specialist", "1v1 Expert"),
        }

        if self.example_config in example_names:
            self.player1_name, self.player2_name = example_names[self.example_config]
        else:
            self.player1_name = f"{self.example_config} Player 1"
            self.player2_name = f"{self.example_config} Player 2"

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

        self.player1_name = self.player1_name or f"{model_to_name(player1_model)} Pro"
        self.player2_name = self.player2_name or f"{model_to_name(player2_model)} Shark"


def create_holdem_config(
    player1_model: str = "gpt-4o",
    player2_model: str = "claude-3-5-sonnet-20240620",
    **kwargs,
) -> ConfigurableHoldemConfig:
    """Create a configurable Hold'em configuration with simple model specifications.

    Args:
        player1_model: Model for player 1 and analyzer
        player2_model: Model for player 2 and analyzer
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableHoldemConfig: Configured Hold'em game

    Example:
        >>> config = create_holdem_config("gpt-4o", "claude-3-opus", temperature=0.5)
        >>> config = create_holdem_config(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     heads_up_mode=True
        ... )
    """
    return ConfigurableHoldemConfig(
        player1_model=player1_model, player2_model=player2_model, **kwargs
    )


def create_holdem_config_from_example(
    example_name: str, **kwargs
) -> ConfigurableHoldemConfig:
    """Create a configurable Hold'em configuration from a predefined example.

    Args:
        example_name: Name of the example configuration
        **kwargs: Additional configuration parameters to override

    Returns:
        ConfigurableHoldemConfig: Configured Hold'em game

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "poker_pros": High-powered models for strategic gameplay
        - "heads_up": Specialized for heads-up play

    Example:
        >>> config = create_holdem_config_from_example("budget", temperature=0.3)
        >>> config = create_holdem_config_from_example("poker_pros", heads_up_mode=True)
    """
    return ConfigurableHoldemConfig(example_config=example_name, **kwargs)


def create_holdem_config_from_player_configs(
    player_configs: Dict[str, PlayerAgentConfig], **kwargs
) -> ConfigurableHoldemConfig:
    """Create a configurable Hold'em configuration from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations
        **kwargs: Additional configuration parameters

    Returns:
        ConfigurableHoldemConfig: Configured Hold'em game

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
        ...         player_name="Poker Pro"
        ...     ),
        ...     "player2_player": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.3,
        ...         player_name="Card Shark"
        ...     ),
        ...     "player1_analyzer": PlayerAgentConfig(
        ...         llm_config="gpt-4o",
        ...         temperature=0.2,
        ...         player_name="Strategic Analyst"
        ...     ),
        ...     "player2_analyzer": PlayerAgentConfig(
        ...         llm_config="claude-3-opus",
        ...         temperature=0.2,
        ...         player_name="Game Theory Expert"
        ...     ),
        ... }
        >>> config = create_holdem_config_from_player_configs(player_configs)
    """
    return ConfigurableHoldemConfig(player_configs=player_configs, **kwargs)


# Convenience functions for common configurations


def create_budget_holdem_config(**kwargs) -> ConfigurableHoldemConfig:
    """Create a budget-friendly Hold'em configuration."""
    return create_holdem_config_from_example("budget", **kwargs)


def create_poker_pro_holdem_config(**kwargs) -> ConfigurableHoldemConfig:
    """Create a poker professional-style Hold'em configuration with powerful models."""
    return create_holdem_config_from_example("poker_pros", **kwargs)


def create_heads_up_holdem_config(**kwargs) -> ConfigurableHoldemConfig:
    """Create a heads-up specialized Hold'em configuration."""
    return create_holdem_config_from_example("heads_up", heads_up_mode=True, **kwargs)


def create_experimental_holdem_config(**kwargs) -> ConfigurableHoldemConfig:
    """Create an experimental Hold'em configuration with mixed providers."""
    return create_holdem_config_from_example("mixed", **kwargs)


# Example configurations for testing and development

EXAMPLE_CONFIGURATIONS = {
    "simple": {
        "description": "Simple GPT vs Claude setup",
        "config": lambda: create_holdem_config("gpt-4o", "claude-3-opus"),
    },
    "budget": {
        "description": "Cost-effective configuration",
        "config": lambda: create_budget_holdem_config(temperature=0.3),
    },
    "poker_pros": {
        "description": "High-performance poker professional setup",
        "config": lambda: create_poker_pro_holdem_config(temperature=0.2),
    },
    "heads_up": {
        "description": "Specialized heads-up configuration",
        "config": lambda: create_heads_up_holdem_config(temperature=0.4),
    },
    "experimental": {
        "description": "Mixed providers and settings",
        "config": lambda: create_experimental_holdem_config(temperature=0.5),
    },
}


def get_example_config(name: str) -> ConfigurableHoldemConfig:
    """Get a predefined example configuration by name.

    Args:
        name: Name of the example configuration

    Returns:
        ConfigurableHoldemConfig: The example configuration

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
    # Note: Using print for demo output (user-facing console application)
    print("🎰 Configurable Hold'em Configuration Demo")
    print("=" * 50)

    # Example 1: Simple configuration
    print("1️⃣ Simple Configuration:")
    config1 = create_holdem_config("gpt-4o", "claude-3-opus")
    print(f"   Player 1: {config1.player1_name}")
    print(f"   Player 2: {config1.player2_name}")
    print(f"   Engines: {len(config1.engines)}")
    print()

    # Example 2: Example configuration
    print("2️⃣ Example Configuration:")
    config2 = create_holdem_config_from_example("poker_pros")
    print(f"   Player 1: {config2.player1_name}")
    print(f"   Player 2: {config2.player2_name}")
    print(f"   Example: {config2.example_config}")
    print()

    # Example 3: Heads-up configuration
    print("3️⃣ Heads-Up Configuration:")
    config3 = create_heads_up_holdem_config(temperature=0.3)
    print(f"   Player 1: {config3.player1_name}")
    print(f"   Player 2: {config3.player2_name}")
    print(f"   Heads-Up Mode: {config3.heads_up_mode}")
    print()

    # List available examples
    print("4️⃣ Available Examples:")
    examples = list_example_configurations()
    for name, desc in examples.items():
        print(f"   {name}: {desc}")
    print()

    print("✅ Hold'em configurable system ready!")
