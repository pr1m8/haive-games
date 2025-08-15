games.single_player.towers_of_hanoi.ui
======================================

.. py:module:: games.single_player.towers_of_hanoi.ui


Attributes
----------

.. autoapisummary::

   games.single_player.towers_of_hanoi.ui.console


Classes
-------

.. autoapisummary::

   games.single_player.towers_of_hanoi.ui.HanoiUI


Functions
---------

.. autoapisummary::

   games.single_player.towers_of_hanoi.ui.main


Module Contents
---------------

.. py:class:: HanoiUI

   Rich UI for Tower of Hanoi game.


   .. autolink-examples:: HanoiUI
      :collapse:

   .. py:method:: ai_move()

      Let AI make a move.


      .. autolink-examples:: ai_move
         :collapse:


   .. py:method:: auto_play(live)

      Auto-play to completion.


      .. autolink-examples:: auto_play
         :collapse:


   .. py:method:: create_display() -> rich.panel.Panel

      Create the game display.


      .. autolink-examples:: create_display
         :collapse:


   .. py:method:: format_moves() -> str

      Format recent moves for display.


      .. autolink-examples:: format_moves
         :collapse:


   .. py:method:: manual_move()

      Allow manual move input.


      .. autolink-examples:: manual_move
         :collapse:


   .. py:method:: play_game()

      Main game loop.


      .. autolink-examples:: play_game
         :collapse:


   .. py:method:: run()

      Run the interactive UI.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: agent
      :type:  haive.games.single_player.towers_of_hanoi.agent.HanoiAgent | None
      :value: None



   .. py:attribute:: game
      :type:  haive.games.single_player.towers_of_hanoi.game.HanoiGame | None
      :value: None



   .. py:attribute:: state


.. py:function:: main()

   Run the Tower of Hanoi UI.


   .. autolink-examples:: main
      :collapse:

.. py:data:: console

