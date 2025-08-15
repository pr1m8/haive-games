games.chess.api_client_example
==============================

.. py:module:: games.chess.api_client_example

.. autoapi-nested-parse::

   Example client for the Chess API.

   This shows how to interact with the chess API to create and play games.


   .. autolink-examples:: games.chess.api_client_example
      :collapse:


Classes
-------

.. autoapisummary::

   games.chess.api_client_example.ChessAPIClient


Functions
---------

.. autoapisummary::

   games.chess.api_client_example.main


Module Contents
---------------

.. py:class:: ChessAPIClient(base_url: str = 'http://localhost:8000')

   Simple client for the Chess API.


   .. autolink-examples:: ChessAPIClient
      :collapse:

   .. py:method:: create_game(white_provider: str = 'anthropic', white_model: str | None = None, black_provider: str = 'anthropic', black_model: str | None = None, enable_analysis: bool = True, max_moves: int = 200)

      Create a new game.


      .. autolink-examples:: create_game
         :collapse:


   .. py:method:: delete_game(game_id: str)

      Delete a game.


      .. autolink-examples:: delete_game
         :collapse:


   .. py:method:: get_game_state(game_id: str)

      Get current game state.


      .. autolink-examples:: get_game_state
         :collapse:


   .. py:method:: list_games()

      List all active games.


      .. autolink-examples:: list_games
         :collapse:


   .. py:method:: list_providers()

      Get available LLM providers.


      .. autolink-examples:: list_providers
         :collapse:


   .. py:method:: stream_game(game_id: str, callback=None)

      Stream game events.


      .. autolink-examples:: stream_game
         :collapse:


   .. py:attribute:: base_url
      :value: 'http://localhost:8000'



.. py:function:: main()

   Example usage of the Chess API client.


   .. autolink-examples:: main
      :collapse:

