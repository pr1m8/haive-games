"""Among Us game engines using AugLLMConfig.

This module provides LLM engine configurations for Among Us game agents, including:
    - Player engines for crewmates and impostors
    - Analyzer engines for deduction and strategy
    - Prompt templates with Among Us-specific instructions
    - Structured output models for actions and analysis

The engines use LLM configurations optimized for social deduction gameplay,
with prompt templates designed to generate high-quality moves and analysis.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AnthropicLLMConfig, OpenAILLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.among_us.models import (
    AmongUsAnalysis,
    AmongUsPlayerDecision,
    PlayerRole,
)


def generate_crewmate_prompt() -> ChatPromptTemplate:
    """Generate prompt for crewmate players.

    Returns:
        ChatPromptTemplate: A prompt template for crewmate gameplay
    """
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


def generate_impostor_prompt() -> ChatPromptTemplate:
    """Generate prompt for impostor players.

    Returns:
        ChatPromptTemplate: A prompt template for impostor gameplay
    """
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


def generate_analysis_prompt() -> ChatPromptTemplate:
    """Generate analysis prompt for game state evaluation.

    Returns:
        ChatPromptTemplate: A prompt template for game analysis
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert Among Us strategist analyzing the current game state.\n\n"
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


def build_among_us_aug_llms() -> dict[str, AugLLMConfig]:
    """Build augmented LLM configurations for Among Us game.

    Returns:
        dict[str, AugLLMConfig]: Dictionary of engine configurations
    """
    engines = {}

    # Crewmate player engine
    engines["crewmate_player"] = AugLLMConfig(
        name="crewmate_player",
        llm_config=OpenAILLMConfig(model="gpt-4o", temperature=0.7),
        prompt_template=generate_crewmate_prompt(),
        structured_output_model=AmongUsPlayerDecision,
        structured_output_version="v1",
        description="LLM engine for crewmate players",
    )

    # Impostor player engine
    engines["impostor_player"] = AugLLMConfig(
        name="impostor_player",
        llm_config=AnthropicLLMConfig(
            model="claude-3-5-sonnet-20240620", temperature=0.8
        ),
        prompt_template=generate_impostor_prompt(),
        structured_output_model=AmongUsPlayerDecision,
        structured_output_version="v1",
        description="LLM engine for impostor players",
    )

    # Game analyzer engine
    engines["game_analyzer"] = AugLLMConfig(
        name="game_analyzer",
        llm_config=OpenAILLMConfig(model="gpt-4o", temperature=0.3),
        prompt_template=generate_analysis_prompt(),
        structured_output_model=AmongUsAnalysis,
        structured_output_version="v1",
        description="LLM engine for game state analysis",
    )

    return engines


# Engine configuration functions for easy access


def get_crewmate_engine() -> AugLLMConfig:
    """Get the crewmate player engine."""
    return build_among_us_aug_llms()["crewmate_player"]


def get_impostor_engine() -> AugLLMConfig:
    """Get the impostor player engine."""
    return build_among_us_aug_llms()["impostor_player"]


def get_analyzer_engine() -> AugLLMConfig:
    """Get the game analyzer engine."""
    return build_among_us_aug_llms()["game_analyzer"]
