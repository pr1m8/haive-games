from typing import ClassVar, Dict, List, Literal, Sequence

from pydantic import BaseModel, Field

from haive.games.checkers.models import CheckersAnalysis, CheckersMove


class CheckersState(BaseModel):
    board: List[List[Literal[0, 1, 2, 3, 4]]] = Field(
        default_factory=lambda: CheckersState._default_board(),
        description="2D grid representation of the board",
    )
    # symbols = {0: ".", 1: "r", 2: "R", 3: "b", 4: "B"}
    board_string: str = Field(
        default_factory=lambda: CheckersState._create_board_string(
            CheckersState._default_board()
        ),
        description="String representation of the board",
    )
    turn: Literal["red", "black"] = Field(default="red")
    move_history: Sequence[CheckersMove] = Field(default_factory=list)
    game_status: Literal["ongoing", "game_over"] = Field(default="ongoing")
    winner: Literal["red", "black"] | None = None
    red_analysis: Sequence[CheckersAnalysis] = Field(default_factory=list)
    black_analysis: Sequence[CheckersAnalysis] = Field(default_factory=list)
    captured_pieces: Dict[str, List[str]] = Field(
        default_factory=lambda: {"red": [], "black": []}
    )

    __board_size: ClassVar[int] = 8
    __symbols: ClassVar[Dict[int, str]] = {0: ".", 1: "r", 2: "R", 3: "b", 4: "B"}

    @classmethod
    def _default_board(cls) -> list[list[int]]:
        return [
            [0, 3, 0, 3, 0, 3, 0, 3],
            [3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

    @classmethod
    def _create_board_string(cls, board: list[list[int]]) -> str:
        rows = [
            f"{cls.__board_size - i} | "
            + " ".join(cls._get_symbol(cell) for cell in row)
            for i, row in enumerate(board)
        ]
        col_labels = "    " + " ".join("abcdefgh")
        return "\n".join(rows) + "\n" + col_labels

    @classmethod
    def _get_symbol(cls, cell: int) -> str:
        return cls.__symbols[cell]

    @classmethod
    def initialize(cls) -> "CheckersState":
        board = cls._default_board()
        return cls(board=board, board_string=cls._create_board_string(board))

    class Config:
        arbitrary_types_allowed = True
