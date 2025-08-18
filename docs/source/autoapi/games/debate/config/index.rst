games.debate.config
===================

.. py:module:: games.debate.config

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

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



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.debate.config.DebateAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


            Comprehensive configuration for debate agents with format-specific settings.

            This configuration class provides extensive customization options for debate
            agents, supporting various debate formats, role assignments, timing controls,
            and engine configurations. It includes validation for debate-specific parameters
            and provides factory methods for common debate formats.

            The configuration system supports:
            - Multiple debate formats (standard, parliamentary, oxford, trial, presidential)
            - Flexible role assignment system for participants
            - Timing controls and statement limits
            - Interruption and voting settings
            - Custom engine configurations for different participant roles

            .. attribute:: debate_format

               Format type determining debate structure and rules.
               Supported formats: "standard", "parliamentary", "oxford", "trial",
               "presidential", "panel", "lincoln_douglas".

               :type: str

            .. attribute:: time_limit

               Maximum time in seconds per debate phase.
               None means no time limit. Typical values: 60-600 seconds.

               :type: Optional[int]

            .. attribute:: max_statements

               Maximum statements per participant per phase.
               None means unlimited statements. Typical values: 1-5 statements.

               :type: Optional[int]

            .. attribute:: allow_interruptions

               Whether participants can interrupt each other
               during their statements. Common in presidential and panel formats.

               :type: bool

            .. attribute:: voting_enabled

               Whether to include a voting phase at debate end.
               Typically enabled for competitive debates, disabled for discussions.

               :type: bool

            .. attribute:: moderator_role

               Specific role identifier for the moderator.
               None means no dedicated moderator. Common value: "moderator".

               :type: Optional[str]

            .. attribute:: participant_roles

               Mapping of participant IDs to their roles.
               Keys are participant identifiers, values are role names like "pro",
               "con", "judge", "moderator", "prosecutor", "defense", "witness".

               :type: Dict[str, str]

            .. attribute:: state_schema

               Pydantic model class for debate state.
               Defaults to DebateState but can be customized for specific formats.

               :type: Type[BaseModel]

            .. attribute:: engines

               Engine configurations for different roles.
               Automatically built by build_debate_engines but can be customized.

               :type: Dict[str, AugLLMConfig]

            .. rubric:: Examples

            Basic debate configuration:

            .. code-block:: python

                config = DebateAgentConfig(
                    name="climate_debate",
                    debate_format="oxford",
                    time_limit=300,
                    max_statements=3,
                    participant_roles={
                        "scientist": "pro",
                        "economist": "con",
                        "moderator": "moderator"
                    }
                )

            Trial simulation configuration::

                config = DebateAgentConfig(
                    name="murder_trial",
                    debate_format="trial",
                    time_limit=600,
                    allow_interruptions=False,
                    participant_roles={
                        "prosecutor": "prosecutor",
                        "defense_attorney": "defense",
                        "judge": "judge",
                        "witness_1": "witness",
                        "witness_2": "witness"
                    }
                )

            Parliamentary debate configuration::

                config = DebateAgentConfig(
                    name="parliament_session",
                    debate_format="parliamentary",
                    time_limit=180,
                    allow_interruptions=True,
                    voting_enabled=True,
                    participant_roles={
                        "pm": "government",
                        "deputy_pm": "government",
                        "leader_opposition": "opposition",
                        "deputy_opposition": "opposition",
                        "speaker": "moderator"
                    }
                )

            .. note::

               The configuration automatically sets up appropriate engines for each role
               using the build_debate_engines factory. Custom engines can be provided
               to override defaults for specific use cases or to add specialized capabilities.


            .. py:method:: default()
               :classmethod:


               Create a default configuration for standard debate.



            .. py:method:: panel_discussion()
               :classmethod:


               Create a configuration for a panel discussion.



            .. py:method:: presidential()
               :classmethod:


               Create a configuration for presidential debate.



            .. py:method:: trial()
               :classmethod:


               Create a configuration for a trial format.



            .. py:method:: validate_debate_format(v: str) -> str
               :classmethod:


               Validate debate format is supported.

               :param v: Debate format to validate.
               :type v: str

               :returns: Validated format string.
               :rtype: str

               :raises ValueError: If format is not supported.



            .. py:method:: validate_participant_roles(v: dict[str, str]) -> dict[str, str]
               :classmethod:


               Validate participant role assignments.

               :param v: Role assignments to validate.
               :type v: Dict[str, str]

               :returns: Validated role assignments.
               :rtype: Dict[str, str]

               :raises ValueError: If role assignments are invalid.



            .. py:attribute:: allow_interruptions
               :type:  bool
               :value: None



            .. py:attribute:: debate_format
               :type:  str
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: max_statements
               :type:  int | None
               :value: None



            .. py:attribute:: moderator_role
               :type:  str | None
               :value: None



            .. py:attribute:: participant_roles
               :type:  dict[str, str]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[pydantic.BaseModel]
               :value: None



            .. py:attribute:: time_limit
               :type:  int | None
               :value: None



            .. py:attribute:: voting_enabled
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

