piece
=====

.. py:module:: piece

Module documentation for piece


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      piece.CrosswordLetter

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordLetter

            Bases: :py:obj:`haive.games.core.piece.base.GamePiece`\ [\ :py:obj:`haive.games.core.position.base.GridPosition`\ ]


            A letter in a crossword puzzle.


            .. py:method:: can_move_to(position: haive.games.core.position.base.GridPosition, board: haive.games.single_player.crossword_puzzle.game.board.CrosswordBoard) -> bool

               Check if this letter can be placed at this position.



            .. py:method:: validate_letter(v: str) -> str
               :classmethod:


               Ensure letter is a single uppercase character.



            .. py:attribute:: is_filled
               :type:  bool
               :value: False



            .. py:attribute:: letter
               :type:  str





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from piece import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

