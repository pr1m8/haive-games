games.hold_em.aug_llms
======================

.. py:module:: games.hold_em.aug_llms

Texas Hold'em specialized augmented LLM configurations.

This module provides specialized augmented LLM configurations for Texas Hold'em poker,
with customized prompts, output schemas, and model configurations for different
aspects of poker gameplay:
    - Hand evaluation and analysis
    - Opponent modeling and profiling
    - Betting strategy and decision-making
    - Position-based play adaptation
    - Pot odds and equity calculations

These specialized configurations build on the base engines in engines.py but provide
more targeted capabilities for specific poker reasoning tasks.

.. rubric:: Example

>>> from haive.games.hold_em.aug_llms import get_hand_analyzer, get_bluff_detector
>>> from haive.core.engine.aug_llm import AugLLMConfig
>>>
>>> # Get a specialized hand analyzer
>>> hand_analyzer = get_hand_analyzer("advanced")
>>> result = hand_analyzer.invoke({
>>>     "hole_cards": ["Ah", "Kh"],
>>>     "community_cards": ["Qh", "Jh", "2s", "7c", "9d"],
>>> })



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">7 functions</span>   </div>

.. autoapi-nested-parse::

   Texas Hold'em specialized augmented LLM configurations.

   This module provides specialized augmented LLM configurations for Texas Hold'em poker,
   with customized prompts, output schemas, and model configurations for different
   aspects of poker gameplay:
       - Hand evaluation and analysis
       - Opponent modeling and profiling
       - Betting strategy and decision-making
       - Position-based play adaptation
       - Pot odds and equity calculations

   These specialized configurations build on the base engines in engines.py but provide
   more targeted capabilities for specific poker reasoning tasks.

   .. rubric:: Example

   >>> from haive.games.hold_em.aug_llms import get_hand_analyzer, get_bluff_detector
   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> # Get a specialized hand analyzer
   >>> hand_analyzer = get_hand_analyzer("advanced")
   >>> result = hand_analyzer.invoke({
   >>>     "hole_cards": ["Ah", "Kh"],
   >>>     "community_cards": ["Qh", "Jh", "2s", "7c", "9d"],
   >>> })



      
            
            
            

.. admonition:: Functions (7)
   :class: info

   .. autoapisummary::

      games.hold_em.aug_llms.get_betting_strategist
      games.hold_em.aug_llms.get_bluff_detector
      games.hold_em.aug_llms.get_complete_llm_suite
      games.hold_em.aug_llms.get_hand_analyzer
      games.hold_em.aug_llms.get_opponent_profiler
      games.hold_em.aug_llms.get_situation_analyzer
      games.hold_em.aug_llms.get_table_dynamics_analyzer

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_betting_strategist(style: str = 'gto') -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized betting strategy configuration.

            This function returns an augmented LLM configuration specialized for making
            betting decisions with different strategic approaches:
            - gto: Game Theory Optimal balanced approach
            - exploitative: Adjusts to exploit opponent tendencies
            - aggressive: Higher variance, aggressive betting strategy
            - conservative: Lower variance, tighter betting strategy

            :param style: Strategic style ("gto", "exploitative", "aggressive", or "conservative")

            :returns: Configured betting strategist
            :rtype: AugLLMConfig



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_bluff_detector(sensitivity: str = 'balanced') -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized bluff detection configuration.

            This function returns an augmented LLM configuration specialized for detecting
            opponent bluffs with different sensitivity levels:
            - conservative: Lower false positive rate, only identifies clear bluffs
            - balanced: Moderate sensitivity to bluffing signals
            - aggressive: Higher sensitivity, may have more false positives

            :param sensitivity: Bluff detection sensitivity ("conservative", "balanced", or "aggressive")

            :returns: Configured bluff detector
            :rtype: AugLLMConfig



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_complete_llm_suite(player_style: str = 'balanced') -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Get a complete suite of specialized LLMs for a poker player.

            This function creates a coordinated set of specialized LLM configurations
            that work well together based on a player's overall style.

            :param player_style: Overall player style ("tight", "loose", "aggressive",
                                 "passive", "balanced", or "tricky")

            :returns: Dictionary of specialized LLM configurations
            :rtype: Dict[str, AugLLMConfig]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_hand_analyzer(level: str = 'standard') -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized hand analyzer configuration.

            This function returns an augmented LLM configuration specialized for analyzing
            poker hands with different levels of sophistication:
            - basic: Simple hand strength evaluation
            - standard: Balanced analysis considering draws and relative strength
            - advanced: Sophisticated analysis with equity calculations and range analysis

            :param level: Complexity level of the analyzer ("basic", "standard", or "advanced")

            :returns: Configured hand analyzer
            :rtype: AugLLMConfig



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_opponent_profiler(tracking_depth: str = 'standard') -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized opponent profiling configuration.

            This function returns an augmented LLM configuration specialized for building
            opponent models with different levels of detail:
            - basic: Simple tracking of betting patterns
            - standard: Balanced profiling of play style and tendencies
            - deep: Sophisticated profiling with psychological modeling

            :param tracking_depth: Depth of opponent tracking ("basic", "standard", or "deep")

            :returns: Configured opponent profiler
            :rtype: AugLLMConfig



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_situation_analyzer(focus: str = 'general') -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized situation analyzer configuration.

            This function returns an augmented LLM configuration specialized for analyzing
            poker game situations with different focus areas:
            - general: Balanced analysis of the overall situation
            - positional: Focus on positional dynamics and advantages
            - tournament: Specialized for tournament situations with ICM considerations
            - cash_game: Specialized for cash game dynamics

            :param focus: Analysis focus ("general", "positional", "tournament", or "cash_game")

            :returns: Configured situation analyzer
            :rtype: AugLLMConfig



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_table_dynamics_analyzer() -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized table dynamics analyzer configuration.

            This function returns an augmented LLM configuration specialized for analyzing
            overall poker table dynamics, player interactions, and meta-game considerations.

            :returns: Configured table dynamics analyzer
            :rtype: AugLLMConfig





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.aug_llms import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

