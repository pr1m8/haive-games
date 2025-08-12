
:py:mod:`games.hold_em.example`
===============================

.. py:module:: games.hold_em.example

Example usage of the Texas Hold'em poker implementation.

This example script demonstrates how to:
    - Create and configure a Texas Hold'em game
    - Set up player agents with different playing styles
    - Run a complete game with the Rich UI
    - Access and analyze game results

Run this script directly to see a Hold'em game in action.


.. autolink-examples:: games.hold_em.example
   :collapse:


Functions
---------

.. autoapisummary::

   games.hold_em.example.analyze_game_results
   games.hold_em.example.create_custom_game
   games.hold_em.example.main
   games.hold_em.example.run_example_game

.. py:function:: analyze_game_results(agent: haive.games.hold_em.HoldemGameAgent)

   Analyze the results of a completed game.

   :param agent: The game agent after running a game


   .. autolink-examples:: analyze_game_results
      :collapse:

.. py:function:: create_custom_game(player_names: list[str], player_styles: list[str] | None = None, starting_chips: int = 1000, small_blind: int = 10, big_blind: int = 20, max_hands: int = 50) -> haive.games.hold_em.HoldemGameAgent

   Create a custom Hold'em game with specified players and settings.

   :param player_names: List of player names
   :param player_styles: Optional list of player styles (defaults to "balanced" for all)
   :param starting_chips: Starting chips per player
   :param small_blind: Small blind amount
   :param big_blind: Big blind amount
   :param max_hands: Maximum hands to play

   :returns: Configured game agent ready to run
   :rtype: HoldemGameAgent


   .. autolink-examples:: create_custom_game
      :collapse:

.. py:function:: main()

   Main entry point with command line argument handling.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_example_game(game_type: str = 'default', delay: float = 1.5)

   Run an example Hold'em game with the specified configuration.

   :param game_type: Type of game to run ("default", "heads-up", "tournament", "cash", "custom")
   :param delay: Delay between UI updates (seconds)


   .. autolink-examples:: run_example_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.hold_em.example
   :collapse:
   
.. autolink-skip:: next
