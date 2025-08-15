games.cards.standard.blackjack.config
=====================================

.. py:module:: games.cards.standard.blackjack.config


Classes
-------

.. autoapisummary::

   games.cards.standard.blackjack.config.BetAmount
   games.cards.standard.blackjack.config.BlackjackAgentConfig


Functions
---------

.. autoapisummary::

   games.cards.standard.blackjack.config.build_blackjack_aug_llms
   games.cards.standard.blackjack.config.generate_betting_prompt
   games.cards.standard.blackjack.config.generate_player_action_prompt


Module Contents
---------------

.. py:class:: BetAmount(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for betting amount.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BetAmount
      :collapse:

   .. py:attribute:: amount
      :type:  float
      :value: None



.. py:class:: BlackjackAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a multi-player Blackjack game agent.

   .. attribute:: num_players

      Number of players in the game

   .. attribute:: max_rounds

      Maximum number of rounds to play

   .. attribute:: initial_chips

      Starting chip amount for each player

   .. attribute:: state_schema

      State schema for the Blackjack game


   .. autolink-examples:: BlackjackAgentConfig
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: build_blackjack_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :classmethod:


      Build AugLLM configurations for different game stages.


      .. autolink-examples:: build_blackjack_aug_llms
         :collapse:


   .. py:method:: default()
      :classmethod:


      Create a default configuration for Blackjack.


      .. autolink-examples:: default
         :collapse:


   .. py:attribute:: initial_chips
      :type:  float
      :value: None



   .. py:attribute:: max_rounds
      :type:  int
      :value: None



   .. py:attribute:: num_players
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:function:: build_blackjack_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLM configurations for the Blackjack game.


   .. autolink-examples:: build_blackjack_aug_llms
      :collapse:

.. py:function:: generate_betting_prompt() -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_player_action_prompt() -> langchain_core.prompts.ChatPromptTemplate

