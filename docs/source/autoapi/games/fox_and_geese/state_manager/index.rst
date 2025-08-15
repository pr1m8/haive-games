games.fox_and_geese.state_manager
=================================

.. py:module:: games.fox_and_geese.state_manager

.. autoapi-nested-parse::

   State manager for the Fox and Geese game.

   This module defines the state manager for the Fox and Geese game, which manages the
   state of the game and provides methods for initializing, applying moves, checking game
   status, and getting legal moves for the Fox and Geese game.


   .. autolink-examples:: games.fox_and_geese.state_manager
      :collapse:


Attributes
----------

.. autoapisummary::

   games.fox_and_geese.state_manager.logger


Classes
-------

.. autoapisummary::

   games.fox_and_geese.state_manager.FoxAndGeeseStateManager


Module Contents
---------------

.. py:class:: FoxAndGeeseStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.fox_and_geese.state.FoxAndGeeseState`\ ]


   Manager for Fox and Geese game state.

   This class provides methods for initializing, applying moves, checking game status,
   and getting legal moves for the Fox and Geese game.



   .. autolink-examples:: FoxAndGeeseStateManager
      :collapse:

   .. py:method:: _get_fox_moves(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> list[haive.games.fox_and_geese.models.FoxAndGeeseMove]
      :classmethod:


      Get all legal moves for the fox.

      This method returns a list of all legal moves for the fox in the given game
      state. It checks all possible diagonal directions from the fox's current
      position and creates moves for each valid direction.



      .. autolink-examples:: _get_fox_moves
         :collapse:


   .. py:method:: _get_geese_moves(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> list[haive.games.fox_and_geese.models.FoxAndGeeseMove]
      :classmethod:


      Get all legal moves for the geese.

      This method returns a list of all legal moves for the geese in the given game
      state. It checks all possible diagonal directions from the geese's current
      position and creates moves for each valid direction.



      .. autolink-examples:: _get_geese_moves
         :collapse:


   .. py:method:: apply_move(state: haive.games.fox_and_geese.state.FoxAndGeeseState, move: haive.games.fox_and_geese.models.FoxAndGeeseMove) -> haive.games.fox_and_geese.state.FoxAndGeeseState
      :classmethod:


      Apply a move to the Fox and Geese state.

      This method updates the state of the game based on the move made by the current
      player. It handles both regular moves and capture moves, updating the position
      of the fox and geese accordingly. It also updates the move history and switches
      turns between fox and geese.



      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> haive.games.fox_and_geese.state.FoxAndGeeseState
      :classmethod:


      Check and update game status.

      This method checks the current game status and updates the state accordingly. It
      determines if the fox has won by capturing too many geese or if the geese have
      won by trapping the fox. It also updates the game status and winner.



      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> list[haive.games.fox_and_geese.models.FoxAndGeeseMove]
      :classmethod:


      Get all legal moves for the current state.

      This method returns a list of all legal moves for the current player in the
      given game state. It checks the current player's turn and calls the appropriate
      method to get the legal moves for the fox or geese.



      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize() -> haive.games.fox_and_geese.state.FoxAndGeeseState
      :classmethod:


      Initialize a new Fox and Geese game.

      Creates initial game state with fox in center position and geese
      arranged in checkerboard pattern on the first two rows.

      :returns: Initial game state with positions set up.
      :rtype: FoxAndGeeseState


      .. autolink-examples:: initialize
         :collapse:


.. py:data:: logger

