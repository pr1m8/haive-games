games.go.go_engine
==================

.. py:module:: games.go.go_engine

Simple Go engine wrapper using sgfmill instead of sente.

This module provides a compatibility layer to replace sente with sgfmill, which is
compatible with Python 3.12.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">3 functions</span> • <span class="module-stat">4 attributes</span>   </div>

.. autoapi-nested-parse::

   Simple Go engine wrapper using sgfmill instead of sente.

   This module provides a compatibility layer to replace sente with sgfmill, which is
   compatible with Python 3.12.



      

.. admonition:: Attributes (4)
   :class: tip

   .. autoapisummary::

      games.go.go_engine.BLACK
      games.go.go_engine.SGFMILL_AVAILABLE
      games.go.go_engine.WHITE
      games.go.go_engine.logger

            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.go.go_engine.GoGame
      games.go.go_engine.sgf

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.go.go_engine.Game
      games.go.go_engine.dumps_sgf
      games.go.go_engine.loads_sgf

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GoGame(board_size: int = 19)

            Simple Go game wrapper using sgfmill.


            .. py:method:: play_move(color: str, move: tuple[int, int] | None)

               Play a move on the board.

               :param color: 'b' for black, 'w' for white
               :param move: (row, col) tuple or None for pass



            .. py:method:: to_sgf() -> str

               Convert game to SGF format.



            .. py:method:: turn() -> str

               Get current player to move.



            .. py:attribute:: board


            .. py:attribute:: board_size
               :value: 19



            .. py:attribute:: captured


            .. py:attribute:: current_player
               :value: 'b'



            .. py:attribute:: move_history
               :value: []



            .. py:attribute:: passes
               :value: 0




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: sgf

            SGF compatibility wrapper.


            .. py:method:: dumps(game)
               :staticmethod:


               Save game to SGF.



            .. py:method:: loads(sgf_string: str)
               :staticmethod:


               Load game from SGF.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: Game(board_size: int = 19) -> GoGame

            Create a new Go game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: dumps_sgf(game: GoGame) -> str

            Convert game to SGF string.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: loads_sgf(sgf_string: str) -> GoGame

            Load a game from SGF string.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: BLACK
            :value: 'b'



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: SGFMILL_AVAILABLE
            :value: True



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: WHITE
            :value: 'w'



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.go.go_engine import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

