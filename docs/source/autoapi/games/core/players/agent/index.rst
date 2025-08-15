games.core.players.agent
========================

.. py:module:: games.core.players.agent


Classes
-------

.. autoapisummary::

   games.core.players.agent.BasePlayerAgent


Module Contents
---------------

.. py:class:: BasePlayerAgent(game_config: haive.games.core.agent.game_config.GameConfig, player_config: PlayerConfig)

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`, :py:obj:`abc.ABC`


   Base class for player agents.


   .. autolink-examples:: BasePlayerAgent
      :collapse:

   .. py:attribute:: analysis_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate


   .. py:attribute:: move_model
      :type:  pydantic.BaseModel


   .. py:attribute:: move_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate


