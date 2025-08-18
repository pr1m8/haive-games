games.tic_tac_toe.state
=======================

.. py:module:: games.tic_tac_toe.state

Comprehensive state management system for strategic Tic Tac Toe gameplay.

from typing import Any
This module provides sophisticated state management for Tic Tac Toe games with
complete support for game mechanics, strategic analysis, and LangGraph integration.
The state system maintains game rules, move validation, and comprehensive game
history for educational and competitive gameplay.

The state system supports:
- Complete 3x3 board representation with move validation
- Turn-based gameplay with X and O player management
- Move history tracking for game replay and analysis
- Strategic analysis integration for both players
- Win condition detection (rows, columns, diagonals)
- Draw detection and game status management
- LangGraph reducers for concurrent state updates
- Error handling and recovery mechanisms

.. rubric:: Examples

Initializing a new game::

    state = TicTacToeState.initialize(
        first_player="X",
        player_X="player1",
        player_O="player2"
    )

Making a move and checking status::

    # Make a center move
    state.board[1][1] = "X"
    state.move_history.append(
        TicTacToeMove(row=1, col=1, player="X")
    )

    # Check game state
    if state.is_board_full:
        state.game_status = "draw"

Analyzing board positions::

    empty_cells = state.empty_cells
    print(f"Available moves: {empty_cells}")

    # Pretty print the board
    print(state.board_string)

Managing player turns::

    current = state.current_player_name
    if state.turn == "X":
        state.turn = "O"
    else:
        state.turn = "X"

.. note::

   All state updates should use LangGraph Commands to ensure proper
   reducer behavior and concurrent update handling.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">3 functions</span>   </div>

