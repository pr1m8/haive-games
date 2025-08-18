games.reversi.example
=====================

.. py:module:: games.reversi.example

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span>   </div>

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



      
            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.reversi.example.run_reversi_demo

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_reversi_demo()

            Run a quick Reversi demo - only when called directly.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.reversi.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

