games.hold_em.engines
=====================

.. py:module:: games.hold_em.engines

Texas Hold'em engines and prompts module - FIXED VERSION.

This module provides LLM configurations and prompts for Hold'em agents.
Fixed variable naming consistency issues.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">8 functions</span> • <span class="module-stat">6 attributes</span>   </div>

.. autoapi-nested-parse::

   Texas Hold'em engines and prompts module - FIXED VERSION.

   This module provides LLM configurations and prompts for Hold'em agents.
   Fixed variable naming consistency issues.



      

.. admonition:: Attributes (6)
   :class: tip

   .. autoapisummary::

      games.hold_em.engines.hand_analysis_prompt
      games.hold_em.engines.opponent_analysis_prompt
      games.hold_em.engines.postflop_decision_prompt
      games.hold_em.engines.preflop_decision_prompt
      games.hold_em.engines.situation_analysis_prompt
      games.hold_em.engines.tournament_decision_prompt

            
            
            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.hold_em.engines.build_holdem_game_engines
      games.hold_em.engines.build_player_engines
      games.hold_em.engines.create_player_decision_prompt
      games.hold_em.engines.create_style_specific_engines
      games.hold_em.engines.prepare_decision_context
      games.hold_em.engines.prepare_hand_context
      games.hold_em.engines.prepare_opponent_context
      games.hold_em.engines.prepare_situation_context

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_holdem_game_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Build engines for the main game agent.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_player_engines(player_name: str, player_style: str, heads_up: bool = False) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Build LLM engines for a player agent.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_player_decision_prompt(player_style: str = 'balanced') -> langchain_core.prompts.ChatPromptTemplate

            Create a decision-making prompt based on player style.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_style_specific_engines(player_style: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create engines optimized for specific playing styles.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: prepare_decision_context(game_state, player, analyses) -> dict[str, str]

            Prepare context dictionary for final decision making.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: prepare_hand_context(game_state, player) -> dict[str, str]

            Prepare context dictionary for hand analysis.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: prepare_opponent_context(game_state, opponents) -> dict[str, str]

            Prepare context dictionary for opponent analysis.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: prepare_situation_context(game_state, player) -> dict[str, str]

            Prepare context dictionary for situation analysis with correct variable names.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: hand_analysis_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: opponent_analysis_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: postflop_decision_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: preflop_decision_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: situation_analysis_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: tournament_decision_prompt




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

