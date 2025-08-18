games.mastermind.config
=======================

.. py:module:: games.mastermind.config

Configuration for the Mastermind game agent.

This module defines the configuration for the Mastermind game agent, including game
state schema, engines, analysis settings, visualization, and game parameters.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Configuration for the Mastermind game agent.

   This module defines the configuration for the Mastermind game agent, including game
   state schema, engines, analysis settings, visualization, and game parameters.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mastermind.config.VERSION

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mastermind.config.MastermindConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MastermindConfig

            Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


            Configuration for the Mastermind game agent.

            This class defines the configuration for the Mastermind game agent, including game
            state schema, engines, analysis settings, visualization, and game parameters.



            .. py:method:: default_config() -> MastermindConfig
               :classmethod:


               Create a default configuration.

               :returns: Default configuration for Mastermind game.
               :rtype: MastermindConfig



            .. py:attribute:: code_length
               :type:  int
               :value: None



            .. py:attribute:: codemaker
               :type:  str
               :value: None



            .. py:attribute:: colors
               :type:  list[str]
               :value: None



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: max_turns
               :type:  int
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: secret_code
               :type:  list[str] | None
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.mastermind.state.MastermindState]
               :value: None



            .. py:attribute:: version
               :type:  str
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: VERSION
            :value: '1.1.0'





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mastermind.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

