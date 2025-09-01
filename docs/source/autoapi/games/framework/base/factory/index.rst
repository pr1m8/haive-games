games.framework.base.factory
============================

.. py:module:: games.framework.base.factory

.. autoapi-nested-parse::

   Factory module for creating game agents.

   This module provides a factory class for creating game agents with standardized
   workflows and configurations. It simplifies the process of creating new game
   agents by providing a flexible, composable pattern.

   .. rubric:: Examples

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



Attributes
----------

.. autoapisummary::

   games.framework.base.factory.T


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/framework/base/factory/GameAgentFactory

.. autoapisummary::

   games.framework.base.factory.GameAgentFactory


Module Contents
---------------

.. py:data:: T

