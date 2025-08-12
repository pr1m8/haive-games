
:py:mod:`games.framework.base.factory`
======================================

.. py:module:: games.framework.base.factory

Factory module for creating game agents.

This module provides a factory class for creating game agents with standardized
workflows and configurations. It simplifies the process of creating new game
agents by providing a flexible, composable pattern.

.. rubric:: Example

>>> # Create a new chess agent
>>> chess_agent = GameAgentFactory.create_game_agent(
...     name="ChessAgent",
...     state_schema=ChessState,
...     state_manager=ChessStateManager,
...     enable_analysis=True
... )
>>>
>>> # Create a standard workflow
>>> graph = StateGraph()
>>> graph = GameAgentFactory.create_standard_workflow(graph)

Typical usage:
    - Use create_game_agent to generate new game agent classes
    - Use create_standard_workflow to set up game workflows
    - Customize agents with analysis, custom nodes, and edges


.. autolink-examples:: games.framework.base.factory
   :collapse:

Classes
-------

.. autoapisummary::

   games.framework.base.factory.GameAgentFactory


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameAgentFactory:

   .. graphviz::
      :align: center

      digraph inheritance_GameAgentFactory {
        node [shape=record];
        "GameAgentFactory" [label="GameAgentFactory"];
      }

.. autoclass:: games.framework.base.factory.GameAgentFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.framework.base.factory
   :collapse:
   
.. autolink-skip:: next
