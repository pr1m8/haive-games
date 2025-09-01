games.battleship.utils
======================

.. py:module:: games.battleship.utils

.. autoapi-nested-parse::

   Battleship game utility functions.

   This module provides helper functions for the Battleship game, including:
       - Board visualization
       - Coordinate formatting
       - Game status checking



Functions
---------

.. autoapisummary::

   games.battleship.utils.calculate_game_stats
   games.battleship.utils.check_all_ships_placed
   games.battleship.utils.format_coordinates_list
   games.battleship.utils.format_ship_types
   games.battleship.utils.visualize_board


Module Contents
---------------

.. py:function:: calculate_game_stats(move_history: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]

   Calculate game statistics from move history.

   :param move_history: List of (player, outcome) tuples

   :returns: Dictionary of game statistics


.. py:function:: check_all_ships_placed(ship_placements: list[dict[str, Any]]) -> tuple[bool, str | None]

   Check if all required ships have been placed.

   :param ship_placements: List of ship placement dictionaries

   :returns: Tuple of (is_complete, error_message)


.. py:function:: format_coordinates_list(coords_list: list[dict[str, int]]) -> str

   Format a list of coordinates for display.

   :param coords_list: List of coordinate dictionaries

   :returns: Formatted string of coordinates


.. py:function:: format_ship_types(ship_types: list[str]) -> str

   Format a list of ship types for display.

   :param ship_types: List of ship type strings

   :returns: Formatted string of ship types


.. py:function:: visualize_board(board: dict[str, Any], is_opponent: bool = False) -> str

   Create a string representation of the Battleship board.

   :param board: Dictionary containing board information
   :param is_opponent: Whether this is the opponent's board

   :returns: String representation of the board


