# game_framework/games/rubiks_cube/prompts.py
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

# Base template for Rubik's Cube solving
RUBIKS_CUBE_SYSTEM_PROMPT = """You are an expert Rubik's Cube solver with deep knowledge of:
- Standard notation (U, D, F, B, L, R for faces, ' for counter-clockwise, 2 for 180°)
- CFOP method (Cross, F2L, OLL, PLL)
- Layer-by-layer solving approach
- Pattern recognition and algorithms

You must analyze the cube state and select optimal moves to progress toward the solution."""

RUBIKS_CUBE_HUMAN_PROMPT = """Current Cube State:
{cube_state}

Move History: {move_history}
Move Count: {move_count}
Current Phase: {current_phase}

Valid Moves: {valid_moves}

Analyze this position and select the best next move. You must choose from the valid moves listed above."""

# Create the prompt template
rubiks_cube_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(RUBIKS_CUBE_SYSTEM_PROMPT),
        HumanMessagePromptTemplate.from_template(RUBIKS_CUBE_HUMAN_PROMPT),
    ]
)
