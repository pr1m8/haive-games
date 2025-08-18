games.single_player.towers_of_hanoi.position
============================================

.. py:module:: games.single_player.towers_of_hanoi.position

Module documentation for games.single_player.towers_of_hanoi.position


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.towers_of_hanoi.position.PegPosition

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PegPosition(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.core.position.Position`


            Position on a Tower of Hanoi peg.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool

               Equality check must be implemented by subclasses.

               The base implementation just checks if the IDs match.




            .. py:method:: __hash__() -> int

               Hash implementation must be consistent with __eq__.

               The base implementation uses the ID.




            .. py:method:: validate_level(v: int) -> int
               :classmethod:


               Ensure level is valid.



            .. py:property:: display_coords
               :type: str


               Return human-readable coordinates.


            .. py:attribute:: level
               :type:  int


            .. py:attribute:: peg
               :type:  PegNumber





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.towers_of_hanoi.position import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

