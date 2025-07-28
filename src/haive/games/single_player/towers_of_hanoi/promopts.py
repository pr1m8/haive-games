"""Promopts core module.

This module provides promopts functionality for the Haive framework.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Analysis prompt
HANOI_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a Tower of Hanoi master strategist.

Game Rules:
- {num_disks} disks numbered 1 (smallest) to {num_disks} (largest)
- {num_pegs} pegs numbered 1 to {num_pegs}
- Goal: Move all disks from peg 1 to peg {num_pegs}
- Only move one disk at a time
- Never place a larger disk on a smaller disk

Provide strategic analysis including:
1. Current progress assessment
2. Key patterns to follow
3. Next 3-5 move strategy
4. Efficiency considerations""",
        ),
        (
            "human",
            """Current Board:
{board_state}

Moves: {move_count}/{optimal_moves} (optimal)
Valid moves: {valid_moves}

Analyze this position.""",
        ),
    ]
)

# Move selection prompt
HANOI_MOVE_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a Tower of Hanoi expert. Select the optimal move."""),
        MessagesPlaceholder(variable_name="messages", optional=True),
        (
            "human",
            """Current Board:
{board_state}

Valid moves:
{valid_moves}

Select the best move.""",
        ),
    ]
)
