games.framework.multi_player.models
===================================

.. py:module:: games.framework.multi_player.models

Models for multi-player game framework.

This module provides common enumerations and base models used across
multi-player games. These models serve as building blocks for creating
game-specific implementations.

.. rubric:: Example

>>> from haive.agents.agent_games.framework.multi_player.models import GamePhase
>>>
>>> # Use game phases in your game state
>>> current_phase = GamePhase.SETUP
>>> if current_phase == GamePhase.MAIN:
...     # Handle main game phase
...     pass



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Models for multi-player game framework.

   This module provides common enumerations and base models used across
   multi-player games. These models serve as building blocks for creating
   game-specific implementations.

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.models import GamePhase
   >>>
   >>> # Use game phases in your game state
   >>> current_phase = GamePhase.SETUP
   >>> if current_phase == GamePhase.MAIN:
   ...     # Handle main game phase
   ...     pass



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.multi_player.models.GamePhase

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Common game phases that many games share.

            This enumeration defines standard game phases that are common across
            different types of games. Games can extend or modify these phases
            based on their specific needs.

            .. attribute:: SETUP

               Initial game setup phase for player assignments, etc.

               :type: str

            .. attribute:: MAIN

               Main gameplay phase where core game actions occur.

               :type: str

            .. attribute:: SCORING

               Phase for calculating and updating scores.

               :type: str

            .. attribute:: END

               Game conclusion phase for final state updates.

               :type: str

            .. rubric:: Example

            >>> phase = GamePhase.SETUP
            >>> if phase == GamePhase.MAIN:
            ...     # Handle main game phase
            ...     pass
            >>> # Check if game is over
            >>> is_game_over = phase == GamePhase.END

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: END
               :value: 'end'



            .. py:attribute:: MAIN
               :value: 'main'



            .. py:attribute:: SCORING
               :value: 'scoring'



            .. py:attribute:: SETUP
               :value: 'setup'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.multi_player.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

