"""Engines for the Nim game."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.nim.models import NimAnalysis, NimMove


def generate_move_prompt(player: str) -> ChatPromptTemplate:
    """Generate a prompt for making a move in Nim.

    Args:
        player (str): The player to generate the prompt for.
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are the {player} in a game of Nim. Your goal is to make optimal moves based on game state.\n\n"
                f"Rules:\n"
                f"1. Players take turns removing stones from piles.\n"
                f"2. On your turn, you must take at least one stone, and you can take any number of stones from a single pile.\n"
                f"3. In standard Nim, the player who takes the last stone wins. In misere Nim, the player who takes the last stone loses.",
            ),
            (
                "human",
                "Current Game State:\n"
                "{board_string}\n\n"
                "You are playing as {player}. It's your turn.\n\n"
                "Game Mode: {misere_mode}\n\n"
                "Legal Moves Available:\n{legal_moves}\n\n"
                "Recent Moves:\n{move_history}\n\n"
                "Choose one of the available legal moves. Provide your reasoning and return a move object. "
                "Consider the nim-sum strategy if you are familiar with it.",
            ),
        ]
    )


def generate_analysis_prompt(player: str) -> ChatPromptTemplate:
    """Generate a prompt for analyzing a Nim position with structured output.

    Args:
        player (str): The player to generate the analysis for.
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are a Nim strategy expert analyzing the game from the perspective of {player}. "
                f"Your goal is to evaluate the current position and provide a structured analysis using "
                f"the nim-sum strategy and other Nim game theory concepts.",
            ),
            (
                "human",
                "Current Game State:\n{board_string}\n\n"
                "Player: {player}\n"
                "Nim Sum: {nim_sum}\n"
                "Misere Mode: {misere_mode}\n\n"
                "Recent Moves:\n{move_history}\n\n"
                "Please analyze the position and provide a structured analysis with the following information:\n"
                "1. Calculate the nim-sum of the piles\n"
                "2. Determine if the current position is winning or losing\n"
                "3. Recommend the best move to make\n"
                "4. Explain your reasoning\n\n"
                "Return a structured NimAnalysis object with the following fields:\n"
                "- nim_sum (int): The nim-sum of the pile sizes\n"
                "- position_evaluation (str): one of ['winning', 'losing', 'unclear']\n"
                "- recommended_move (NimMove): The best move to make with pile_index and stones_taken\n"
                "- explanation (str): Detailed explanation of your analysis\n\n"
                "Respond with a structured NimAnalysis object.",
            ),
        ]
    )


# Define the AugLLM configurations
nim_engines = {
    "player1_player": AugLLMConfig(
        name="player1_player",
        llm_config=AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.7}),
        prompt_template=generate_move_prompt("player1"),
        structured_output_model=NimMove,
    ),
    "player2_player": AugLLMConfig(
        name="player2_player",
        llm_config=AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.7}),
        prompt_template=generate_move_prompt("player2"),
        structured_output_model=NimMove,
    ),
    "player1_analyzer": AugLLMConfig(
        name="player1_analyzer",
        llm_config=AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.2}),
        prompt_template=generate_analysis_prompt("player1"),
        structured_output_model=NimAnalysis,
    ),
    "player2_analyzer": AugLLMConfig(
        name="player2_analyzer",
        llm_config=AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.2}),
        prompt_template=generate_analysis_prompt("player2"),
        structured_output_model=NimAnalysis,
    ),
}
