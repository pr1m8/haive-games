games.single_player.flow_free.config
====================================

.. py:module:: games.single_player.flow_free.config

Configuration for Flow Free game agent.

This module defines the configuration for the Flow Free game agent, including player
type, game mode, and difficulty settings.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration for Flow Free game agent.

   This module defines the configuration for the Flow Free game agent, including player
   type, game mode, and difficulty settings.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.flow_free.config.FlowFreeConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeConfig(/, **data: Any)

            Bases: :py:obj:`haive.games.single_player.base.SinglePlayerGameConfig`


            Configuration for the Flow Free game agent.

            .. attribute:: name

               Name of the game agent.

            .. attribute:: state_schema

               State schema for the game.

            .. attribute:: player_type

               Type of player.

            .. attribute:: game_mode

               Mode of operation.

            .. attribute:: difficulty

               Difficulty level of the game.

            .. attribute:: max_hints

               Maximum number of hints allowed.

            .. attribute:: auto_analyze

               Whether to automatically analyze after each move.

            .. attribute:: rows

               Number of rows in the grid.

            .. attribute:: cols

               Number of columns in the grid.

            .. attribute:: num_flows

               Number of flows to include. If None, determined by difficulty.

            .. attribute:: engines

               Configurations for game LLMs.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: default_config()
               :classmethod:


               Create a default configuration for a new Flow Free game.

               :returns: An instance of the default game configuration.
               :rtype: FlowFreeConfig



            .. py:method:: easy_config()
               :classmethod:


               Create an easy configuration for a new Flow Free game.

               :returns: An instance of the easy game configuration.
               :rtype: FlowFreeConfig



            .. py:method:: interactive_config()
               :classmethod:


               Create an interactive configuration for a new Flow Free game.

               :returns: An instance of the interactive game configuration.
               :rtype: FlowFreeConfig



            .. py:attribute:: auto_analyze
               :type:  bool
               :value: None



            .. py:attribute:: cols
               :type:  int
               :value: None



            .. py:attribute:: difficulty
               :type:  haive.games.single_player.base.GameDifficulty
               :value: None



            .. py:attribute:: engines
               :type:  dict
               :value: None



            .. py:attribute:: game_mode
               :type:  haive.games.single_player.base.GameMode
               :value: None



            .. py:attribute:: max_hints
               :type:  int
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: num_flows
               :type:  int | None
               :value: None



            .. py:attribute:: player_type
               :type:  haive.games.single_player.base.PlayerType
               :value: None



            .. py:attribute:: rows
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.single_player.flow_free.state.FlowFreeState]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.flow_free.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

