games.mancala.config
====================

.. py:module:: games.mancala.config

.. autoapi-nested-parse::

   Configuration for the Mancala game agent.

   This module defines the configuration for the Mancala game agent, which includes the
   game name, state schema, engine configurations, enable_analysis, visualize, and
   stones_per_pit.


   .. autolink-examples:: games.mancala.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.mancala.config.MancalaConfig


Module Contents
---------------

.. py:class:: MancalaConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Configuration for the Mancala game agent.

   This class defines the configuration for the Mancala game agent, which includes the
   game name, state schema, engine configurations, enable_analysis, visualize, and
   stones_per_pit.



   .. autolink-examples:: MancalaConfig
      :collapse:

   .. py:method:: default_config()
      :classmethod:


      Create a default configuration.

      :returns: Default configuration for the Mancala game.
      :rtype: MancalaConfig


      .. autolink-examples:: default_config
         :collapse:


   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.mancala.state.MancalaState]
      :value: None



   .. py:attribute:: stones_per_pit
      :type:  int
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



