games.framework.core.turn
=========================

.. py:module:: games.framework.core.turn


Attributes
----------

.. autoapisummary::

   games.framework.core.turn.M


Classes
-------

.. autoapisummary::

   games.framework.core.turn.Turn
   games.framework.core.turn.TurnPhase


Module Contents
---------------

.. py:class:: Turn(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`M`\ ]


   Represents a player's turn in a game.

   A turn tracks who is active, what phase the turn is in, and what moves have been
   made.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Turn
      :collapse:

   .. py:method:: add_move(move: M) -> None

      Record a move made during this turn.

      :param move: The move that was made


      .. autolink-examples:: add_move
         :collapse:


   .. py:method:: get_move_count() -> int

      Get the number of moves made this turn.


      .. autolink-examples:: get_move_count
         :collapse:


   .. py:method:: next_phase() -> TurnPhase

      Advance to the next phase.

      :returns: The new phase


      .. autolink-examples:: next_phase
         :collapse:


   .. py:method:: set_phase(phase: TurnPhase) -> None

      Set the current phase of the turn.

      :param phase: The phase to set


      .. autolink-examples:: set_phase
         :collapse:


   .. py:attribute:: moves
      :type:  list[M]
      :value: None



   .. py:attribute:: phase
      :type:  TurnPhase


   .. py:attribute:: player_id
      :type:  str


   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: turn_number
      :type:  int


.. py:class:: TurnPhase

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Common phases within a turn.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TurnPhase
      :collapse:

   .. py:attribute:: CLEANUP
      :value: 'cleanup'



   .. py:attribute:: MAIN
      :value: 'main'



   .. py:attribute:: SETUP
      :value: 'setup'



.. py:data:: M

