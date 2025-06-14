"""Chess game engines using AugLLMConfig."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AnthropicLLMConfig, AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.chess.models import ChessPlayerDecision, SegmentedAnalysis


def create_white_player_engine() -> AugLLMConfig:
    """Create white player engine configuration."""

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are playing chess as WHITE. You are an expert chess player.

CRITICAL MOVE FORMAT RULES:
- You MUST provide moves in UCI format: start square + end square (e.g., 'e2e4', 'g1f3')
- Castling: 'e1g1' (kingside), 'e1c1' (queenside)
- Promotion: add piece letter at end (e.g., 'a7a8q' for queen promotion)
- Do NOT use algebraic notation (e.g., 'Nf3', 'Bxe5')
- Do NOT include piece symbols or capture notation

EXAMPLES OF CORRECT MOVES:
- Pawn move: 'e2e4' (e2 to e4)
- Knight move: 'g1f3' (knight from g1 to f3)
- Capture: 'd4e5' (piece on d4 captures on e5)
- Castle kingside: 'e1g1'
- Promotion: 'h7h8q' (pawn promotes to queen)

{error_context}

Evaluate the position carefully and select the best strategic move from the legal moves provided.""",
            ),
            (
                "human",
                """Current position (FEN): {current_board_fen}

Recent moves: {recent_moves}

Captured pieces: {captured_pieces}

LEGAL MOVES AVAILABLE:
{legal_moves}

You MUST select one of the legal moves listed above. Analyze the position and choose your move.""",
            ),
        ]
    )

    return AugLLMConfig(
        name="white_player",
        llm_config=AnthropicLLMConfig(model="claude-3-5-sonnet-20240620"),
        prompt_template=prompt,
        structured_output_model=ChessPlayerDecision,
        temperature=0.7,
        description="White player move generation",
        structured_output_version="v1",
    )


def create_black_player_engine() -> AugLLMConfig:
    """Create black player engine configuration."""

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are playing chess as BLACK. You are an expert chess player.

CRITICAL MOVE FORMAT RULES:
- You MUST provide moves in UCI format: start square + end square (e.g., 'e7e5', 'g8f6')
- Castling: 'e8g8' (kingside), 'e8c8' (queenside)
- Promotion: add piece letter at end (e.g., 'a2a1q' for queen promotion)
- Do NOT use algebraic notation (e.g., 'Nf6', 'Bxe5')
- Do NOT include piece symbols or capture notation

EXAMPLES OF CORRECT MOVES:
- Pawn move: 'e7e5' (e7 to e5)
- Knight move: 'g8f6' (knight from g8 to f6)
- Capture: 'd7e6' (piece on d7 captures on e6)
- Castle queenside: 'e8c8'
- Promotion: 'b2b1n' (pawn promotes to knight)

{error_context}

Evaluate the position carefully and select the best strategic move from the legal moves provided.""",
            ),
            (
                "human",
                """Current position (FEN): {current_board_fen}

Recent moves: {recent_moves}

Captured pieces: {captured_pieces}

LEGAL MOVES AVAILABLE:
{legal_moves}

You MUST select one of the legal moves listed above. Analyze the position and choose your move.""",
            ),
        ]
    )

    return AugLLMConfig(
        name="black_player",
        llm_config=AnthropicLLMConfig(model="claude-3-5-sonnet-20240620"),
        prompt_template=prompt,
        structured_output_model=ChessPlayerDecision,
        temperature=0.7,
        description="Black player move generation",
        structured_output_version="v1",
    )


def create_white_analyzer_engine() -> AugLLMConfig:
    """Create white analyzer engine configuration."""

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are analyzing the chess position from WHITE's perspective.

Provide strategic insights including:
1. Position score from -10 to +10 (positive favors White, negative favors Black)
2. Attacking chances: describe White's offensive opportunities
3. Defensive needs: identify threats and weaknesses
4. Suggested plans: provide 2-3 concrete strategic plans

Be specific and focus on the current position's tactical and strategic elements.""",
            ),
            (
                "human",
                """Position (FEN): {current_board_fen}

Recent moves: {recent_moves}

Captured pieces: {captured_pieces}

Analyze this position strategically from White's perspective.""",
            ),
        ]
    )

    return AugLLMConfig(
        name="white_analyzer",
        llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7),
        prompt_template=prompt,
        structured_output_model=SegmentedAnalysis,
        description="White position analysis",
        structured_output_version="v1",
    )


def create_black_analyzer_engine() -> AugLLMConfig:
    """Create black analyzer engine configuration."""

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are analyzing the chess position from BLACK's perspective.

Provide strategic insights including:
1. Position score from -10 to +10 (positive favors White, negative favors Black)
2. Attacking chances: describe Black's offensive opportunities
3. Defensive needs: identify threats and weaknesses
4. Suggested plans: provide 2-3 concrete strategic plans

Be specific and focus on the current position's tactical and strategic elements.""",
            ),
            (
                "human",
                """Position (FEN): {current_board_fen}

Recent moves: {recent_moves}

Captured pieces: {captured_pieces}

Analyze this position strategically from Black's perspective.""",
            ),
        ]
    )

    return AugLLMConfig(
        name="black_analyzer",
        llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7),
        prompt_template=prompt,
        structured_output_model=SegmentedAnalysis,
        description="Black position analysis",
        structured_output_version="v1",
    )


def build_chess_aug_llms() -> dict[str, AugLLMConfig]:
    """Build AugLLMConfig dictionary for chess game engines."""
    return {
        "white_player": create_white_player_engine(),
        "black_player": create_black_player_engine(),
        "white_analyzer": create_white_analyzer_engine(),
        "black_analyzer": create_black_analyzer_engine(),
    }
