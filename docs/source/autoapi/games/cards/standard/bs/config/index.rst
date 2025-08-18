games.cards.standard.bs.config
==============================

.. py:module:: games.cards.standard.bs.config

Module documentation for games.cards.standard.bs.config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">3 functions</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.cards.standard.bs.config.BullshitAgentConfig

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.cards.standard.bs.config.build_bullshit_aug_llms
      games.cards.standard.bs.config.generate_challenge_prompt
      games.cards.standard.bs.config.generate_claim_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BullshitAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


            Configuration for a Bullshit (BS) card game agent.

            .. attribute:: num_players

               Number of players in the game

            .. attribute:: max_rounds

               Maximum number of rounds to play

            .. attribute:: state_schema

               State schema for the Bullshit game


            .. py:class:: Config

               Pydantic configuration.


               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: build_bullshit_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :classmethod:


               Build AugLLM configurations for different game stages.



            .. py:method:: default() -> Any
               :classmethod:


               Create a default configuration for Bullshit.



            .. py:attribute:: max_rounds
               :type:  int
               :value: None



            .. py:attribute:: num_players
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type[pydantic.BaseModel]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_bullshit_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Build AugLLM configurations for the Bullshit game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_challenge_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Create a prompt for players to decide whether to challenge another player.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_claim_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Create a prompt for players to make a claim during their turn.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.bs.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

