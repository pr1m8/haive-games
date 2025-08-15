games.mafia.state
=================

.. py:module:: games.mafia.state

.. autoapi-nested-parse::

   Game state models for the Mafia game.

   This module defines the core state model for the Mafia game, extending the
   base MultiPlayerGameState with Mafia-specific functionality.

   The state model tracks:
       - Player roles and statuses
       - Game phase and progression
       - Voting and action history
       - Public announcements
       - Night action outcomes

   .. rubric:: Example

   >>> from mafia.state import MafiaGameState
   >>> from mafia.models import PlayerRole, GamePhase
   >>>
   >>> # Create a new game state
   >>> state = MafiaGameState(
   ...     players=["Player_1", "Player_2", "Narrator"],
   ...     roles={"Player_1": PlayerRole.VILLAGER,
   ...            "Player_2": PlayerRole.MAFIA,
   ...            "Narrator": PlayerRole.NARRATOR},
   ...     game_phase=GamePhase.SETUP
   ... )


   .. autolink-examples:: games.mafia.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.mafia.state.MafiaGameState


Module Contents
---------------

.. py:class:: MafiaGameState

   Bases: :py:obj:`haive.games.framework.multi_player.state.MultiPlayerGameState`


   State model for a Mafia game.

   This class extends MultiPlayerGameState to provide Mafia-specific state
   tracking, including roles, votes, and game progression.

   .. attribute:: players

      List of player names/IDs

      :type: List[str]

   .. attribute:: current_player_idx

      Index of current player in players list

      :type: int

   .. attribute:: game_status

      Status of the game (ongoing, ended)

      :type: str

   .. attribute:: move_history

      History of moves

      :type: List[Dict[str, Any]]

   .. attribute:: round_number

      Current round number

      :type: int

   .. attribute:: player_data

      Player-specific data

      :type: Dict[str, Dict[str, Any]]

   .. attribute:: public_state

      Public game state visible to all

      :type: Dict[str, Any]

   .. attribute:: error_message

      Error message if any

      :type: Optional[str]

   .. attribute:: game_phase

      Current phase of the game

      :type: GamePhase

   .. attribute:: roles

      Mapping of player IDs to roles

      :type: Dict[str, PlayerRole]

   .. attribute:: player_states

      Player state information

      :type: Dict[str, PlayerState]

   .. attribute:: votes

      Player votes during voting phase

      :type: Dict[str, str]

   .. attribute:: action_history

      History of all actions

      :type: List[Dict[str, Any]]

   .. attribute:: public_announcements

      Public game announcements

      :type: List[str]

   .. attribute:: alive_mafia_count

      Number of mafia members alive

      :type: int

   .. attribute:: alive_village_count

      Number of villagers alive

      :type: int

   .. attribute:: alive_doctor_count

      Number of doctors alive

      :type: int

   .. attribute:: alive_detective_count

      Number of detectives alive

      :type: int

   .. attribute:: killed_at_night

      Player targeted by mafia

      :type: Optional[str]

   .. attribute:: saved_at_night

      Player saved by doctor

      :type: Optional[str]

   .. attribute:: night_deaths

      Players who died during the night

      :type: List[str]

   .. attribute:: day_number

      Current day number

      :type: int

   .. attribute:: winner

      Winner (village or mafia)

      :type: Optional[str]

   .. rubric:: Example

   >>> state = MafiaGameState(
   ...     players=["Player_1", "Player_2", "Narrator"],
   ...     roles={"Player_1": PlayerRole.VILLAGER,
   ...            "Player_2": PlayerRole.MAFIA,
   ...            "Narrator": PlayerRole.NARRATOR},
   ...     game_phase=GamePhase.SETUP
   ... )
   >>> print(state.game_phase)  # Shows SETUP


   .. autolink-examples:: MafiaGameState
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add_public_announcement(announcement: str) -> None

      Add an announcement to the public record.

      :param announcement: The announcement to add
      :type announcement: str

      .. rubric:: Example

      >>> state.add_public_announcement("Night falls on the village.")
      >>> print(state.public_announcements[-1])


      .. autolink-examples:: add_public_announcement
         :collapse:


   .. py:method:: log_action(action: haive.games.mafia.models.MafiaAction | haive.games.mafia.models.NarratorAction) -> None

      Log an action in the game history.

      This method records player and narrator actions in both the action_history
      and move_history, ensuring proper serialization of complex objects.

      :param action: Action to log
      :type action: Union[MafiaAction, NarratorAction]

      .. rubric:: Example

      >>> action = MafiaAction(
      ...     player_id="Player_1",
      ...     action_type=ActionType.VOTE,
      ...     target_id="Player_2",
      ...     phase=GamePhase.DAY_VOTING,
      ...     round_number=1
      ... )
      >>> state.log_action(action)


      .. autolink-examples:: log_action
         :collapse:


   .. py:method:: model_copy(*, deep: bool = False, **kwargs)

      Create a copy of the model.

      :param deep: Whether to create a deep copy. Defaults to False.
      :type deep: bool, optional
      :param \*\*kwargs: Additional arguments to pass to model_copy

      :returns: A copy of the current state
      :rtype: MafiaGameState

      .. rubric:: Example

      >>> new_state = state.model_copy(deep=True)


      .. autolink-examples:: model_copy
         :collapse:


   .. py:method:: update_alive_counts()

      Update the count of alive players in different roles.

      This method recalculates the number of alive players in each role
      category based on the current player states.

      .. note::

         This should be called after any change that might affect player
         life status (e.g., night kills, voting execution).

      .. rubric:: Example

      >>> state.player_states["Player_1"].is_alive = False
      >>> state.update_alive_counts()
      >>> print(state.alive_village_count)  # Shows updated count


      .. autolink-examples:: update_alive_counts
         :collapse:


   .. py:attribute:: action_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: alive_detective_count
      :type:  int
      :value: None



   .. py:attribute:: alive_doctor_count
      :type:  int
      :value: None



   .. py:attribute:: alive_mafia_count
      :type:  int
      :value: None



   .. py:attribute:: alive_village_count
      :type:  int
      :value: None



   .. py:attribute:: current_player_idx
      :type:  int
      :value: None



   .. py:attribute:: day_number
      :type:  int
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_phase
      :type:  haive.games.mafia.models.GamePhase
      :value: None



   .. py:attribute:: game_status
      :type:  str
      :value: None



   .. py:attribute:: killed_at_night
      :type:  str | None
      :value: None



   .. py:attribute:: move_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: night_deaths
      :type:  list[str]
      :value: None



   .. py:attribute:: player_data
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: player_states
      :type:  dict[str, haive.games.mafia.models.PlayerState]
      :value: None



   .. py:attribute:: players
      :type:  list[str]
      :value: None



   .. py:attribute:: public_announcements
      :type:  list[str]
      :value: None



   .. py:attribute:: public_state
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: roles
      :type:  dict[str, haive.games.mafia.models.PlayerRole]
      :value: None



   .. py:attribute:: round_number
      :type:  int
      :value: None



   .. py:attribute:: saved_at_night
      :type:  str | None
      :value: None



   .. py:attribute:: votes
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



