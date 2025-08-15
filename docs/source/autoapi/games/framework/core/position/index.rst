games.framework.core.position
=============================

.. py:module:: games.framework.core.position


Classes
-------

.. autoapisummary::

   games.framework.core.position.Position


Module Contents
---------------

.. py:class:: Position(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for all position types in games.

   A Position represents a location in a game, with different games using different
   coordinate systems.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Position
      :collapse:

   .. py:class:: Config

      .. py:attribute:: frozen
         :value: True




   .. py:method:: __eq__(other: object) -> bool

      Equality check must be implemented by subclasses.

      The base implementation just checks if the IDs match.



      .. autolink-examples:: __eq__
         :collapse:


   .. py:method:: __hash__() -> int

      Hash implementation must be consistent with __eq__.

      The base implementation uses the ID.



      .. autolink-examples:: __hash__
         :collapse:


   .. py:method:: serialize() -> dict[str, Any]

      Convert the position to a serializable dictionary.


      .. autolink-examples:: serialize
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



