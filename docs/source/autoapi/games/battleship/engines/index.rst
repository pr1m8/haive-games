games.battleship.engines
========================

.. py:module:: games.battleship.engines

.. autoapi-nested-parse::

   Battleship game engine configurations.

   This module provides engine configurations for the Battleship game, including:
       - Player decision engines
       - Ship placement engines
       - Analysis engines



Functions
---------

.. autoapisummary::

   games.battleship.engines.build_battleship_engines


Module Contents
---------------

.. py:function:: build_battleship_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build engine configurations for the Battleship game.

   This function creates AugLLMConfig objects for:
       - Player 1 ship placement
       - Player 2 ship placement
       - Player 1 move selection
       - Player 2 move selection
       - Player 1 analysis
       - Player 2 analysis

   :returns: Dictionary of engine configurations
   :rtype: Dict[str, AugLLMConfig]


