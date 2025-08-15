games.multi_player.factory
==========================

.. py:module:: games.multi_player.factory

.. autoapi-nested-parse::

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

.. py:class:: MultiPlayerGameFactory

   Factory for creating multi-player game agents.

   This class provides static methods for creating game-specific agent
   classes with proper configuration and state management. It handles:
       - Agent class creation with proper inheritance
       - Configuration class creation
       - State management integration
       - Custom method injection
       - Agent registration

   .. rubric:: Example

   >>> # Create a new game agent class
   >>> MafiaAgent = MultiPlayerGameFactory.create_game_agent(
   ...     name="MafiaAgent",
   ...     state_schema=MafiaState,
   ...     state_manager=MafiaStateManager,
   ...     player_roles=["villager", "mafia", "detective"],
   ...     aug_llm_configs={
   ...         "villager": {"vote": villager_config},
   ...         "mafia": {"kill": mafia_config},
   ...         "detective": {"investigate": detective_config}
   ...     }
   ... )


   .. autolink-examples:: MultiPlayerGameFactory
      :collapse:

   .. py:method:: create_game_agent(name: str, state_schema: type[haive.games.framework.multi_player.state.MultiPlayerGameState], state_manager: type[haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager], player_roles: list[str], aug_llm_configs: dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]], custom_methods: dict[str, collections.abc.Callable] = None) -> type[haive.core.engine.agent.agent.Agent]
      :staticmethod:


      Create a new multi-player game agent class.

      This method creates a new agent class with proper configuration,
      state management, and custom methods. The created class is
      automatically registered with the agent registry.

      :param name: Name of the agent class.
      :type name: str
      :param state_schema: The game state schema class.
      :type state_schema: Type[MultiPlayerGameState]
      :param state_manager: The game state manager class.
      :type state_manager: Type[MultiPlayerGameStateManager]
      :param player_roles: List of player roles.
      :type player_roles: List[str]
      :param aug_llm_configs: LLM configurations by role and function.
      :type aug_llm_configs: Dict[str, Dict[str, AugLLMConfig]]
      :param custom_methods: Additional methods for the agent.
      :type custom_methods: Dict[str, Callable], optional

      :returns: A new agent class ready for instantiation.
      :rtype: Type[Agent]

      .. rubric:: Example

      >>> # Create a chess agent with custom methods
      >>> ChessAgent = MultiPlayerGameFactory.create_game_agent(
      ...     name="ChessAgent",
      ...     state_schema=ChessState,
      ...     state_manager=ChessStateManager,
      ...     player_roles=["white", "black"],
      ...     aug_llm_configs={
      ...         "white": {"move": white_config},
      ...         "black": {"move": black_config}
      ...     },
      ...     custom_methods={
      ...         "evaluate_position": my_eval_function,
      ...         "get_piece_moves": my_move_generator
      ...     }
      ... )


      .. autolink-examples:: create_game_agent
         :collapse:


