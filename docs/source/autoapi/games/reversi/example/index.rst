games.reversi.example
=====================

.. py:module:: games.reversi.example

.. autoapi-nested-parse::

   Example Reversi (Othello) game demonstrating the Haive Reversi implementation.

   This module provides a simple example of running a Reversi game with AI players
   using the Haive framework. Reversi, also known as Othello, is a strategy board
   game where players flip opponent pieces by trapping them between their own pieces.

   The example demonstrates:
       - Creating a Reversi agent with default configuration
       - Running a complete game with visual board display
       - AI players making strategic moves
       - Automatic piece flipping and rule enforcement
       - Winner determination based on final piece count

   Usage:
       Run directly:
           $ python example.py

       Import and use:
           >>> from haive.games.reversi.agent import ReversiAgent
           >>> agent = ReversiAgent()
           >>> final_state = agent.run_game(visualize=True)

   Game Rules:
       - Players take turns placing pieces on the board
       - Valid moves must flip at least one opponent piece
       - Pieces are flipped when trapped between two of your pieces
       - Game ends when no valid moves remain
       - Winner has the most pieces on the board

   .. rubric:: Example

   >>> # Create and run a Reversi game
   >>> agent = ReversiAgent()
   >>> state = agent.run_game(visualize=True)
   >>> print(f"Winner: {state.get('winner', 'Draw')}")


   .. autolink-examples:: games.reversi.example
      :collapse:


Functions
---------

.. autoapisummary::

   games.reversi.example.run_reversi_demo


Module Contents
---------------

.. py:function:: run_reversi_demo()

   Run a quick Reversi demo - only when called directly.


   .. autolink-examples:: run_reversi_demo
      :collapse:

