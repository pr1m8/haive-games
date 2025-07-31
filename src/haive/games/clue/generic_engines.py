"""Generic Clue engine creation using the generic player agent system.

This module provides generic engine creation functions for Clue games,
allowing for configurable LLM models and game-specific player
identifiers.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.clue.models import ClueGuess, ClueResponse
from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class CluePlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Clue game."""

    def __init__(self) -> None:
        super().__init__(player1="detective", player2="suspect")


class CluePromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Clue game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Clue player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Clue game. You are a detective in a Clue game. Your goal is to solve the mystery by determining who committed the murder, with what weapon, and in which room.\n\n"
                    "As a Clue player:\n"
                    "- Make strategic suggestions to gather information"
                    "- Track which cards other players have seen"
                    "- Use deductive reasoning to eliminate possibilities"
                    "- Pay attention to other players' reactions and responses"
                    "- Make accusations only when you're confident in the solution\n\n"
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
        """Create analysis prompt for Clue game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Clue strategist analyzing the current game state for {player}.\n\n"
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


class ClueEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Clue game engines."""

    def __init__(self) -> None:
        identifiers = CluePlayerIdentifiers()
        prompt_generator = CluePromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return ClueResponse
        return ClueGuess


# Factory instance
clue_factory = ClueEngineFactory()


def create_generic_clue_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Clue engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Clue engines

    Expected roles:
        - "detective_player": Player 1 configuration
        - "suspect_player": Player 2 configuration
        - "detective_analyzer": Player 1 analyzer configuration
        - "suspect_analyzer": Player 2 analyzer configuration
    """
    return clue_factory.create_engines(player_configs)


def create_generic_clue_engines_simple(
    detective_model: str, suspect_model: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Clue engines with simple model specifications.

    Args:
        detective_model: Model for detective and analyzer
        suspect_model: Model for suspect and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Clue engines
    """
    return create_engines_from_simple_configs(
        clue_factory, detective_model, suspect_model, temperature
    )


def create_generic_clue_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Clue engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Clue engines

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

    detective_model, suspect_model = examples[example_name]
    return create_generic_clue_engines_simple(
        detective_model, suspect_model, temperature
    )


# Convenience functions for common configurations


def create_advanced_clue_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create advanced Clue engines with high-powered models."""
    return create_generic_clue_config_from_example("advanced", **kwargs)


def create_budget_clue_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create budget-friendly Clue engines."""
    return create_generic_clue_config_from_example("budget", **kwargs)


def create_mixed_clue_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create mixed-provider Clue engines."""
    return create_generic_clue_config_from_example("mixed", **kwargs)
