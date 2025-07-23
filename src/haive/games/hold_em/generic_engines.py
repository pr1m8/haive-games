"""Generic Hold'em engine creation using the generic player agent system.

This module provides generic engine creation functions for Texas Hold'em games,
allowing for configurable LLM models and game-specific player identifiers.
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
from haive.games.hold_em.models import (
    BettingDecision,
    PlayerDecisionModel,
    PokerAnalysis,
)


class HoldemPlayerIdentifiers(GamePlayerIdentifiers[str, str]):
    """Player identifiers for Texas Hold'em game."""

    def __init__(self) -> None:
        super().__init__(player1="player1", player2="player2")


class HoldemPromptGenerator(GenericPromptGenerator[str, str]):
    """Prompt generator for Texas Hold'em game."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create move prompt for Hold'em player."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are {player} in a Texas Hold'em poker game. Your goal is to make optimal betting decisions to maximize your winnings.\n\n"
                    "As a poker player:\n"
                    "- Analyze your hole cards and community cards\n"
                    "- Consider pot odds and implied odds\n"
                    "- Assess your position relative to other players\n"
                    "- Read opponent betting patterns and tendencies\n"
                    "- Manage your bankroll and betting strategy\n"
                    "- Adapt your play style based on table dynamics\n\n"
                    "Key poker strategies:\n"
                    "- Play tight-aggressive with premium hands\n"
                    "- Consider bluffing with semi-bluffs and position\n"
                    "- Use pot odds to make mathematical decisions\n"
                    "- Adjust strategy based on stack sizes\n"
                    "- Pay attention to betting patterns for tells\n"
                    "- Balance your range to avoid being predictable",
                ),
                (
                    "human",
                    "Current Game State:\n"
                    "{game_state}\n\n"
                    "Your Hole Cards:\n"
                    "{hole_cards}\n\n"
                    "Community Cards:\n"
                    "{community_cards}\n\n"
                    "Current Pot: ${pot_size}\n"
                    "Your Stack: ${your_stack}\n"
                    "Current Bet: ${current_bet}\n"
                    "Amount to Call: ${amount_to_call}\n\n"
                    "Betting History:\n"
                    "{betting_history}\n\n"
                    "Position: {position}\n"
                    "Players Remaining: {players_in_hand}\n\n"
                    "Make your betting decision. Consider your hand strength, position, pot odds, and opponent tendencies.",
                ),
            ]
        )

    def create_analyzer_prompt(self, player: str) -> ChatPromptTemplate:
        """Create analysis prompt for Hold'em game state."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an expert poker strategist analyzing the current game state for {player}.\n\n"
                    "Analyze the situation considering:\n"
                    "- Hand strength and potential draws\n"
                    "- Pot odds and implied odds\n"
                    "- Position and betting action\n"
                    "- Opponent playing styles and tendencies\n"
                    "- Stack sizes and ICM considerations\n"
                    "- Table dynamics and meta-game\n"
                    "- Optimal betting strategy and sizing\n"
                    "- Bluffing opportunities and fold equity",
                ),
                (
                    "human",
                    "Game State to Analyze:\n"
                    "{game_state}\n\n"
                    "Player Information:\n"
                    "{player_info}\n\n"
                    "Hand Analysis:\n"
                    "{hand_analysis}\n\n"
                    "Betting Action:\n"
                    "{betting_action}\n\n"
                    "Stack Information:\n"
                    "{stack_info}\n\n"
                    "Opponent Profiles:\n"
                    "{opponent_profiles}\n\n"
                    "Provide a comprehensive analysis of the position, "
                    "including hand strength assessment, optimal strategy, and expected value calculations.",
                ),
            ]
        )


class HoldemEngineFactory(GenericGameEngineFactory[str, str]):
    """Factory for creating Texas Hold'em game engines."""

    def __init__(self) -> None:
        identifiers = HoldemPlayerIdentifiers()
        prompt_generator = HoldemPromptGenerator()
        super().__init__(identifiers, prompt_generator)

    def get_structured_output_model(self, role: str) -> type:
        """Get the structured output model for a specific role."""
        if "analyzer" in role:
            return PokerAnalysis
        if "decision" in role:
            return BettingDecision
        return PlayerDecisionModel


# Factory instance
holdem_factory = HoldemEngineFactory()


def create_generic_holdem_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Hold'em engines from detailed player configurations.

    Args:
        player_configs: Dictionary mapping role names to player configurations

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Hold'em engines

    Expected roles:
        - "player1_player": Player 1 configuration
        - "player2_player": Player 2 configuration
        - "player1_analyzer": Player 1 analyzer configuration
        - "player2_analyzer": Player 2 analyzer configuration
    """
    return holdem_factory.create_engines(player_configs)


def create_generic_holdem_engines_simple(
    player1_model: str, player2_model: str, temperature: float = 0.4
) -> dict[str, AugLLMConfig]:
    """Create Hold'em engines with simple model specifications.

    Args:
        player1_model: Model for player 1 and analyzer
        player2_model: Model for player 2 and analyzer
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Hold'em engines
    """
    return create_engines_from_simple_configs(
        holdem_factory, player1_model, player2_model, temperature
    )


def create_generic_holdem_config_from_example(
    example_name: str, temperature: float = 0.4
) -> dict[str, AugLLMConfig]:
    """Create Hold'em engines from a predefined example configuration.

    Args:
        example_name: Name of the example configuration
        temperature: Generation temperature

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of Hold'em engines

    Available examples:
        - "gpt_vs_claude": GPT vs Claude
        - "gpt_only": GPT for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "poker_pros": High-powered models for strategic gameplay
        - "heads_up": Specialized for heads-up play
    """
    examples = {
        "gpt_vs_claude": ("gpt-4o", "claude-3-5-sonnet-20240620"),
        "gpt_only": ("gpt-4o", "gpt-4o"),
        "claude_only": ("claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"),
        "budget": ("gpt-3.5-turbo", "claude-3-haiku"),
        "mixed": ("gpt-4o", "claude-3-opus"),
        "poker_pros": ("gpt-4o", "claude-3-opus"),
        "heads_up": ("gpt-4o", "claude-3-5-sonnet-20240620"),
    }

    if example_name not in examples:
        available = ", ".join(examples.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    player1_model, player2_model = examples[example_name]
    return create_generic_holdem_engines_simple(
        player1_model, player2_model, temperature
    )


# Convenience functions for common configurations


def create_poker_pro_holdem_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create poker professional-style Hold'em engines with high-powered models."""
    return create_generic_holdem_config_from_example("poker_pros", **kwargs)


def create_budget_holdem_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create budget-friendly Hold'em engines."""
    return create_generic_holdem_config_from_example("budget", **kwargs)


def create_heads_up_holdem_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create specialized Hold'em engines for heads-up play."""
    return create_generic_holdem_config_from_example("heads_up", **kwargs)


def create_mixed_holdem_engines(**kwargs) -> dict[str, AugLLMConfig]:
    """Create mixed-provider Hold'em engines."""
    return create_generic_holdem_config_from_example("mixed", **kwargs)
