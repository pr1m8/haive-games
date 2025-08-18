games.framework.core.move
=========================

.. py:module:: games.framework.core.move

Module documentation for games.framework.core.move


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.framework.core.move.S

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.move.Move

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Move(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`S`\ ]


            Base class for game moves.

            Moves represent changes to the game state initiated by players.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: apply(game_state: S) -> S
               :abstractmethod:


               Apply this move to the game state.

               :param game_state: The current game state

               :returns: Updated game state after applying the move



            .. py:method:: is_valid(game_state: S) -> bool
               :abstractmethod:


               Check if this move is valid in the current game state.

               :param game_state: The current game state

               :returns: True if the move is valid, False otherwise



            .. py:attribute:: move_type
               :type:  str


            .. py:attribute:: player_id
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: S




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.move import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

