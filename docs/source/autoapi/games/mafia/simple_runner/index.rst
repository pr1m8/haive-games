games.mafia.simple_runner
=========================

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

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



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mafia.simple_runner.logger

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.mafia.simple_runner.main
      games.mafia.simple_runner.run_mafia_game_simple

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main() -> None

            Main entry point for command-line execution.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mafia.simple_runner import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

