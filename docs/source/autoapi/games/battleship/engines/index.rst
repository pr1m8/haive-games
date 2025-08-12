
:py:mod:`games.battleship.engines`
==================================

.. py:module:: games.battleship.engines

Battleship game engine configurations.

This module provides engine configurations for the Battleship game, including:
    - Player decision engines
    - Ship placement engines
    - Analysis engines


.. autolink-examples:: games.battleship.engines
   :collapse:


Functions
---------

.. autoapisummary::

   games.battleship.engines.build_battleship_engines

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


   .. autolink-examples:: build_battleship_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.battleship.engines
   :collapse:
   
.. autolink-skip:: next
