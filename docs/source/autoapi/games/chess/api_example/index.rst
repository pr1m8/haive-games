
:py:mod:`games.chess.api_example`
=================================

.. py:module:: games.chess.api_example

FastAPI example for chess game with configurable LLMs.

This module demonstrates how to create API endpoints for chess games with configurable
LLM providers and models.


.. autolink-examples:: games.chess.api_example
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.api_example.CreateGameRequest
   games.chess.api_example.GameResponse
   games.chess.api_example.GameStateResponse
   games.chess.api_example.LLMConfig
   games.chess.api_example.MoveStreamEvent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CreateGameRequest:

   .. graphviz::
      :align: center

      digraph inheritance_CreateGameRequest {
        node [shape=record];
        "CreateGameRequest" [label="CreateGameRequest"];
        "pydantic.BaseModel" -> "CreateGameRequest";
      }

.. autopydantic_model:: games.chess.api_example.CreateGameRequest
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameResponse:

   .. graphviz::
      :align: center

      digraph inheritance_GameResponse {
        node [shape=record];
        "GameResponse" [label="GameResponse"];
        "pydantic.BaseModel" -> "GameResponse";
      }

.. autopydantic_model:: games.chess.api_example.GameResponse
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameStateResponse:

   .. graphviz::
      :align: center

      digraph inheritance_GameStateResponse {
        node [shape=record];
        "GameStateResponse" [label="GameStateResponse"];
        "pydantic.BaseModel" -> "GameStateResponse";
      }

.. autopydantic_model:: games.chess.api_example.GameStateResponse
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LLMConfig {
        node [shape=record];
        "LLMConfig" [label="LLMConfig"];
        "pydantic.BaseModel" -> "LLMConfig";
      }

.. autopydantic_model:: games.chess.api_example.LLMConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MoveStreamEvent:

   .. graphviz::
      :align: center

      digraph inheritance_MoveStreamEvent {
        node [shape=record];
        "MoveStreamEvent" [label="MoveStreamEvent"];
        "pydantic.BaseModel" -> "MoveStreamEvent";
      }

.. autopydantic_model:: games.chess.api_example.MoveStreamEvent
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



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



.. rubric:: Related Links

.. autolink-examples:: games.chess.api_example
   :collapse:
   
.. autolink-skip:: next
