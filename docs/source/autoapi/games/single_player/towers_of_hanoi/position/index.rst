games.single_player.towers_of_hanoi.position
============================================

.. py:module:: games.single_player.towers_of_hanoi.position


Classes
-------

.. autoapisummary::

   games.single_player.towers_of_hanoi.position.PegPosition


Module Contents
---------------

.. py:class:: PegPosition

   Bases: :py:obj:`haive.games.framework.core.position.Position`


   Position on a Tower of Hanoi peg.


   .. autolink-examples:: PegPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: validate_level(v: int) -> int
      :classmethod:


      Ensure level is valid.


      .. autolink-examples:: validate_level
         :collapse:


   .. py:property:: display_coords
      :type: str


      Return human-readable coordinates.

      .. autolink-examples:: display_coords
         :collapse:


   .. py:attribute:: level
      :type:  int


   .. py:attribute:: peg
      :type:  PegNumber


