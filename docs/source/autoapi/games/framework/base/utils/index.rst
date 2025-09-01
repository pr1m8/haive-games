games.framework.base.utils
==========================

.. py:module:: games.framework.base.utils

.. autoapi-nested-parse::

   Utility functions for game agents.

   This module provides utility functions for running and managing game agents,
   including game execution and state visualization.

   .. rubric:: Example

   >>> agent = ChessAgent(config)
   >>> run_game(agent)  # Run a new game
   >>> run_game(agent, initial_state=saved_state)  # Continue from a saved state

   Typical usage:
       - Use run_game to execute a complete game with an agent
       - Provide optional initial state to continue from a specific point
       - Monitor game progress through visualization and status updates



Functions
---------

.. autoapisummary::

   games.framework.base.utils.run_game


Module Contents
---------------

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


