games.debate.state_manager
==========================

.. py:module:: games.debate.state_manager


Classes
-------

.. autoapisummary::

   games.debate.state_manager.DebateStateManager


Module Contents
---------------

.. py:class:: DebateStateManager

   Bases: :py:obj:`haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager`\ [\ :py:obj:`haive.games.debate.state.DebateState`\ ]


   Manager for debate game states.


   .. autolink-examples:: DebateStateManager
      :collapse:

   .. py:method:: advance_phase(state: haive.games.debate.state.DebateState) -> haive.games.debate.state.DebateState
      :classmethod:


      Advance to the next debate phase.

      :param state: Current debate state

      :returns: State in the next phase
      :rtype: DebateState


      .. autolink-examples:: advance_phase
         :collapse:


   .. py:method:: apply_move(state: haive.games.debate.state.DebateState, player_id: str, move: dict[str, Any]) -> haive.games.debate.state.DebateState
      :classmethod:


      Apply a player's move to the state.

      :param state: Current debate state
      :param player_id: ID of the player making the move
      :param move: Move to apply (typically a statement)

      :returns: Updated debate state
      :rtype: DebateState


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.debate.state.DebateState) -> haive.games.debate.state.DebateState
      :classmethod:


      Check and update game status.

      :param state: Current debate state

      :returns: Updated debate state with status
      :rtype: DebateState


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: filter_state_for_player(state: haive.games.debate.state.DebateState, player_id: str) -> dict[str, Any]
      :classmethod:


      Filter state information for a specific player.

      :param state: Current debate state
      :param player_id: ID of the player

      :returns: Filtered state visible to the player
      :rtype: Dict[str, Any]


      .. autolink-examples:: filter_state_for_player
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.debate.state.DebateState, player_id: str) -> list[dict[str, Any]]
      :classmethod:


      Get legal moves for a player.

      :param state: Current debate state
      :param player_id: ID of the player

      :returns: List of legal moves
      :rtype: List[Dict[str, Any]]


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize(player_names: list[str], topic: haive.games.debate.models.Topic, format_type: str = 'standard', **kwargs) -> haive.games.debate.state.DebateState
      :classmethod:


      Initialize a new debate state.

      :param player_names: List of participant IDs
      :param topic: The debate topic
      :param format_type: Type of debate (presidential, trial, etc.)
      :param \*\*kwargs: Additional format-specific parameters

      :returns: A new debate state
      :rtype: DebateState


      .. autolink-examples:: initialize
         :collapse:


