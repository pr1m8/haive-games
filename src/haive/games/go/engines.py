"""Go game engines using AugLLMConfig.

This module provides LLM engine configurations for Go game agents, including:
    - Player engines for black and white players
    - Analyzer engines for position evaluation and strategy
    - Prompt templates with Go-specific instructions
    - Structured output models for moves and analysis

The engines use LLM configurations optimized for strategic gameplay,
with prompt templates designed to generate high-quality moves and analysis.

"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AnthropicLLMConfig, OpenAILLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.go.models import GoAnalysis, GoPlayerDecision


def generate_black_prompt() -> ChatPromptTemplate:
    """Generate prompt for black player.

    Returns:
        ChatPromptTemplate: A prompt template for black player gameplay

    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are playing Go as the BLACK player. Your goal is to control more territory than your opponent.\n\n"
                "As the black player:\n"
                "- You play first and have a slight advantage\n"
                "- Focus on claiming territory and building strong groups\n"
                "- Consider both offense and defense in your moves\n"
                "- Look for opportunities to capture opponent stones\n"
                "- Avoid creating weak groups that can be attacked\n\n"
                "Key strategies:\n"
                "- Corner positions are generally safer and worth more points\n"
                "- Connect your stones to form strong groups\n"
                "- Cut opponent connections when possible\n"
                "- Balance territory and influence\n"
                "- Consider the whole board, not just local fights",
            ),
            (
                "human",
                "Current Board State:\n"
                "{board_state}\n\n"
                "Move History:\n"
                "{move_history}\n\n"
                "Captured Stones:\n"
                "Black: {black_captured}, White: {white_captured}\n\n"
                "As the black player, what move do you want to make? "
                "Provide the coordinates and explain your reasoning.",
            ),
        ]
    )


def generate_white_prompt() -> ChatPromptTemplate:
    """Generate prompt for white player.

    Returns:
        ChatPromptTemplate: A prompt template for white player gameplay

    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are playing Go as the WHITE player. Your goal is to control more territory than your opponent.\n\n"
                "As the white player:\n"
                "- You play second but receive komi compensation\n"
                "- Focus on disrupting black's plans while building your own territory\n"
                "- Look for weaknesses in black's position\n"
                "- Build strong, connected groups\n"
                "- Consider both local tactics and global strategy\n\n"
                "Key strategies:\n"
                "- Respond to black's moves while pursuing your own agenda\n"
                "- Invade or reduce black's potential territory\n"
                "- Create complications when behind\n"
                "- Secure your own groups before attacking\n"
                "- Use the komi advantage in close games",
            ),
            (
                "human",
                "Current Board State:\n"
                "{board_state}\n\n"
                "Move History:\n"
                "{move_history}\n\n"
                "Captured Stones:\n"
                "Black: {black_captured}, White: {white_captured}\n\n"
                "As the white player, what move do you want to make? "
                "Provide the coordinates and explain your reasoning.",
            ),
        ]
    )


def generate_analysis_prompt() -> ChatPromptTemplate:
    """Generate analysis prompt for Go position evaluation.

    Returns:
        ChatPromptTemplate: A prompt template for position analysis

    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert Go analyst evaluating the current position.\n\n"
                "Analyze the position considering:\n"
                "- Territory control and potential\n"
                "- Group strength and weaknesses\n"
                "- Strategic opportunities\n"
                "- Tactical threats\n"
                "- Overall position assessment\n"
                "- Key points and urgent moves",
            ),
            (
                "human",
                "Board Position to Analyze:\n"
                "{board_state}\n\n"
                "Move History:\n"
                "{move_history}\n\n"
                "Game Information:\n"
                "Komi: {komi}\n"
                "Captured - Black: {black_captured}, White: {white_captured}\n\n"
                "Provide a comprehensive analysis of the position, "
                "including territory estimates, group evaluations, and strategic recommendations.",
            ),
        ]
    )


def build_go_aug_llms() -> dict[str, AugLLMConfig]:
    """Build augmented LLM configurations for Go game.

    Returns:
        dict[str, AugLLMConfig]: Dictionary of engine configurations

    """
    engines = {}

    # Black player engine
    engines["black_player"] = AugLLMConfig(
        name="black_player",
        llm_config=OpenAILLMConfig(model="gpt-4o", temperature=0.7),
        prompt_template=generate_black_prompt(),
        structured_output_model=GoPlayerDecision,
        structured_output_version="v1",
        description="LLM engine for black player",
    )

    # White player engine
    engines["white_player"] = AugLLMConfig(
        name="white_player",
        llm_config=AnthropicLLMConfig(
            model="claude-3-5-sonnet-20240620", temperature=0.7
        ),
        prompt_template=generate_white_prompt(),
        structured_output_model=GoPlayerDecision,
        structured_output_version="v1",
        description="LLM engine for white player",
    )

    # Game analyzer engine
    engines["game_analyzer"] = AugLLMConfig(
        name="game_analyzer",
        llm_config=OpenAILLMConfig(model="gpt-4o", temperature=0.3),
        prompt_template=generate_analysis_prompt(),
        structured_output_model=GoAnalysis,
        structured_output_version="v1",
        description="LLM engine for position analysis",
    )

    return engines


# Engine configuration functions for easy access


def get_black_engine() -> AugLLMConfig:
    """Get the black player engine."""
    return build_go_aug_llms()["black_player"]


def get_white_engine() -> AugLLMConfig:
    """Get the white player engine."""
    return build_go_aug_llms()["white_player"]


def get_analyzer_engine() -> AugLLMConfig:
    """Get the game analyzer engine."""
    return build_go_aug_llms()["game_analyzer"]
