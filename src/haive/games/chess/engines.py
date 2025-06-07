# In aug_llms.py

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AnthropicLLMConfig, AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from .models import ChessPlayerDecision, SegmentedAnalysis

# Create the move selection prompts
white_move_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are playing chess as WHITE. You are an expert chess player.\n\n"
            "MOVE FORMAT RULES:\n"
            "- Provide moves in UCI format: start square + end square (e.g., 'e2e4', 'g1f3')\n"
            "- Castling: 'e1g1' (kingside), 'e1c1' (queenside)\n"
            "- Promotion: add piece letter at end (e.g., 'a7a8q' for queen)\n"
            "- Do NOT use algebraic notation (e.g., 'Nf3') or piece symbols\n\n"
            "Evaluate the position and select the best strategic move.",
        ),
        (
            "human",
            "Position (FEN): {current_board_fen}\n"
            "Recent moves: {recent_moves}\n"
            "Captured pieces: {captured_pieces}\n"
            "{legal_moves_section}"
            "\nSelect your move and explain your reasoning.",
        ),
    ]
).partial(legal_moves_section="")

black_move_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are playing chess as BLACK. You are an expert chess player.\n\n"
            "MOVE FORMAT RULES:\n"
            "- Provide moves in UCI format: start square + end square (e.g., 'e7e5', 'g8f6')\n"
            "- Castling: 'e8g8' (kingside), 'e8c8' (queenside)\n"
            "- Promotion: add piece letter at end (e.g., 'a2a1q' for queen)\n"
            "- Do NOT use algebraic notation (e.g., 'Nf6') or piece symbols\n\n"
            "Evaluate the position and select the best strategic move.",
        ),
        (
            "human",
            "Position (FEN): {current_board_fen}\n"
            "Recent moves: {recent_moves}\n"
            "Captured pieces: {captured_pieces}\n"
            "{legal_moves_section}"
            "\nSelect your move and explain your reasoning.",
        ),
    ]
).partial(legal_moves_section="Legal moves: {legal_moves}")

# Create the analysis prompts
white_analysis_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are analyzing the chess position from WHITE's perspective.\n"
            "Provide strategic insights including position score (-10 to +10), "
            "attacking chances, defensive needs, and 2-3 concrete plans.",
        ),
        (
            "human",
            "Position (FEN): {current_board_fen}\n"
            "Recent moves: {recent_moves}\n"
            "Captured pieces: {captured_pieces}\n\n"
            "Analyze this position strategically.",
        ),
    ]
)

black_analysis_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are analyzing the chess position from BLACK's perspective.\n"
            "Provide strategic insights including position score (-10 to +10), "
            "attacking chances, defensive needs, and 2-3 concrete plans.",
        ),
        (
            "human",
            "Position (FEN): {current_board_fen}\n"
            "Recent moves: {recent_moves}\n"
            "Captured pieces: {captured_pieces}\n\n"
            "Analyze this position strategically.",
        ),
    ]
)


def build_chess_aug_llms() -> dict[str, AugLLMConfig]:
    """Build LLM configs for chess players and analyzers."""
    # Default LLM configuration
    default_llm_config = AzureLLMConfig(model="gpt-4o", temperature=0.7)

    return {
        "white_player": AugLLMConfig(
            name="white_player",
            llm_config=AnthropicLLMConfig(model="claude-3-5-sonnet-20240620"),
            prompt_template=white_move_prompt,
            structured_output_model=ChessPlayerDecision,
            force_tool_choice=True,
            description="White player move generation",
            structured_output_version="v1",
        ),
        "black_player": AugLLMConfig(
            name="black_player",
            llm_config=AnthropicLLMConfig(model="claude-3-5-sonnet-20240620"),
            prompt_template=black_move_prompt,
            structured_output_model=ChessPlayerDecision,
            force_tool_choice=True,
            description="Black player move generation",
            structured_output_version="v1",
        ),
        "white_analyzer": AugLLMConfig(
            name="white_analyzer",
            llm_config=default_llm_config,
            prompt_template=white_analysis_prompt,
            structured_output_model=SegmentedAnalysis,
            force_tool_choice=True,
            description="White position analysis",
            structured_output_version="v1",
        ),
        "black_analyzer": AugLLMConfig(
            name="black_analyzer",
            llm_config=default_llm_config,
            prompt_template=black_analysis_prompt,
            structured_output_model=SegmentedAnalysis,
            force_tool_choice=True,
            description="Black position analysis",
            structured_output_version="v1",
        ),
    }
