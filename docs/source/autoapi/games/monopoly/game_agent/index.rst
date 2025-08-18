games.monopoly.game_agent
=========================

.. py:module:: games.monopoly.game_agent

Fixed Monopoly game agent implementation.

This module provides the corrected main game agent for orchestrating a Monopoly game,
with proper handling of BaseModel objects from LangGraph instead of dictionaries.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span>   </div>

.. autoapi-nested-parse::

   Fixed Monopoly game agent implementation.

   This module provides the corrected main game agent for orchestrating a Monopoly game,
   with proper handling of BaseModel objects from LangGraph instead of dictionaries.



      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.monopoly.game_agent.MonopolyGameAgent
      games.monopoly.game_agent.MonopolyGameAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyGameAgent(config: MonopolyGameAgentConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`MonopolyGameAgentConfig`\ ]


            Main game agent for orchestrating Monopoly.

            Initialize the game agent.


            .. py:method:: check_doubles(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               Check if doubles were rolled and handle accordingly.



            .. py:method:: check_game_end_node(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               Check if the game should end.



            .. py:method:: end_turn(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               End the current player's turn.



            .. py:method:: handle_jail_turn(state: haive.games.monopoly.state.MonopolyState) -> langgraph.types.Command

               Handle a turn when player is in jail.



            .. py:method:: handle_landing(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               Handle the player landing on a space.



            .. py:method:: handle_property_space(state: haive.games.monopoly.state.MonopolyState, property_name: str) -> langgraph.types.Command

               Handle landing on a property space.



            .. py:method:: handle_special_space(state: haive.games.monopoly.state.MonopolyState, space_name: str) -> langgraph.types.Command

               Handle landing on special spaces like GO, Jail, etc.



            .. py:method:: move_player_node(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               Move the current player based on dice roll.



            .. py:method:: offer_property_purchase(state: haive.games.monopoly.state.MonopolyState, property_obj) -> langgraph.types.Command

               Offer property purchase to current player.



            .. py:method:: pay_rent(state: haive.games.monopoly.state.MonopolyState, property_obj) -> langgraph.types.Command

               Handle rent payment.



            .. py:method:: roll_dice_node(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               Roll dice for the current player.



            .. py:method:: route_after_doubles(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> str

               Route based on doubles status.



            .. py:method:: route_game_end(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> str

               Route based on game end status.



            .. py:method:: setup_workflow() -> None

               Set up the main game workflow.



            .. py:method:: start_turn(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

               Start a player's turn.



            .. py:attribute:: player_agent



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyGameAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


            Configuration for monopoly game agent.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:attribute:: enable_trading
               :type:  bool
               :value: None



            .. py:attribute:: max_turns
               :type:  int
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: player_agent
               :type:  Any
               :value: None



            .. py:attribute:: player_names
               :type:  list[str]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[pydantic.BaseModel]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.game_agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

