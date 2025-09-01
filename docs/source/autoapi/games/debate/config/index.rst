games.debate.config
===================

.. py:module:: games.debate.config

.. autoapi-nested-parse::

   Configuration classes for debate agent setup and customization.

   This module provides comprehensive configuration options for debate agents,
   including format-specific presets, role assignments, timing controls, and
   engine configurations. The configuration system supports various debate
   formats from formal parliamentary debates to trial simulations.

   The configuration classes use Pydantic for validation and provide factory
   methods for common debate formats including standard debates, presidential
   debates, trial formats, and panel discussions.

   .. rubric:: Examples

   Creating a standard debate configuration:

   .. code-block:: python

       config = DebateAgentConfig.default()
       agent = DebateAgent(config)

   Creating a custom trial simulation::

       config = DebateAgentConfig.trial()
       config.time_limit = 600  # 10 minutes per phase
       config.participant_roles["witness_1"] = "witness"
       agent = DebateAgent(config)

   Creating a presidential debate format::

       config = DebateAgentConfig.presidential()
       config.allow_interruptions = True
       config.moderator_role = "moderator"
       agent = DebateAgent(config)

   Creating a custom configuration::

       config = DebateAgentConfig(
           name="custom_debate",
           debate_format="oxford",
           time_limit=300,
           max_statements=5,
           allow_interruptions=False,
           voting_enabled=True,
           participant_roles={
               "pro_1": "pro", "pro_2": "pro",
               "con_1": "con", "con_2": "con",
               "moderator": "moderator"
           }
       )

   .. note::

      All configuration classes inherit from AgentConfig and include automatic
      engine setup through the build_debate_engines factory function.
      Custom engine configurations can be provided to override defaults.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/debate/config/DebateAgentConfig

.. autoapisummary::

   games.debate.config.DebateAgentConfig


