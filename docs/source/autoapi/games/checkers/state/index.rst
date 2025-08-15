games.checkers.state
====================

.. py:module:: games.checkers.state


Classes
-------

.. autoapisummary::

   games.checkers.state.CheckersState
   games.checkers.state.GamePhase
   games.checkers.state.PieceType


Module Contents
---------------

.. py:class:: CheckersState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive state model for Checkers gameplay with strategic analysis support.

   This class provides complete state management for Checkers games, supporting
   both game mechanics and strategic analysis. The state system maintains board
   representation, move history, strategic context, and performance metrics for
   advanced AI decision-making and game analysis.

   The state system supports:
   - Complete board representation with algebraic notation conversion
   - Strategic analysis history for both players with pattern tracking
   - Comprehensive move tracking with game phase detection
   - Performance metrics and statistical analysis
   - Rule variant support for different Checkers types
   - Game completion detection and winner determination

   Board representation uses a 2D grid with these piece values:
   - 0: Empty square
   - 1: Red piece (regular)
   - 2: Red king
   - 3: Black piece (regular)
   - 4: Black king

   .. attribute:: board

      2D grid representation of the board
      using PieceType enum values for type safety and clarity.

      :type: List[List[Literal[0, 1, 2, 3, 4]]]

   .. attribute:: board_string

      Human-readable string representation of the board with
      coordinates for visualization and debugging.

      :type: str

   .. attribute:: turn

      Current player's turn with validation.

      :type: Literal["red", "black"]

   .. attribute:: move_history

      Complete chronological history of
      all moves made in the game with strategic context.

      :type: Sequence[CheckersMove]

   .. attribute:: game_status

      Current game status with
      automatic detection of terminal positions.

      :type: Literal["ongoing", "game_over"]

   .. attribute:: winner

      Winner of the game if completed,
      None if game is still in progress.

      :type: Optional[Literal["red", "black"]]

   .. attribute:: red_analysis

      Complete history of strategic
      analyses from red's perspective for learning and adaptation.

      :type: Sequence[CheckersAnalysis]

   .. attribute:: black_analysis

      Complete history of strategic
      analyses from black's perspective for learning and adaptation.

      :type: Sequence[CheckersAnalysis]

   .. attribute:: captured_pieces

      Comprehensive tracking of pieces
      captured by each player with position information.

      :type: Dict[str, List[str]]

   .. attribute:: turn_number

      Current turn number starting from 1 for game tracking.

      :type: int

   .. attribute:: last_capture_turn

      Turn number of the last capture for
      draw rule enforcement (50-move rule equivalent).

      :type: Optional[int]

   .. rubric:: Examples

   Creating a new game state::\n

       state = CheckersState.initialize()
       assert state.turn == "red"
       assert state.game_status == "ongoing"
       assert state.turn_number == 1

   Accessing board information::\n

       # Check piece at algebraic position
       piece = state.get_piece_at("a3")
       assert piece == PieceType.RED_PIECE

       # Get board visualization
       print(state.board_string)

       # Check if position is empty
       if state.is_empty_at("d4"):
           print("Position d4 is empty")

   Managing strategic analysis::\n

       analysis = CheckersAnalysis(
           material_advantage="Red +1 piece advantage",
           control_of_center="Red controls 3 of 4 center squares",
           suggested_moves=["e3-f4", "c3-d4", "g3-h4"],
           positional_evaluation="Slight advantage to Red"
       )
       state.add_analysis(analysis, "red")

       # Access latest analysis
       latest = state.get_latest_analysis("red")

   Game state queries::\n

       # Check game completion
       if state.is_game_over():
           winner = state.winner
           phase = state.game_phase

       # Material and position analysis
       material = state.material_balance
       kings = state.king_count
       center_control = state.center_control_score

       # Move pattern analysis
       recent_moves = state.get_recent_moves(5)
       capture_count = state.total_captures

   Advanced state analysis::\n

       # Performance metrics
       stats = state.game_statistics
       print(f"Game phase: {stats['game_phase']}")
       print(f"Move count: {stats['move_count']}")

       # Strategic position evaluation
       evaluation = state.position_evaluation
       print(f"Material score: {evaluation['material_score']}")
       print(f"Positional score: {evaluation['positional_score']}")

   .. note::

      The state uses Pydantic for validation and supports both JSON serialization
      and integration with LangGraph for distributed game systems.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CheckersState
      :collapse:

   .. py:method:: _create_board_string(board: list[list[int]]) -> str
      :classmethod:


      Create a string representation of the board for display.

      Converts the 2D grid representation to a human-readable string with
      row and column coordinates for visualization and debugging.

      :param board: 2D grid representation of the board.
      :type board: List[List[int]]

      :returns: String representation of the board with coordinates.
      :rtype: str

      .. rubric:: Examples

      Creating board visualization::\n

          board = CheckersState._default_board()
          print(CheckersState._create_board_string(board))
          # Output:
          # 8 | . b . b . b . b
          # 7 | b . b . b . b .
          # 6 | . b . b . b . b
          # 5 | . . . . . . . .
          # 4 | . . . . . . . .
          # 3 | r . r . r . r .
          # 2 | . r . r . r . r
          # 1 | r . r . r . r .
          #     a b c d e f g h


      .. autolink-examples:: _create_board_string
         :collapse:


   .. py:method:: _default_board() -> list[list[int]]
      :classmethod:


      Create the default starting board for checkers.

      Creates an 8x8 checkers board with the standard starting positions:
      - Black pieces on top three rows (rows 0-2)
      - Red pieces on bottom three rows (rows 5-7)
      - Empty middle rows (rows 3-4)

      :returns: 2D grid representation of the default board.
      :rtype: List[List[int]]

      .. note::

         The board uses PieceType enum values:
         - 0: Empty square
         - 1: Red piece
         - 2: Red king
         - 3: Black piece
         - 4: Black king


      .. autolink-examples:: _default_board
         :collapse:


   .. py:method:: _get_symbol(cell: int) -> str
      :classmethod:


      Get the symbol for a cell value.

      Converts the numeric cell value to its corresponding display symbol:
      - 0: "." (empty)
      - 1: "r" (red piece)
      - 2: "R" (red king)
      - 3: "b" (black piece)
      - 4: "B" (black king)

      :param cell: Cell value (0-4).
      :type cell: int

      :returns: Symbol representing the cell.
      :rtype: str


      .. autolink-examples:: _get_symbol
         :collapse:


   .. py:method:: add_analysis(analysis: haive.games.checkers.models.CheckersAnalysis, player: str) -> None

      Add strategic analysis for a player.

      :param analysis: Analysis to add.
      :type analysis: CheckersAnalysis
      :param player: Player the analysis is for ("red" or "black").
      :type player: str

      :raises ValueError: If player is not "red" or "black".


      .. autolink-examples:: add_analysis
         :collapse:


   .. py:method:: get_latest_analysis(player: str) -> haive.games.checkers.models.CheckersAnalysis | None

      Get the latest analysis for a player.

      :param player: Player to get analysis for ("red" or "black").
      :type player: str

      :returns: Latest analysis or None if no analysis exists.
      :rtype: Optional[CheckersAnalysis]


      .. autolink-examples:: get_latest_analysis
         :collapse:


   .. py:method:: get_piece_at(position: str) -> int

      Get the piece at a specific algebraic position.

      :param position: Algebraic position (e.g., "a3", "h6").
      :type position: str

      :returns: Piece type at the position (PieceType enum value).
      :rtype: int

      :raises ValueError: If position format is invalid.

      .. rubric:: Examples

      Getting piece at position::\n

          state = CheckersState.initialize()
          piece = state.get_piece_at("a3")
          assert piece == PieceType.RED_PIECE

          # Check if position is empty
          if state.get_piece_at("d4") == PieceType.EMPTY:
              print("Position d4 is empty")


      .. autolink-examples:: get_piece_at
         :collapse:


   .. py:method:: get_recent_moves(count: int) -> list[haive.games.checkers.models.CheckersMove]

      Get the most recent moves from the game history.

      :param count: Number of recent moves to return.
      :type count: int

      :returns: List of recent moves (up to count).
      :rtype: List[CheckersMove]


      .. autolink-examples:: get_recent_moves
         :collapse:


   .. py:method:: initialize() -> CheckersState
      :classmethod:


      Initialize a new checkers game state.

      Creates a fresh checkers state with the standard starting board,
      red to move first, and default values for all other fields.

      :returns: A new game state ready to play.
      :rtype: CheckersState

      .. rubric:: Examples

      Creating a new game::\n

          state = CheckersState.initialize()
          assert state.turn == "red"
          assert state.game_status == "ongoing"
          assert state.turn_number == 1
          assert len(state.move_history) == 0

      Verifying initial board setup::\n

          state = CheckersState.initialize()
          material = state.material_balance
          assert material["red_total"] == 12
          assert material["black_total"] == 12
          assert material["red_kings"] == 0
          assert material["black_kings"] == 0


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_empty_at(position: str) -> bool

      Check if a position is empty.

      :param position: Algebraic position to check.
      :type position: str

      :returns: True if position is empty, False otherwise.
      :rtype: bool


      .. autolink-examples:: is_empty_at
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.

      :returns: True if game is over, False otherwise.
      :rtype: bool


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: validate_turn_number(v: int) -> int
      :classmethod:


      Validate turn number is positive.

      :param v: Turn number to validate.
      :type v: int

      :returns: Validated turn number.
      :rtype: int

      :raises ValueError: If turn number is not positive.


      .. autolink-examples:: validate_turn_number
         :collapse:


   .. py:attribute:: __board_size
      :type:  ClassVar[int]
      :value: 8



   .. py:attribute:: __piece_symbols
      :type:  ClassVar[dict[int, str]]


   .. py:attribute:: __symbols
      :type:  ClassVar[dict[int, str]]


   .. py:attribute:: black_analysis
      :type:  collections.abc.Sequence[haive.games.checkers.models.CheckersAnalysis]
      :value: None



   .. py:attribute:: board
      :type:  list[list[Literal[0, 1, 2, 3, 4]]]
      :value: None



   .. py:attribute:: board_string
      :type:  str
      :value: None



   .. py:attribute:: captured_pieces
      :type:  dict[str, list[str]]
      :value: None



   .. py:property:: center_control_score
      :type: dict[str, int | float]


      Calculate center control score for strategic evaluation.

      :returns: Center control statistics.
      :rtype: Dict[str, Union[int, float]]

      .. autolink-examples:: center_control_score
         :collapse:


   .. py:property:: game_phase
      :type: GamePhase


      Determine the current game phase based on piece count and move history.

      :returns: Current phase of the game (opening, middle, endgame, finished).
      :rtype: GamePhase

      .. autolink-examples:: game_phase
         :collapse:


   .. py:property:: game_statistics
      :type: dict[str, int | float | str]


      Generate comprehensive game statistics.

      :returns: Game statistics and metrics.
      :rtype: Dict[str, Union[int, float, str]]

      .. autolink-examples:: game_statistics
         :collapse:


   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'game_over']
      :value: None



   .. py:property:: king_count
      :type: dict[str, int]


      Count kings for each player.

      :returns: Number of kings for each player.
      :rtype: Dict[str, int]

      .. autolink-examples:: king_count
         :collapse:


   .. py:attribute:: last_capture_turn
      :type:  int | None
      :value: None



   .. py:property:: material_balance
      :type: dict[str, int | float]


      Calculate material balance and piece distribution.

      :returns:

                Material balance statistics including
                    piece counts, king counts, and overall material score.
      :rtype: Dict[str, Union[int, float]]

      .. autolink-examples:: material_balance
         :collapse:


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: move_history
      :type:  collections.abc.Sequence[haive.games.checkers.models.CheckersMove]
      :value: None



   .. py:property:: position_evaluation
      :type: dict[str, int | float | str]


      Generate comprehensive position evaluation.

      :returns: Position evaluation metrics.
      :rtype: Dict[str, Union[int, float, str]]

      .. autolink-examples:: position_evaluation
         :collapse:


   .. py:attribute:: red_analysis
      :type:  collections.abc.Sequence[haive.games.checkers.models.CheckersAnalysis]
      :value: None



   .. py:property:: total_captures
      :type: int


      Count total number of captures in the game.

      :returns: Total number of pieces captured by both players.
      :rtype: int

      .. autolink-examples:: total_captures
         :collapse:


   .. py:attribute:: turn
      :type:  Literal['red', 'black']
      :value: None



   .. py:attribute:: turn_number
      :type:  int
      :value: None



   .. py:attribute:: winner
      :type:  Literal['red', 'black'] | None
      :value: None



