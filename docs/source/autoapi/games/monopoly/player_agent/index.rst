games.monopoly.player_agent
===========================

.. py:module:: games.monopoly.player_agent

.. autoapi-nested-parse::

   Monopoly player agent implementation.

   This module provides the player agent (subgraph) for making individual
   player decisions in Monopoly, including:
       - Property purchase decisions
       - Jail decisions
       - Building decisions
       - Trade negotiations


   .. autolink-examples:: games.monopoly.player_agent
      :collapse:


Classes
-------

.. autoapisummary::

   games.monopoly.player_agent.MonopolyGameAgentConfig
   games.monopoly.player_agent.MonopolyPlayerAgent
   games.monopoly.player_agent.MonopolyPlayerAgentConfig
   games.monopoly.player_agent.PlayerDecisionState


Module Contents
---------------

.. py:class:: MonopolyGameAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   Configuration class for monopoly game agents.

   This class defines the configuration parameters for monopoly agents, including:
       - Game settings (players, turn limits)
       - Player decision configurations
       - Board and game state initialization

   .. attribute:: state_schema

      The state schema for the game

      :type: type

   .. attribute:: player_names

      Names of players in the game

      :type: List[str]

   .. attribute:: max_turns

      Maximum turns before ending game

      :type: int

   .. attribute:: enable_trading

      Whether to enable trade negotiations

      :type: bool

   .. attribute:: enable_building

      Whether to enable house/hotel building

      :type: bool


   .. autolink-examples:: MonopolyGameAgentConfig
      :collapse:

   .. py:class:: Config

      Pydantic configuration class.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: create_initial_state() -> haive.games.monopoly.state.MonopolyState

      Create the initial game state with all required fields and proper.
      validation.


      .. autolink-examples:: create_initial_state
         :collapse:


   .. py:method:: create_player_agent() -> Any

      Create the player decision agent.


      .. autolink-examples:: create_player_agent
         :collapse:


   .. py:method:: setup_player_agent_engines() -> None

      Set up the engines for the player agent if not already configured.


      .. autolink-examples:: setup_player_agent_engines
         :collapse:


   .. py:attribute:: enable_auctions
      :type:  bool
      :value: None



   .. py:attribute:: enable_building
      :type:  bool
      :value: None



   .. py:attribute:: enable_trading
      :type:  bool
      :value: None



   .. py:attribute:: max_turns
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: player_agent_config
      :type:  MonopolyPlayerAgentConfig
      :value: None



   .. py:attribute:: player_names
      :type:  list[str]
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: MonopolyPlayerAgent(config: MonopolyPlayerAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`MonopolyPlayerAgentConfig`\ ]


   Player agent for making individual decisions in Monopoly.

   Initialize the player agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MonopolyPlayerAgent
      :collapse:

   .. py:method:: _prepare_jail_context(decision_state: PlayerDecisionState) -> dict[str, Any]

      Prepare context for jail decision.


      .. autolink-examples:: _prepare_jail_context
         :collapse:


   .. py:method:: _prepare_property_context(decision_state: PlayerDecisionState) -> dict[str, Any]

      Prepare context for property decision.


      .. autolink-examples:: _prepare_property_context
         :collapse:


   .. py:method:: get_decision_route(state: pydantic.BaseModel) -> str

      Get the route for the decision.


      .. autolink-examples:: get_decision_route
         :collapse:


   .. py:method:: make_building_decision(state: pydantic.BaseModel) -> langgraph.types.Command

      Make a building decision.


      .. autolink-examples:: make_building_decision
         :collapse:


   .. py:method:: make_jail_decision(state: pydantic.BaseModel) -> langgraph.types.Command

      Make a jail-related decision.


      .. autolink-examples:: make_jail_decision
         :collapse:


   .. py:method:: make_property_decision(state: pydantic.BaseModel) -> langgraph.types.Command

      Make a property purchase decision.


      .. autolink-examples:: make_property_decision
         :collapse:


   .. py:method:: make_trade_decision(state: pydantic.BaseModel) -> langgraph.types.Command

      Make a trade decision.


      .. autolink-examples:: make_trade_decision
         :collapse:


   .. py:method:: route_decision(state: pydantic.BaseModel) -> langgraph.types.Command

      Route to appropriate decision node based on decision type.


      .. autolink-examples:: route_decision
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the player decision workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: engines


.. py:class:: MonopolyPlayerAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   Configuration for monopoly player decision agent.


   .. autolink-examples:: MonopolyPlayerAgentConfig
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: PlayerDecisionState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State for player decision subgraph.


   .. autolink-examples:: PlayerDecisionState
      :collapse:

   .. py:property:: decision
      :type: haive.games.monopoly.models.PropertyDecision | haive.games.monopoly.models.JailDecision | haive.games.monopoly.models.BuildingDecision | haive.games.monopoly.models.TradeResponse | str | Any


      Get the decision.

      .. autolink-examples:: decision
         :collapse:


   .. py:attribute:: decision_type
      :type:  haive.games.monopoly.models.PlayerActionType | Any
      :value: None



   .. py:attribute:: decisions
      :type:  Annotated[list[haive.games.monopoly.models.PropertyDecision | haive.games.monopoly.models.JailDecision | haive.games.monopoly.models.BuildingDecision | haive.games.monopoly.models.TradeResponse | str | Any], operator.add]
      :value: None



   .. py:attribute:: dice_roll
      :type:  int
      :value: None



   .. py:attribute:: error_message
      :type:  str
      :value: None



   .. py:attribute:: game_state
      :type:  haive.games.monopoly.state.MonopolyState
      :value: None



   .. py:attribute:: player_money
      :type:  int
      :value: None



   .. py:attribute:: player_name
      :type:  str
      :value: None



   .. py:attribute:: property_name
      :type:  str
      :value: None



   .. py:attribute:: property_price
      :type:  int
      :value: None



   .. py:attribute:: reasoning
      :type:  Annotated[list[str], operator.add]
      :value: None



