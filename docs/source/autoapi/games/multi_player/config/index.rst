games.multi_player.config
=========================

.. py:module:: games.multi_player.config

Configuration for multi-player game agents.

This module provides the configuration class for multi-player game agents,
supporting features like:
    - Role-based player configurations
    - LLM engine configurations per role
    - Game state schema definitions
    - Visualization settings
    - Game flow control

.. rubric:: Example

>>> from haive.agents.agent_games.framework.multi_player.config import MultiPlayerGameConfig
>>> from haive.core.engine.aug_llm import AugLLMConfig
>>>
>>> # Create a game configuration
>>> config = MultiPlayerGameConfig(
...     state_schema=MyGameState,
...     engines={
...         "player": {"move": player_llm_config},
...         "narrator": {"narrate": narrator_llm_config}
...     }
... )



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration for multi-player game agents.

   This module provides the configuration class for multi-player game agents,
   supporting features like:
       - Role-based player configurations
       - LLM engine configurations per role
       - Game state schema definitions
       - Visualization settings
       - Game flow control

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.config import MultiPlayerGameConfig
   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> # Create a game configuration
   >>> config = MultiPlayerGameConfig(
   ...     state_schema=MyGameState,
   ...     engines={
   ...         "player": {"move": player_llm_config},
   ...         "narrator": {"narrate": narrator_llm_config}
   ...     }
   ... )



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.multi_player.config.MultiPlayerGameConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MultiPlayerGameConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


            Configuration for multi-player game agents.

            This class defines the configuration for multi-player game agents,
            including state management, player roles, and LLM configurations.

            .. attribute:: state_schema

               State schema for the game.

               :type: Type[MultiPlayerGameState]

            .. attribute:: player_schemas

               Role-specific schemas.

               :type: Dict[str, Type[BaseModel]]

            .. attribute:: engines

               LLM configs by role.

               :type: Dict[str, Dict[str, AugLLMConfig]]

            .. attribute:: initial_player_count

               Default number of players.

               :type: int

            .. attribute:: visualize

               Whether to visualize the game.

               :type: bool

            .. attribute:: max_rounds

               Maximum number of rounds.

               :type: Optional[int]

            .. attribute:: async_mode

               Whether to run players asynchronously.

               :type: bool

            .. rubric:: Example

            >>> config = MultiPlayerGameConfig(
            ...     state_schema=MyGameState,
            ...     engines={
            ...         "player": {
            ...             "move": AugLLMConfig(
            ...                 name="player_move",
            ...                 llm_config=my_llm_config,
            ...                 prompt_template=move_prompt
            ...             )
            ...         }
            ...     },
            ...     initial_player_count=4
            ... )


            .. py:class:: Config

               Pydantic configuration.


               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:attribute:: async_mode
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]
               :value: None



            .. py:attribute:: initial_player_count
               :type:  int
               :value: None



            .. py:attribute:: max_rounds
               :type:  int | None
               :value: None



            .. py:attribute:: player_schemas
               :type:  dict[str, type[pydantic.BaseModel]]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.framework.multi_player.state.MultiPlayerGameState]
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.multi_player.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

