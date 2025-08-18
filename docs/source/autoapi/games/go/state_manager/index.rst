games.go.state_manager
======================

.. py:module:: games.go.state_manager

Go game state management module.

This module provides comprehensive state management functionality for the ancient
strategy game of Go (also known as Weiqi or Baduk), including move validation,
stone capture mechanics, and game progression tracking.

Go is an abstract strategy board game for two players in which the aim is to
surround more territory than the opponent. The game is played on a 19×19 grid
(though 13×13 and 9×9 are common variants) where players alternate placing black
and white stones. Players capture opponents' stones by completely surrounding them.

Classes:
    GoGameStateManager: Main state management class for Go game operations.

.. rubric:: Example

Basic Go game setup and play:

    >>> from haive.games.go.state_manager import GoGameStateManager
    >>> from haive.games.go.models import GoMove
    >>>
    >>> # Initialize standard 19×19 Go game
    >>> state = GoGameStateManager.initialize(board_size=19)
    >>> print(f"Board size: {state.board_size}×{state.board_size}")
    >>> print(f"Current player: {state.turn}")  # "black"
    >>>
    >>> # Make a move (place stone at coordinates)
    >>> move_coords = (3, 4)  # (row, col)
    >>> new_state = GoGameStateManager.apply_move(state, move_coords)
    >>> print(f"Stone placed at {move_coords}")
    >>>
    >>> # Pass turn (no stone placed)
    >>> pass_state = GoGameStateManager.apply_move(new_state, None)
    >>> print(f"Pass count: {pass_state.passes}")

.. note::

   - Standard board sizes: 19×19 (professional), 13×13, 9×9 (beginners)
   - Players are "black" and "white" with black moving first
   - Coordinates are (row, col) tuples using 0-based indexing
   - Pass moves are represented as None coordinates
   - Game ends when both players pass consecutively
   - Stone capture follows the rule of liberty (breathing spaces)
   - Uses Sente library for Go game logic and SGF format



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Go game state management module.

   This module provides comprehensive state management functionality for the ancient
   strategy game of Go (also known as Weiqi or Baduk), including move validation,
   stone capture mechanics, and game progression tracking.

   Go is an abstract strategy board game for two players in which the aim is to
   surround more territory than the opponent. The game is played on a 19×19 grid
   (though 13×13 and 9×9 are common variants) where players alternate placing black
   and white stones. Players capture opponents' stones by completely surrounding them.

   Classes:
       GoGameStateManager: Main state management class for Go game operations.

   .. rubric:: Example

   Basic Go game setup and play:

       >>> from haive.games.go.state_manager import GoGameStateManager
       >>> from haive.games.go.models import GoMove
       >>>
       >>> # Initialize standard 19×19 Go game
       >>> state = GoGameStateManager.initialize(board_size=19)
       >>> print(f"Board size: {state.board_size}×{state.board_size}")
       >>> print(f"Current player: {state.turn}")  # "black"
       >>>
       >>> # Make a move (place stone at coordinates)
       >>> move_coords = (3, 4)  # (row, col)
       >>> new_state = GoGameStateManager.apply_move(state, move_coords)
       >>> print(f"Stone placed at {move_coords}")
       >>>
       >>> # Pass turn (no stone placed)
       >>> pass_state = GoGameStateManager.apply_move(new_state, None)
       >>> print(f"Pass count: {pass_state.passes}")

   .. note::

      - Standard board sizes: 19×19 (professional), 13×13, 9×9 (beginners)
      - Players are "black" and "white" with black moving first
      - Coordinates are (row, col) tuples using 0-based indexing
      - Pass moves are represented as None coordinates
      - Game ends when both players pass consecutively
      - Stone capture follows the rule of liberty (breathing spaces)
      - Uses Sente library for Go game logic and SGF format



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.go.state_manager.GoGameStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GoGameStateManager

            Manager class for Go game state operations.

            This class provides static methods for initializing and modifying
            Go game states, including:
                - Game initialization
                - Move application and validation
                - Pass move handling
                - Game end detection

            .. rubric:: Example

            >>> # Initialize a new game
            >>> state = GoGameStateManager.initialize(board_size=19)
            >>>
            >>> # Apply a move
            >>> new_state = GoGameStateManager.apply_move(state, (3, 4))
            >>> print(new_state.turn)  # 'white'


            .. py:method:: apply_move(state: haive.games.go.state.GoGameState, move: tuple[int, int] | None) -> haive.games.go.state.GoGameState
               :staticmethod:


               Apply a move to the current game state.

               This method handles:
                   - Move validation and application
                   - Pass moves (when move is None)
                   - Capture counting
                   - Turn alternation
                   - Game end detection

               :param state: Current game state.
               :type state: GoGameState
               :param move: Move coordinates or None for pass.
               :type move: Optional[Tuple[int, int]]

               :returns: New game state after applying the move.
               :rtype: GoGameState

               .. rubric:: Example

               >>> state = GoGameStateManager.initialize()
               >>> # Play a move at (3, 4)
               >>> new_state = GoGameStateManager.apply_move(state, (3, 4))
               >>> print(new_state.turn)  # 'white'
               >>>
               >>> # Pass move
               >>> pass_state = GoGameStateManager.apply_move(new_state, None)
               >>> print(pass_state.passes)  # 1



            .. py:method:: initialize(board_size: int = 19) -> haive.games.go.state.GoGameState
               :staticmethod:


               Initialize a new Go game state.

               :param board_size: Size of the board (default: 19).
               :type board_size: int

               :returns: Initial game state.
               :rtype: GoGameState

               .. rubric:: Example

               >>> state = GoGameStateManager.initialize(board_size=13)
               >>> print(state.board_size)  # 13
               >>> print(state.turn)  # 'black'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.go.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

