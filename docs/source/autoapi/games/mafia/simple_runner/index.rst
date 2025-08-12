
:py:mod:`games.mafia.simple_runner`
===================================

.. py:module:: games.mafia.simple_runner

Simple runner for the Mafia game that avoids LangGraph issues.

This module provides a simplified version of the Mafia game runner that
avoids the streaming issues in LangGraph by:
    - Using direct state manipulation instead of graph streaming
    - Following the game logic manually through phases
    - Providing the same visualization and game experience

.. rubric:: Example

```bash
python simple_runner.py --players 7 --days 3 --debug
```


.. autolink-examples:: games.mafia.simple_runner
   :collapse:


Functions
---------

.. autoapisummary::

   games.mafia.simple_runner.main
   games.mafia.simple_runner.run_mafia_game_simple

.. py:function:: main() -> None

   Main entry point for command-line execution.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_mafia_game_simple(player_count: int = 5, max_days: int = 1, debug: bool = True) -> None

   Run a simplified Mafia game simulation with direct state management.

   This function sets up and executes a full Mafia game, handling:
       - Player creation and role assignment
       - Game state initialization
       - Turn-based gameplay execution
       - State visualization
       - Game end conditions

   :param player_count: Total number of players including narrator.
                        Must be at least 4 (3 players + narrator). Defaults to 5.
   :param max_days: Maximum number of in-game days before forcing
                    game end. Defaults to 3.
   :param debug: Enable debug mode for detailed logging.
                 Defaults to True.

   :raises ValueError: If player_count is less than 4.


   .. autolink-examples:: run_mafia_game_simple
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mafia.simple_runner
   :collapse:
   
.. autolink-skip:: next
