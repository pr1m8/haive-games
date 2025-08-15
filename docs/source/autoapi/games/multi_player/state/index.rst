games.multi_player.state
========================

.. py:module:: games.multi_player.state

.. autoapi-nested-parse::

   Base state management for multi-player games.

   This module provides the foundational state model for multi-player games,
   supporting features like:
       - Player tracking and turn management
       - Game phase transitions
       - Move history recording
       - Public and private state management
       - Error handling

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.state import MultiPlayerGameState
   >>>
   >>> # Create a game state
   >>> state = MultiPlayerGameState(
   ...     players=["player1", "player2", "player3"],
   ...     game_phase=GamePhase.SETUP
   ... )
   >>>
   >>> # Advance to next player
   >>> next_player = state.advance_player()


   .. autolink-examples:: games.multi_player.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.multi_player.state.MultiPlayerGameState


Module Contents
---------------

.. py:class:: MultiPlayerGameState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base game state for multi-player games.

   This class provides the foundation for managing game state in multi-player
   games. It handles player turns, game phases, move history, and both public
   and private state information.

   .. attribute:: players

      List of player names/IDs.

      :type: List[str]

   .. attribute:: current_player_idx

      Index of current player in players list.

      :type: int

   .. attribute:: game_phase

      Current phase of the game (see GamePhase enum).

      :type: str

   .. attribute:: game_status

      Status of the game (e.g., "ongoing", "ended").

      :type: str

   .. attribute:: move_history

      History of all moves made.

      :type: List[Dict[str, Any]]

   .. attribute:: round_number

      Current round number.

      :type: int

   .. attribute:: player_data

      Private data for each player.

      :type: Dict[str, Dict[str, Any]]

   .. attribute:: public_state

      Public game state visible to all.

      :type: Dict[str, Any]

   .. attribute:: error_message

      Error message if any.

      :type: Optional[str]

   .. rubric:: Example

   >>> state = MultiPlayerGameState(
   ...     players=["player1", "player2"],
   ...     game_phase=GamePhase.SETUP
   ... )
   >>> state.advance_player()
   'player2'
   >>> private_data = state.get_player_private_data("player1")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiPlayerGameState
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: advance_player() -> str

      Advance to the next player and return their name/ID.

      This method updates the current_player_idx to the next player in
      the rotation and returns the new current player's name/ID.

      :returns: The next player's name/ID.
      :rtype: str

      .. rubric:: Example

      >>> state = MultiPlayerGameState(players=["p1", "p2", "p3"])
      >>> state.advance_player()
      'p2'
      >>> state.advance_player()  # Advances to p3
      'p3'
      >>> state.advance_player()  # Wraps back to p1
      'p1'


      .. autolink-examples:: advance_player
         :collapse:


   .. py:method:: get_player_private_data(player_id: str) -> dict[str, Any]

      Get private data for a specific player.

      This method safely retrieves the private state data for a given player,
      returning an empty dict if no data exists.

      :param player_id: The ID of the player whose data to retrieve.
      :type player_id: str

      :returns: The player's private data, or empty dict if none exists.
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> state = MultiPlayerGameState(players=["p1", "p2"])
      >>> state.player_data["p1"] = {"secret_info": 42}
      >>> state.get_player_private_data("p1")
      {'secret_info': 42}
      >>> state.get_player_private_data("unknown")
      {}


      .. autolink-examples:: get_player_private_data
         :collapse:


   .. py:property:: current_player
      :type: str


      Get the current player's name/ID.

      :returns: The current player's name/ID, or empty string if invalid index.
      :rtype: str

      .. rubric:: Example

      >>> state = MultiPlayerGameState(players=["p1", "p2"])
      >>> state.current_player
      'p1'

      .. autolink-examples:: current_player
         :collapse:


   .. py:attribute:: current_player_idx
      :type:  int
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_phase
      :type:  str
      :value: None



   .. py:attribute:: game_status
      :type:  str
      :value: None



   .. py:attribute:: move_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: player_data
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: players
      :type:  list[str]
      :value: None



   .. py:attribute:: public_state
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: round_number
      :type:  int
      :value: None



