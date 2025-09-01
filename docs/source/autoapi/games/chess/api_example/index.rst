games.chess.api_example
=======================

.. py:module:: games.chess.api_example

.. autoapi-nested-parse::

   FastAPI example for chess game with configurable LLMs.

   This module demonstrates how to create API endpoints for chess games with configurable
   LLM providers and models.



Attributes
----------

.. autoapisummary::

   games.chess.api_example.active_games
   games.chess.api_example.app


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/chess/api_example/CreateGameRequest
   /autoapi/games/chess/api_example/GameResponse
   /autoapi/games/chess/api_example/GameStateResponse
   /autoapi/games/chess/api_example/LLMConfig
   /autoapi/games/chess/api_example/MoveStreamEvent

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

.. py:function:: create_game(request: CreateGameRequest)
   :async:


   Create a new chess game.


.. py:function:: delete_game(game_id: str)
   :async:


   Delete a game.


.. py:function:: get_game_state(game_id: str)
   :async:


   Get the current state of a game.


.. py:function:: list_games()
   :async:


   List all active games.


.. py:function:: list_providers()
   :async:


   List available LLM providers.


.. py:function:: root()
   :async:


   Root endpoint with API information.


.. py:function:: stream_game(game_id: str, background_tasks: fastapi.BackgroundTasks)
   :async:


   Stream game execution events.


.. py:data:: active_games
   :type:  dict[str, dict[str, Any]]

.. py:data:: app

