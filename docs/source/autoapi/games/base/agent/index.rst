
:py:mod:`games.base.agent`
==========================

.. py:module:: games.base.agent

Base game agent module.

This module provides the foundational GameAgent class that implements common workflow patterns
for game-specific agents. It handles game initialization, move generation, position analysis,
and game flow control.

.. rubric:: Example

>>> class ChessAgent(GameAgent[ChessConfig]):
...     def __init__(self, config: ChessConfig):
...         super().__init__(config)
...         self.state_manager = ChessStateManager

Typical usage:
    - Inherit from GameAgent to create game-specific agents
    - Override necessary methods like prepare_move_context and extract_move
    - Use the setup_workflow method to customize the game flow


.. autolink-examples:: games.base.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.base.agent.GameAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GameAgent {
        node [shape=record];
        "GameAgent" [label="GameAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.framework.base.config.GameConfig]" -> "GameAgent";
        "Generic[T]" -> "GameAgent";
      }

.. autoclass:: games.base.agent.GameAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.base.agent.run_game

.. py:function:: run_game(agent: GameAgent, initial_state: dict[str, Any] | None = None)

   Run a complete game with the given agent.

   This function executes a game from start to finish using the provided agent.
   It handles game initialization, move execution, state visualization, and
   error reporting. The game can optionally start from a provided initial state.

   :param agent: The game agent to run the game with.
   :type agent: GameAgent
   :param initial_state: Initial game state.
                         If not provided, a new game will be initialized. Defaults to None.
   :type initial_state: Optional[Dict[str, Any]], optional

   .. rubric:: Example

   >>> agent = ChessAgent(ChessConfig())
   >>> # Start a new game
   >>> run_game(agent)
   >>>
   >>> # Continue from a saved state
   >>> run_game(agent, saved_state)

   .. note::

      - The function will print game progress to the console
      - Game visualization depends on the agent's visualize_state method
      - Game history will be saved using the agent's save_state_history method


   .. autolink-examples:: run_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.base.agent
   :collapse:
   
.. autolink-skip:: next
