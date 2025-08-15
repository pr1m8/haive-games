games.framework.core.game
=========================

.. py:module:: games.framework.core.game


Attributes
----------

.. autoapisummary::

   games.framework.core.game.M
   games.framework.core.game.S


Classes
-------

.. autoapisummary::

   games.framework.core.game.Game
   games.framework.core.game.GameStatus
   games.framework.core.game.Player


Module Contents
---------------

.. py:class:: Game(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`S`\ , :py:obj:`M`\ ]


   Base class for all games.

   A Game represents a complete playable game with turns, moves, and state.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Game
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add_player(player: Player) -> None

      Add a player to the game.

      :param player: The player to add


      .. autolink-examples:: add_player
         :collapse:


   .. py:method:: check_game_over() -> bool

      Check if the game is over.

      :returns: True if the game is over, False otherwise


      .. autolink-examples:: check_game_over
         :collapse:


   .. py:method:: end_turn() -> None

      End the current turn and advance to the next player.


      .. autolink-examples:: end_turn
         :collapse:


   .. py:method:: get_current_player() -> Player | None

      Get the current player.

      :returns: The current player, or None if no players


      .. autolink-examples:: get_current_player
         :collapse:


   .. py:method:: make_move(move: M) -> bool

      Make a move in the game.

      Validates the move, applies it to the state, and updates the turn.

      :param move: The move to make

      :returns: True if the move was valid and applied, False otherwise


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: start_game() -> None

      Start the game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:method:: start_turn() -> haive.games.framework.core.turn.Turn[M]

      Start a new turn for the current player.

      :returns: The new turn


      .. autolink-examples:: start_turn
         :collapse:


   .. py:attribute:: current_player_idx
      :type:  int
      :value: 0



   .. py:property:: current_turn
      :type: haive.games.framework.core.turn.Turn[M] | None


      Get the current turn, if any.

      .. autolink-examples:: current_turn
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: players
      :type:  list[Player]
      :value: None



   .. py:attribute:: state
      :type:  S


   .. py:attribute:: status
      :type:  GameStatus


   .. py:property:: turn_number
      :type: int


      Get the current turn number.

      .. autolink-examples:: turn_number
         :collapse:


   .. py:attribute:: turns
      :type:  list[haive.games.framework.core.turn.Turn[M]]
      :value: None



   .. py:attribute:: winner_id
      :type:  str | None
      :value: None



.. py:class:: GameStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Possible statuses of a game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameStatus
      :collapse:

   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: NOT_STARTED
      :value: 'not_started'



   .. py:attribute:: PAUSED
      :value: 'paused'



.. py:class:: Player(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A player in a game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Player
      :collapse:

   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



.. py:data:: M

.. py:data:: S

