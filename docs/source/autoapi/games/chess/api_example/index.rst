games.chess.api_example
=======================

.. py:module:: games.chess.api_example

FastAPI example for chess game with configurable LLMs.

This module demonstrates how to create API endpoints for chess games with configurable
LLM providers and models.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span> • <span class="module-stat">7 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   FastAPI example for chess game with configurable LLMs.

   This module demonstrates how to create API endpoints for chess games with configurable
   LLM providers and models.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.chess.api_example.active_games
      games.chess.api_example.app

            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.chess.api_example.CreateGameRequest
      games.chess.api_example.GameResponse
      games.chess.api_example.GameStateResponse
      games.chess.api_example.LLMConfig
      games.chess.api_example.MoveStreamEvent

            

.. admonition:: Functions (7)
   :class: info

   .. autoapisummary::

      games.chess.api_example.create_game
      games.chess.api_example.delete_game
      games.chess.api_example.get_game_state
      games.chess.api_example.list_games
      games.chess.api_example.list_providers
      games.chess.api_example.root
      games.chess.api_example.stream_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CreateGameRequest(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Request to create a new chess game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: black_llm
               :type:  LLMConfig
               :value: None



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: max_moves
               :type:  int
               :value: None



            .. py:attribute:: white_llm
               :type:  LLMConfig
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameResponse(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Response with game information.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: config
               :type:  dict[str, Any]


            .. py:attribute:: created_at
               :type:  str


            .. py:attribute:: game_id
               :type:  str


            .. py:attribute:: status
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameStateResponse(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Response with current game state.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: board_fen
               :type:  str


            .. py:attribute:: current_player
               :type:  str


            .. py:attribute:: game_id
               :type:  str


            .. py:attribute:: game_result
               :type:  str | None


            .. py:attribute:: move_count
               :type:  int


            .. py:attribute:: move_history
               :type:  list[tuple[str, str]]


            .. py:attribute:: status
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LLMConfig(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            LLM configuration for a player.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: model
               :type:  str | None
               :value: None



            .. py:attribute:: provider
               :type:  str
               :value: None



            .. py:attribute:: temperature
               :type:  float | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MoveStreamEvent(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Event streamed during game execution.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: data
               :type:  dict[str, Any]


            .. py:attribute:: event
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_game(request: CreateGameRequest)
            :async:


            Create a new chess game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: delete_game(game_id: str)
            :async:


            Delete a game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_game_state(game_id: str)
            :async:


            Get the current state of a game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: list_games()
            :async:


            List all active games.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: list_providers()
            :async:


            List available LLM providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: root()
            :async:


            Root endpoint with API information.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: stream_game(game_id: str, background_tasks: fastapi.BackgroundTasks)
            :async:


            Stream game execution events.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: active_games
            :type:  dict[str, dict[str, Any]]


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: app




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.api_example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

