games.nim.ui
============

.. py:module:: games.nim.ui

.. autoapi-nested-parse::

   Rich UI implementation for the Nim game.

   This module provides a Rich-based UI for visualizing and interacting with the Nim game.
   It includes a NimUI class that handles visualization of the game state, piles, and game
   information.


   .. autolink-examples:: games.nim.ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.nim.ui.RICH_AVAILABLE
   games.nim.ui.logger


Classes
-------

.. autoapisummary::

   games.nim.ui.NimUI


Module Contents
---------------

.. py:class:: NimUI

   Rich terminal UI for the Nim game.

   This class provides methods for visualizing the Nim game state using the Rich
   library. It includes methods for displaying the game board, piles, game information,
   and analysis.


   Initialize the UI with a Rich console if available.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NimUI
      :collapse:

   .. py:method:: _display_text_ui(state: haive.games.nim.state.NimState)

      Display a text-based UI for the game state when Rich is not available.

      :param state: The current game state.


      .. autolink-examples:: _display_text_ui
         :collapse:


   .. py:method:: create_analysis_panel(state: haive.games.nim.state.NimState) -> rich.panel.Panel | None

      Create a panel showing the latest analysis if available.

      :param state: The current game state.

      :returns: A Rich panel containing analysis information, or None if no analysis.
      :rtype: Optional[Panel]


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_header(state: haive.games.nim.state.NimState) -> rich.panel.Panel

      Create header panel with game info.

      :param state: The current game state.

      :returns: A Rich panel containing the game header information.
      :rtype: Panel


      .. autolink-examples:: create_header
         :collapse:


   .. py:method:: create_layout(state: haive.games.nim.state.NimState) -> rich.layout.Layout

      Create the complete layout for the game display.

      :param state: The current game state.

      :returns: A Rich layout for the complete game display.
      :rtype: Layout


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: create_moves_table(state: haive.games.nim.state.NimState) -> rich.table.Table

      Create a table showing move history.

      :param state: The current game state.

      :returns: A Rich table containing the move history.
      :rtype: Table


      .. autolink-examples:: create_moves_table
         :collapse:


   .. py:method:: create_piles_panel(state: haive.games.nim.state.NimState) -> rich.panel.Panel

      Create a panel showing the piles of stones.

      :param state: The current game state.

      :returns: A Rich panel containing visualizations of the piles.
      :rtype: Panel


      .. autolink-examples:: create_piles_panel
         :collapse:


   .. py:method:: display_game_state(state: haive.games.nim.state.NimState | dict[str, Any])

      Display the current game state using Rich UI or fallback text UI.

      :param state: The current game state as a NimState object or dict.


      .. autolink-examples:: display_game_state
         :collapse:


   .. py:method:: prompt_for_move(state: haive.games.nim.state.NimState) -> haive.games.nim.models.NimMove

      Prompt the user to input a move.

      :param state: The current game state.

      :returns: The move chosen by the user.
      :rtype: NimMove


      .. autolink-examples:: prompt_for_move
         :collapse:


   .. py:attribute:: EMPTY_SYMBOL
      :value: '⚫'



   .. py:attribute:: STATUS_EMOJIS


   .. py:attribute:: STONE_SYMBOL
      :value: '🔵'



   .. py:attribute:: delay
      :value: 0.5



.. py:data:: RICH_AVAILABLE
   :value: True


.. py:data:: logger

