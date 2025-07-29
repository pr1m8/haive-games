"""Generic Tic Tac Toe engines using the new generic player agent system.

This module demonstrates how to use the generic player agent system for
Tic Tac Toe, showing the same pattern working across different games
with different player identifiers.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm import LLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.core.agent.generic_player_agent import (
    GenericGameEngineFactory,
    GenericPromptGenerator,
    TicTacToePlayerIdentifiers,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig
from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove


class TicTacToePromptGenerator(GenericPromptGenerator[str, str]):
    """Tic Tac Toe-specific prompt generator using the generic system."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create a Tic Tac Toe move prompt for the specified player.

        Args:
            player: Player symbol ("X" or "O")

        Returns:
            ChatPromptTemplate: Prompt template for move generation
        """
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are playing as {player} in a game of Tic Tac Toe. "
                    f"Your goal is to get three of your symbols in a row (horizontally, vertically, or diagonally).\n\n"
                    f"Rules:\n"
                    f"1. Players take turns placing their symbol (X or O) on the board.\n"
                    f"2. The first player to get three of their symbols in a row wins.\n"
                    f"3. If the board fills up with neither player getting three in a row, the game is a draw.",
                ),
                (
                    "human",
                    "Current Board:\n"
                    "{board_string}\n\n"
                    "It's your turn ({current_player}).\n\n"
                    "Legal moves (row, col):\n{legal_moves}\n\n"
                    "Previous analysis (if available):\n{player_analysis}\n\n"
                    "Choose one of the legal moves. Explain your reasoning and return a TicTacToeMove object with your row, col, and player.",
                ),
            ]
        )

    def create_analysis_prompt(self, player: str) -> ChatPromptTemplate:
        """Create a Tic Tac Toe analysis prompt for the specified player.

        Args:
            player: Player symbol ("X" or "O")

        Returns:
            ChatPromptTemplate: Prompt template for position analysis
        """
        opponent = "O" if player == "X" else "X"

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are a Tic Tac Toe strategy expert. Analyze the position from the perspective of player {player}.\n\n"
                    f"Key Tic Tac Toe concepts:\n"
                    f"- Win: Complete a line of three of your symbols\n"
                    f"- Block: Prevent your opponent from completing a line\n"
                    f"- Fork: Create two winning threats simultaneously\n"
                    f"- Center control: The center position (1,1) is strategically valuable\n"
                    f"- Corner play: Corner positions are more valuable than edge positions\n"
                    f"- Evaluate the position: Is it winning, losing, or drawing?\n",
                ),
                (
                    "human",
                    "Current Board:\n"
                    "{board_string}\n\n"
                    f"Player: {player}\n"
                    f"Opponent: {opponent}\n\n"
                    "Analyze this position. Consider the following:\n"
                    "1. Are there any immediate winning moves?\n"
                    "2. Are there any moves you need to make to block your opponent's win?\n"
                    "3. Can you create a fork (two simultaneous winning ways)?\n"
                    "4. What is the best strategic move?\n"
                    "5. Provide an overall evaluation of the position\n\n"
                    "Provide a detailed analysis including specific moves by coordinates (row, col) and your reasoning behind each one.",
                ),
            ]
        )

    def get_move_output_model(self) -> type:
        """Get the structured output model for Tic Tac Toe moves."""
        return TicTacToeMove

    def get_analysis_output_model(self) -> type:
        """Get the structured output model for Tic Tac Toe analysis."""
        return TicTacToeAnalysis


# Create the global Tic Tac Toe factory instance
ttt_players = TicTacToePlayerIdentifiers()  # player1="X", player2="O"
ttt_prompt_generator = TicTacToePromptGenerator(ttt_players)
ttt_engine_factory = GenericGameEngineFactory(
    ttt_players, ttt_prompt_generator, default_temperature=0.3, analyzer_temperature=0.2
)


# Convenience functions for Tic Tac Toe using the generic system


def create_generic_ttt_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Tic Tac Toe engines using the generic system.

    Args:
        player_configs: Dictionary of role name to player configuration

    Returns:
        dict[str, AugLLMConfig]: Dictionary of configured engines

    Example:
        >>> configs = {
        ...     "X_player": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "O_player": PlayerAgentConfig(llm_config="claude-3-opus"),
        ...     "X_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "O_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
        ... }
        >>> engines = create_generic_ttt_engines(configs)
    """
    return ttt_engine_factory.create_engines_from_player_configs(player_configs)


