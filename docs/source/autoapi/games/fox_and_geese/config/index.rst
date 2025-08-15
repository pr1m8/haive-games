games.fox_and_geese.config
==========================

.. py:module:: games.fox_and_geese.config

.. autoapi-nested-parse::

   Configuration for the Fox and Geese game agent.

   This module defines the configuration for the Fox and Geese game agent, which includes
   the game name, state schema, AugLLM configurations, enable_analysis, visualize, and
   max_turns.


   .. autolink-examples:: games.fox_and_geese.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.fox_and_geese.config.FoxAndGeeseConfig


Module Contents
---------------

.. py:class:: FoxAndGeeseConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Configuration for the Fox and Geese game agent.

   This class defines the configuration for the Fox and Geese game agent, which
   includes the game name, state schema, AugLLM configurations, enable_analysis,
   visualize, recursion_limit and max_turns.



   .. autolink-examples:: FoxAndGeeseConfig
      :collapse:

   .. py:method:: default_config()
      :classmethod:


      Create a default configuration.


      .. autolink-examples:: default_config
         :collapse:


   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: input_schema
      :type:  type[haive.games.fox_and_geese.state.FoxAndGeeseState]
      :value: None



   .. py:attribute:: max_turns
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: recursion_limit
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.fox_and_geese.state.FoxAndGeeseState]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



