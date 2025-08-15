games.single_player.wordle.config
=================================

.. py:module:: games.single_player.wordle.config


Classes
-------

.. autoapisummary::

   games.single_player.wordle.config.WordConnectionsAgentConfig
   games.single_player.wordle.config.WordConnectionsGuess


Functions
---------

.. autoapisummary::

   games.single_player.wordle.config.create_game_prompt


Module Contents
---------------

.. py:class:: WordConnectionsAgentConfig

   Bases: :py:obj:`haive.games.framework.base.GameConfig`


   Configuration for Word Connections agent.


   .. autolink-examples:: WordConnectionsAgentConfig
      :collapse:

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



.. py:class:: WordConnectionsGuess(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A guess in Word Connections.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WordConnectionsGuess
      :collapse:

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



.. py:function:: create_game_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create the main game playing prompt.


   .. autolink-examples:: create_game_prompt
      :collapse:

