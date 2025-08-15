games.chess.state
=================

.. py:module:: games.chess.state

.. autoapi-nested-parse::

   Chess game state models.

   This module defines the state schema for chess games, including:
       - Board state representation using FEN notation
       - Move history tracking
       - Game status management
       - Position analysis storage
       - Player turn tracking

   The state schema provides a complete representation of a chess game state
   that can be used by the agent and state manager.


   .. autolink-examples:: games.chess.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.chess.state.ChessState


Module Contents
---------------

.. py:class:: ChessState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   State schema for the chess game.

   This class extends StateSchema to provide a comprehensive representation
   of a chess game, including board state, move history, game status, and
   analysis information.

   .. attribute:: board_fens

      List of FEN board states, with the most recent at the end.

      :type: List[str]

   .. attribute:: move_history

      List of (player_color, UCI move) tuples.

      :type: List[tuple[str, str]]

   .. attribute:: current_player

      Color of the player making the current move.

      :type: Literal["white", "black"]

   .. attribute:: turn

      Current turn color.

      :type: Literal["white", "black"]

   .. attribute:: game_status

      Current status of the game.

      :type: Literal["ongoing", "check", "checkmate", "stalemate", "draw"]

   .. attribute:: game_result

      Final game result (white_win, black_win, draw) if game is over.

      :type: Optional[str]

   .. attribute:: white_analysis

      Position analysis from white's perspective.

      :type: List[Dict[str, Any]]

   .. attribute:: black_analysis

      Position analysis from black's perspective.

      :type: List[Dict[str, Any]]

   .. attribute:: captured_pieces

      Pieces captured by each player.

      :type: Dict[str, List[str]]

   .. attribute:: error_message

      Error message if any error occurred.

      :type: Optional[str]

   .. attribute:: legal_moves

      String representation of legal moves in current position.

      :type: Optional[str]

   .. attribute:: recent_moves

      Recent moves formatted for LLM context.

      :type: Optional[str]

   .. rubric:: Examples

   >>> from haive.games.chess import ChessState
   >>> state = ChessState()
   >>> state.board_fen
   'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
   >>> board = state.get_board()
   >>> board.is_check()
   False


   .. autolink-examples:: ChessState
      :collapse:

   .. py:method:: get_board() -> chess.Board

      Get a chess.Board object for the current position.

      Creates a Python-chess Board object initialized with the current FEN position.

      :returns: Board object representing the current position.
      :rtype: chess.Board

      :raises ValueError: If the FEN string is invalid or cannot be parsed.

      .. rubric:: Example

      >>> state = ChessState()
      >>> board = state.get_board()
      >>> board.is_game_over()
      False


      .. autolink-examples:: get_board
         :collapse:


   .. py:attribute:: black_analysis
      :type:  list[dict[str, Any]]
      :value: None



   .. py:property:: board_fen
      :type: str


      Get the current board state as FEN notation.

      :returns: The FEN representation of the current board position.
      :rtype: str

      .. autolink-examples:: board_fen
         :collapse:


   .. py:attribute:: board_fens
      :type:  list[str]
      :value: None



   .. py:attribute:: captured_pieces
      :type:  dict[str, list[str]]
      :value: None



   .. py:property:: current_board_fen
      :type: str


      Alias for board_fen for backwards compatibility.

      :returns: The FEN representation of the current board position.
      :rtype: str

      .. autolink-examples:: current_board_fen
         :collapse:


   .. py:attribute:: current_player
      :type:  Literal['white', 'black']
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_result
      :type:  str | None
      :value: None



   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'check', 'checkmate', 'stalemate', 'draw']
      :value: None



   .. py:attribute:: legal_moves
      :type:  str | None
      :value: None



   .. py:attribute:: move_history
      :type:  list[tuple[str, str]]
      :value: None



   .. py:attribute:: recent_moves
      :type:  str | None
      :value: None



   .. py:attribute:: turn
      :type:  Literal['white', 'black']
      :value: None



   .. py:attribute:: white_analysis
      :type:  list[dict[str, Any]]
      :value: None



