games.monopoly.game_agent
=========================

.. py:module:: games.monopoly.game_agent

.. autoapi-nested-parse::

   Fixed Monopoly game agent implementation.

   This module provides the corrected main game agent for orchestrating a Monopoly game,
   with proper handling of BaseModel objects from LangGraph instead of dictionaries.


   .. autolink-examples:: games.monopoly.game_agent
      :collapse:


Classes
-------

.. autoapisummary::

   games.monopoly.game_agent.MonopolyGameAgent
   games.monopoly.game_agent.MonopolyGameAgentConfig


Module Contents
---------------

.. py:class:: MonopolyGameAgent(config: MonopolyGameAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`MonopolyGameAgentConfig`\ ]


   Main game agent for orchestrating Monopoly.

   Initialize the game agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MonopolyGameAgent
      :collapse:

   .. py:method:: check_doubles(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      Check if doubles were rolled and handle accordingly.


      .. autolink-examples:: check_doubles
         :collapse:


   .. py:method:: check_game_end_node(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      Check if the game should end.


      .. autolink-examples:: check_game_end_node
         :collapse:


   .. py:method:: end_turn(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      End the current player's turn.


      .. autolink-examples:: end_turn
         :collapse:


   .. py:method:: handle_jail_turn(state: haive.games.monopoly.state.MonopolyState) -> langgraph.types.Command

      Handle a turn when player is in jail.


      .. autolink-examples:: handle_jail_turn
         :collapse:


   .. py:method:: handle_landing(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      Handle the player landing on a space.


      .. autolink-examples:: handle_landing
         :collapse:


   .. py:method:: handle_property_space(state: haive.games.monopoly.state.MonopolyState, property_name: str) -> langgraph.types.Command

      Handle landing on a property space.


      .. autolink-examples:: handle_property_space
         :collapse:


   .. py:method:: handle_special_space(state: haive.games.monopoly.state.MonopolyState, space_name: str) -> langgraph.types.Command

      Handle landing on special spaces like GO, Jail, etc.


      .. autolink-examples:: handle_special_space
         :collapse:


   .. py:method:: move_player_node(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      Move the current player based on dice roll.


      .. autolink-examples:: move_player_node
         :collapse:


   .. py:method:: offer_property_purchase(state: haive.games.monopoly.state.MonopolyState, property_obj) -> langgraph.types.Command

      Offer property purchase to current player.


      .. autolink-examples:: offer_property_purchase
         :collapse:


   .. py:method:: pay_rent(state: haive.games.monopoly.state.MonopolyState, property_obj) -> langgraph.types.Command

      Handle rent payment.


      .. autolink-examples:: pay_rent
         :collapse:


   .. py:method:: roll_dice_node(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      Roll dice for the current player.


      .. autolink-examples:: roll_dice_node
         :collapse:


   .. py:method:: route_after_doubles(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> str

      Route based on doubles status.


      .. autolink-examples:: route_after_doubles
         :collapse:


   .. py:method:: route_game_end(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> str

      Route based on game end status.


      .. autolink-examples:: route_game_end
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the main game workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: start_turn(state: haive.games.monopoly.state.MonopolyState | pydantic.BaseModel | dict[str, Any]) -> langgraph.types.Command

      Start a player's turn.


      .. autolink-examples:: start_turn
         :collapse:


   .. py:attribute:: player_agent


.. py:class:: MonopolyGameAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   Configuration for monopoly game agent.


   .. autolink-examples:: MonopolyGameAgentConfig
      :collapse:

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



