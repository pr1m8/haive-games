games.among_us.generic_engines
==============================

.. py:module:: games.among_us.generic_engines

.. autoapi-nested-parse::

   Generic Among Us engine creation using the generic player agent system.

   This module provides generic engine creation functions for Among Us games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.among_us.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.among_us.generic_engines.among_us_factory


Classes
-------

.. autoapisummary::

   games.among_us.generic_engines.AmongUsEngineFactory
   games.among_us.generic_engines.AmongUsPlayerIdentifiers
   games.among_us.generic_engines.AmongUsPromptGenerator


Functions
---------

.. autoapisummary::

   games.among_us.generic_engines.create_budget_among_us_engines
   games.among_us.generic_engines.create_detective_among_us_engines
   games.among_us.generic_engines.create_generic_among_us_config_from_example
   games.among_us.generic_engines.create_generic_among_us_engines
   games.among_us.generic_engines.create_generic_among_us_engines_simple
   games.among_us.generic_engines.create_mixed_among_us_engines


Module Contents
---------------

.. py:class:: AmongUsEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Among Us game engines.


   .. autolink-examples:: AmongUsEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: AmongUsPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Among Us game.


   .. autolink-examples:: AmongUsPlayerIdentifiers
      :collapse:

.. py:class:: AmongUsPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Among Us game.


   .. autolink-examples:: AmongUsPromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Among Us game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Among Us player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_budget_among_us_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Among Us engines.


   .. autolink-examples:: create_budget_among_us_engines
      :collapse:

.. py:function:: create_detective_among_us_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create detective-style Among Us engines with high-powered models.


   .. autolink-examples:: create_detective_among_us_engines
      :collapse:

.. py:function:: create_generic_among_us_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Among Us engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Among Us engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT crewmate vs Claude impostor
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "detective_vs_mastermind": High-powered models for intense gameplay



   .. autolink-examples:: create_generic_among_us_config_from_example
      :collapse:

.. py:function:: create_generic_among_us_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Among Us engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Among Us engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "crewmate_player": Crewmate player configuration
       - "impostor_player": Impostor player configuration
       - "crewmate_analyzer": Crewmate analyzer configuration
       - "impostor_analyzer": Impostor analyzer configuration



   .. autolink-examples:: create_generic_among_us_engines
      :collapse:

.. py:function:: create_generic_among_us_engines_simple(crewmate_model: str, impostor_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Among Us engines with simple model specifications.

   :param crewmate_model: Model for crewmate player and analyzer
   :param impostor_model: Model for impostor player and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Among Us engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_among_us_engines_simple
      :collapse:

.. py:function:: create_mixed_among_us_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Among Us engines.


   .. autolink-examples:: create_mixed_among_us_engines
      :collapse:

.. py:data:: among_us_factory

