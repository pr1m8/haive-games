games.dominoes.state_manager
============================

.. py:module:: games.dominoes.state_manager

Module documentation for games.dominoes.state_manager


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.dominoes.state_manager.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.dominoes.state_manager.DominoesStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesStateManager

            Bases: :py:obj:`haive.games.framework.base.GameStateManager`\ [\ :py:obj:`haive.games.dominoes.state.DominoesState`\ ]


            Manager for dominoes game state.


            .. py:method:: apply_move(state: haive.games.dominoes.state.DominoesState, move: haive.games.dominoes.models.DominoMove | Literal['pass']) -> haive.games.dominoes.state.DominoesState
               :classmethod:


               Apply a move to the dominoes state.



            .. py:method:: check_game_status(state: haive.games.dominoes.state.DominoesState) -> haive.games.dominoes.state.DominoesState
               :classmethod:


               Check and update the game status.



            .. py:method:: get_legal_moves(state: haive.games.dominoes.state.DominoesState) -> list[haive.games.dominoes.models.DominoMove | Literal['pass']]
               :classmethod:


               Get all legal moves for the current player.



            .. py:method:: initialize(player_names: list[str] = None, tiles_per_hand: int = 7) -> haive.games.dominoes.state.DominoesState
               :classmethod:


               Initialize a new dominoes game.



            .. py:method:: update_analysis(state: haive.games.dominoes.state.DominoesState, analysis: Any, player: str) -> haive.games.dominoes.state.DominoesState
               :classmethod:


               Update state with analysis.

               :param state: Current game state
               :param analysis: Analysis to add
               :param player: Player who made the analysis

               :returns: Updated game state with analysis




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.dominoes.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

