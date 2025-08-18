games.clue.example
==================

.. py:module:: games.clue.example

Clue example module.

This module provides an example of running a Clue game with the rich UI visualization.

It demonstrates how to:
    - Configure and initialize the Clue game
    - Set up the game state
    - Visualize the game with the rich UI
    - Process game turns with guesses and responses
    - Handle game over conditions

The module uses a standard CLI interface with argument parsing
to allow customization of game behavior.

.. rubric:: Example

Run this script directly to start a Clue game:
    python -m haive.games.clue.example

Command-line options:
    --debug: Enable debug mode with detailed logging
    --turns: Set maximum number of turns (default: 10)
    --delay: Set delay between moves in seconds (default: 1.0)



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Clue example module.

   This module provides an example of running a Clue game with the rich UI visualization.

   It demonstrates how to:
       - Configure and initialize the Clue game
       - Set up the game state
       - Visualize the game with the rich UI
       - Process game turns with guesses and responses
       - Handle game over conditions

   The module uses a standard CLI interface with argument parsing
   to allow customization of game behavior.

   .. rubric:: Example

   Run this script directly to start a Clue game:
       python -m haive.games.clue.example

   Command-line options:
       --debug: Enable debug mode with detailed logging
       --turns: Set maximum number of turns (default: 10)
       --delay: Set delay between moves in seconds (default: 1.0)



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.clue.example.logger
      games.clue.example.parser

            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.clue.example.run_clue_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_clue_game(debug: bool = False, max_turns: int = 10, delay: float = 1.0)

            Run a Clue game with rich UI visualization.

            This function sets up and runs a Clue game with test moves (for demonstration)
            with rich terminal visualization. It handles a simplified game flow with
            a few predetermined moves for UI testing.

            :param debug: Enable debug mode with detailed logging
            :type debug: bool
            :param max_turns: Maximum number of turns before the game ends
            :type max_turns: int
            :param delay: Delay between moves in seconds for better readability
            :type delay: float

            :returns: None

            .. rubric:: Example

            >>> run_clue_game(debug=True, max_turns=5, delay=0.5)
            # Runs a test game with debug logging, 5 max turns, and 0.5s delay



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: parser




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

