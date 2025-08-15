games.mastermind.config
=======================

.. py:module:: games.mastermind.config

.. autoapi-nested-parse::

   Configuration for the Mastermind game agent.

   This module defines the configuration for the Mastermind game agent, including game
   state schema, engines, analysis settings, visualization, and game parameters.


   .. autolink-examples:: games.mastermind.config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mastermind.config.VERSION


Classes
-------

.. autoapisummary::

   games.mastermind.config.MastermindConfig


Module Contents
---------------

.. py:class:: MastermindConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Configuration for the Mastermind game agent.

   This class defines the configuration for the Mastermind game agent, including game
   state schema, engines, analysis settings, visualization, and game parameters.



   .. autolink-examples:: MastermindConfig
      :collapse:

   .. py:method:: default_config() -> MastermindConfig
      :classmethod:


      Create a default configuration.

      :returns: Default configuration for Mastermind game.
      :rtype: MastermindConfig


      .. autolink-examples:: default_config
         :collapse:


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



.. py:data:: VERSION
   :value: '1.1.0'


