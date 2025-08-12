
:py:mod:`games.connect4.configurable_config`
============================================

.. py:module:: games.connect4.configurable_config

Configurable Connect4 agent configuration using player agents.

from typing import Any This module provides a Connect4 configuration that supports
configurable player agents instead of hardcoded engine configurations.


.. autolink-examples:: games.connect4.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.connect4.configurable_config.ConfigurableConnect4Config


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableConnect4Config:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableConnect4Config {
        node [shape=record];
        "ConfigurableConnect4Config" [label="ConfigurableConnect4Config"];
        "haive.core.engine.agent.agent.AgentConfig" -> "ConfigurableConnect4Config";
      }

.. autoclass:: games.connect4.configurable_config.ConfigurableConnect4Config
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.connect4.configurable_config.create_connect4_config
   games.connect4.configurable_config.create_connect4_config_from_example
   games.connect4.configurable_config.create_connect4_config_from_player_configs

.. py:function:: create_connect4_config(red_model: str = 'gpt-4o', yellow_model: str = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, enable_analysis: bool = False, **kwargs) -> ConfigurableConnect4Config

   Create a Connect4 configuration with simple model strings.

   :param red_model: Model for red player
   :param yellow_model: Model for yellow player
   :param temperature: Temperature for all engines
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Connect4 agent
   :rtype: ConfigurableConnect4Config

   .. rubric:: Example

   >>> config = create_connect4_config("gpt-4", "claude-3-opus", temperature=0.8)


   .. autolink-examples:: create_connect4_config
      :collapse:

.. py:function:: create_connect4_config_from_example(example_name: str, enable_analysis: bool = False, **kwargs) -> ConfigurableConnect4Config

   Create a Connect4 configuration from an example.

   :param example_name: Name of the example configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Connect4 agent
   :rtype: ConfigurableConnect4Config

   Available examples: gpt_vs_claude, gpt_only, claude_only, budget, mixed

   .. rubric:: Example

   >>> config = create_connect4_config_from_example("budget")


   .. autolink-examples:: create_connect4_config_from_example
      :collapse:

.. py:function:: create_connect4_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], enable_analysis: bool = False, **kwargs) -> ConfigurableConnect4Config

   Create a Connect4 configuration from player agent configurations.

   :param player_configs: Dictionary of role to player configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Connect4 agent
   :rtype: ConfigurableConnect4Config

   .. rubric:: Example

   >>> configs = {
   ...     "red_player": create_player_config("gpt-4", player_name="Red Master"),
   ...     "yellow_player": create_player_config("claude-3-opus", player_name="Yellow Pro"),
   ... }
   >>> config = create_connect4_config_from_player_configs(configs)


   .. autolink-examples:: create_connect4_config_from_player_configs
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.connect4.configurable_config
   :collapse:
   
.. autolink-skip:: next
