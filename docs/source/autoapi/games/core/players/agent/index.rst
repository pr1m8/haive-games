games.core.players.agent
========================

.. py:module:: games.core.players.agent

Module documentation for games.core.players.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.core.players.agent.BasePlayerAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BasePlayerAgent(game_config: haive.games.core.agent.game_config.GameConfig, player_config: PlayerConfig)

            Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`, :py:obj:`abc.ABC`


            Base class for player agents.


            .. py:attribute:: analysis_prompt
               :type:  langchain_core.prompts.ChatPromptTemplate


            .. py:attribute:: move_model
               :type:  pydantic.BaseModel


            .. py:attribute:: move_prompt
               :type:  langchain_core.prompts.ChatPromptTemplate





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.players.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

