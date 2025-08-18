games.among_us.agent
====================

.. py:module:: games.among_us.agent

Module documentation for games.among_us.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.among_us.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.among_us.agent.AmongUsAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsAgent(config)

            Bases: :py:obj:`haive.games.among_us.state_manager.AmongUsStateManagerMixin`, :py:obj:`haive.games.framework.multi_player.agent.MultiPlayerGameAgent`\ [\ :py:obj:`haive.games.among_us.config.AmongUsAgentConfig`\ ]


            Agent implementation for the Among Us game.

            This class inherits state management from AmongUsStateManagerMixin and agent
            behavior from MultiPlayerGameAgent.


            Initialize the Among Us agent with configuration.


            .. py:method:: extract_move(response: Any, role: str) -> dict[str, Any]

               Extract structured move from engine response.



            .. py:method:: get_engine_for_player(role: str, engine_key: str) -> Any | None

               Get the appropriate engine for a player based on their role and the current.
               phase.

               :param role: Player role (CREWMATE or IMPOSTOR)
               :param engine_key: Engine type key (player, meeting, voting)

               :returns: The appropriate engine runnable



            .. py:method:: prepare_move_context(state: haive.games.among_us.state.AmongUsState, player_id: str) -> dict[str, Any]

               Prepare context for a player's move decision.



            .. py:method:: visualize_state(state: dict[str, Any] | haive.games.among_us.state.AmongUsState) -> None

               Visualize the current game state using the AmongUsUI.

               This method is required by the MultiPlayerGameAgent parent class.

               :param state: Current game state (dict or AmongUsState object)



            .. py:attribute:: state_manager


            .. py:attribute:: ui



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

