"""Generic Mancala engine creation using the generic player agent system.

This module provides generic engine creation functions for Mancala
games, allowing for configurable LLM models and game-specific player
identifiers.
"""

from typing import Dict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.mancala.models import (
    MancalaAnalysis,
    MancalaMove,
)


class MancalaPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Mancala game."""

    def __init__(self):
        super().__init__(player1="player1", player2="player2")


class MancalaPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Mancala game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Mancala player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Mancala game. You are playing Mancala. Your goal is to capture more stones than your opponent.\n\n"
                    "As a Mancala player:\n"
                    "- Aim for extra turns by landing in your mancala"
                    "- Capture opponent's stones when possible"
                    "- Control the tempo of the game"
                    "- Plan sequences of moves for maximum effect"
                    "- Empty your side of the board at the right time\n\n"
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
        """Create analysis prompt for Mancala game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Mancala strategist analyzing the current game state for {player}.\n\n"
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


class MancalaEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Mancala game engines."""

    def __init__(self):
        identifiers = MancalaPlayerIdentifiers()
        prompt_generator = MancalaPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return MancalaAnalysis
        else:
            return MancalaMove


# Factory instance
mancala_factory = MancalaEngineFactory()


def create_generic_mancala_engines(
    player_configs: Dict[str, PlayerAgentConfig],
) -> Dict[str, AugLLMConfig]:
    """Create Mancala engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mancala engines

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzer": Player 2 analyzer configuration
    """
    return mancala_factory.create_engines(player_configs)


def create_generic_mancala_engines_simple(
    player1_model: str, player2_model: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Mancala engines with simple model specifications.

    Args:
        player1_model: Model for player1 and analyzer
        player2_model: Model for player2 and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mancala engines
    """
    return create_engines_from_simple_configs(
        mancala_factory, player1_model, player2_model, temperature
    )


def create_generic_mancala_config_from_example(
    example_name: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Mancala engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mancala engines

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

    player1_model, player2_model = examples[example_name]
    return create_generic_mancala_engines_simple(
        player1_model, player2_model, temperature
    )


# Convenience functions for common configurations


def create_advanced_mancala_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create advanced Mancala engines with high-powered models."""
    return create_generic_mancala_config_from_example("advanced", **kwargs)


def create_budget_mancala_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create budget-friendly Mancala engines."""
    return create_generic_mancala_config_from_example("budget", **kwargs)


def create_mixed_mancala_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create mixed-provider Mancala engines."""
    return create_generic_mancala_config_from_example("mixed", **kwargs)
