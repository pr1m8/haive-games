games.framework.core.board
==========================

.. py:module:: games.framework.core.board

Module documentation for games.framework.core.board


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">3 attributes</span>   </div>


      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.framework.core.board.P
      games.framework.core.board.S
      games.framework.core.board.T

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.board.Board

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Board(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`S`\ , :py:obj:`P`\ , :py:obj:`T`\ ]


            Base class for all game boards.

            A Board represents the playing surface in a game, containing spaces where pieces can
            be placed. It manages the spatial relationships between spaces.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: add_space(space: S) -> str

               Add a space to the board.

               :param space: The space to add

               :returns: ID of the added space



            .. py:method:: connect_spaces(space1_id: str, space2_id: str) -> None

               Connect two spaces bidirectionally.

               :param space1_id: ID of the first space
               :param space2_id: ID of the second space

               :raises ValueError: If either space doesn't exist on the board



            .. py:method:: get_space_at_position(position: P) -> S | None
               :abstractmethod:


               Get the space at the specified position.

               This is an abstract method that must be implemented by subclasses
               to provide position-based lookup.

               :param position: The position to look up

               :returns: The space at the position, or None if no space exists there



            .. py:method:: place_piece(piece: T, position: P) -> bool

               Place a piece at the specified position.

               :param piece: The piece to place
               :param position: Position to place the piece at

               :returns: True if placement was successful, False otherwise



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str


            .. py:attribute:: properties
               :type:  dict[str, Any]
               :value: None



            .. py:attribute:: spaces
               :type:  dict[str, S]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: P


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: S


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.board import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

