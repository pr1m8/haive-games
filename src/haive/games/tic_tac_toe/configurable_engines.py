"""Configurable Tic Tac Toe engines using the new player agent system.

This module provides Tic Tac Toe engine configurations that use configurable
player agents instead of hardcoded LLM configurations.
"""

from typing import Dict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.core.agent.player_agent import (
    GamePlayerRole,
    PlayerAgentConfig,
    PlayerAgentFactory,
)
from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove


def create_tic_tac_toe_move_prompt(player_symbol: str) -> ChatPromptTemplate:
    """Create a Tic Tac Toe move prompt for the specified player.

    Args:
        player_symbol: Player symbol ("X" or "O")

    Returns:
        ChatPromptTemplate: Prompt template for move generation
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are playing as {player_symbol} in a game of Tic Tac Toe. "
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


def create_tic_tac_toe_analysis_prompt(player_symbol: str) -> ChatPromptTemplate:
    """Create a Tic Tac Toe analysis prompt for the specified player.

    Args:
        player_symbol: Player symbol ("X" or "O")

    Returns:
        ChatPromptTemplate: Prompt template for position analysis
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are a Tic Tac Toe strategy expert. Analyze the position from the perspective of player {player_symbol}.\n\n"
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
                "Player: {player_symbol}\n"
                "Opponent: {opponent_symbol}\n\n"
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


def get_tic_tac_toe_role_definitions() -> Dict[str, GamePlayerRole]:
    """Get role definitions for Tic Tac Toe players and analyzers.

    Returns:
        Dict[str, GamePlayerRole]: Dictionary of role definitions
    """
    return {
        "X_player": GamePlayerRole(
            role_name="X_player",
            prompt_template=create_tic_tac_toe_move_prompt("X"),
            structured_output_model=TicTacToeMove,
            temperature=0.3,
            description="X player move generation",
        ),
        "O_player": GamePlayerRole(
            role_name="O_player",
            prompt_template=create_tic_tac_toe_move_prompt("O"),
            structured_output_model=TicTacToeMove,
            temperature=0.3,
            description="O player move generation",
        ),
        "X_analyzer": GamePlayerRole(
            role_name="X_analyzer",
            prompt_template=create_tic_tac_toe_analysis_prompt("X"),
            structured_output_model=TicTacToeAnalysis,
            temperature=0.2,
            description="X position analysis",
        ),
        "O_analyzer": GamePlayerRole(
            role_name="O_analyzer",
            prompt_template=create_tic_tac_toe_analysis_prompt("O"),
            structured_output_model=TicTacToeAnalysis,
            temperature=0.2,
            description="O position analysis",
        ),
    }


def create_configurable_tic_tac_toe_engines(
    player_configs: Dict[str, PlayerAgentConfig],
) -> Dict[str, AugLLMConfig]:
    """Create Tic Tac Toe engines from configurable player agents.

    Args:
        player_configs: Dictionary of role name to player configuration

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of configured engines

    Example:
        >>> configs = {
        ...     "X_player": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "O_player": PlayerAgentConfig(llm_config="claude-3-opus"),
        ...     "X_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "O_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
        ... }
        >>> engines = create_configurable_tic_tac_toe_engines(configs)
    """
    roles = get_tic_tac_toe_role_definitions()
    return PlayerAgentFactory.create_engines_from_player_configs(roles, player_configs)


# Convenience functions for common Tic Tac Toe configurations


def create_simple_tic_tac_toe_player_configs(
    x_model: str = "gpt-4o",
    o_model: str = "claude-3-5-sonnet-20240620",
    temperature: float = 0.3,
) -> Dict[str, PlayerAgentConfig]:
    """Create simple player configurations for Tic Tac Toe.

    Args:
        x_model: Model for X player
        o_model: Model for O player
        temperature: Temperature for both players

    Returns:
        Dict[str, PlayerAgentConfig]: Player configurations
    """
    return {
        "X_player": PlayerAgentConfig(
            llm_config=x_model, temperature=temperature, player_name="X Player"
        ),
        "O_player": PlayerAgentConfig(
            llm_config=o_model, temperature=temperature, player_name="O Player"
        ),
        "X_analyzer": PlayerAgentConfig(
            llm_config=x_model, temperature=0.2, player_name="X Analyzer"
        ),
        "O_analyzer": PlayerAgentConfig(
            llm_config=o_model, temperature=0.2, player_name="O Analyzer"
        ),
    }


def create_tic_tac_toe_engines_from_models(
    x_model: str = "gpt-4o",
    o_model: str = "claude-3-5-sonnet-20240620",
    temperature: float = 0.3,
) -> Dict[str, AugLLMConfig]:
    """Create Tic Tac Toe engines using simple model strings.

    Args:
        x_model: Model for X player and analyzer
        o_model: Model for O player and analyzer
        temperature: Temperature for all engines

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of engines
    """
    configs = create_simple_tic_tac_toe_player_configs(x_model, o_model, temperature)
    return create_configurable_tic_tac_toe_engines(configs)


# Example configurations for Tic Tac Toe

EXAMPLE_TTT_CONFIGS = {
    "gpt_vs_claude": lambda: create_tic_tac_toe_engines_from_models(
        "openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"
    ),
    "gpt_only": lambda: create_tic_tac_toe_engines_from_models("gpt-4o", "gpt-4o"),
    "claude_only": lambda: create_tic_tac_toe_engines_from_models(
        "claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20240620"
    ),
    "budget": lambda: create_tic_tac_toe_engines_from_models(
        "gpt-3.5-turbo", "groq:llama-3.1-8b-instant"
    ),
    "mixed": lambda: create_configurable_tic_tac_toe_engines(
        {
            "X_player": PlayerAgentConfig(llm_config="openai:gpt-4o", temperature=0.3),
            "O_player": PlayerAgentConfig(
                llm_config="anthropic:claude-3-opus", temperature=0.3
            ),
            "X_analyzer": PlayerAgentConfig(
                llm_config="google:gemini-1.5-pro", temperature=0.2
            ),
            "O_analyzer": PlayerAgentConfig(
                llm_config="groq:llama-3.1-70b-versatile", temperature=0.2
            ),
        }
    ),
}


def get_example_tic_tac_toe_engines(config_name: str) -> Dict[str, AugLLMConfig]:
    """Get example Tic Tac Toe engine configuration by name.

    Args:
        config_name: Name of the configuration from EXAMPLE_TTT_CONFIGS

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of engines

    Available configs: gpt_vs_claude, gpt_only, claude_only, budget, mixed
    """
    if config_name not in EXAMPLE_TTT_CONFIGS:
        available = ", ".join(EXAMPLE_TTT_CONFIGS.keys())
        raise ValueError(f"Unknown config '{config_name}'. Available: {available}")

    return EXAMPLE_TTT_CONFIGS[config_name]()
