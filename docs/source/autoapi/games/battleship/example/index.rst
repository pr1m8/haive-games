games.battleship.example
========================

.. py:module:: games.battleship.example

.. autoapi-nested-parse::

   Main script to run the Battleship game.

   This module provides a standalone command-line interface for running
   the Battleship game with LLM-powered agents. It features:
       - Rich text-based visualization of game boards and states
       - Command-line options for customizing game behavior
       - Progress tracking and game statistics
       - Error handling and graceful termination

   Run this script directly to start a Battleship game:
       python -m haive.games.battleship.example

   Command-line options:
       --no-visual: Disable board visualization
       --no-analysis: Disable strategic analysis
       --debug: Enable debug mode with detailed logs
       --delay: Set delay between game steps (default: 0.5s)



Attributes
----------

.. autoapisummary::

   games.battleship.example.console


Functions
---------

.. autoapisummary::

   games.battleship.example.main
   games.battleship.example.run_game


Module Contents
---------------

.. py:function:: main()

   Parse command-line arguments and run the Battleship game.

   This function handles command-line argument parsing and launches
   the Battleship game with the specified configuration options.

   Command-line arguments:
       --no-visual: Disable board visualization
       --no-analysis: Disable strategic analysis
       --debug: Enable debug mode with detailed logs
       --delay: Set delay between game steps (default: 0.5s)

   :returns: None


.. py:function:: run_game(visualize=True, debug=False, analysis=True, delay=0.5)

   Run a Battleship game with rich visualization.

   Creates and runs a complete Battleship game with the specified configuration
   options. Displays game progress, board states, and strategic analysis in
   the terminal using rich text formatting.

   :param visualize: Whether to visualize the game boards
   :param debug: Whether to enable debug mode with verbose logging
   :param analysis: Whether to enable strategic analysis by LLM agents
   :param delay: Delay between steps in seconds (controls game speed)

   :returns: None

   :raises KeyboardInterrupt: If the game is interrupted by the user
   :raises Exception: For any unexpected errors during gameplay

   .. rubric:: Examples

   >>> run_game(visualize=True, debug=False, analysis=True, delay=0.5)
   # Displays an interactive game in the terminal

   >>> run_game(visualize=False, debug=True, analysis=False)
   # Runs a game with debug logging but no visualization or analysis


.. py:data:: console

