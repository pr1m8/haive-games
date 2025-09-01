games.go.agent
==============

.. py:module:: games.go.agent

.. autoapi-nested-parse::

   Go game agent implementation.

   This module provides a Go game agent that supports:
       - Standard Go game rules and mechanics
       - Black and white player moves
       - Optional position analysis
       - Game state tracking and visualization
       - SGF format support via sente library

   .. rubric:: Example

   >>> from haive.games.go import GoAgent, GoAgentConfig
   >>>
   >>> # Create a Go agent with analysis enabled
   >>> config = GoAgentConfig(include_analysis=True)
   >>> agent = GoAgent(config)
   >>>
   >>> # Run a game
   >>> run_go_game(agent)



Attributes
----------

.. autoapisummary::

   games.go.agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/go/agent/GoAgent

.. autoapisummary::

   games.go.agent.GoAgent


Functions
---------

.. autoapisummary::

   games.go.agent.run_go_game


Module Contents
---------------

.. py:function:: run_go_game(agent: GoAgent) -> None

   Run a Go game with visualization and structured output.

   This function manages the game loop and provides rich visualization
   of the game state, including:
       - Board visualization using ASCII art
       - Move history tracking
       - Position analysis display
       - Captured stones counting
       - Game status updates

   :param agent: The Go agent to run the game with.
   :type agent: GoAgent

   .. rubric:: Example

   >>> agent = GoAgent(GoAgentConfig(include_analysis=True))
   >>> run_go_game(agent)

   🔷 Current Board Position:
   . . . . . . . . .
   . . . . . . . . .
   . . + . . . + . .
   . . . . . . . . .
   . . . . + . . . .
   . . . . . . . . .
   . . + . . . + . .
   . . . . . . . . .
   . . . . . . . . .

   🎮 Current Player: Black
   📌 Game Status: ongoing
   --------------------------------------------------


.. py:data:: logger

