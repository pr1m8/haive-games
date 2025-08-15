games.nim.config
================

.. py:module:: games.nim.config

.. autoapi-nested-parse::

   Configuration for the Nim game.

   This module defines the configuration for the Nim game, which includes the state schema,
   engines, enable_analysis, visualize, and pile_sizes.


   .. autolink-examples:: games.nim.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.nim.config.NimConfig


Module Contents
---------------

.. py:class:: NimConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Configuration for the Nim agent.

   .. attribute:: state_schema

      The state schema for the Nim game.

      :type: Type[NimState]

   .. attribute:: engines

      The engines for the Nim game.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: enable_analysis

      Whether to enable analysis.

      :type: bool

   .. attribute:: visualize

      Whether to visualize the game.

      :type: bool


   .. autolink-examples:: NimConfig
      :collapse:

   .. py:method:: default_config()
      :classmethod:


      Create a default configuration.

      :returns: The default configuration.
      :rtype: NimConfig


      .. autolink-examples:: default_config
         :collapse:


   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: misere_mode
      :type:  bool
      :value: None



   .. py:attribute:: pile_sizes
      :type:  list[int]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.nim.state.NimState]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



