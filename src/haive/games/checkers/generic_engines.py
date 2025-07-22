"""Generic Checkers engines using the new generic player agent system.

from typing import Any
This module demonstrates how to use the generic player agent system for Checkers,
showing the same pattern working across different games with different player identifiers.
"""

from langchain_core.prompts import ChatPromptTemplate

from .checkers.models import CheckersAnalysis, CheckersPlayerDecision
from .core.agent.generic_player_agent import (
    CheckersPlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
)
from .core.agent.player_agent import PlayerAgentConfig
from .engine.aug_llm import AugLLMConfig
from .models.llm import LLMConfig


class CheckersPromptGenerator(GenericPromptGenerator[str, str]):
    """Checkers-specific prompt generator using the generic system."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create a Checkers move prompt for the specified player.

        Args:
            player: Player color ("red" or "black")

        Returns:
            ChatPromptTemplate: Prompt template for move generation
        """
        player_upper = player.upper()

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are playing checkers as {player_upper}. You are an expert checkers player.\n\n"
                    f"Checkers Rules:\n"
                    f"1. Pieces move diagonally on dark squares only\n"
                    f"2. Regular pieces can only move forward\n"
                    f"3. Kings can move both forward and backward\n"
                    f"4. Captures are mandatory when available\n"
                    f"5. Multiple jumps must be taken if possible\n"
                    f"6. When a piece reaches the opposite end, it becomes a king\n\n"
                    f"Strategy Tips:\n"
                    f"- Control the center squares (d4, e4, d5, e5)\n"
                    f"- Advance pieces together to support each other\n"
                    f"- Look for forcing moves and tactics\n"
                    f"- Kings are more valuable than regular pieces\n"
                    f"- Edge pieces are safer but less active",
                ),
                (
                    "human",
                    "Current Board:\n"
                    "{board_representation}\n\n"
                    "It's your turn ({current_player}).\n\n"
                    "Legal moves:\n{legal_moves}\n\n"
                    "Move history:\n{move_history}\n\n"
                    "Previous analysis (if available):\n{player_analysis}\n\n"
                    f"As {player_upper}, analyze the position and choose your best move. "
                    f"Consider captures first (they are mandatory), then positional improvements. "
                    f"Explain your reasoning and return a CheckersPlayerDecision with your move choice.",
                ),
            ]
        )

    def create_analysis_prompt(self, player: str) -> ChatPromptTemplate:
        """Create a Checkers analysis prompt for the specified player.

        Args:
            player: Player color ("red" or "black")

        Returns:
            ChatPromptTemplate: Prompt template for position analysis
        """
        player_upper = player.upper()
        opponent = "BLACK" if player == "red" else "RED"

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are a checkers strategy expert. Analyze the position from the perspective of {player_upper}.\n\n"
                    f"Key Checkers Evaluation Factors:\n"
                    f"- Material count: Number of pieces for each side\n"
                    f"- King advantage: Kings vs regular pieces\n"
                    f"- Center control: Control of d4, e4, d5, e5 squares\n"
                    f"- Piece mobility: Number of available moves\n"
                    f"- Piece safety: Pieces under attack or defended\n"
                    f"- Advancement: How close pieces are to promotion\n"
                    f"- Tempo: Who has the initiative\n"
                    f"- Endgame factors: Opposition, key squares, breakthrough potential",
                ),
                (
                    "human",
                    "Current Board:\n"
                    "{board_representation}\n\n"
                    f"Player to analyze for: {player_upper}\n"
                    f"Opponent: {opponent}\n\n"
                    "Move history:\n{move_history}\n\n"
                    "Analyze this checkers position. Consider:\n"
                    "1. Material advantage: Count pieces and kings for both sides\n"
                    "2. Center control: Who controls the important central squares?\n"
                    "3. Piece mobility: Which side has more move options?\n"
                    "4. Safety: Are any pieces under attack or poorly defended?\n"
                    "5. Advancement: Which pieces are close to becoming kings?\n"
                    "6. Tactical opportunities: Are there any immediate captures or threats?\n"
                    "7. Strategic plans: What should the long-term plan be?\n\n"
                    "Provide specific move suggestions with coordinates (e.g., 'a3-b4', 'c5xd6') "
                    "and explain the reasoning behind each recommendation.",
                ),
            ]
        )

    def get_move_output_model(self) -> type:
        """Get the structured output model for Checkers moves."""
        return CheckersPlayerDecision

    def get_analysis_output_model(self) -> type:
        """Get the structured output model for Checkers analysis."""
        return CheckersAnalysis


# Create the global Checkers factory instance
checkers_players = CheckersPlayerIdentifiers()  # player1="red", player2="black"
checkers_prompt_generator = CheckersPromptGenerator(checkers_players)
checkers_engine_factory = GenericGameEngineFactory(
    checkers_players,
    checkers_prompt_generator,
    default_temperature=0.3,
    analyzer_temperature=0.2,
)


# Convenience functions for Checkers using the generic system


def create_generic_checkers_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Checkers engines using the generic system.

    Args:
        player_configs: Dictionary of role name to player configuration

    Returns:
        dict[str, AugLLMConfig]: Dictionary of configured engines

    Example:
        >>> configs = {
        ...     "red_player": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
        ...     "red_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
        ... }
        >>> engines = create_generic_checkers_engines(configs)
    """
    return checkers_engine_factory.create_engines_from_player_configs(player_configs)


def create_generic_checkers_engines_simple(
    red_model: str | LLMConfig = "gpt-4o",
    black_model: str | LLMConfig = "claude-3-5-sonnet-20240620",
    temperature: float = 0.3,
    **kwargs,
) -> dict[str, AugLLMConfig]:
    """Create Checkers engines with simple model configurations using generics.

    Args:
        red_model: Model for red player and analyzer
        black_model: Model for black player and analyzer
        temperature: Temperature for player engines
        **kwargs: Additional configuration parameters

    Returns:
        dict[str, AugLLMConfig]: Dictionary of engines

    Example:
        >>> engines = create_generic_checkers_engines_simple("gpt-4", "claude-3-opus")
        >>> engines = create_generic_checkers_engines_simple(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     temperature=0.5
        ... )
    """
    return checkers_engine_factory.create_engines_from_simple_configs(
        red_model, black_model, temperature=temperature, **kwargs
    )


def create_generic_checkers_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Checkers engines from predefined examples using generics.

    Args:
        example_name: Name of the example configuration
        temperature: Temperature for all engines

    Returns:
        dict[str, AugLLMConfig]: Dictionary of engines

    Available examples:
        - "gpt_vs_claude": GPT-4 vs Claude
        - "gpt_only": GPT-4 for both players
        - "claude_only": Claude for both players
        - "budget": Cost-effective models
        - "mixed": Different provider per role
        - "checkers_masters": High-powered models for competitive play
    """
    example_configs = {
        "gpt_vs_claude": {
            "red": "openai:gpt-4o",
            "black": "anthropic:claude-3-5-sonnet-20240620",
        },
        "gpt_only": {"red": "openai:gpt-4o", "black": "openai:gpt-4o"},
        "claude_only": {
            "red": "anthropic:claude-3-5-sonnet-20240620",
            "black": "anthropic:claude-3-5-sonnet-20240620",
        },
        "budget": {"red": "openai:gpt-3.5-turbo", "black": "groq:llama-3.1-8b-instant"},
        "mixed": {"red": "openai:gpt-4o", "black": "anthropic:claude-3-opus"},
        "checkers_masters": {
            "red": "openai:gpt-4o",
            "black": "anthropic:claude-3-5-sonnet-20240620",
        },
    }

    if example_name not in example_configs:
        available = ", ".join(example_configs.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    config = example_configs[example_name]
    return create_generic_checkers_engines_simple(
        config["red"], config["black"], temperature=temperature
    )


# Demonstrate the cross-game pattern


def compare_checkers_with_other_games() -> None:
    """Compare the checkers pattern with other games to show generalization.

    This function demonstrates how the same generic system works for
    different games with different player naming conventions.
    """
    # Chess pattern
    chess_engines = {
        "white_player": "White player moves",
        "black_player": "Black player moves",
        "white_analyzer": "White position analysis",
        "black_analyzer": "Black position analysis",
    }
    for _role, _desc in chess_engines.items():
        pass

    # Checkers pattern
    checkers_engines = {
        "red_player": "Red player moves",
        "black_player": "Black player moves",
        "red_analyzer": "Red position analysis",
        "black_analyzer": "Black position analysis",
    }
    for _role, _desc in checkers_engines.items():
        pass

    # Tic Tac Toe pattern
    ttt_engines = {
        "X_player": "X player moves",
        "O_player": "O player moves",
        "X_analyzer": "X position analysis",
        "O_analyzer": "O position analysis",
    }
    for _role, _desc in ttt_engines.items():
        pass


# Advanced example: Multi-game configuration


def create_multi_game_checkers_demo() -> Any:
    """Create engines for multiple games including checkers.

    This demonstrates how the same configuration approach works
    across different games with the generic system.
    """
    # Same models, different games
    model1 = "openai:gpt-4o"
    model2 = "anthropic:claude-3-5-sonnet-20240620"

    # Import other game engines for comparison
    try:
        from haive.games.chess.generic_engines import (
            create_generic_chess_engines_simple,
        )

        chess_engines = create_generic_chess_engines_simple(model1, model2)
        has_chess = True
    except ImportError:
        has_chess = False

    try:
        from haive.games.tic_tac_toe.generic_engines import (
            create_generic_ttt_engines_simple,
        )

        ttt_engines = create_generic_ttt_engines_simple(model1, model2)
        has_ttt = True
    except ImportError:
        has_ttt = False

    # Checkers engines
    checkers_engines = create_generic_checkers_engines_simple(model1, model2)

    if has_chess:
        for role in sorted(chess_engines.keys()):
            engine = chess_engines[role]
            getattr(engine.llm_config, "model", "unknown")

    for role in sorted(checkers_engines.keys()):
        engine = checkers_engines[role]
        getattr(engine.llm_config, "model", "unknown")

    if has_ttt:
        for role in sorted(ttt_engines.keys()):
            engine = ttt_engines[role]
            getattr(engine.llm_config, "model", "unknown")


if __name__ == "__main__":
    compare_checkers_with_other_games()
    create_multi_game_checkers_demo()
