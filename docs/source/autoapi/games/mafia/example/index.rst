
:py:mod:`games.mafia.example`
=============================

.. py:module:: games.mafia.example

Example implementation and runner for the Mafia game.

This module provides a complete example of how to set up and run a Mafia game,
including:
    - Game configuration and initialization
    - Player setup with role assignment
    - Game execution with visualization
    - Debug logging and error handling
    - Command-line interface for game parameters

.. rubric:: Example

To run a game from the command line:
```bash
python example.py --players 7 --days 3 --debug
```

To run programmatically:
```python
from mafia.example import run_mafia_game
run_mafia_game(player_count=7, max_days=3, debug=True)
```


.. autolink-examples:: games.mafia.example
   :collapse:


Functions
---------

.. autoapisummary::

   games.mafia.example.main
   games.mafia.example.run_mafia_game

.. py:function:: main()

   Main entry point for command-line execution.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_mafia_game(player_count: int = 5, max_days: int = 3, debug: bool = True) -> None

   Run a complete Mafia game simulation with visualization.

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
   :raises Exception: If game setup or execution fails.


   .. autolink-examples:: run_mafia_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mafia.example
   :collapse:
   
.. autolink-skip:: next
