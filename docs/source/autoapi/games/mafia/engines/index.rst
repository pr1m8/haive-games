
:py:mod:`games.mafia.engines`
=============================

.. py:module:: games.mafia.engines

LLM engine configurations for the Mafia game.

This module defines the LLM configurations and prompts for each role in the
Mafia game. It provides:
    - Role-specific prompt templates
    - LLM configurations for each role
    - Structured output schemas for decisions
    - Example prompts and responses

The module uses Azure OpenAI's GPT-4 model for all roles, with custom
prompts designed to elicit appropriate role-playing behavior.

.. rubric:: Example

>>> from mafia.engines import aug_llm_configs
>>>
>>> # Get the villager player engine config
>>> villager_config = aug_llm_configs["villager"]["player"]
>>> print(villager_config.name)  # Shows "villager_player"


.. autolink-examples:: games.mafia.engines
   :collapse:


Functions
---------

.. autoapisummary::

   games.mafia.engines.generate_detective_prompt
   games.mafia.engines.generate_doctor_prompt
   games.mafia.engines.generate_mafia_prompt
   games.mafia.engines.generate_narrator_prompt
   games.mafia.engines.generate_villager_prompt

.. py:function:: generate_detective_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for a detective in Mafia.

   This function creates a prompt that guides detective behavior, focusing on:
       - Strategic investigation target selection
       - Using investigation results effectively
       - Contributing to discussions without revealing role

   :returns: Configured prompt template for detective role
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_detective_prompt()
   >>> messages = prompt.format_messages(
   ...     player_id="Player_1",
   ...     phase="night",
   ...     day_number=1,
   ...     alive_players=["Player_1", "Player_2"],
   ...     private_info=["Player_2 is not mafia"]
   ... )


   .. autolink-examples:: generate_detective_prompt
      :collapse:

.. py:function:: generate_doctor_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for a doctor in Mafia.

   This function creates a prompt that guides doctor behavior, focusing on:
       - Strategic protection target selection
       - Pattern recognition for mafia targets
       - Contributing to discussions without revealing role

   :returns: Configured prompt template for doctor role
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_doctor_prompt()
   >>> messages = prompt.format_messages(
   ...     player_id="Player_1",
   ...     phase="night",
   ...     day_number=1,
   ...     alive_players=["Player_1", "Player_2"],
   ...     private_info=["You saved Player_2 last night"]
   ... )


   .. autolink-examples:: generate_doctor_prompt
      :collapse:

.. py:function:: generate_mafia_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for a mafia member in Mafia.

   This function creates a prompt that guides mafia behavior, focusing on:
       - Coordinating with other mafia members
       - Maintaining cover during discussions
       - Strategic target selection at night

   :returns: Configured prompt template for mafia role
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_mafia_prompt()
   >>> messages = prompt.format_messages(
   ...     player_id="Player_1",
   ...     phase="night",
   ...     day_number=1,
   ...     alive_players=["Player_1", "Player_2"],
   ...     private_info=["Other mafia: Player_3"]
   ... )


   .. autolink-examples:: generate_mafia_prompt
      :collapse:

.. py:function:: generate_narrator_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for the narrator in Mafia.

   This function creates a prompt that guides narrator behavior, focusing on:
       - Creating engaging narrative descriptions
       - Managing game flow and phase transitions
       - Providing appropriate information to players

   :returns: Configured prompt template for narrator role
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_narrator_prompt()
   >>> messages = prompt.format_messages(
   ...     phase="night",
   ...     day_number=1,
   ...     player_summary="5 alive, 2 dead",
   ...     alive_mafia_count=2,
   ...     alive_village_count=3
   ... )


   .. autolink-examples:: generate_narrator_prompt
      :collapse:

.. py:function:: generate_villager_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for a villager in Mafia.

   This function creates a prompt that guides villager behavior, focusing on:
       - Analyzing other players' behavior
       - Making strategic decisions during discussions
       - Voting based on observed patterns

   :returns: Configured prompt template for villager role
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_villager_prompt()
   >>> messages = prompt.format_messages(
   ...     player_id="Player_1",
   ...     phase="day_discussion",
   ...     day_number=1,
   ...     alive_players=["Player_1", "Player_2"],
   ...     public_info=["Night falls..."]
   ... )


   .. autolink-examples:: generate_villager_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mafia.engines
   :collapse:
   
.. autolink-skip:: next
