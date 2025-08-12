
:py:mod:`games.tic_tac_toe.state`
=================================

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


.. autolink-examples:: games.tic_tac_toe.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.tic_tac_toe.state.TicTacToeState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TicTacToeState:

   .. graphviz::
      :align: center

      digraph inheritance_TicTacToeState {
        node [shape=record];
        "TicTacToeState" [label="TicTacToeState"];
        "haive.games.framework.base.state.GameState" -> "TicTacToeState";
      }

.. autoclass:: games.tic_tac_toe.state.TicTacToeState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.tic_tac_toe.state.add_messages_reducer
   games.tic_tac_toe.state.replace_board_reducer
   games.tic_tac_toe.state.replace_reducer

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


   .. autolink-examples:: add_messages_reducer
      :collapse:

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


   .. autolink-examples:: replace_board_reducer
      :collapse:

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


   .. autolink-examples:: replace_reducer
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.tic_tac_toe.state
   :collapse:
   
.. autolink-skip:: next
