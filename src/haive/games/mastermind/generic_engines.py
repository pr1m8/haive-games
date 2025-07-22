"""Generic Mastermind engine creation using the generic player agent system.

This module provides generic engine creation functions for Mastermind games,
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
from .mastermind.models import (
    MastermindAnalysis,
    MastermindGuess,
)


class MastermindPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Mastermind game."""

    def __init__(self) -> None:
        super().__init__(player1="codemaker", player2="codebreaker")


class MastermindPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Mastermind game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Mastermind player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Mastermind game. You are playing Mastermind. As codemaker, create a challenging code; as codebreaker, deduce the secret code.\n\n"
                    "As a Mastermind player:\n"
                    "- Use logical deduction to narrow down possibilities"
                    "- Choose guesses that maximize information gain"
                    "- Keep track of all feedback systematically"
                    "- Eliminate impossible combinations efficiently"
                    "- Balance exploration with exploitation of known information\n\n"
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
        """Create analysis prompt for Mastermind game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Mastermind strategist analyzing the current game state for {player}.\n\n"
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


class MastermindEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Mastermind game engines."""

    def __init__(self) -> None:
        identifiers = MastermindPlayerIdentifiers()
        prompt_generator = MastermindPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return MastermindAnalysis
        return MastermindGuess


# Factory instance
mastermind_factory = MastermindEngineFactory()


def create_generic_mastermind_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Mastermind engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mastermind engines

    Expected roles:
        - "codemaker_player": Player 1 configuration
        - "codebreaker_player": Player 2 configuration
        - "codemaker_analyzer": Player 1 analyzer configuration
        - "codebreaker_analyzer": Player 2 analyzer configuration
    """
    return mastermind_factory.create_engines(player_configs)


def create_generic_mastermind_engines_simple(
    codemaker_model: str, codebreaker_model: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Mastermind engines with simple model specifications.

    Args:
        codemaker_model: Model for codemaker and analyzer
        codebreaker_model: Model for codebreaker and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mastermind engines
    """
    return create_engines_from_simple_configs(
        mastermind_factory, codemaker_model, codebreaker_model, temperature
    )


def create_generic_mastermind_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Mastermind engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Mastermind engines

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

    codemaker_model, codebreaker_model = examples[example_name]
    return create_generic_mastermind_engines_simple(
        codemaker_model, codebreaker_model, temperature
    )


# Convenience functions for common configurations


def create_advanced_mastermind_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create advanced Mastermind engines with high-powered models."""
    return create_generic_mastermind_config_from_example("advanced", **kwargs)


def create_budget_mastermind_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create budget-friendly Mastermind engines."""
    return create_generic_mastermind_config_from_example("budget", **kwargs)


def create_mixed_mastermind_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create mixed-provider Mastermind engines."""
    return create_generic_mastermind_config_from_example("mixed", **kwargs)
