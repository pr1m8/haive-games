games.hold_em.engines
=====================

.. py:module:: games.hold_em.engines

.. autoapi-nested-parse::

   Texas Hold'em engines and prompts module - FIXED VERSION.

   This module provides LLM configurations and prompts for Hold'em agents.
   Fixed variable naming consistency issues.



Attributes
----------

.. autoapisummary::

   games.hold_em.engines.hand_analysis_prompt
   games.hold_em.engines.opponent_analysis_prompt
   games.hold_em.engines.postflop_decision_prompt
   games.hold_em.engines.preflop_decision_prompt
   games.hold_em.engines.situation_analysis_prompt
   games.hold_em.engines.tournament_decision_prompt


Functions
---------

.. autoapisummary::

   games.hold_em.engines.build_holdem_game_engines
   games.hold_em.engines.build_player_engines
   games.hold_em.engines.create_player_decision_prompt
   games.hold_em.engines.create_style_specific_engines
   games.hold_em.engines.prepare_decision_context
   games.hold_em.engines.prepare_hand_context
   games.hold_em.engines.prepare_opponent_context
   games.hold_em.engines.prepare_situation_context


Module Contents
---------------

.. py:function:: build_holdem_game_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build engines for the main game agent.


.. py:function:: build_player_engines(player_name: str, player_style: str, heads_up: bool = False) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build LLM engines for a player agent.


.. py:function:: create_player_decision_prompt(player_style: str = 'balanced') -> langchain_core.prompts.ChatPromptTemplate

   Create a decision-making prompt based on player style.


.. py:function:: create_style_specific_engines(player_style: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create engines optimized for specific playing styles.


.. py:function:: prepare_decision_context(game_state, player, analyses) -> dict[str, str]

   Prepare context dictionary for final decision making.


.. py:function:: prepare_hand_context(game_state, player) -> dict[str, str]

   Prepare context dictionary for hand analysis.


.. py:function:: prepare_opponent_context(game_state, opponents) -> dict[str, str]

   Prepare context dictionary for opponent analysis.


.. py:function:: prepare_situation_context(game_state, player) -> dict[str, str]

   Prepare context dictionary for situation analysis with correct variable names.


.. py:data:: hand_analysis_prompt

.. py:data:: opponent_analysis_prompt

.. py:data:: postflop_decision_prompt

.. py:data:: preflop_decision_prompt

.. py:data:: situation_analysis_prompt

.. py:data:: tournament_decision_prompt

