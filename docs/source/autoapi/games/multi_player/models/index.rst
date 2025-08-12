
:py:mod:`games.multi_player.models`
===================================

.. py:module:: games.multi_player.models

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_GamePhase {
        node [shape=record];
        "GamePhase" [label="GamePhase"];
        "str" -> "GamePhase";
        "enum.Enum" -> "GamePhase";
      }

.. autoclass:: games.multi_player.models.GamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePhase** is an Enum defined in ``games.multi_player.models``.





.. rubric:: Related Links

.. autolink-examples:: games.multi_player.models
   :collapse:
   
.. autolink-skip:: next
