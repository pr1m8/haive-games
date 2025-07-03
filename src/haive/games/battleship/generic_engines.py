"""Generic Battleship engine creation using the generic player agent system.

This module provides generic engine creation functions for Battleship games,
allowing for configurable LLM models and game-specific player identifiers.
"""

from typing import Any, Dict, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.battleship.models import (
    Analysis,
    MoveCommand,
    ShipPlacementWrapper,
)
from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class BattleshipPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Battleship game."""

    def __init__(self):
        super().__init__(player1="player1", player2="player2")


class BattleshipPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Battleship game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Battleship player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Battleship game. Your goal is to sink all of your opponent's ships.\n\n"
                    "As a Battleship player:\n"
                    "- Make strategic attacks to find and sink enemy ships\n"
                    "- Use hit patterns to locate adjacent ship segments\n"
                    "- Remember previous hits and misses\n"
                    "- Think systematically about ship placement patterns\n"
                    "- Use probability and logic to make optimal moves\n\n"
                    "Key strategies:\n"
                    "- After hitting a ship, check adjacent squares\n"
                    "- Ships are placed horizontally or vertically only\n"
                    "- Use checkerboard patterns for initial searching\n"
                    "- Focus fire on areas where large ships can fit\n"
                    "- Eliminate impossible positions based on previous hits",
                ),
                (
                    "human",
                    "Current Game State:\n"
                    "{game_state}\n\n"
                    "Your Board (Ships and Hits Received):\n"
                    "{your_board}\n\n"
                    "Opponent's Board (Your Attacks):\n"
                    "{opponent_board}\n\n"
                    "Attack History:\n"
                    "{attack_history}\n\n"
                    "Make your next attack. Choose coordinates to attack and explain your strategy.",
                ),
            ]
        )

    def create_analyzer_prompt(self, player: str) -> ChatPromptTemplate:
        """Create analysis prompt for Battleship game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Battleship strategist analyzing the current game state for {player}.\n\n"
                    "Analyze the game considering:\n"
                    "- Current ship positions and damage\n"
                    "- Attack patterns and hit probability\n"
                    "- Remaining ship possibilities\n"
                    "- Strategic attack priorities\n"
                    "- Risk assessment\n"
                    "- Optimal target selection",
                ),
                (
                    "human",
                    "Game State to Analyze:\n"
                    "{game_state}\n\n"
                    "Player Board Status:\n"
                    "{player_board}\n\n"
                    "Attack History:\n"
                    "{attack_history}\n\n"
                    "Ship Status:\n"
                    "{ship_status}\n\n"
                    "Provide a comprehensive analysis of the position, "
                    "including target priorities and strategic recommendations.",
                ),
            ]
        )


class BattleshipEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Battleship game engines."""

    def __init__(self):
        identifiers = BattleshipPlayerIdentifiers()
        prompt_generator = BattleshipPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return Analysis
        else:
            return MoveCommand


# Factory instance
battleship_factory = BattleshipEngineFactory()


def create_generic_battleship_engines(
    player_configs: Dict[str, PlayerAgentConfig],
) -> Dict[str, AugLLMConfig]:
    """Create Battleship engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Battleship engines

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzer": Player 2 analyzer configuration
    """
    return battleship_factory.create_engines(player_configs)


def create_generic_battleship_engines_simple(
    player1_model: str, player2_model: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Battleship engines with simple model specifications.

    Args:
        player1_model: Model for player 1 and analyzer
        player2_model: Model for player 2 and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Battleship engines
    """
    return create_engines_from_simple_configs(
        battleship_factory, player1_model, player2_model, temperature
    )


def create_generic_battleship_config_from_example(
    example_name: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Battleship engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Battleship engines

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "naval_commanders": High-powered models for strategic gameplay
    """
    examples = {
        "gpt_vs_claude": ("gpt-4o", "claude-3-5-sonnet-20240620"),
        "gpt_only": ("gpt-4o", "gpt-4o"),
        "claude_only": ("claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"),
        "budget": ("gpt-3.5-turbo", "claude-3-haiku"),
        "mixed": ("gpt-4o", "claude-3-opus"),
        "naval_commanders": ("gpt-4o", "claude-3-opus"),
    }

    if example_name not in examples:
        available = ", ".join(examples.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    player1_model, player2_model = examples[example_name]
    return create_generic_battleship_engines_simple(
        player1_model, player2_model, temperature
    )


# Convenience functions for common configurations


def create_naval_battleship_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create naval commander-style Battleship engines with high-powered models."""
    return create_generic_battleship_config_from_example("naval_commanders", **kwargs)


def create_budget_battleship_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create budget-friendly Battleship engines."""
    return create_generic_battleship_config_from_example("budget", **kwargs)


def create_mixed_battleship_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create mixed-provider Battleship engines."""
    return create_generic_battleship_config_from_example("mixed", **kwargs)
