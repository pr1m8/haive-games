"""Generic Monopoly engine creation using the generic player agent system.

This module provides generic engine creation functions for Monopoly games,
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
from .monopoly.models import (
    BuildingDecision,
    JailDecision,
    PlayerAnalysis,
    PropertyDecision,
    TradeResponse,
)


class MonopolyPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Monopoly game."""

    def __init__(self) -> None:
        super().__init__(player1="player1", player2="player2")


class MonopolyPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Monopoly game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Monopoly player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Monopoly game. Your goal is to bankrupt other players by acquiring properties and building a real estate empire.\n\n"
                    "As a Monopoly player:\n"
                    "- Make strategic property purchases to build monopolies\n"
                    "- Manage your cash flow and avoid bankruptcy\n"
                    "- Negotiate trades to complete color groups\n"
                    "- Build houses and hotels to maximize rent income\n"
                    "- Consider mortgaging properties when cash is tight\n"
                    "- Use position and timing to your advantage\n\n"
                    "Key strategies:\n"
                    "- Focus on completing color groups for monopolies\n"
                    "- Orange and red properties have high landing probability\n"
                    "- Railroads provide steady income with low risk\n"
                    "- Build housing shortages to limit opponents\n"
                    "- Keep enough cash for rent payments and opportunities\n"
                    "- Trade wisely - avoid helping opponents more than yourself",
                ),
                (
                    "human",
                    "Current Game State:\n"
                    "{game_state}\n\n"
                    "Your Properties:\n"
                    "{your_properties}\n\n"
                    "Your Money: ${your_money}\n"
                    "Your Position: {your_position}\n\n"
                    "Property You Landed On:\n"
                    "{current_property}\n\n"
                    "Available Actions:\n"
                    "{available_actions}\n\n"
                    "Other Players:\n"
                    "{other_players}\n\n"
                    "Property Market:\n"
                    "{property_market}\n\n"
                    "Make your decision. Consider your financial position, strategic goals, and the potential return on investment.",
                ),
            ]
        )

    def create_analyzer_prompt(self, player: str) -> ChatPromptTemplate:
        """Create analysis prompt for Monopoly game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert Monopoly strategist analyzing the current game state for {player}.\n\n"
                    "Analyze the game considering:\n"
                    "- Property portfolio and monopoly potential\n"
                    "- Cash flow and financial stability\n"
                    "- Opponent positions and threats\n"
                    "- Market opportunities and risks\n"
                    "- Trading possibilities and negotiations\n"
                    "- Building strategies and housing market\n"
                    "- Endgame scenarios and winning conditions\n"
                    "- Risk management and bankruptcy avoidance",
                ),
                (
                    "human",
                    "Game State to Analyze:\n"
                    "{game_state}\n\n"
                    "Player Portfolio:\n"
                    "{player_portfolio}\n\n"
                    "Financial Status:\n"
                    "{financial_status}\n\n"
                    "Property Market:\n"
                    "{property_market}\n\n"
                    "Opponent Analysis:\n"
                    "{opponent_analysis}\n\n"
                    "Recent Transactions:\n"
                    "{recent_transactions}\n\n"
                    "Provide a comprehensive analysis of the position, "
                    "including strategic priorities, investment opportunities, and risk assessment.",
                ),
            ]
        )


class MonopolyEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Monopoly game engines."""

    def __init__(self) -> None:
        identifiers = MonopolyPlayerIdentifiers()
        prompt_generator = MonopolyPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return PlayerAnalysis
        if "property" in role:
            return PropertyDecision
        if "jail" in role:
            return JailDecision
        if "building" in role:
            return BuildingDecision
        if "trade" in role:
            return TradeResponse
        return PropertyDecision


# Factory instance
monopoly_factory = MonopolyEngineFactory()


def create_generic_monopoly_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Monopoly engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Monopoly engines

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzer": Player 2 analyzer configuration
    """
    return monopoly_factory.create_engines(player_configs)


def create_generic_monopoly_engines_simple(
    player1_model: str, player2_model: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Monopoly engines with simple model specifications.

    Args:
        player1_model: Model for player 1 and analyzer
        player2_model: Model for player 2 and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Monopoly engines
    """
    return create_engines_from_simple_configs(
        monopoly_factory, player1_model, player2_model, temperature
    )


def create_generic_monopoly_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Monopoly engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Monopoly engines

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "real_estate_moguls": High-powered models for strategic gameplay
        - "property_tycoons": Specialized for property investment
    """
    examples = {
        "gpt_vs_claude": ("gpt-4o", "claude-3-5-sonnet-20240620"),
        "gpt_only": ("gpt-4o", "gpt-4o"),
        "claude_only": ("claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"),
        "budget": ("gpt-3.5-turbo", "claude-3-haiku"),
        "mixed": ("gpt-4o", "claude-3-opus"),
        "real_estate_moguls": ("gpt-4o", "claude-3-opus"),
        "property_tycoons": ("gpt-4o", "claude-3-5-sonnet-20240620"),
    }

    if example_name not in examples:
        available = ", ".join(examples.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    player1_model, player2_model = examples[example_name]
    return create_generic_monopoly_engines_simple(
        player1_model, player2_model, temperature
    )


# Convenience functions for common configurations


def create_real_estate_mogul_monopoly_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create real estate mogul-style Monopoly engines with high-powered models."""
    return create_generic_monopoly_config_from_example("real_estate_moguls", **kwargs)


def create_budget_monopoly_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create budget-friendly Monopoly engines."""
    return create_generic_monopoly_config_from_example("budget", **kwargs)


def create_property_tycoon_monopoly_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create property tycoon-style Monopoly engines."""
    return create_generic_monopoly_config_from_example("property_tycoons", **kwargs)


def create_mixed_monopoly_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create mixed-provider Monopoly engines."""
    return create_generic_monopoly_config_from_example("mixed", **kwargs)
