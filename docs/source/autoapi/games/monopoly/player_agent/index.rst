games.monopoly.player_agent
===========================

.. py:module:: games.monopoly.player_agent

Monopoly player agent implementation.

This module provides the player agent (subgraph) for making individual
player decisions in Monopoly, including:
    - Property purchase decisions
    - Jail decisions
    - Building decisions
    - Trade negotiations



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>

.. autoapi-nested-parse::

   Monopoly player agent implementation.

   This module provides the player agent (subgraph) for making individual
   player decisions in Monopoly, including:
       - Property purchase decisions
       - Jail decisions
       - Building decisions
       - Trade negotiations



      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.monopoly.player_agent.MonopolyGameAgentConfig
      games.monopoly.player_agent.MonopolyPlayerAgent
      games.monopoly.player_agent.MonopolyPlayerAgentConfig
      games.monopoly.player_agent.PlayerDecisionState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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


            .. py:class:: Config

               Pydantic configuration class.


               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: create_initial_state() -> haive.games.monopoly.state.MonopolyState

               Create the initial game state with all required fields and proper.
               validation.



            .. py:method:: create_player_agent() -> Any

               Create the player decision agent.



            .. py:method:: setup_player_agent_engines() -> None

               Set up the engines for the player agent if not already configured.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyPlayerAgent(config: MonopolyPlayerAgentConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`MonopolyPlayerAgentConfig`\ ]


            Player agent for making individual decisions in Monopoly.

            Initialize the player agent.


            .. py:method:: _prepare_jail_context(decision_state: PlayerDecisionState) -> dict[str, Any]

               Prepare context for jail decision.



            .. py:method:: _prepare_property_context(decision_state: PlayerDecisionState) -> dict[str, Any]

               Prepare context for property decision.



            .. py:method:: get_decision_route(state: pydantic.BaseModel) -> str

               Get the route for the decision.



            .. py:method:: make_building_decision(state: pydantic.BaseModel) -> langgraph.types.Command

               Make a building decision.



            .. py:method:: make_jail_decision(state: pydantic.BaseModel) -> langgraph.types.Command

               Make a jail-related decision.



            .. py:method:: make_property_decision(state: pydantic.BaseModel) -> langgraph.types.Command

               Make a property purchase decision.



            .. py:method:: make_trade_decision(state: pydantic.BaseModel) -> langgraph.types.Command

               Make a trade decision.



            .. py:method:: route_decision(state: pydantic.BaseModel) -> langgraph.types.Command

               Route to appropriate decision node based on decision type.



            .. py:method:: setup_workflow() -> None

               Set up the player decision workflow.



            .. py:attribute:: engines



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyPlayerAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


            Configuration for monopoly player decision agent.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerDecisionState(/, **data: Any)

            Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


            State for player decision subgraph.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:property:: decision
               :type: haive.games.monopoly.models.PropertyDecision | haive.games.monopoly.models.JailDecision | haive.games.monopoly.models.BuildingDecision | haive.games.monopoly.models.TradeResponse | str | Any


               Get the decision.


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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.player_agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

