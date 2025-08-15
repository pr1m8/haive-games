games.multi_player.models
=========================

.. py:module:: games.multi_player.models

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


   .. autolink-examples:: games.multi_player.models
      :collapse:


Classes
-------

.. autoapisummary::

   games.multi_player.models.GamePhase


Module Contents
---------------

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


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePhase
      :collapse:

   .. py:attribute:: END
      :value: 'end'



   .. py:attribute:: MAIN
      :value: 'main'



   .. py:attribute:: SCORING
      :value: 'scoring'



   .. py:attribute:: SETUP
      :value: 'setup'



