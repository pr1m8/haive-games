games.dominoes.enhanced_example
===============================

.. py:module:: games.dominoes.enhanced_example

.. autoapi-nested-parse::

   Example runner for Dominoes game with enhanced Rich UI visualization.



Attributes
----------

.. autoapisummary::

   games.dominoes.enhanced_example.parser


Functions
---------

.. autoapisummary::

   games.dominoes.enhanced_example.demo_ui_features
   games.dominoes.enhanced_example.run_dominoes_game


Module Contents
---------------

.. py:function:: demo_ui_features(delay: float = 0.5)

   Demonstrate UI features with a sample game state.

   :param delay: Delay between demonstrations in seconds


.. py:function:: run_dominoes_game(agent: haive.games.dominoes.agent.DominoesAgent, delay: float = 1.2, use_rich_ui: bool = True)

   Run a Dominoes game with visualization.

   :param agent: Configured DominoesAgent
   :param delay: Delay between moves in seconds
   :param use_rich_ui: Whether to use the enhanced Rich UI (vs. the basic UI)

   :returns: The final game state


.. py:data:: parser

