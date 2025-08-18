games.framework.core.space
==========================

.. py:module:: games.framework.core.space

Module documentation for games.framework.core.space


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">2 attributes</span>   </div>


      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.framework.core.space.P
      games.framework.core.space.T

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.space.Space

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Space(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


            A single space on a game board that can hold a piece.

            Spaces are the fundamental units that make up a board. Each space has a position and
            can optionally contain a game piece.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: is_occupied() -> bool

               Check if this space contains a piece.



            .. py:method:: place_piece(piece: T) -> bool

               Place a piece on this space.

               :param piece: The piece to place

               :returns: True if the piece was placed successfully, False otherwise



            .. py:method:: remove_piece() -> T | None

               Remove the piece from this space.

               :returns: The removed piece, or None if there was no piece



            .. py:attribute:: connections
               :type:  set[str]
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str | None
               :value: None



            .. py:attribute:: piece
               :type:  T | None
               :value: None



            .. py:attribute:: position
               :type:  P


            .. py:attribute:: properties
               :type:  dict[str, Any]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: P


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.space import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

