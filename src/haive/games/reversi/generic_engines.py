"""Generic Reversi engine creation using the generic player agent system.

This module provides generic engine creation functions for Reversi games,
allowing for configurable LLM models and game-specific player identifiers.
"""

from typing import Any, Dict, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.reversi.models import (
    ReversiAnalysis,
    ReversiMove,
)


class ReversiPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Reversi game."""

    def __init__(self):
        super().__init__(player1="black", player2="white")


class ReversiPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Reversi game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Reversi player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Reversi game. You are playing Reversi/Othello. Your goal is to have more discs of your color than your opponent when the board is full.\n\n"
                    "As a Reversi player:\n"
                    "- Control corners and edges for permanent positions"
                    "- Minimize opponent's mobility when possible"
                    "- Plan for the late game when few moves remain"
                    "- Sacrifice pieces temporarily for positional advantage"
                    "- Count and evaluate potential moves carefully\n\n"
                    "Key strategies:\n"
                    "- Think several moves ahead\n"
                    "- Adapt your strategy based on game state\n"
                    "- Make calculated decisions\n"
                    "- Learn from opponent's patterns\n"
                    "- Stay focused on your win condition",
                ),
                (
                    "human",
                    "Current Game State:\n"
                    "{game_state}\n\n"
                    "Game History:\n"
                    "{game_history}\n\n"
                    "Available Actions:\n"
                    "{available_actions}\n\n"
                    "Make your next move. Analyze the position and choose your action carefully.",
                ),
            ]
        )

    def create_analyzer_prompt(self, player: str) -> ChatPromptTemplate:
        """Create analysis prompt for Reversi game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Reversi strategist analyzing the current game state for {player}.\n\n"
                    "Analyze the game considering:\n"
                    "- Current position and opportunities\n"
                    "- Strategic advantages and disadvantages\n"
                    "- Potential moves and their consequences\n"
                    "- Opponent's possible strategies\n"
                    "- Risk assessment and probability\n"
                    "- Optimal decision-making",
                ),
                (
                    "human",
                    "Game State to Analyze:\n"
                    "{game_state}\n\n"
                    "Player Status:\n"
                    "{player_status}\n\n"
                    "Game History:\n"
                    "{game_history}\n\n"
                    "Current Situation:\n"
                    "{current_situation}\n\n"
                    "Provide a comprehensive analysis of the position, "
                    "including strategic recommendations and tactical considerations.",
                ),
            ]
        )


class ReversiEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Reversi game engines."""

    def __init__(self):
        identifiers = ReversiPlayerIdentifiers()
        prompt_generator = ReversiPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return ReversiAnalysis
        else:
            return ReversiMove


# Factory instance
reversi_factory = ReversiEngineFactory()


def create_generic_reversi_engines(
    player_configs: Dict[str, PlayerAgentConfig],
) -> Dict[str, AugLLMConfig]:
    """Create Reversi engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Reversi engines

    Expected roles:
        - "black_player": Player 1 configuration
        - "white_player": Player 2 configuration
        - "black_analyzer": Player 1 analyzer configuration
        - "white_analyzer": Player 2 analyzer configuration
    """
    return reversi_factory.create_engines(player_configs)


def create_generic_reversi_engines_simple(
    black_model: str, white_model: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Reversi engines with simple model specifications.

    Args:
        black_model: Model for black and analyzer
        white_model: Model for white and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Reversi engines
    """
    return create_engines_from_simple_configs(
        reversi_factory, black_model, white_model, temperature
    )


def create_generic_reversi_config_from_example(
    example_name: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Reversi engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Reversi engines

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "advanced": High-powered models for strategic gameplay
    """
    examples = {
        "gpt_vs_claude": ("gpt-4o", "claude-3-5-sonnet-20240620"),
        "gpt_only": ("gpt-4o", "gpt-4o"),
        "claude_only": ("claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"),
        "budget": ("gpt-3.5-turbo", "claude-3-haiku"),
        "mixed": ("gpt-4o", "claude-3-opus"),
        "advanced": ("gpt-4o", "claude-3-opus"),
    }

    if example_name not in examples:
        available = ", ".join(examples.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    black_model, white_model = examples[example_name]
    return create_generic_reversi_engines_simple(black_model, white_model, temperature)


# Convenience functions for common configurations


def create_advanced_reversi_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create advanced Reversi engines with high-powered models."""
    return create_generic_reversi_config_from_example("advanced", **kwargs)


def create_budget_reversi_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create budget-friendly Reversi engines."""
    return create_generic_reversi_config_from_example("budget", **kwargs)


def create_mixed_reversi_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create mixed-provider Reversi engines."""
    return create_generic_reversi_config_from_example("mixed", **kwargs)
