# src/haive/games/checkers/aug_llms.py

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.checkers.models import CheckersAnalysis, CheckersPlayerDecision


def generate_move_prompt(color: str) -> ChatPromptTemplate:
    """Generate move selection prompt for checkers."""
    color_upper = color.upper()
    opponent = "BLACK" if color == "red" else "RED"

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are playing checkers as {color_upper}. You are an expert checkers player.\n\n"
                "CRITICAL INSTRUCTIONS:\n"
                "1. You MUST choose ONLY from the PROVIDED LEGAL MOVES LIST\n"
                "2. Moves are in checkers notation: 'a3-b4' for regular moves, 'a3xc5' for jumps\n"
                "3. If jumps are available, you MUST take them (mandatory jump rule)\n"
                "4. Choose the move that gives you the best strategic advantage\n\n"
                "BOARD SYMBOLS:\n"
                "- '.' = empty square\n"
                "- 'r' = red piece\n"
                "- 'R' = red king\n"
                "- 'b' = black piece\n"
                "- 'B' = black king\n\n"
                "OUTPUT FORMAT (CheckersPlayerDecision):\n"
                "{{\n"
                '  "move": {{\n'
                '    "from_position": "EXACT_FROM_POSITION",\n'
                '    "to_position": "EXACT_TO_POSITION",\n'
                f'    "player": "{color}",\n'
                '    "is_jump": true/false,\n'
                '    "captured_position": "position_if_jump_else_null"\n'
                "  }},\n"
                '  "reasoning": "Your strategic reasoning",\n'
                '  "evaluation": "Position evaluation",\n'
                '  "alternatives": ["other moves considered"]\n'
                "}}",
            ),
            (
                "human",
                f"CHECKERS GAME - {color_upper} TO MOVE\n\n"
                "CURRENT BOARD:\n"
                "{board}\n\n"
                "LEGAL MOVES AVAILABLE (YOU MUST CHOOSE FROM THIS LIST):\n"
                "{legal_moves}\n\n"
                "{error_context}"
                "Game Info:\n"
                f"- You are: {color_upper}\n"
                f"- Opponent is: {opponent}\n"
                "- Captured pieces - Red: {captured_red}, Black: {captured_black}\n"
                "- Recent moves: {move_history}\n\n"
                "Previous analysis: {player_analysis}\n\n"
                "Select the BEST move from the legal moves list above.",
            ),
        ]
    )


def generate_analysis_prompt(color: str) -> ChatPromptTemplate:
    """Generate analysis prompt for checkers."""
    color_upper = color.upper()

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are analyzing a checkers position from {color_upper}'s perspective.\n\n"
                "Provide strategic insights focusing on:\n"
                "1. Material count (pieces and kings)\n"
                "2. Board control and positioning\n"
                "3. Immediate threats and opportunities\n"
                "4. Long-term strategic plans\n\n"
                "OUTPUT FORMAT (CheckersAnalysis):\n"
                "{{\n"
                '  "material_advantage": "description of material balance",\n'
                '  "control_of_center": "assessment of center control",\n'
                '  "suggested_moves": ["move1", "move2", "move3"],\n'
                '  "positional_evaluation": "overall position assessment"\n'
                "}}",
            ),
            (
                "human",
                f"ANALYZE POSITION FOR {color_upper}:\n\n"
                "CURRENT BOARD:\n"
                "{board}\n\n"
                "Game State:\n"
                "- Turn: {turn}\n"
                "- Captured - Red: {captured_red}, Black: {captured_black}\n"
                "- Recent moves: {move_history}\n\n"
                "Provide strategic analysis.",
            ),
        ]
    )


def build_checkers_aug_llms() -> dict[str, AugLLMConfig]:
    """Build LLM configs for checkers players and analyzers."""
    default_llm_config = AzureLLMConfig(model="gpt-4o", temperature=0.7)

    return {
        "red_player": AugLLMConfig(
            name="red_player",
            llm_config=default_llm_config,
            prompt_template=generate_move_prompt("red"),
            structured_output_model=CheckersPlayerDecision,
            force_tool_choice=True,
            structured_output_version="v1",
            description="Red player move generation",
        ),
        "black_player": AugLLMConfig(
            name="black_player",
            llm_config=default_llm_config,
            prompt_template=generate_move_prompt("black"),
            structured_output_model=CheckersPlayerDecision,
            force_tool_choice=True,
            structured_output_version="v1",
            description="Black player move generation",
        ),
        "red_analyzer": AugLLMConfig(
            name="red_analyzer",
            llm_config=default_llm_config,
            prompt_template=generate_analysis_prompt("red"),
            structured_output_model=CheckersAnalysis,
            force_tool_choice=True,
            structured_output_version="v1",
            description="Red position analysis",
        ),
        "black_analyzer": AugLLMConfig(
            name="black_analyzer",
            llm_config=default_llm_config,
            prompt_template=generate_analysis_prompt("black"),
            structured_output_model=CheckersAnalysis,
            force_tool_choice=True,
            structured_output_version="v1",
            description="Black position analysis",
        ),
    }
