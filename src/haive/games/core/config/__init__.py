"""Core configuration system for games.

This module provides the base configuration classes and utilities
for creating flexible, configurable game agents.
"""

from haive.games.core.config.base import (
    BaseGameConfig,
    ConfigMode,
    GamePlayerRole,
    create_advanced_config,
    create_example_config,
    create_simple_config,
)

__all__ = [
    "BaseGameConfig",
    "ConfigMode",
    "GamePlayerRole",
    "create_simple_config",
    "create_example_config",
    "create_advanced_config",
]
