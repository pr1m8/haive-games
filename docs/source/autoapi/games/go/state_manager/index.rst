
:py:mod:`games.go.state_manager`
================================

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


.. autolink-examples:: games.go.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.go.state_manager.GoGameStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoGameStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_GoGameStateManager {
        node [shape=record];
        "GoGameStateManager" [label="GoGameStateManager"];
      }

.. autoclass:: games.go.state_manager.GoGameStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.go.state_manager
   :collapse:
   
.. autolink-skip:: next
