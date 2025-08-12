
:py:mod:`games.among_us.generic_engines`
========================================

.. py:module:: games.among_us.generic_engines

Generic Among Us engine creation using the generic player agent system.

This module provides generic engine creation functions for Among Us games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.among_us.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.among_us.generic_engines.AmongUsEngineFactory
   games.among_us.generic_engines.AmongUsPlayerIdentifiers
   games.among_us.generic_engines.AmongUsPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsEngineFactory {
        node [shape=record];
        "AmongUsEngineFactory" [label="AmongUsEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "AmongUsEngineFactory";
      }

.. autoclass:: games.among_us.generic_engines.AmongUsEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsPlayerIdentifiers {
        node [shape=record];
        "AmongUsPlayerIdentifiers" [label="AmongUsPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "AmongUsPlayerIdentifiers";
      }

.. autoclass:: games.among_us.generic_engines.AmongUsPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsPromptGenerator {
        node [shape=record];
        "AmongUsPromptGenerator" [label="AmongUsPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "AmongUsPromptGenerator";
      }

.. autoclass:: games.among_us.generic_engines.AmongUsPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.among_us.generic_engines.create_budget_among_us_engines
   games.among_us.generic_engines.create_detective_among_us_engines
   games.among_us.generic_engines.create_generic_among_us_config_from_example
   games.among_us.generic_engines.create_generic_among_us_engines
   games.among_us.generic_engines.create_generic_among_us_engines_simple
   games.among_us.generic_engines.create_mixed_among_us_engines

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



.. rubric:: Related Links

.. autolink-examples:: games.among_us.generic_engines
   :collapse:
   
.. autolink-skip:: next
