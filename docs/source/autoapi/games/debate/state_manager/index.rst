games.debate.state_manager
==========================

.. py:module:: games.debate.state_manager

Module documentation for games.debate.state_manager


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.debate.state_manager.DebateStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateStateManager

            Bases: :py:obj:`haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager`\ [\ :py:obj:`haive.games.debate.state.DebateState`\ ]


            Manager for debate game states.


            .. py:method:: advance_phase(state: haive.games.debate.state.DebateState) -> haive.games.debate.state.DebateState
               :classmethod:


               Advance to the next debate phase.

               :param state: Current debate state

               :returns: State in the next phase
               :rtype: DebateState



            .. py:method:: apply_move(state: haive.games.debate.state.DebateState, player_id: str, move: dict[str, Any]) -> haive.games.debate.state.DebateState
               :classmethod:


               Apply a player's move to the state.

               :param state: Current debate state
               :param player_id: ID of the player making the move
               :param move: Move to apply (typically a statement)

               :returns: Updated debate state
               :rtype: DebateState



            .. py:method:: check_game_status(state: haive.games.debate.state.DebateState) -> haive.games.debate.state.DebateState
               :classmethod:


               Check and update game status.

               :param state: Current debate state

               :returns: Updated debate state with status
               :rtype: DebateState



            .. py:method:: filter_state_for_player(state: haive.games.debate.state.DebateState, player_id: str) -> dict[str, Any]
               :classmethod:


               Filter state information for a specific player.

               :param state: Current debate state
               :param player_id: ID of the player

               :returns: Filtered state visible to the player
               :rtype: Dict[str, Any]



            .. py:method:: get_legal_moves(state: haive.games.debate.state.DebateState, player_id: str) -> list[dict[str, Any]]
               :classmethod:


               Get legal moves for a player.

               :param state: Current debate state
               :param player_id: ID of the player

               :returns: List of legal moves
               :rtype: List[Dict[str, Any]]



            .. py:method:: initialize(player_names: list[str], topic: haive.games.debate.models.Topic, format_type: str = 'standard', **kwargs) -> haive.games.debate.state.DebateState
               :classmethod:


               Initialize a new debate state.

               :param player_names: List of participant IDs
               :param topic: The debate topic
               :param format_type: Type of debate (presidential, trial, etc.)
               :param \*\*kwargs: Additional format-specific parameters

               :returns: A new debate state
               :rtype: DebateState






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

