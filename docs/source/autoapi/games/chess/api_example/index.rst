games.chess.api_example
=======================

.. py:module:: games.chess.api_example

.. autoapi-nested-parse::

   FastAPI example for chess game with configurable LLMs.

   This module demonstrates how to create API endpoints for chess games with configurable
   LLM providers and models.


   .. autolink-examples:: games.chess.api_example
      :collapse:


Attributes
----------

.. autoapisummary::

   games.chess.api_example.active_games
   games.chess.api_example.app


Classes
-------

.. autoapisummary::

   games.chess.api_example.CreateGameRequest
   games.chess.api_example.GameResponse
   games.chess.api_example.GameStateResponse
   games.chess.api_example.LLMConfig
   games.chess.api_example.MoveStreamEvent


Functions
---------

.. autoapisummary::

   games.chess.api_example.create_game
   games.chess.api_example.delete_game
   games.chess.api_example.get_game_state
   games.chess.api_example.list_games
   games.chess.api_example.list_providers
   games.chess.api_example.root
   games.chess.api_example.stream_game


Module Contents
---------------

.. py:class:: CreateGameRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Request to create a new chess game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CreateGameRequest
      :collapse:

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



.. py:class:: GameResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response with game information.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameResponse
      :collapse:

   .. py:attribute:: config
      :type:  dict[str, Any]


   .. py:attribute:: created_at
      :type:  str


   .. py:attribute:: game_id
      :type:  str


   .. py:attribute:: status
      :type:  str


.. py:class:: GameStateResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response with current game state.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameStateResponse
      :collapse:

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


.. py:class:: LLMConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   LLM configuration for a player.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LLMConfig
      :collapse:

   .. py:attribute:: model
      :type:  str | None
      :value: None



   .. py:attribute:: provider
      :type:  str
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



.. py:class:: MoveStreamEvent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Event streamed during game execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MoveStreamEvent
      :collapse:

   .. py:attribute:: data
      :type:  dict[str, Any]


   .. py:attribute:: event
      :type:  str


.. py:function:: create_game(request: CreateGameRequest)
   :async:


   Create a new chess game.


   .. autolink-examples:: create_game
      :collapse:

.. py:function:: delete_game(game_id: str)
   :async:


   Delete a game.


   .. autolink-examples:: delete_game
      :collapse:

.. py:function:: get_game_state(game_id: str)
   :async:


   Get the current state of a game.


   .. autolink-examples:: get_game_state
      :collapse:

.. py:function:: list_games()
   :async:


   List all active games.


   .. autolink-examples:: list_games
      :collapse:

.. py:function:: list_providers()
   :async:


   List available LLM providers.


   .. autolink-examples:: list_providers
      :collapse:

.. py:function:: root()
   :async:


   Root endpoint with API information.


   .. autolink-examples:: root
      :collapse:

.. py:function:: stream_game(game_id: str, background_tasks: fastapi.BackgroundTasks)
   :async:


   Stream game execution events.


   .. autolink-examples:: stream_game
      :collapse:

.. py:data:: active_games
   :type:  dict[str, dict[str, Any]]

.. py:data:: app

