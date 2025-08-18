games.chess.api_client_example
==============================

.. py:module:: games.chess.api_client_example

Example client for the Chess API.

This shows how to interact with the chess API to create and play games.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Example client for the Chess API.

   This shows how to interact with the chess API to create and play games.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.api_client_example.ChessAPIClient

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.chess.api_client_example.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessAPIClient(base_url: str = 'http://localhost:8000')

            Simple client for the Chess API.


            .. py:method:: create_game(white_provider: str = 'anthropic', white_model: str | None = None, black_provider: str = 'anthropic', black_model: str | None = None, enable_analysis: bool = True, max_moves: int = 200)

               Create a new game.



            .. py:method:: delete_game(game_id: str)

               Delete a game.



            .. py:method:: get_game_state(game_id: str)

               Get current game state.



            .. py:method:: list_games()

               List all active games.



            .. py:method:: list_providers()

               Get available LLM providers.



            .. py:method:: stream_game(game_id: str, callback=None)

               Stream game events.



            .. py:attribute:: base_url
               :value: 'http://localhost:8000'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Example usage of the Chess API client.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.api_client_example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

