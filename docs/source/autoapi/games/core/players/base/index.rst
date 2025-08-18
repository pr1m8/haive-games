games.core.players.base
=======================

.. py:module:: games.core.players.base

Module documentation for games.core.players.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>


      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.core.players.base.AIPlayer
      games.core.players.base.HumanPlayer
      games.core.players.base.Player
      games.core.players.base.PlayerTypes

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AIPlayer(/, **data: Any)

            Bases: :py:obj:`Player`


            An AI player.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HumanPlayer(/, **data: Any)

            Bases: :py:obj:`Player`


            A human player.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: player_type
               :type:  PlayerTypes



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Player(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Base class for all players.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: id
               :type:  str


            .. py:attribute:: name
               :type:  str


            .. py:attribute:: player_type
               :type:  PlayerTypes



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerTypes

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of players in a game.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: AI
               :value: 'ai'



            .. py:attribute:: HUMAN
               :value: 'human'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.players.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

