games.single_player.wordle.example
==================================

.. py:module:: games.single_player.wordle.example

.. autoapi-nested-parse::

   Example Word Connections game with interactive UI.

   Uses the May 22, 2025 puzzle (#711).


   .. autolink-examples:: games.single_player.wordle.example
      :collapse:


Classes
-------

.. autoapisummary::

   games.single_player.wordle.example.WordConnectionsUI


Functions
---------

.. autoapisummary::

   games.single_player.wordle.example.main


Module Contents
---------------

.. py:class:: WordConnectionsUI

   Interactive UI for Word Connections game.


   .. autolink-examples:: WordConnectionsUI
      :collapse:

   .. py:method:: display_grid(state: haive.games.single_player.wordle.models.WordConnectionsState)

      Display the game grid in a nice format.


      .. autolink-examples:: display_grid
         :collapse:


   .. py:method:: display_solution(state: haive.games.single_player.wordle.models.WordConnectionsState)

      Display the full solution.


      .. autolink-examples:: display_solution
         :collapse:


   .. py:method:: play_game()
      :async:


      Play the game with AI assistance.


      .. autolink-examples:: play_game
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: config


   .. py:attribute:: state
      :type:  haive.games.single_player.wordle.models.WordConnectionsState | None
      :value: None



.. py:function:: main()
   :async:


   Run the example game.


   .. autolink-examples:: main
      :collapse:

