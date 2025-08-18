games.single_player.wordle.state_manager
========================================

.. py:module:: games.single_player.wordle.state_manager

Module documentation for games.single_player.wordle.state_manager


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.wordle.state_manager.WordConnectionsStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsStateManager

            Bases: :py:obj:`haive.games.framework.base.GameStateManager`\ [\ :py:obj:`haive.games.single_player.wordle.models.WordConnectionsState`\ ]


            Manager for Word Connections game state.


            .. py:method:: apply_move(state: haive.games.single_player.wordle.models.WordConnectionsState, move: haive.games.single_player.wordle.models.WordConnectionsMove) -> haive.games.single_player.wordle.models.WordConnectionsState
               :classmethod:


               Apply a move to the game state.

               :param state: Current game state
               :param move: Move to apply

               :returns: Updated game state



            .. py:method:: check_game_status(state: haive.games.single_player.wordle.models.WordConnectionsState) -> haive.games.single_player.wordle.models.WordConnectionsState
               :classmethod:


               Check and update game status.

               :param state: Current game state

               :returns: Updated game state



            .. py:method:: get_hint(state: haive.games.single_player.wordle.models.WordConnectionsState) -> str
               :classmethod:


               Get a hint for the current state.

               :param state: Current game state

               :returns: Hint string



            .. py:method:: initialize(puzzle_index: int | None = None, **kwargs) -> haive.games.single_player.wordle.models.WordConnectionsState
               :classmethod:


               Initialize a new Word Connections game.

               :param puzzle_index: Optional index of puzzle to use (0 = most recent)
               :param \*\*kwargs: Additional options

               :returns: Initialized game state



            .. py:attribute:: NYT_PUZZLES





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.wordle.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

