
:py:mod:`games.clue.runner`
===========================

.. py:module:: games.clue.runner

Runner script for the Clue game.

This script demonstrates how to initialize and run a Clue game.


.. autolink-examples:: games.clue.runner
   :collapse:


Functions
---------

.. autoapisummary::

   games.clue.runner.main
   games.clue.runner.run_clue_game

.. py:function:: main()
   :async:


   Run the Clue game as a demonstration.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_clue_game(player_names: list[str], max_turns: int = 20, num_ai_players: int = 0) -> dict[str, Any]
   :async:


   Run a complete Clue game with the specified players.

   :param player_names: Names of the players
   :param max_turns: Maximum number of turns
   :param num_ai_players: Number of AI players (the first n players will be AI)

   :returns: Final game state information


   .. autolink-examples:: run_clue_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.clue.runner
   :collapse:
   
.. autolink-skip:: next
