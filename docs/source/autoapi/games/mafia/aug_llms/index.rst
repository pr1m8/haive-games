games.mafia.aug_llms
====================

.. py:module:: games.mafia.aug_llms

Specialized LLM configurations for the Mafia game.

This module provides specialized augmented LLM configurations for different
aspects of the Mafia game, including:
    - Role-specific analyzer LLMs
    - Strategic decision-making models
    - Game state evaluators

These configurations extend the basic engines.py configurations with more
sophisticated models tailored for specific game aspects.

.. rubric:: Example

>>> from haive.games.mafia.aug_llms import get_mafia_analyzer
>>>
>>> # Get an analyzer for evaluating player suspicion levels
>>> analyzer = get_mafia_analyzer("suspicion")
>>> analysis = analyzer.invoke(game_state)



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span> • <span class="module-stat">4 attributes</span>   </div>

.. autoapi-nested-parse::

   Specialized LLM configurations for the Mafia game.

   This module provides specialized augmented LLM configurations for different
   aspects of the Mafia game, including:
       - Role-specific analyzer LLMs
       - Strategic decision-making models
       - Game state evaluators

   These configurations extend the basic engines.py configurations with more
   sophisticated models tailored for specific game aspects.

   .. rubric:: Example

   >>> from haive.games.mafia.aug_llms import get_mafia_analyzer
   >>>
   >>> # Get an analyzer for evaluating player suspicion levels
   >>> analyzer = get_mafia_analyzer("suspicion")
   >>> analysis = analyzer.invoke(game_state)



      

.. admonition:: Attributes (4)
   :class: tip

   .. autoapisummary::

      games.mafia.aug_llms.psychology_analyzer
      games.mafia.aug_llms.strategy_analyzer
      games.mafia.aug_llms.suspicion_analyzer
      games.mafia.aug_llms.voting_analyzer

            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.mafia.aug_llms.get_mafia_analyzer

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_mafia_analyzer(analyzer_type: str) -> haive.core.engine.aug_llm.AugLLMConfig

            Get a specialized Mafia game analyzer.

            This function returns a configured analyzer LLM for specific
            Mafia game analysis tasks, such as suspicion evaluation,
            player psychology, strategy optimization, or voting analysis.

            :param analyzer_type: Type of analyzer to get ("suspicion", "psychology",
                                  "strategy", or "voting")

            :returns: Configured analyzer
            :rtype: AugLLMConfig

            :raises ValueError: If analyzer_type is not recognized

            .. rubric:: Example

            >>> analyzer = get_mafia_analyzer("suspicion")
            >>> analysis = analyzer.invoke(game_context)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: psychology_analyzer


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: strategy_analyzer


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: suspicion_analyzer


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: voting_analyzer




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mafia.aug_llms import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

