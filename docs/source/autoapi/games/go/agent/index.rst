
:py:mod:`games.go.agent`
========================

.. py:module:: games.go.agent

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


.. autolink-examples:: games.go.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.go.agent.GoAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GoAgent {
        node [shape=record];
        "GoAgent" [label="GoAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.go.config.GoAgentConfig]" -> "GoAgent";
      }

.. autoclass:: games.go.agent.GoAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.go.agent.run_go_game

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


   .. autolink-examples:: run_go_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.go.agent
   :collapse:
   
.. autolink-skip:: next
