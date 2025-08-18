games.single_player.wordle.config
=================================

.. py:module:: games.single_player.wordle.config

Module documentation for games.single_player.wordle.config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">1 functions</span>   </div>


      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.single_player.wordle.config.WordConnectionsAgentConfig
      games.single_player.wordle.config.WordConnectionsGuess

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.single_player.wordle.config.create_game_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsAgentConfig

            Bases: :py:obj:`haive.games.framework.base.GameConfig`


            Configuration for Word Connections agent.


            .. py:attribute:: game_engine
               :type:  haive.core.engine.aug_llm.AugLLMConfig
               :value: None



            .. py:attribute:: puzzle_set
               :type:  str
               :value: None



            .. py:attribute:: state_schema
               :type:  type
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsGuess(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A guess in Word Connections.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: category
               :type:  str
               :value: None



            .. py:attribute:: confidence
               :type:  float
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None



            .. py:attribute:: words
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_game_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Create the main game playing prompt.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.wordle.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

