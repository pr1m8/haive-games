"""Generic Mafia engine creation using the generic player agent system.

This module provides generic engine creation functions for Mafia games,
allowing for configurable LLM models and game-specific player identifiers.
"""

from langchain_core.prompts import ChatPromptTemplate

from .core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from .core.agent.player_agent import PlayerAgentConfig
from .engine.aug_llm import AugLLMConfig
from .mafia.models import (
    MafiaAction,
)


class MafiaPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Mafia game."""

    def __init__(self) -> None:
        super().__init__(player1="mafia", player2="town")


class MafiaPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Mafia game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Mafia player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Mafia game. You are playing Mafia. As mafia, eliminate town members; as town, identify and eliminate mafia.\n\n"
                    "As a Mafia player:\n"
                    "- Observe voting patterns and player behavior\n"
                    "- Use psychological tactics and misdirection\n"
                    "- Form strategic alliances when beneficial\n"
                    "- Analyze claims and counter-claims carefully\n"
                    "- Balance aggression with self-preservation\n\n"
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
        """Create analysis prompt for Mafia game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Mafia strategist analyzing the current game state for {player}.\n\n"
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


class MafiaEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Mafia game engines."""

    def __init__(self) -> None:
        identifiers = MafiaPlayerIdentifiers()
        prompt_generator = MafiaPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return MafiaAction
        return MafiaAction


# Factory instance
mafia_factory = MafiaEngineFactory()


def create_generic_mafia_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Mafia engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mafia engines

    Expected roles:
        - "mafia_player": Player 1 configuration
        - "town_player": Player 2 configuration
        - "mafia_analyzer": Player 1 analyzer configuration
        - "town_analyzer": Player 2 analyzer configuration
    """
    return mafia_factory.create_engines(player_configs)


def create_generic_mafia_engines_simple(
    mafia_model: str, town_model: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Mafia engines with simple model specifications.

    Args:
        mafia_model: Model for mafia and analyzer
        town_model: Model for town and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mafia engines
    """
    return create_engines_from_simple_configs(
        mafia_factory, mafia_model, town_model, temperature
    )


def create_generic_mafia_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Mafia engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mafia engines

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

    mafia_model, town_model = examples[example_name]
    return create_generic_mafia_engines_simple(mafia_model, town_model, temperature)


# Convenience functions for common configurations


def create_advanced_mafia_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create advanced Mafia engines with high-powered models."""
    return create_generic_mafia_config_from_example("advanced", **kwargs)


def create_budget_mafia_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create budget-friendly Mafia engines."""
    return create_generic_mafia_config_from_example("budget", **kwargs)


def create_mixed_mafia_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create mixed-provider Mafia engines."""
    return create_generic_mafia_config_from_example("mixed", **kwargs)
