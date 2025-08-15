games.dominoes.config
=====================

.. py:module:: games.dominoes.config


Classes
-------

.. autoapisummary::

   games.dominoes.config.DominoesAgentConfig


Module Contents
---------------

.. py:class:: DominoesAgentConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Configuration for the dominoes agent.


   .. autolink-examples:: DominoesAgentConfig
      :collapse:

   .. py:method:: default_config() -> Any
      :classmethod:



   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: hand_size
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.dominoes.state.DominoesState]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



