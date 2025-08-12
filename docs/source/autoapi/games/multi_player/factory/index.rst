
:py:mod:`games.multi_player.factory`
====================================

.. py:module:: games.multi_player.factory

Factory for creating multi-player game agents.

This module provides a factory class for creating multi-player game agents,
automating the creation of game-specific agent classes with proper configuration
and state management.

.. rubric:: Example

>>> from haive.agents.agent_games.framework.multi_player.factory import MultiPlayerGameFactory
>>>
>>> # Create a new chess agent class
>>> ChessAgent = MultiPlayerGameFactory.create_game_agent(
...     name="ChessAgent",
...     state_schema=ChessState,hv
...     state_manager=ChessStateManager,
...     player_roles=["white", "black"],
...     aug_llm_configs={
...         "white": {"move": white_llm_config},
...         "black": {"move": black_llm_config}
...     }
... )


.. autolink-examples:: games.multi_player.factory
   :collapse:

Classes
-------

.. autoapisummary::

   games.multi_player.factory.MultiPlayerGameFactory


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiPlayerGameFactory:

   .. graphviz::
      :align: center

      digraph inheritance_MultiPlayerGameFactory {
        node [shape=record];
        "MultiPlayerGameFactory" [label="MultiPlayerGameFactory"];
      }

.. autoclass:: games.multi_player.factory.MultiPlayerGameFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.multi_player.factory
   :collapse:
   
.. autolink-skip:: next
