games.base.factory
==================

.. py:module:: games.base.factory

.. autoapi-nested-parse::

   Factory module for creating game agents.

   from typing import Any, Dict
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


   .. autolink-examples:: games.base.factory
      :collapse:


Attributes
----------

.. autoapisummary::

   games.base.factory.T


Classes
-------

.. autoapisummary::

   games.base.factory.GameAgentFactory


Module Contents
---------------

.. py:class:: GameAgentFactory

   Factory for creating game agents using a flexible, composable pattern.

   This factory class provides methods for creating game agents and their
   workflows. It simplifies the process of creating new game agents by:
   1. Generating workflow nodes from a standardized template
   2. Using DynamicGraph for simplified graph building
   3. Supporting consistent extension patterns for analysis and custom workflows

   The factory supports:
   - Creation of game agent classes with standard methods
   - Configuration of analysis steps and custom nodes
   - Flexible workflow definition with conditional edges
   - Registration of agents with their configs

   .. rubric:: Example

   >>> # Create a new chess agent
   >>> chess_agent = GameAgentFactory.create_game_agent(
   ...     name="ChessAgent",
   ...     state_schema=ChessState,
   ...     state_manager=ChessStateManager
   ... )
   >>>
   >>> # Create an instance with custom config
   >>> agent = chess_agent(ChessConfig())


   .. autolink-examples:: GameAgentFactory
      :collapse:

   .. py:method:: create_game_agent(name: str, state_schema: type[haive.games.framework.base.GameState], state_manager: type[haive.games.framework.base.GameStateManager], player1_name: str = 'player1', player2_name: str = 'player2', enable_analysis: bool = True, aug_llm_configs: dict[str, haive.core.engine.aug_llm.AugLLMConfig] | None = None, custom_nodes: dict[str, collections.abc.Callable] | None = None, custom_edges: list[dict[str, Any]] | None = None, conditional_edges: dict[str, dict[str, Any]] | None = None) -> type[haive.core.engine.agent.agent.Agent]
      :staticmethod:


      Create a new game agent class with a complete workflow.

      This method generates a new game agent class with all necessary methods
      and workflow configuration. It creates both the agent class and its
      corresponding config class.

      :param name: Name of the agent class.
      :type name: str
      :param state_schema: The game state schema class.
      :type state_schema: Type[GameState]
      :param state_manager: The game state manager class.
      :type state_manager: Type[GameStateManager]
      :param player1_name: Name for player 1. Defaults to "player1".
      :type player1_name: str, optional
      :param player2_name: Name for player 2. Defaults to "player2".
      :type player2_name: str, optional
      :param enable_analysis: Whether to enable analysis steps. Defaults to True.
      :type enable_analysis: bool, optional
      :param aug_llm_configs: LLM configurations. Defaults to None.
      :type aug_llm_configs: Optional[Dict[str, AugLLMConfig]], optional
      :param custom_nodes: Custom node functions. Defaults to None.
      :type custom_nodes: Optional[Dict[str, Callable]], optional
      :param custom_edges: Custom edges. Defaults to None.
      :type custom_edges: Optional[List[Dict[str, Any]]], optional
      :param conditional_edges: Conditional edges. Defaults to None.
      :type conditional_edges: Optional[Dict[str, Dict[str, Any]]], optional

      :returns: A new agent class with all methods and workflow configured.
      :rtype: Type[Agent]

      .. rubric:: Example

      >>> # Create a chess agent with analysis
      >>> chess_agent = GameAgentFactory.create_game_agent(
      ...     name="ChessAgent",
      ...     state_schema=ChessState,
      ...     state_manager=ChessStateManager,
      ...     enable_analysis=True,
      ...     aug_llm_configs={
      ...         "player1": player1_config,
      ...         "player2": player2_config
      ...     }
      ... )


      .. autolink-examples:: create_game_agent
         :collapse:


   .. py:method:: create_standard_workflow(graph: langgraph.graph.StateGraph, enable_analysis: bool = True) -> langgraph.graph.StateGraph
      :staticmethod:


      Add a standard game workflow to an existing graph.

      This method creates the typical workflow for a turn-based game with
      two players, optionally including analysis steps. It modifies the
      provided graph by adding nodes and edges for the standard game flow.

      :param graph: The state graph to modify.
      :type graph: StateGraph
      :param enable_analysis: Whether to include analysis steps.
                              Defaults to True.
      :type enable_analysis: bool, optional

      :returns: The modified graph with standard workflow added.
      :rtype: StateGraph

      .. rubric:: Example

      >>> # Create a basic graph and add standard workflow
      >>> graph = StateGraph()
      >>> graph = GameAgentFactory.create_standard_workflow(
      ...     graph,
      ...     enable_analysis=True
      ... )


      .. autolink-examples:: create_standard_workflow
         :collapse:


.. py:data:: T

