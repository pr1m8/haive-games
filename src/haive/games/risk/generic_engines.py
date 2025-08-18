"""Generic Risk engine creation using the generic player agent system.

This module provides generic engine creation functions for Risk games, allowing for
configurable LLM models and game-specific player identifiers.

"""

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.core.agent.generic_player_agent import (
    GamePlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
    create_engines_from_simple_configs,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.risk.models import MoveType, RiskAnalysis


class RiskPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Risk game."""

    def __init__(self):
        """  Init  .
"""
        super().__init__(player1="player1", player2="player2")


class RiskPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Risk game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Risk player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Risk game. You are playing Risk. Your goal is to conquer territories and eliminate opponents.\n\n"
                    "As a Risk player:\n"
                    "- Secure continents for bonus reinforcements"
                    "- Control key strategic positions and chokepoints"
                    "- Balance expansion with defense"
                    "- Form and break alliances strategically"
                    "- Manage troop deployment and reinforcement efficiently\n\n"
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
        """Create analysis prompt for Risk game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Risk strategist analyzing the current game state for {player}.\n\n"
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


class RiskEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Risk game engines."""

    def __init__(self):
        """  Init  .
"""
        identifiers = RiskPlayerIdentifiers()
        prompt_generator = RiskPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return RiskAnalysis
        else:
            return MoveType


# Factory instance
risk_factory = RiskEngineFactory()


def create_generic_risk_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Risk engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Risk engines

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzer": Player 2 analyzer configuration

    """
    return risk_factory.create_engines(player_configs)


def create_generic_risk_engines_simple(
    player1_model: str, player2_model: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Risk engines with simple model specifications.

    Args:
        player1_model: Model for player1 and analyzer
        player2_model: Model for player2 and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Risk engines

    """
    return create_engines_from_simple_configs(
        risk_factory, player1_model, player2_model, temperature
    )


def create_generic_risk_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Risk engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Risk engines

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
    return create_generic_risk_engines_simple(player1_model, player2_model, temperature)


# Convenience functions for common configurations


def create_advanced_risk_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create advanced Risk engines with high-powered models."""
    return create_generic_risk_config_from_example("advanced", **kwargs)


def create_budget_risk_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create budget-friendly Risk engines."""
    return create_generic_risk_config_from_example("budget", **kwargs)


def create_mixed_risk_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create mixed-provider Risk engines."""
    return create_generic_risk_config_from_example("mixed", **kwargs)
