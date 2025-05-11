"""Chess game augmented LLM configurations module.

This module provides LLM configurations for the chess game, including:
    - Move generation prompts for players
    - Position analysis prompts
    - Structured output models
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from .models import ChessPlayerDecision, SegmentedAnalysis


def generate_move_prompt(color: str) -> ChatPromptTemplate:
    """Generate a prompt for move selection.

    Args:
        color: Player color ("white" or "black")

    Returns:
        ChatPromptTemplate: Template for move selection
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are the {color} chess player. Your goal is to play the best possible move according to chess strategy.\n\n"
                "IMPORTANT: You MUST provide moves in UCI (Universal Chess Interface) format ONLY:\n"
                "- UCI format uses the start square and end square: e.g., 'e2e4' or 'g1f3'\n"
                "- DO NOT use algebraic notation like 'e4' or 'Nf3'\n"
                "- DO NOT include piece symbols like 'P', 'N', 'B', 'R', 'Q', 'K'\n"
                "- For castling: 'e1g1' (white kingside), 'e1c1' (white queenside), 'e8g8' (black kingside), 'e8c8' (black queenside)\n"
                "- For promotion: add the piece letter at the end (lowercase), e.g., 'a7a8q' for queen promotion\n\n"
                "CORRECT examples: 'e2e4', 'g1f3', 'e7e5', 'e1g1', 'a7a8q'\n"
                "INCORRECT examples: 'e4', 'Nf3', 'P-K4', 'O-O', 'Bf1c4'\n\n"
                "Your output MUST follow the ChessPlayerDecision format with these fields:\n"
                '- selected_move: { move: "MOVE_IN_UCI_FORMAT", explanation: "Explanation" }\n'
                '- position_eval: "Your evaluation of the position"\n'
                '- alternatives: [{ move: "ALTERNATIVE_MOVE_IN_UCI_FORMAT", explanation: "Explanation" }]\n'
                '- reasoning: "Your detailed reasoning"\n',
            ),
            (
                "human",
                "📌 **Game Context for {color}:**\n"
                "♟️ **Current Board Position (FEN):** {current_board_fen}\n"
                "🕰️ **Previous Board Position (FEN):** {previous_board_fen}\n"
                "📜 **Move History (Last Moves):** {recent_moves}\n"
                "🎯 **Captured Pieces:** {captured_pieces}\n\n"
                "🔍 **Your Last Analysis:** {player_analysis}\n"
                "⚠️ **Opponent's Plans Are Hidden** (You only see your perspective)\n\n"
                f"💡 **Your Turn! Choose the best move for {color}** in **UCI format** (start square to end square, e.g., e2e4, g1f3).\n"
                "Remember: UCI format ONLY, no piece symbols, just the square coordinates (e.g., for knight from g1 to f3, use 'g1f3', NOT 'Nf3' or 'Ng1f3').",
            ),
        ]
    )


def generate_analysis_prompt(color: str) -> ChatPromptTemplate:
    """Generate a prompt for position analysis.

    Args:
        color: Player color ("white" or "black")

    Returns:
        ChatPromptTemplate: Template for position analysis
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are analyzing {color}'s position in a chess game. Your task is to evaluate the strategic outlook.\n\n"
                "IMPORTANT: Your output MUST follow the SegmentedAnalysis format with these EXACT fields:\n"
                "- position_score: A numerical value (float) between -10.0 and 10.0, where positive favors White, negative favors Black\n"
                "- attacking_chances: A string description of attack opportunities\n"
                "- suggested_plans: An array of specific strategic plans as strings\n"
                "- defensive_needs: A string description of defensive requirements\n\n"
                "You MUST provide values for ALL fields. Each field must be properly formatted:\n"
                '- position_score must be a NUMBER, not text (e.g., 0.5, not "slightly better")\n'
                "- attacking_chances must be a descriptive STRING\n"
                "- suggested_plans must be an ARRAY of strings\n"
                "- defensive_needs must be a STRING\n\n"
                "Sample output structure:\n"
                "{{\n"
                '  "position_score": 0.3,\n'
                '  "attacking_chances": "Moderate attacking opportunities on kingside",\n'
                '  "suggested_plans": ["Control the center with d4", "Develop bishop to f4"],\n'
                '  "defensive_needs": "Watch for counterplay on the queenside"\n'
                "}}",
            ),
            (
                "human",
                "📌 **Game Analysis for {color}:**\n"
                "♟️ **Current Board Position (FEN):** {current_board_fen}\n"
                "🕰️ **Previous Board Position (FEN):** {previous_board_fen}\n"
                "📜 **Recent Moves:** {recent_moves}\n"
                "🎯 **Captured Pieces:** {captured_pieces}\n\n"
                "📝 **Your Task:**\n"
                "1️⃣ Assess {color}'s position strength (as a numerical score between -10.0 and 10.0)\n"
                "2️⃣ Identify attacking chances (as a descriptive string)\n"
                "3️⃣ Suggest 2-3 concrete strategic plans (as an array of strings)\n"
                "4️⃣ Note any defensive needs (as a descriptive string)\n\n"
                "Ensure all fields are properly formatted according to the required structure.",
            ),
        ]
    )


def build_chess_aug_llms() -> dict[str, AugLLMConfig]:
    """Build LLM configs for chess players and analyzers.

    This function creates AugLLMConfig objects for:
        - White player move generation
        - Black player move generation
        - White position analysis
        - Black position analysis

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of LLM configurations
    """
    # Default LLM configuration
    default_llm_config = AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.7})

    return {
        "white_player": AugLLMConfig(
            name="white_player",
            llm_config=default_llm_config,
            prompt_template=generate_move_prompt("white"),
            structured_output_model=ChessPlayerDecision,
            description="White player move generation",
        ),
        "black_player": AugLLMConfig(
            name="black_player",
            llm_config=default_llm_config,
            prompt_template=generate_move_prompt("black"),
            structured_output_model=ChessPlayerDecision,
            description="Black player move generation",
        ),
        "white_analyzer": AugLLMConfig(
            name="white_analyzer",
            llm_config=default_llm_config,
            prompt_template=generate_analysis_prompt("white"),
            structured_output_model=SegmentedAnalysis,
            description="White position analysis",
        ),
        "black_analyzer": AugLLMConfig(
            name="black_analyzer",
            llm_config=default_llm_config,
            prompt_template=generate_analysis_prompt("black"),
            structured_output_model=SegmentedAnalysis,
            description="Black position analysis",
        ),
    }
