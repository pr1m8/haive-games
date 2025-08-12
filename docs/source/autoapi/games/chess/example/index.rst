
:py:mod:`games.chess.example`
=============================

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


.. autolink-examples:: games.chess.example
   :collapse:


Functions
---------

.. autoapisummary::

   games.chess.example.run_chess_game

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



   .. autolink-examples:: run_chess_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.chess.example
   :collapse:
   
.. autolink-skip:: next
