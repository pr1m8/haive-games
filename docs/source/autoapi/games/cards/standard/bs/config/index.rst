games.cards.standard.bs.config
==============================

.. py:module:: games.cards.standard.bs.config


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.config.BullshitAgentConfig


Functions
---------

.. autoapisummary::

   games.cards.standard.bs.config.build_bullshit_aug_llms
   games.cards.standard.bs.config.generate_challenge_prompt
   games.cards.standard.bs.config.generate_claim_prompt


Module Contents
---------------

.. py:class:: BullshitAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a Bullshit (BS) card game agent.

   .. attribute:: num_players

      Number of players in the game

   .. attribute:: max_rounds

      Maximum number of rounds to play

   .. attribute:: state_schema

      State schema for the Bullshit game


   .. autolink-examples:: BullshitAgentConfig
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: build_bullshit_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :classmethod:


      Build AugLLM configurations for different game stages.


      .. autolink-examples:: build_bullshit_aug_llms
         :collapse:


   .. py:method:: default() -> Any
      :classmethod:


      Create a default configuration for Bullshit.


      .. autolink-examples:: default
         :collapse:


   .. py:attribute:: max_rounds
      :type:  int
      :value: None



   .. py:attribute:: num_players
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:function:: build_bullshit_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLM configurations for the Bullshit game.


   .. autolink-examples:: build_bullshit_aug_llms
      :collapse:

.. py:function:: generate_challenge_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for players to decide whether to challenge another player.


   .. autolink-examples:: generate_challenge_prompt
      :collapse:

.. py:function:: generate_claim_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for players to make a claim during their turn.


   .. autolink-examples:: generate_claim_prompt
      :collapse:

