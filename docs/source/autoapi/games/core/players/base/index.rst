games.core.players.base
=======================

.. py:module:: games.core.players.base


Classes
-------

.. autoapisummary::

   games.core.players.base.AIPlayer
   games.core.players.base.HumanPlayer
   games.core.players.base.Player
   games.core.players.base.PlayerTypes


Module Contents
---------------

.. py:class:: AIPlayer(/, **data: Any)

   Bases: :py:obj:`Player`


   An AI player.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AIPlayer
      :collapse:

.. py:class:: HumanPlayer(/, **data: Any)

   Bases: :py:obj:`Player`


   A human player.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HumanPlayer
      :collapse:

   .. py:attribute:: player_type
      :type:  PlayerTypes


.. py:class:: Player(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for all players.

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


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: player_type
      :type:  PlayerTypes


.. py:class:: PlayerTypes

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of players in a game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerTypes
      :collapse:

   .. py:attribute:: AI
      :value: 'ai'



   .. py:attribute:: HUMAN
      :value: 'human'



