games.framework.core.container
==============================

.. py:module:: games.framework.core.container

Module documentation for games.framework.core.container


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.framework.core.container.T

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.container.GamePieceContainer

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePieceContainer(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


            Base container for game pieces.

            This represents a collection of game pieces like a deck of cards, a bag of tiles, or
            a player's hand.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: add(piece: T, position: str = 'top') -> None

               Add a piece to this container.

               :param piece: The piece to add
               :param position: Where to add the piece ("top", "bottom", or "random")



            .. py:method:: count() -> int

               Count pieces in the container.



            .. py:method:: is_empty() -> bool

               Check if container is empty.



            .. py:method:: remove(piece_id: str) -> T | None

               Remove a piece by ID.

               :param piece_id: ID of the piece to remove

               :returns: The removed piece, or None if not found



            .. py:method:: shuffle() -> None

               Shuffle the pieces in the container.



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str


            .. py:attribute:: pieces
               :type:  list[T]
               :value: None



            .. py:attribute:: properties
               :type:  dict[str, Any]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.container import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

