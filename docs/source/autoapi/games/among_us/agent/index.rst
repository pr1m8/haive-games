games.among_us.agent
====================

.. py:module:: games.among_us.agent


Attributes
----------

.. autoapisummary::

   games.among_us.agent.logger


Classes
-------

.. autoapisummary::

   games.among_us.agent.AmongUsAgent


Module Contents
---------------

.. py:class:: AmongUsAgent(config)

   Bases: :py:obj:`haive.games.among_us.state_manager.AmongUsStateManagerMixin`, :py:obj:`haive.games.framework.multi_player.agent.MultiPlayerGameAgent`\ [\ :py:obj:`haive.games.among_us.config.AmongUsAgentConfig`\ ]


   Agent implementation for the Among Us game.

   This class inherits state management from AmongUsStateManagerMixin and agent
   behavior from MultiPlayerGameAgent.


   Initialize the Among Us agent with configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AmongUsAgent
      :collapse:

   .. py:method:: extract_move(response: Any, role: str) -> dict[str, Any]

      Extract structured move from engine response.


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: get_engine_for_player(role: str, engine_key: str) -> Any | None

      Get the appropriate engine for a player based on their role and the current.
      phase.

      :param role: Player role (CREWMATE or IMPOSTOR)
      :param engine_key: Engine type key (player, meeting, voting)

      :returns: The appropriate engine runnable


      .. autolink-examples:: get_engine_for_player
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.among_us.state.AmongUsState, player_id: str) -> dict[str, Any]

      Prepare context for a player's move decision.


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any] | haive.games.among_us.state.AmongUsState) -> None

      Visualize the current game state using the AmongUsUI.

      This method is required by the MultiPlayerGameAgent parent class.

      :param state: Current game state (dict or AmongUsState object)


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: state_manager


   .. py:attribute:: ui


.. py:data:: logger

