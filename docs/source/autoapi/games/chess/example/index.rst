games.chess.example
===================

.. py:module:: games.chess.example

Example chess game runner.

This module provides an example of how to run a complete chess game
using the Haive chess module, demonstrating:
    - Agent configuration
    - State initialization
    - Game streaming
    - Event monitoring

This is intended as a basic demonstration of the chess module's capabilities
and can be used as a starting point for more complex implementations.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Example chess game runner.

   This module provides an example of how to run a complete chess game
   using the Haive chess module, demonstrating:
       - Agent configuration
       - State initialization
       - Game streaming
       - Event monitoring

   This is intended as a basic demonstration of the chess module's capabilities
   and can be used as a starting point for more complex implementations.



      
            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.chess.example.run_chess_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_chess_game(thread_id: str = None)

            Run a complete chess game with LLM players.

            Creates and runs a chess game between two LLM players, streaming
            the game events and tracking the game status until completion.

            :param thread_id: Unique identifier for the game thread.
                              If not provided, a random ID will be generated. Defaults to None.
            :type thread_id: str, optional

            :returns: The function outputs game progress to the console.
            :rtype: None

            .. rubric:: Examples

            >>> # Run a game with a random thread ID
            >>> run_chess_game()

            >>> # Run a game with a specific thread ID
            >>> run_chess_game("chess_custom_id")

            .. note::

               This function will run a full chess game with the following configuration:
               - Both white and black players powered by LLMs
               - Position analysis enabled
               - Maximum 200 moves before forcing a draw
               - Streaming output of game events

            The function handles errors gracefully and reports the final game result.






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

