"""Prompt generation and engine configuration for Flow Free.

This module defines prompt templates and LLM configurations for
move generation and position analysis in the Flow Free game.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.single_player.flow_free.models import FlowFreeAnalysis, FlowFreeMove


def generate_move_prompt() -> ChatPromptTemplate:
    """Generate a prompt template for Flow Free move generation.

    Returns:
        A prompt template for move generation.
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are playing the Flow Free puzzle game. In this game, you need to connect pairs of colored dots with pipes. The rules are:

1. Connect each pair of same-colored dots with a continuous pipe
2. Pipes cannot cross or overlap
3. Every cell on the grid must be filled with a pipe
4. A pipe can only make 90-degree turns

Your job is to decide the next move in the game based on the current board state.
""",
            ),
            (
                "human",
                """Current Board:
{board_display}

Game Status:
- Moves so far: {move_count}
- Completed Flows: {completed_flows_count}/{total_flows}
- Board Fill: {board_fill_percentage:.1f}%

{flow_status}

The valid moves are:
{valid_moves}

You need to select the next move. Consider which flow to extend and where to place the next pipe segment.
Think carefully about avoiding blocking other flows and ensuring all cells can eventually be filled.

Return your move as a FlowFreeMove object with the flow_id and position (row, col) of where to place the next pipe segment.
""",
            ),
        ]
    )


def generate_analysis_prompt() -> ChatPromptTemplate:
    """Generate a prompt template for Flow Free position analysis.

    Returns:
        A prompt template for position analysis.
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an expert Flow Free puzzle analyzer. In this game, the goal is to connect pairs of colored dots with pipes while following these rules:

1. Connect each pair of same-colored dots with a continuous pipe
2. Pipes cannot cross or overlap
3. Every cell on the grid must be filled with a pipe
4. A pipe can only make 90-degree turns

Your job is to analyze the current board state, identify critical flows, blocked paths, and recommend the best next move.
""",
            ),
            (
                "human",
                """Current Board:
{board_display}

Game Status:
- Moves so far: {move_count}
- Completed Flows: {completed_flows_count}/{total_flows}
- Board Fill: {board_fill_percentage:.1f}%

{flow_status}

{hint_request}

Analyze this position. Consider:
1. Which flows are most constrained and should be prioritized?
2. Are there any flows at risk of being blocked?
3. Which flow should be extended next and in which direction?
4. What is the optimal strategy for completing the puzzle?

Provide a detailed analysis and recommend the best next move.
""",
            ),
        ]
    )


# Configure LLM engines
flow_free_engines = {
    "player_move": AugLLMConfig(
        name="flow_free_player",
        llm_config=AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.3}),
        prompt_template=generate_move_prompt(),
        structured_output_model=FlowFreeMove,
    ),
    "game_analyzer": AugLLMConfig(
        name="flow_free_analyzer",
        llm_config=AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.2}),
        prompt_template=generate_analysis_prompt(),
        structured_output_model=FlowFreeAnalysis,
    ),
}
