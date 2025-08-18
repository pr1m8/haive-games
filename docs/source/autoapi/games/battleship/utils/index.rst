games.battleship.utils
======================

.. py:module:: games.battleship.utils

Battleship game utility functions.

This module provides helper functions for the Battleship game, including:
    - Board visualization
    - Coordinate formatting
    - Game status checking



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 functions</span>   </div>

.. autoapi-nested-parse::

   Battleship game utility functions.

   This module provides helper functions for the Battleship game, including:
       - Board visualization
       - Coordinate formatting
       - Game status checking



      
            
            
            

.. admonition:: Functions (5)
   :class: info

   .. autoapisummary::

      games.battleship.utils.calculate_game_stats
      games.battleship.utils.check_all_ships_placed
      games.battleship.utils.format_coordinates_list
      games.battleship.utils.format_ship_types
      games.battleship.utils.visualize_board

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: calculate_game_stats(move_history: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]

            Calculate game statistics from move history.

            :param move_history: List of (player, outcome) tuples

            :returns: Dictionary of game statistics



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: check_all_ships_placed(ship_placements: list[dict[str, Any]]) -> tuple[bool, str | None]

            Check if all required ships have been placed.

            :param ship_placements: List of ship placement dictionaries

            :returns: Tuple of (is_complete, error_message)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: format_coordinates_list(coords_list: list[dict[str, int]]) -> str

            Format a list of coordinates for display.

            :param coords_list: List of coordinate dictionaries

            :returns: Formatted string of coordinates



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: format_ship_types(ship_types: list[str]) -> str

            Format a list of ship types for display.

            :param ship_types: List of ship type strings

            :returns: Formatted string of ship types



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: visualize_board(board: dict[str, Any], is_opponent: bool = False) -> str

            Create a string representation of the Battleship board.

            :param board: Dictionary containing board information
            :param is_opponent: Whether this is the opponent's board

            :returns: String representation of the board





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.utils import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