.. py:class:: GamePhase

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of game phases in Checkers.

   Defines the different phases of a Checkers game, which affects
   strategic considerations and AI decision-making approaches.

   Values:
       OPENING: Early game with full piece complement
       MIDDLE: Mid-game with active piece development
       ENDGAME: Late game with few pieces remaining
       FINISHED: Game has concluded with a winner


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePhase
      :collapse:

   .. py:attribute:: ENDGAME
      :value: 'endgame'



   .. py:attribute:: FINISHED
      :value: 'finished'



   .. py:attribute:: MIDDLE
      :value: 'middle'



   .. py:attribute:: OPENING
      :value: 'opening'



.. py:class:: PieceType

   Bases: :py:obj:`int`, :py:obj:`enum.Enum`


   Enumeration of piece types in Checkers.

   Defines the numeric values used in the board representation for different
   piece types, supporting both regular pieces and kings for each player.

   Values:
       EMPTY: Empty square (0)
       RED_PIECE: Regular red piece (1)
       RED_KING: Red king piece (2)
       BLACK_PIECE: Regular black piece (3)
       BLACK_KING: Black king piece (4)


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PieceType
      :collapse:

   .. py:attribute:: BLACK_KING
      :value: 4



   .. py:attribute:: BLACK_PIECE
      :value: 3



   .. py:attribute:: EMPTY
      :value: 0



   .. py:attribute:: RED_KING
      :value: 2



   .. py:attribute:: RED_PIECE
      :value: 1



