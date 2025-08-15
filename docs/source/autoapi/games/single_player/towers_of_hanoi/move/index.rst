games.single_player.towers_of_hanoi.move
========================================

.. py:module:: games.single_player.towers_of_hanoi.move

.. autoapi-nested-parse::

   Tower of Hanoi move model.


   .. autolink-examples:: games.single_player.towers_of_hanoi.move
      :collapse:


Classes
-------

.. autoapisummary::

   games.single_player.towers_of_hanoi.move.HanoiMoveModel


Module Contents
---------------

.. py:class:: HanoiMoveModel(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for structured output of Tower of Hanoi moves.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HanoiMoveModel
      :collapse:

   .. py:method:: validate_from_peg(v: int) -> int
      :classmethod:



   .. py:method:: validate_to_peg(v: int, info: Any) -> int
      :classmethod:



   .. py:attribute:: from_peg
      :type:  int
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: to_peg
      :type:  int
      :value: None



