
:py:mod:`games.mafia.aug_llms`
==============================

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


.. autolink-examples:: games.mafia.aug_llms
   :collapse:


Functions
---------

.. autoapisummary::

   games.mafia.aug_llms.get_mafia_analyzer

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


   .. autolink-examples:: get_mafia_analyzer
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mafia.aug_llms
   :collapse:
   
.. autolink-skip:: next
