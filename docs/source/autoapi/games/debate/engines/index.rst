games.debate.engines
====================

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


Module Contents
---------------

.. py:function:: build_debate_engines() -> dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]

   Build engines for different debate roles.


.. py:function:: generate_debater_prompt(position: str = None) -> langchain_core.prompts.ChatPromptTemplate

   Generate Debater Prompt.

   :param position: [TODO: Add description]

   :returns: Add return description]
   :rtype: [TODO


.. py:function:: generate_defense_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate Defense Prompt.

   :returns: Add return description]
   :rtype: [TODO


.. py:function:: generate_judge_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate Judge Prompt.

   :returns: Add return description]
   :rtype: [TODO


.. py:function:: generate_moderator_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate Moderator Prompt.

   :returns: Add return description]
   :rtype: [TODO


.. py:function:: generate_persona_prompt(persona_traits: dict[str, str]) -> langchain_core.prompts.ChatPromptTemplate

   Generate Persona Prompt.

   :param persona_traits: [TODO: Add description]

   :returns: Add return description]
   :rtype: [TODO


.. py:function:: generate_prosecutor_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate Prosecutor Prompt.

   :returns: Add return description]
   :rtype: [TODO


