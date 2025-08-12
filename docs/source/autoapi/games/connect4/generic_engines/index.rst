
:py:mod:`games.connect4.generic_engines`
========================================

.. py:module:: games.connect4.generic_engines

Generic Connect4 engines using the new generic player agent system.

This module demonstrates how to use the generic player agent system for Connect4,
showing the same pattern working with red/yellow player identifiers.


.. autolink-examples:: games.connect4.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.connect4.generic_engines.Connect4PromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Connect4PromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4PromptGenerator {
        node [shape=record];
        "Connect4PromptGenerator" [label="Connect4PromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "Connect4PromptGenerator";
      }

.. autoclass:: games.connect4.generic_engines.Connect4PromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.connect4.generic_engines.create_generic_connect4_config_from_example
   games.connect4.generic_engines.create_generic_connect4_engines
   games.connect4.generic_engines.create_generic_connect4_engines_simple

.. py:function:: create_generic_connect4_config_from_example(example_name: str, temperature: float = 0.7) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Connect4 engines from predefined examples using generics.

   :param example_name: Name of the example configuration
   :param temperature: Temperature for all engines

   :returns: Dictionary of engines
   :rtype: dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT-4 vs Claude
       - "gpt_only": GPT-4 for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role



   .. autolink-examples:: create_generic_connect4_config_from_example
      :collapse:

.. py:function:: create_generic_connect4_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Connect4 engines using the generic system.

   :param player_configs: Dictionary of role name to player configuration

   :returns: Dictionary of configured engines
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> configs = {
   ...     "red_player": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "yellow_player": PlayerAgentConfig(llm_config="claude-3-opus"),
   ...     "red_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "yellow_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
   ... }
   >>> engines = create_generic_connect4_engines(configs)


   .. autolink-examples:: create_generic_connect4_engines
      :collapse:

.. py:function:: create_generic_connect4_engines_simple(red_model: str | haive.core.models.llm.LLMConfig = 'gpt-4o', yellow_model: str | haive.core.models.llm.LLMConfig = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Connect4 engines with simple model configurations using generics.

   :param red_model: Model for red player and analyzer
   :param yellow_model: Model for yellow player and analyzer
   :param temperature: Temperature for player engines
   :param \*\*kwargs: Additional configuration parameters

   :returns: Dictionary of engines
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> engines = create_generic_connect4_engines_simple("gpt-4", "claude-3-opus")
   >>> engines = create_generic_connect4_engines_simple(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     temperature=0.8
   ... )


   .. autolink-examples:: create_generic_connect4_engines_simple
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.connect4.generic_engines
   :collapse:
   
.. autolink-skip:: next
