games.hold_em.example
=====================

.. py:module:: games.hold_em.example

Example usage of the Texas Hold'em poker implementation.

This example script demonstrates how to:
    - Create and configure a Texas Hold'em game
    - Set up player agents with different playing styles
    - Run a complete game with the Rich UI
    - Access and analyze game results

Run this script directly to see a Hold'em game in action.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Example usage of the Texas Hold'em poker implementation.

   This example script demonstrates how to:
       - Create and configure a Texas Hold'em game
       - Set up player agents with different playing styles
       - Run a complete game with the Rich UI
       - Access and analyze game results

   Run this script directly to see a Hold'em game in action.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.hold_em.example.logger

            
            
            

.. admonition:: Functions (4)
   :class: info

   .. autoapisummary::

      games.hold_em.example.analyze_game_results
      games.hold_em.example.create_custom_game
      games.hold_em.example.main
      games.hold_em.example.run_example_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: analyze_game_results(agent: haive.games.hold_em.HoldemGameAgent)

            Analyze the results of a completed game.

            :param agent: The game agent after running a game



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Main entry point with command line argument handling.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_example_game(game_type: str = 'default', delay: float = 1.5)

            Run an example Hold'em game with the specified configuration.

            :param game_type: Type of game to run ("default", "heads-up", "tournament", "cash", "custom")
            :param delay: Delay between UI updates (seconds)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

