"""Specialized LLM configurations for the Mafia game.

This module provides specialized augmented LLM configurations for different
aspects of the Mafia game, including:
    - Role-specific analyzer LLMs
    - Strategic decision-making models
    - Game state evaluators

These configurations extend the basic engines.py configurations with more
sophisticated models tailored for specific game aspects.

Example:
    >>> from haive.games.mafia.aug_llms import get_mafia_analyzer
    >>>
    >>> # Get an analyzer for evaluating player suspicion levels
    >>> analyzer = get_mafia_analyzer("suspicion")
    >>> analysis = analyzer.invoke(game_state)

"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

# from haive.games.mafia.models import MafiaAnalysis  # TODO: Define this model


def get_mafia_analyzer(analyzer_type: str) -> AugLLMConfig:
    """Get a specialized Mafia game analyzer.

    This function returns a configured analyzer LLM for specific
    Mafia game analysis tasks, such as suspicion evaluation,
    player psychology, strategy optimization, or voting analysis.

    Args:
        analyzer_type: Type of analyzer to get ("suspicion", "psychology",
            "strategy", or "voting")

    Returns:
        AugLLMConfig: Configured analyzer

    Raises:
        ValueError: If analyzer_type is not recognized

    Example:
        >>> analyzer = get_mafia_analyzer("suspicion")
        >>> analysis = analyzer.invoke(game_context)

    """
    if analyzer_type == "suspicion":
        return AugLLMConfig(
            name="mafia_suspicion_analyzer",
            llm_config=AzureLLMConfig(model="gpt-4o"),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a Mafia game analyzer focused on evaluating player suspicion "
                        "levels. Analyze player behaviors, voting patterns, and statements to "
                        "determine who is acting suspiciously. Provide a ranked list of players "
                        "from most to least suspicious, with reasoning for each.",
                    ),
                    (
                        "human",
                        "Game State:\n"
                        "- Current Day: {day_number}\n"
                        "- Alive Players: {alive_players}\n"
                        "- Dead Players: {dead_players}\n\n"
                        "Recent Actions:\n{action_history}\n\n"
                        "Voting Patterns:\n{voting_patterns}\n\n"
                        "Player Statements:\n{player_statements}\n\n"
                        "Analyze the suspicion level of each player and provide "
                        "a ranked assessment with reasoning.",
                    ),
                ]
            ),
            # structured_output_model=MafiaAnalysis,  # TODO: Define this model
        )

    if analyzer_type == "psychology":
        return AugLLMConfig(
            name="mafia_psychology_analyzer",
            llm_config=AzureLLMConfig(model="gpt-4o"),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a Mafia game psychology analyzer. Your job is to analyze the "
                        "psychological patterns of players, looking for tells, inconsistencies, "
                        "and emotional responses that might reveal their true roles. Focus on "
                        "communication style, defensive reactions, and alliance dynamics.",
                    ),
                    (
                        "human",
                        "Game State:\n"
                        "- Current Day: {day_number}\n"
                        "- Alive Players: {alive_players}\n"
                        "- Dead Players: {dead_players}\n\n"
                        "Player Communications:\n{player_communications}\n\n"
                        "Alliances and Conflicts:\n{alliances}\n\n"
                        "Analyze the psychological patterns of each player and identify "
                        "potential tells that might reveal their true roles.",
                    ),
                ]
            ),
            # structured_output_model=MafiaAnalysis,  # TODO: Define this model
        )

    if analyzer_type == "strategy":
        return AugLLMConfig(
            name="mafia_strategy_analyzer",
            llm_config=AzureLLMConfig(model="gpt-4o"),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a Mafia game strategy analyzer. Your job is to analyze the current "
                        "game state and recommend optimal strategies for a player based on their "
                        "role. Consider game phase, player dynamics, and risk assessment to "
                        "provide actionable strategic advice.",
                    ),
                    (
                        "human",
                        "Game State:\n"
                        "- Current Day: {day_number}\n"
                        "- Current Phase: {phase}\n"
                        "- Your Role: {role}\n"
                        "- Alive Players: {alive_players}\n"
                        "- Dead Players: {dead_players}\n\n"
                        "Your Known Information:\n{known_info}\n\n"
                        "Recent Events:\n{recent_events}\n\n"
                        "Analyze the current game state and provide strategic "
                        "recommendations for optimal play based on my role.",
                    ),
                ]
            ),
            # structured_output_model=MafiaAnalysis,  # TODO: Define this model
        )

    if analyzer_type == "voting":
        return AugLLMConfig(
            name="mafia_voting_analyzer",
            llm_config=AzureLLMConfig(model="gpt-4o"),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a Mafia game voting analyzer. Your job is to analyze voting "
                        "patterns across multiple days to identify coalitions, bloc voting, "
                        "and suspicious voting behaviors that might reveal player roles. "
                        "Look for patterns that suggest coordination or role-specific motives.",
                    ),
                    (
                        "human",
                        "Game State:\n"
                        "- Current Day: {day_number}\n"
                        "- Alive Players: {alive_players}\n"
                        "- Dead Players: {dead_players}\n\n"
                        "Voting History:\n{voting_history}\n\n"
                        "Analyze the voting patterns to identify coalitions, blocs, "
                        "and suspicious behaviors that might reveal player roles.",
                    ),
                ]
            ),
            # structured_output_model=MafiaAnalysis,  # TODO: Define this model
        )

    raise TypeError(f"Unknown analyzer type: {analyzer_type}")


# Pre-configured analyzers
suspicion_analyzer = get_mafia_analyzer("suspicion")
psychology_analyzer = get_mafia_analyzer("psychology")
strategy_analyzer = get_mafia_analyzer("strategy")
voting_analyzer = get_mafia_analyzer("voting")


# Export all analyzers
__all__ = [
    "get_mafia_analyzer",
    "psychology_analyzer",
    "strategy_analyzer",
    "suspicion_analyzer",
    "voting_analyzer",
]
