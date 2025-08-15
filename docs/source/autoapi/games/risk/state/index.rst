games.risk.state
================

.. py:module:: games.risk.state

.. autoapi-nested-parse::

   State model for the Risk game.

   This module defines the state model for the Risk game, tracking the game board, player
   information, and game status.


   .. autolink-examples:: games.risk.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.risk.state.RiskState


Module Contents
---------------

.. py:class:: RiskState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for the Risk game.

   .. attribute:: territories

      Dictionary of territory objects, keyed by name.

   .. attribute:: continents

      Dictionary of continent objects, keyed by name.

   .. attribute:: players

      Dictionary of player objects, keyed by name.

   .. attribute:: current_player

      Name of the player whose turn it is.

   .. attribute:: phase

      Current phase of the game.

   .. attribute:: game_status

      Current status of the game.

   .. attribute:: turn_number

      Current turn number.

   .. attribute:: deck

      List of cards in the deck.

   .. attribute:: next_card_set_value

      Value of the next set of cards to be traded in.

   .. attribute:: move_history

      List of moves that have been made.

   .. attribute:: player_analyses

      Dictionary of player analyses, keyed by player name.

   .. attribute:: attacker_captured_territory

      Whether the attacker captured a territory this turn.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RiskState
      :collapse:

   .. py:method:: _initialize_armies() -> None

      Calculate and assign initial armies to players.


      .. autolink-examples:: _initialize_armies
         :collapse:


   .. py:method:: _initialize_deck() -> None

      Initialize the deck of Risk cards.


      .. autolink-examples:: _initialize_deck
         :collapse:


   .. py:method:: _initialize_map() -> None

      Initialize the Risk map with territories and continents.


      .. autolink-examples:: _initialize_map
         :collapse:


   .. py:method:: get_controlled_continents(player_name: str) -> list[haive.games.risk.models.Continent]

      Get all continents controlled by a player.

      :param player_name: Name of the player.

      :returns: List of continents controlled by the player.


      .. autolink-examples:: get_controlled_continents
         :collapse:


   .. py:method:: get_controlled_territories(player_name: str) -> list[haive.games.risk.models.Territory]

      Get all territories controlled by a player.

      :param player_name: Name of the player.

      :returns: List of territories controlled by the player.


      .. autolink-examples:: get_controlled_territories
         :collapse:


   .. py:method:: get_winner() -> str | None

      Get the winner of the game.

      :returns: Name of the winner, or None if the game is not over.


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: initialize(player_names: list[str]) -> RiskState
      :classmethod:


      Initialize a new Risk game state.

      :param player_names: List of player names.

      :returns: A new RiskState object with default values.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.

      :returns: True if the game is over, False otherwise.


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:attribute:: attacker_captured_territory
      :type:  bool
      :value: False



   .. py:attribute:: continents
      :type:  dict[str, haive.games.risk.models.Continent]
      :value: None



   .. py:attribute:: current_player
      :type:  str
      :value: ''



   .. py:attribute:: deck
      :type:  list[haive.games.risk.models.Card]
      :value: None



   .. py:attribute:: game_status
      :type:  haive.games.risk.models.GameStatus


   .. py:attribute:: move_history
      :type:  list[haive.games.risk.models.RiskMove]
      :value: None



   .. py:attribute:: next_card_set_value
      :type:  int
      :value: 4



   .. py:attribute:: phase
      :type:  haive.games.risk.models.PhaseType


   .. py:attribute:: player_analyses
      :type:  dict[str, list[haive.games.risk.models.RiskAnalysis]]
      :value: None



   .. py:attribute:: players
      :type:  dict[str, haive.games.risk.models.Player]
      :value: None



   .. py:attribute:: territories
      :type:  dict[str, haive.games.risk.models.Territory]
      :value: None



   .. py:attribute:: turn_number
      :type:  int
      :value: 1



