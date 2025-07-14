"""Generic Among Us engine creation using the generic player agent system.

This module provides generic engine creation functions for Among Us games,
allowing for configurable LLM models and game-specific player identifiers.
"""

from typing import Dict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.among_us.models import (
    AmongUsAnalysis,
    AmongUsPlayerDecision,
)
from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class AmongUsPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Among Us game."""

    def __init__(self):
        super().__init__(player1="crewmate", player2="impostor")


class AmongUsPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Among Us game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Among Us player."""
        if player == "crewmate":
            return ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are playing Among Us as a CREWMATE. Your goal is to complete all tasks and identify the impostors.\n\n"
                        "As a crewmate:\n"
                        "- Complete tasks to help your team win\n"
                        "- Watch for suspicious behavior from other players\n"
                        "- Share information during meetings to help identify impostors\n"
                        "- Vote strategically to eliminate impostors\n"
                        "- Be careful not to get eliminated by impostors\n\n"
                        "Key strategies:\n"
                        "- Stick with other players when possible\n"
                        "- Remember who you've seen doing visual tasks\n"
                        "- Pay attention to movement patterns\n"
                        "- Be honest and consistent in your statements",
                    ),
                    (
                        "human",
                        "Current Game State:\n"
                        "{game_state}\n\n"
                        "Available Actions:\n"
                        "{available_actions}\n\n"
                        "Recent Events:\n"
                        "{recent_events}\n\n"
                        "As a crewmate, what action do you want to take? "
                        "Explain your reasoning and provide your decision.",
                    ),
                ]
            )
        else:  # impostor
            return ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are playing Among Us as an IMPOSTOR. Your goal is to eliminate enough crewmates to win.\n\n"
                        "As an impostor:\n"
                        "- Sabotage systems to create chaos and opportunities\n"
                        "- Eliminate crewmates when you have the chance\n"
                        "- Use vents to move quickly and escape detection\n"
                        "- Blend in by pretending to do tasks\n"
                        "- Mislead crewmates during meetings\n"
                        "- Vote strategically to eliminate innocent players\n\n"
                        "Key strategies:\n"
                        "- Don't be too aggressive early on\n"
                        "- Create alibis by being seen in public areas\n"
                        "- Use sabotage to separate players\n"
                        "- Coordinate with other impostors if applicable\n"
                        "- Be convincing in your deception",
                    ),
                    (
                        "human",
                        "Current Game State:\n"
                        "{game_state}\n\n"
                        "Available Actions:\n"
                        "{available_actions}\n\n"
                        "Recent Events:\n"
                        "{recent_events}\n\n"
                        "Other Impostors: {other_impostors}\n\n"
                        "As an impostor, what action do you want to take? "
                        "Explain your reasoning and strategy.",
                    ),
                ]
            )

    def create_analyzer_prompt(self, player: str) -> ChatPromptTemplate:
        """Create analysis prompt for Among Us game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Among Us strategist analyzing the current game state from the perspective of {player}s.\n\n"
                    "Analyze the game from multiple perspectives:\n"
                    "- Task completion progress\n"
                    "- Player behavior patterns\n"
                    "- Voting patterns and alliances\n"
                    "- Suspicious activities\n"
                    "- Strategic opportunities\n"
                    "- Risk assessment",
                ),
                (
                    "human",
                    "Game State to Analyze:\n"
                    "{game_state}\n\n"
                    "Player History:\n"
                    "{player_history}\n\n"
                    "Voting History:\n"
                    "{voting_history}\n\n"
                    "Provide a comprehensive analysis of the current situation, "
                    "including risk assessments and strategic recommendations.",
                ),
            ]
        )


class AmongUsEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Among Us game engines."""

    def __init__(self):
        identifiers = AmongUsPlayerIdentifiers()
        prompt_generator = AmongUsPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return AmongUsAnalysis
        else:
            return AmongUsPlayerDecision


# Factory instance
among_us_factory = AmongUsEngineFactory()


def create_generic_among_us_engines(
    player_configs: Dict[str, PlayerAgentConfig],
) -> Dict[str, AugLLMConfig]:
    """Create Among Us engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Among Us engines

    Expected roles:
        - "crewmate_player": Crewmate player configuration
        - "impostor_player": Impostor player configuration
        - "crewmate_analyzer": Crewmate analyzer configuration
        - "impostor_analyzer": Impostor analyzer configuration
    """
    return among_us_factory.create_engines(player_configs)


def create_generic_among_us_engines_simple(
    crewmate_model: str, impostor_model: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Among Us engines with simple model specifications.

    Args:
        crewmate_model: Model for crewmate player and analyzer
        impostor_model: Model for impostor player and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Among Us engines
    """
    return create_engines_from_simple_configs(
        among_us_factory, crewmate_model, impostor_model, temperature
    )


def create_generic_among_us_config_from_example(
    example_name: str, temperature: float = 0.3
) -> Dict[str, AugLLMConfig]:
    """Create Among Us engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Among Us engines

    Available examples:
        - "gpt_vs_claude": GPT crewmate vs Claude impostor
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "detective_vs_mastermind": High-powered models for intense gameplay
    """
    examples = {
        "gpt_vs_claude": ("gpt-4o", "claude-3-5-sonnet-20240620"),
        "gpt_only": ("gpt-4o", "gpt-4o"),
        "claude_only": ("claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"),
        "budget": ("gpt-3.5-turbo", "claude-3-haiku"),
        "mixed": ("gpt-4o", "claude-3-opus"),
        "detective_vs_mastermind": ("gpt-4o", "claude-3-opus"),
    }

    if example_name not in examples:
        available = ", ".join(examples.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    crewmate_model, impostor_model = examples[example_name]
    return create_generic_among_us_engines_simple(
        crewmate_model, impostor_model, temperature
    )


# Convenience functions for common configurations


def create_detective_among_us_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create detective-style Among Us engines with high-powered models."""
    return create_generic_among_us_config_from_example(
        "detective_vs_mastermind", **kwargs
    )


def create_budget_among_us_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create budget-friendly Among Us engines."""
    return create_generic_among_us_config_from_example("budget", **kwargs)


def create_mixed_among_us_engines(**kwargs) -> Dict[str, AugLLMConfig]:
    """Create mixed-provider Among Us engines."""
    return create_generic_among_us_config_from_example("mixed", **kwargs)