def create_generic_ttt_engines_simple(
    x_model: str | LLMConfig = "gpt-4o",
    o_model: str | LLMConfig = "claude-3-5-sonnet-20240620",
    temperature: float = 0.3,
    **kwargs,
) -> dict[str, AugLLMConfig]:
    """Create Tic Tac Toe engines with simple model configurations using
    generics.

    Args:
        x_model: Model for X player and analyzer
        o_model: Model for O player and analyzer
        temperature: Temperature for player engines
        **kwargs: Additional configuration parameters

    Returns:
        dict[str, AugLLMConfig]: Dictionary of engines

    Example:
        >>> engines = create_generic_ttt_engines_simple("gpt-4", "claude-3-opus")
        >>> engines = create_generic_ttt_engines_simple(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     temperature=0.5
        ... )
    """
    return ttt_engine_factory.create_engines_from_simple_configs(
        x_model, o_model, temperature=temperature, **kwargs
    )


def create_generic_ttt_config_from_example(
    example_name: str, temperature: float = 0.3
) -> dict[str, AugLLMConfig]:
    """Create Tic Tac Toe engines from predefined examples using generics.

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
    """
    example_configs = {
        "gpt_vs_claude": {
            "X": "openai:gpt-4o",
            "O": "anthropic:claude-3-5-sonnet-20240620",
        },
        "gpt_only": {"X": "openai:gpt-4o", "O": "openai:gpt-4o"},
        "claude_only": {
            "X": "anthropic:claude-3-5-sonnet-20240620",
            "O": "anthropic:claude-3-5-sonnet-20240620",
        },
        "budget": {"X": "openai:gpt-3.5-turbo", "O": "groq:llama-3.1-8b-instant"},
        "mixed": {"X": "openai:gpt-4o", "O": "anthropic:claude-3-opus"},
    }

    if example_name not in example_configs:
        available = ", ".join(example_configs.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    config = example_configs[example_name]
    return create_generic_ttt_engines_simple(
        config["X"], config["O"], temperature=temperature
    )


# Demonstrate the cross-game pattern


def compare_chess_vs_ttt_patterns():
    """Compare the chess vs tic-tac-toe patterns to show generalization.

    This function demonstrates how the same generic system works for
    different games with different player naming conventions.
    """
    print("🎯 Cross-Game Pattern Comparison")
    print("=" * 40)

    # Chess pattern
    print("♟️  Chess Pattern:")
    chess_engines = {
        "white_player": "White player moves",
        "black_player": "Black player moves",
        "white_analyzer": "White position analysis",
        "black_analyzer": "Black position analysis",
    }
    for role, desc in chess_engines.items():
        print(f"   {role}: {desc}")

    print()

    # Tic Tac Toe pattern
    print("⭕ Tic Tac Toe Pattern:")
    ttt_engines = {
        "X_player": "X player moves",
        "O_player": "O player moves",
        "X_analyzer": "X position analysis",
        "O_analyzer": "O position analysis",
    }
    for role, desc in ttt_engines.items():
        print(f"   {role}: {desc}")

    print()
    print("🔄 Same Generic Pattern:")
    print("   {player1}_player: First player moves")
    print("   {player2}_player: Second player moves")
    print("   {player1}_analyzer: First player analysis")
    print("   {player2}_analyzer: Second player analysis")

    print()
    print("✅ Type-safe player identifiers")
    print("✅ Consistent role structure")
    print("✅ Configurable LLM per role")
    print("✅ Cross-game compatibility")


# Advanced example: Multi-game configuration


def create_multi_game_comparison():
    """Create engines for multiple games to show the pattern.

    This demonstrates how the same configuration approach works across
    different games with the generic system.
    """
    print("\n🎮 Multi-Game Configuration Demonstration")
    print("=" * 50)

    # Same models, different games
    model1 = "openai:gpt-4o"
    model2 = "anthropic:claude-3-5-sonnet-20240620"

    # Chess engines
    from haive.games.chess.generic_engines import create_generic_chess_engines_simple

    chess_engines = create_generic_chess_engines_simple(model1, model2)

    # Tic Tac Toe engines
    ttt_engines = create_generic_ttt_engines_simple(model1, model2)

    print(f"🔧 Using models: {model1} vs {model2}")
    print()

    print("♟️  Chess roles:")
    for role in sorted(chess_engines.keys()):
        engine = chess_engines[role]
        model = getattr(engine.llm_config, "model", "unknown")
        print(f"   {role}: {model}")

    print()
    print("⭕ Tic Tac Toe roles:")
    for role in sorted(ttt_engines.keys()):
        engine = ttt_engines[role]
        model = getattr(engine.llm_config, "model", "unknown")
        print(f"   {role}: {model}")

    print()
    print("🎯 Benefits of Generic System:")
    print("   ✅ Same configuration API across all games")
    print("   ✅ Type safety prevents configuration errors")
    print("   ✅ Easy to add new games following the pattern")
    print("   ✅ No hardcoded LLM configurations")
    print("   ✅ Consistent role naming conventions")


if __name__ == "__main__":
    compare_chess_vs_ttt_patterns()
    create_multi_game_comparison()
