
:py:mod:`games.fox_and_geese.enhanced_example`
==============================================

.. py:module:: games.fox_and_geese.enhanced_example

Enhanced example runner for Fox and Geese game with Rich UI visualization.


.. autolink-examples:: games.fox_and_geese.enhanced_example
   :collapse:


Functions
---------

.. autoapisummary::

   games.fox_and_geese.enhanced_example.demo_ui_features
   games.fox_and_geese.enhanced_example.run_fox_and_geese_game

.. py:function:: demo_ui_features(delay: float = 0.5)

   Demonstrate UI features with a sample game state.

   :param delay: Delay between demonstrations in seconds


   .. autolink-examples:: demo_ui_features
      :collapse:

.. py:function:: run_fox_and_geese_game(agent: haive.games.fox_and_geese.agent.FoxAndGeeseAgent, delay: float = 1.5, use_rich_ui: bool = True)

   Run a Fox and Geese game with visualization.

   :param agent: Configured FoxAndGeeseAgent
   :param delay: Delay between moves in seconds
   :param use_rich_ui: Whether to use the enhanced Rich UI (vs. the basic UI)

   :returns: The final game state


   .. autolink-examples:: run_fox_and_geese_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.fox_and_geese.enhanced_example
   :collapse:
   
.. autolink-skip:: next