.. autoapi-nested-parse::

   Comprehensive state management system for strategic Tic Tac Toe gameplay.

   from typing import Any
   This module provides sophisticated state management for Tic Tac Toe games with
   complete support for game mechanics, strategic analysis, and LangGraph integration.
   The state system maintains game rules, move validation, and comprehensive game
   history for educational and competitive gameplay.

   The state system supports:
   - Complete 3x3 board representation with move validation
   - Turn-based gameplay with X and O player management
   - Move history tracking for game replay and analysis
   - Strategic analysis integration for both players
   - Win condition detection (rows, columns, diagonals)
   - Draw detection and game status management
   - LangGraph reducers for concurrent state updates
   - Error handling and recovery mechanisms

   .. rubric:: Examples

   Initializing a new game::

       state = TicTacToeState.initialize(
           first_player="X",
           player_X="player1",
           player_O="player2"
       )

   Making a move and checking status::

       # Make a center move
       state.board[1][1] = "X"
       state.move_history.append(
           TicTacToeMove(row=1, col=1, player="X")
       )

       # Check game state
       if state.is_board_full:
           state.game_status = "draw"

   Analyzing board positions::

       empty_cells = state.empty_cells
       print(f"Available moves: {empty_cells}")

       # Pretty print the board
       print(state.board_string)

   Managing player turns::

       current = state.current_player_name
       if state.turn == "X":
           state.turn = "O"
       else:
           state.turn = "X"

   .. note::

      All state updates should use LangGraph Commands to ensure proper
      reducer behavior and concurrent update handling.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.tic_tac_toe.state.TicTacToeState

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.tic_tac_toe.state.add_messages_reducer
      games.tic_tac_toe.state.replace_board_reducer
      games.tic_tac_toe.state.replace_reducer

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TicTacToeState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.state.GameState`


            Comprehensive state model for Tic Tac Toe gameplay with LangGraph integration.

            This class provides complete state management for Tic Tac Toe games, supporting
            both traditional gameplay mechanics and advanced features for AI analysis. The
            state system maintains game rules, validates moves, tracks history, and integrates
            with LangGraph for distributed gameplay and concurrent updates.

            The state model supports:
            - 3x3 board representation with None/X/O values
            - Turn management with alternating X and O players
            - Move history for game replay and analysis
            - Player-specific analysis storage
            - Win/draw detection and game status tracking
            - Error handling for invalid moves
            - LangGraph reducers for proper state updates
            - Pretty-printing for board visualization

            All fields use explicit reducers to ensure proper behavior with LangGraph's
            concurrent update system, preventing state corruption during parallel operations.

            .. attribute:: players

               Player identifiers with accumulating reducer.

               :type: List[str]

            .. attribute:: board

               3x3 game board with replace reducer.

               :type: List[List[Optional[str]]]

            .. attribute:: turn

               Current player's turn with replace reducer.

               :type: Literal["X", "O"]

            .. attribute:: game_status

               Game state (ongoing/X_win/O_win/draw) with replace reducer.

               :type: Literal

            .. attribute:: move_history

               Complete move history with accumulating reducer.

               :type: List[TicTacToeMove]

            .. attribute:: error_message

               Error state with replace reducer.

               :type: Optional[str]

            .. attribute:: winner

               Winner identifier with replace reducer.

               :type: Optional[str]

            .. attribute:: player_X

               Player using X symbol with replace reducer.

               :type: Literal

            .. attribute:: player_O

               Player using O symbol with replace reducer.

               :type: Literal

            .. attribute:: player1_analysis

               Player 1's analyses with accumulating reducer.

               :type: List[TicTacToeAnalysis]

            .. attribute:: player2_analysis

               Player 2's analyses with accumulating reducer.

               :type: List[TicTacToeAnalysis]

            .. rubric:: Examples

            Creating and initializing a game::

                state = TicTacToeState.initialize(
                    first_player="X",
                    player_X="Alice",
                    player_O="Bob"
                )
                assert state.turn == "X"
                assert state.game_status == "ongoing"
                assert all(cell is None for row in state.board for cell in row)

            Making moves and updating state::

                # X plays center
                state.board[1][1] = "X"
                state.move_history.append(
                    TicTacToeMove(row=1, col=1, player="X")
                )
                state.turn = "O"

                # O plays corner
                state.board[0][0] = "O"
                state.move_history.append(
                    TicTacToeMove(row=0, col=0, player="O")
                )
                state.turn = "X"

            Checking win conditions::

                # X wins with diagonal
                state.board = [
                    ["X", "O", None],
                    ["O", "X", None],
                    [None, None, "X"]
                ]
                state.game_status = "X_win"
                state.winner = "player1"

            Board visualization::

                print(state.board_string)
                # Output:
                #    0 1 2
                #   -------
                # 0 |X|O| |
                #   -------
                # 1 |O|X| |
                #   -------
                # 2 | | |X|
                #   -------

            .. note::

               State updates should be performed through LangGraph Commands to ensure
               proper reducer behavior and prevent concurrent update conflicts.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: _default_board() -> list[list[str | None]]
               :staticmethod:


               Create default empty 3x3 board for a new game.

               :returns: 3x3 grid with all cells set to None.
               :rtype: list[list[str | None]]

               .. rubric:: Examples

               >>> board = TicTacToeState._default_board()
               >>> len(board)
               3
               >>> all(len(row) == 3 for row in board)
               True
               >>> all(cell is None for row in board for cell in row)
               True



            .. py:method:: _default_players() -> list[str]
               :staticmethod:


               Create default player list for a two-player game.

               :returns: Default player identifiers ["player1", "player2"].
               :rtype: list[str]



            .. py:method:: initialize(**kwargs) -> TicTacToeState
               :classmethod:


               Initialize a new Tic Tac Toe game with optional configuration.

               Factory method to create a properly initialized game state with all
               required fields set to appropriate starting values.

               :param \*\*kwargs: Optional configuration parameters:
                                  first_player (Literal["X", "O"]): Which player goes first (default: "X").
                                  player_X (Literal["player1", "player2"]): Player using X (default: "player1").
                                  player_O (Literal["player1", "player2"]): Player using O (default: "player2").

               :returns: Newly initialized game state ready for play.
               :rtype: TicTacToeState

               .. rubric:: Examples

               Default initialization::

                   state = TicTacToeState.initialize()
                   assert state.turn == "X"
                   assert state.player_X == "player1"
                   assert state.player_O == "player2"

               Custom player assignment::

                   state = TicTacToeState.initialize(
                       first_player="O",
                       player_X="player2",
                       player_O="player1"
                   )
                   assert state.turn == "O"
                   assert state.current_player_name == "player1"

               Tournament setup::

                   state = TicTacToeState.initialize(
                       first_player="X",
                       player_X="player1",
                       player_O="player2"
                   )
                   # Ready for competitive play



            .. py:method:: validate_board(board) -> Any
               :classmethod:


               Validate that the board is a proper 3x3 grid with valid symbols.

               Ensures the board maintains the correct structure and contains only
               valid values (None for empty, 'X', or 'O' for occupied cells).

               :param board: The board to validate.
               :type board: List[List[Optional[str]]]

               :returns: Validated board or default empty board.
               :rtype: List[List[Optional[str]]]

               :raises ValueError: If the board structure is invalid or contains invalid values.

               .. rubric:: Examples

               Valid board::

                   board = [["X", None, "O"], [None, "X", None], ["O", None, "X"]]
                   # Passes validation

               Invalid board (wrong size)::

                   board = [["X", "O"], ["O", "X"]]  # 2x2 instead of 3x3
                   # Raises ValueError: "Board must have 3 rows"

               Invalid board (invalid symbol)::

                   board = [["X", "Y", "O"], [None, None, None], [None, None, None]]
                   # Raises ValueError: "Cell values must be None, 'X', or 'O', got Y"



            .. py:attribute:: board
               :type:  Annotated[list[list[str | None]], replace_board_reducer]
               :value: None



            .. py:property:: board_string
               :type: str


               Get a pretty-printed string representation of the board.

               Creates a human-readable ASCII representation of the current board state
               with row and column indices for easy reference.

               :returns: Multiline string representing the current board state.
               :rtype: str

               .. rubric:: Examples

               Empty board::

                      0 1 2
                     -------
                   0 | | | |
                     -------
                   1 | | | |
                     -------
                   2 | | | |
                     -------

               Game in progress::

                      0 1 2
                     -------
                   0 |X|O| |
                     -------
                   1 | |X| |
                     -------
                   2 |O| |X|
                     -------


            .. py:property:: current_player_name
               :type: str


               Get the identifier of the player whose turn it is.

               Maps the current turn symbol (X or O) to the assigned player identifier.

               :returns: The player identifier ("player1" or "player2").
               :rtype: str

               .. rubric:: Examples

               >>> state = TicTacToeState.initialize()
               >>> state.turn = "X"
               >>> state.current_player_name
               'player1'

               >>> state.turn = "O"
               >>> state.current_player_name
               'player2'


            .. py:property:: empty_cells
               :type: list[tuple[int, int]]


               Return a list of coordinates for all empty cells on the board.

               Useful for determining available moves and checking if the game can continue.

               :returns: List of (row, col) tuples for empty cells.
               :rtype: list[tuple[int, int]]

               .. rubric:: Examples

               >>> state = TicTacToeState.initialize()
               >>> state.empty_cells
               [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

               >>> state.board[1][1] = "X"
               >>> len(state.empty_cells)
               8


            .. py:attribute:: error_message
               :type:  Annotated[str | None, replace_reducer]
               :value: None



            .. py:attribute:: game_status
               :type:  Annotated[Literal['ongoing', 'X_win', 'O_win', 'draw'], replace_reducer]
               :value: None



            .. py:property:: is_board_full
               :type: bool


               Check whether the board is completely filled with no empty cells.

               Used to detect draw conditions when no player has won.

               :returns: True if all cells are occupied, False otherwise.
               :rtype: bool

               .. rubric:: Examples

               >>> state = TicTacToeState.initialize()
               >>> state.is_board_full
               False

               >>> # Fill the board
               >>> state.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]
               >>> state.is_board_full
               True


            .. py:attribute:: move_history
               :type:  Annotated[list[haive.games.tic_tac_toe.models.TicTacToeMove], add_messages_reducer]
               :value: None



            .. py:attribute:: player1_analysis
               :type:  Annotated[list[haive.games.tic_tac_toe.models.TicTacToeAnalysis], add_messages_reducer]
               :value: None



            .. py:attribute:: player2_analysis
               :type:  Annotated[list[haive.games.tic_tac_toe.models.TicTacToeAnalysis], add_messages_reducer]
               :value: None



            .. py:attribute:: player_O
               :type:  Annotated[Literal['player1', 'player2'], replace_reducer]
               :value: None



            .. py:attribute:: player_X
               :type:  Annotated[Literal['player1', 'player2'], replace_reducer]
               :value: None



            .. py:attribute:: players
               :type:  Annotated[list[str], add_messages_reducer]
               :value: None



            .. py:attribute:: turn
               :type:  Annotated[Literal['X', 'O'], replace_reducer]
               :value: None



            .. py:attribute:: winner
               :type:  Annotated[str | None, replace_reducer]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: add_messages_reducer(left: list, right: list) -> list

            Reducer for message-like lists that should be concatenated.

            This reducer is used for accumulating lists like move history
            and analysis results, preserving all historical data.

            :param left: Existing list in the state.
            :type left: list
            :param right: New items to append.
            :type right: list

            :returns: Concatenated list with all items.
            :rtype: list

            .. rubric:: Examples

            >>> add_messages_reducer([1, 2], [3, 4])
            [1, 2, 3, 4]
            >>> add_messages_reducer([], [1, 2])
            [1, 2]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: replace_board_reducer(left: Any, right: Any) -> Any

            Special reducer for the board that always replaces with the new board.

            This ensures the board state is always consistent and prevents
            partial updates that could create invalid game states.

            :param left: Existing board state.
            :type left: Any
            :param right: New board state.
            :type right: Any

            :returns: The new board state.
            :rtype: Any



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: replace_reducer(left: Any, right: Any) -> Any

            Reducer that always takes the new value (right side).

            This reducer is used for fields that should be completely replaced
            on update rather than merged or concatenated.

            :param left: Existing value in the state.
            :type left: Any
            :param right: New value to replace with.
            :type right: Any

            :returns: The new value (right side).
            :rtype: Any

            .. rubric:: Examples

            >>> replace_reducer("X", "O")
            'O'
            >>> replace_reducer([1, 2], [3, 4])
            [3, 4]





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.tic_tac_toe.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

