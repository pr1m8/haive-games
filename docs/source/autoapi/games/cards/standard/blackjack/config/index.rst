games.cards.standard.blackjack.config
=====================================

.. py:module:: games.cards.standard.blackjack.config

Module documentation for games.cards.standard.blackjack.config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">3 functions</span>   </div>


      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.cards.standard.blackjack.config.BetAmount
      games.cards.standard.blackjack.config.BlackjackAgentConfig

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.cards.standard.blackjack.config.build_blackjack_aug_llms
      games.cards.standard.blackjack.config.generate_betting_prompt
      games.cards.standard.blackjack.config.generate_player_action_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BetAmount(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for betting amount.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: amount
               :type:  float
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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


            .. py:class:: Config

               Pydantic configuration.


               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: build_blackjack_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :classmethod:


               Build AugLLM configurations for different game stages.



            .. py:method:: default()
               :classmethod:


               Create a default configuration for Blackjack.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_blackjack_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Build AugLLM configurations for the Blackjack game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_betting_prompt() -> langchain_core.prompts.ChatPromptTemplate


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_player_action_prompt() -> langchain_core.prompts.ChatPromptTemplate




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.blackjack.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

