games.framework.core.turn
=========================

.. py:module:: games.framework.core.turn

Module documentation for games.framework.core.turn


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.framework.core.turn.M

            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.framework.core.turn.Turn
      games.framework.core.turn.TurnPhase

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Turn(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`M`\ ]


            Represents a player's turn in a game.

            A turn tracks who is active, what phase the turn is in, and what moves have been
            made.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: add_move(move: M) -> None

               Record a move made during this turn.

               :param move: The move that was made



            .. py:method:: get_move_count() -> int

               Get the number of moves made this turn.



            .. py:method:: next_phase() -> TurnPhase

               Advance to the next phase.

               :returns: The new phase



            .. py:method:: set_phase(phase: TurnPhase) -> None

               Set the current phase of the turn.

               :param phase: The phase to set



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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TurnPhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Common phases within a turn.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CLEANUP
               :value: 'cleanup'



            .. py:attribute:: MAIN
               :value: 'main'



            .. py:attribute:: SETUP
               :value: 'setup'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: M




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.turn import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

