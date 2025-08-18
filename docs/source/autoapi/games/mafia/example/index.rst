games.mafia.example
===================

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

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



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mafia.example.logger

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.mafia.example.main
      games.mafia.example.run_mafia_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Main entry point for command-line execution.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mafia.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

