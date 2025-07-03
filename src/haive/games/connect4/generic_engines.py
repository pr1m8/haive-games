"""Generic Connect4 engines using the new generic player agent system.

This module demonstrates how to use the generic player agent system for Connect4,
showing the same pattern working with red/yellow player identifiers.
"""

from typing import Type, Union

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm import LLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.connect4.models import Connect4Analysis, Connect4PlayerDecision
from haive.games.core.agent.generic_player_agent import (
    Connect4PlayerIdentifiers,
    GenericGameEngineFactory,
    GenericPromptGenerator,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class Connect4PromptGenerator(GenericPromptGenerator[str, str]):
    """Connect4-specific prompt generator using the generic system."""

    def create_move_prompt(self, player: str) -> ChatPromptTemplate:
        """Create a Connect4 move prompt for the specified player.

        Args:
            player: Player color ("red" or "yellow")

        Returns:
            ChatPromptTemplate: Prompt template for move generation
        """
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are the {player} player in a game of Connect 4. Your goal is to connect four of your pieces in a row, column, or diagonal. "
                    "Choose the best column to drop your piece.",
                ),
                (
                    "human",
                    "Game Board:\n{board}\n\n"
                    f"You are playing as {player}. It's {'your' if '{{turn}}' == '{player}' else 'not your'} turn.\n\n"
                    "Legal Moves Available:\n{legal_moves}\n\n"
                    "Threats:\n- Winning moves: {threats_winning_moves}\n- Blocking needed: {threats_blocking_moves}\n\n"
                    "Recent Moves:\n{move_history}\n\n"
                    "Your Analysis: {player_analysis}\n\n"
                    f"Select the best column (0-6) for {player}. Provide your reasoning.",
                ),
            ]
        )

    def create_analysis_prompt(self, player: str) -> ChatPromptTemplate:
        """Create a Connect4 analysis prompt for the specified player.

        Args:
            player: Player color ("red" or "yellow")

        Returns:
            ChatPromptTemplate: Prompt template for position analysis
        """
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are a Connect 4 strategy expert, analyzing the board from {player}'s perspective. "
                    "Your objective is to provide a structured evaluation of the current position, including scoring, threats, and strategy recommendations.",
                ),
                (
                    "human",
                    "🔷 **Game Board State:**\n{board}\n\n"
                    f"🎮 **You are playing as {player}.** It's {'your' if '{{turn}}' == '{player}' else 'not your'} turn.\n\n"
                    "📊 **Threats Analysis:**\n"
                    "- **Winning Moves:** {threats_winning_moves}\n"
                    "- **Blocking Moves:** {threats_blocking_moves}\n\n"
                    "🛠 **Board Control Insights:**\n"
                    "- **Column Usage:** {columns_usage} (Number of pieces in each column)\n\n"
                    "🔄 **Recent Move History:**\n{move_history}\n\n"
                    "📈 **Provide a structured analysis including:**\n"
                    "1️⃣ **Position Score:** Evaluate the position from -10 (very bad) to +10 (very strong).\n"
                    "2️⃣ **Threat Assessment:** Identify immediate threats, three-in-a-row opportunities, and opponent weaknesses.\n"
                    "3️⃣ **Center Control:** Rate control of central columns (0-10, where 10 is perfect control of columns 3 and 4).\n"
                    "4️⃣ **Suggested Columns:** List columns in priority order for the best move.\n"
                    "5️⃣ **Defensive Recommendations:** Highlight if defensive play is necessary and where.\n"
                    "6️⃣ **Winning Probability:** Estimate the likelihood of winning (0-100%).\n\n"
                    "📝 **Output structured response following this format:**\n"
                    "{{ \n"
                    '  "position_score": <int>,\n'
                    '  "center_control": <int>,\n'
                    '  "suggested_columns": [<list of column indices>],\n'
                    '  "winning_chances": <int>,\n'
                    '  "threats": {{ \n'
                    '    "winning_moves": [<list of columns>],\n'
                    '    "blocking_moves": [<list of columns>]\n'
                    "  }},\n"
                    "}}",
                ),
            ]
        )

    def get_move_output_model(self) -> Type:
        """Get the structured output model for Connect4 moves."""
        return Connect4PlayerDecision

    def get_analysis_output_model(self) -> Type:
        """Get the structured output model for Connect4 analysis."""
        return Connect4Analysis


# Create the global Connect4 factory instance
connect4_players = Connect4PlayerIdentifiers()  # player1="red", player2="yellow"
connect4_prompt_generator = Connect4PromptGenerator(connect4_players)
connect4_engine_factory = GenericGameEngineFactory(
    connect4_players,
    connect4_prompt_generator,
    default_temperature=0.7,
    analyzer_temperature=0.3,
)


# Convenience functions for Connect4 using the generic system


def create_generic_connect4_engines(
    player_configs: dict[str, PlayerAgentConfig],
) -> dict[str, AugLLMConfig]:
    """Create Connect4 engines using the generic system.

    Args:
        player_configs: Dictionary of role name to player configuration

    Returns:
        dict[str, AugLLMConfig]: Dictionary of configured engines

    Example:
        >>> configs = {
        ...     "red_player": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "yellow_player": PlayerAgentConfig(llm_config="claude-3-opus"),
        ...     "red_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
        ...     "yellow_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
        ... }
        >>> engines = create_generic_connect4_engines(configs)
    """
    return connect4_engine_factory.create_engines_from_player_configs(player_configs)


def create_generic_connect4_engines_simple(
    red_model: Union[str, LLMConfig] = "gpt-4o",
    yellow_model: Union[str, LLMConfig] = "claude-3-5-sonnet-20240620",
    temperature: float = 0.7,
    **kwargs,
) -> dict[str, AugLLMConfig]:
    """Create Connect4 engines with simple model configurations using generics.

    Args:
        red_model: Model for red player and analyzer
        yellow_model: Model for yellow player and analyzer
        temperature: Temperature for player engines
        **kwargs: Additional configuration parameters

    Returns:
        dict[str, AugLLMConfig]: Dictionary of engines

    Example:
        >>> engines = create_generic_connect4_engines_simple("gpt-4", "claude-3-opus")
        >>> engines = create_generic_connect4_engines_simple(
        ...     "openai:gpt-4o",
        ...     "anthropic:claude-3-5-sonnet-20240620",
        ...     temperature=0.8
        ... )
    """
    return connect4_engine_factory.create_engines_from_simple_configs(
        red_model, yellow_model, temperature=temperature, **kwargs
    )


def create_generic_connect4_config_from_example(
    example_name: str, temperature: float = 0.7
) -> dict[str, AugLLMConfig]:
    """Create Connect4 engines from predefined examples using generics.

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
            "red": "openai:gpt-4o",
            "yellow": "anthropic:claude-3-5-sonnet-20240620",
        },
        "gpt_only": {"red": "openai:gpt-4o", "yellow": "openai:gpt-4o"},
        "claude_only": {
            "red": "anthropic:claude-3-5-sonnet-20240620",
            "yellow": "anthropic:claude-3-5-sonnet-20240620",
        },
        "budget": {
            "red": "openai:gpt-3.5-turbo",
            "yellow": "groq:llama-3.1-8b-instant",
        },
        "mixed": {"red": "openai:gpt-4o", "yellow": "anthropic:claude-3-opus"},
    }

    if example_name not in example_configs:
        available = ", ".join(example_configs.keys())
        raise ValueError(f"Unknown example '{example_name}'. Available: {available}")

    config = example_configs[example_name]
    return create_generic_connect4_engines_simple(
        config["red"], config["yellow"], temperature=temperature
    )
