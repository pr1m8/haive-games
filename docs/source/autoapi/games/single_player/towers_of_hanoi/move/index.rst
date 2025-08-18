games.single_player.towers_of_hanoi.move
========================================

.. py:module:: games.single_player.towers_of_hanoi.move

Tower of Hanoi move model.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Tower of Hanoi move model.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.towers_of_hanoi.move.HanoiMoveModel

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HanoiMoveModel(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for structured output of Tower of Hanoi moves.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.towers_of_hanoi.move import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

