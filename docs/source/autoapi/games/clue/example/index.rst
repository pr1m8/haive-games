
:py:mod:`games.clue.example`
============================

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


.. autolink-examples:: games.clue.example
   :collapse:


Functions
---------

.. autoapisummary::

   games.clue.example.run_clue_game

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


   .. autolink-examples:: run_clue_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.clue.example
   :collapse:
   
.. autolink-skip:: next
