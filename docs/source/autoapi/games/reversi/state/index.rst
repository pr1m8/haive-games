games.reversi.state
===================

.. py:module:: games.reversi.state

Reversi (Othello) game state model.

Defines board layout, current game status, turn tracking, move history, analysis
storage, and rendering utilities for the Reversi agent system.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Reversi (Othello) game state model.

   Defines board layout, current game status, turn tracking, move history, analysis
   storage, and rendering utilities for the Reversi agent system.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.reversi.state.ReversiState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ReversiState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.state.GameState`


            State model for a game of Reversi/Othello.

            .. attribute:: board

               8x8 grid representing the game board.

               :type: List[List[Optional[str]]]

            .. attribute:: turn

               The current player's turn ('B' or 'W').

               :type: str

            .. attribute:: game_status

               Overall game status (ongoing, draw, B_win, W_win).

               :type: str

            .. attribute:: move_history

               History of all moves made.

               :type: List[ReversiMove]

            .. attribute:: winner

               Winner symbol ('B' or 'W'), or None.

               :type: Optional[str]

            .. attribute:: player_B

               Identifier for the player using black discs.

               :type: str

            .. attribute:: player_W

               Identifier for the player using white discs.

               :type: str

            .. attribute:: player1_analysis

               Analysis history by player1.

               :type: List[Dict[str, any]]

            .. attribute:: player2_analysis

               Analysis history by player2.

               :type: List[Dict[str, any]]

            .. attribute:: skip_count

               Number of consecutive turns skipped (used for endgame).

               :type: int

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: initialize(first_player: str = 'B', player_B: str = 'player1', player_W: str = 'player2') -> ReversiState
               :classmethod:


               Class-level initializer for ReversiState.

               :param first_player: 'B' or 'W'. Who plays first.
               :type first_player: str
               :param player_B: Which player controls black.
               :type player_B: str
               :param player_W: Which player controls white.
               :type player_W: str

               :returns: Initialized state.
               :rtype: ReversiState



            .. py:method:: validate_board(board: list[list[str | None]]) -> list[list[str | None]]
               :classmethod:


               Validate that the board is an 8x8 grid with only valid values.

               :param board: Input board state.
               :type board: List[List[Optional[str]]]

               :returns: The validated board.
               :rtype: List[List[Optional[str]]]

               :raises ValueError: If the board structure or contents are invalid.



            .. py:attribute:: board
               :type:  list[list[str | None]]
               :value: None



            .. py:property:: board_string
               :type: str


               Get a human-readable string of the current board layout.

               :returns: Formatted board as text.
               :rtype: str


            .. py:property:: current_player_name
               :type: str


               Get the current player's identifier.

               :returns: Either 'player1' or 'player2'.
               :rtype: str


            .. py:property:: disc_count
               :type: dict[str, int]


               Count the number of discs of each color on the board.

               :returns: Dictionary with counts of 'B' and 'W'.
               :rtype: Dict[str, int]


            .. py:attribute:: game_status
               :type:  Literal['ongoing', 'B_win', 'W_win', 'draw']
               :value: None



            .. py:attribute:: move_history
               :type:  list[haive.games.reversi.models.ReversiMove]
               :value: None



            .. py:attribute:: player1_analysis
               :type:  list[dict[str, Any]]
               :value: None



            .. py:attribute:: player2_analysis
               :type:  list[dict[str, Any]]
               :value: None



            .. py:attribute:: player_B
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:attribute:: player_W
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:attribute:: skip_count
               :type:  int
               :value: None



            .. py:attribute:: turn
               :type:  Literal['B', 'W']
               :value: None



            .. py:attribute:: winner
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.reversi.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

