
:py:mod:`games.nim.state_manager`
=================================

.. py:module:: games.nim.state_manager

Nim game state management module.

This module provides comprehensive state management functionality for the Nim game,
including game initialization, move validation, and game status tracking.

The Nim game is a mathematical strategy game where players take turns removing
stones from piles. The goal varies by game mode:
- Standard mode: The player who takes the last stone wins
- Misère mode: The player who takes the last stone loses

Classes:
    NimStateManager: Main state management class for Nim game operations.

.. rubric:: Example

Basic Nim game setup and play:

    >>> from haive.games.nim.state_manager import NimStateManager
    >>> from haive.games.nim.models import NimMove
    >>>
    >>> # Initialize game with custom pile sizes
    >>> state = NimStateManager.initialize(pile_sizes=[3, 5, 7])
    >>> print(f"Starting piles: {state.piles}")
    >>>
    >>> # Get legal moves for current player
    >>> legal_moves = NimStateManager.get_legal_moves(state)
    >>> print(f"Available moves: {len(legal_moves)}")
    >>>
    >>> # Make a move
    >>> move = NimMove(pile_index=1, stones_taken=3, player="player1")
    >>> new_state = NimStateManager.apply_move(state, move)
    >>> print(f"New piles: {new_state.piles}")

.. note::

   This implementation follows the Game State Manager pattern used throughout
   the haive-games package, providing consistent interfaces across all games.


.. autolink-examples:: games.nim.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.nim.state_manager.NimStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_NimStateManager {
        node [shape=record];
        "NimStateManager" [label="NimStateManager"];
        "haive.games.framework.base.state_manager.GameStateManager[haive.games.nim.state.NimState]" -> "NimStateManager";
      }

.. autoclass:: games.nim.state_manager.NimStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.nim.state_manager
   :collapse:
   
.. autolink-skip:: next
