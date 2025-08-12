
:py:mod:`games.debate.engines`
==============================

.. py:module:: games.debate.engines



Functions
---------

.. autoapisummary::

   games.debate.engines.build_debate_engines
   games.debate.engines.generate_debater_prompt
   games.debate.engines.generate_defense_prompt
   games.debate.engines.generate_judge_prompt
   games.debate.engines.generate_moderator_prompt
   games.debate.engines.generate_persona_prompt
   games.debate.engines.generate_prosecutor_prompt

.. py:function:: build_debate_engines() -> dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]

   Build engines for different debate roles.


   .. autolink-examples:: build_debate_engines
      :collapse:

.. py:function:: generate_debater_prompt(position: str = None) -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_defense_prompt() -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_judge_prompt() -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_moderator_prompt() -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_persona_prompt(persona_traits: dict[str, str]) -> langchain_core.prompts.ChatPromptTemplate

.. py:function:: generate_prosecutor_prompt() -> langchain_core.prompts.ChatPromptTemplate



.. rubric:: Related Links

.. autolink-examples:: games.debate.engines
   :collapse:
   
.. autolink-skip:: next
