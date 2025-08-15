games.framework.core.move
=========================

.. py:module:: games.framework.core.move


Attributes
----------

.. autoapisummary::

   games.framework.core.move.S


Classes
-------

.. autoapisummary::

   games.framework.core.move.Move


Module Contents
---------------

.. py:class:: Move(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`S`\ ]


   Base class for game moves.

   Moves represent changes to the game state initiated by players.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Move
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: apply(game_state: S) -> S
      :abstractmethod:


      Apply this move to the game state.

      :param game_state: The current game state

      :returns: Updated game state after applying the move


      .. autolink-examples:: apply
         :collapse:


   .. py:method:: is_valid(game_state: S) -> bool
      :abstractmethod:


      Check if this move is valid in the current game state.

      :param game_state: The current game state

      :returns: True if the move is valid, False otherwise


      .. autolink-examples:: is_valid
         :collapse:


   .. py:attribute:: move_type
      :type:  str


   .. py:attribute:: player_id
      :type:  str


.. py:data:: S

