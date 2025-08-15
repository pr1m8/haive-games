games.dominoes.rich_ui
======================

.. py:module:: games.dominoes.rich_ui

.. autoapi-nested-parse::

   Enhanced Rich UI module for Dominoes game visualization.

   This module provides an enhanced rich console UI for visualizing the Dominoes game, with
   better styling, clearer representation of dominoes, and improved game animations.


   .. autolink-examples:: games.dominoes.rich_ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.dominoes.rich_ui.logger


Classes
-------

.. autoapisummary::

   games.dominoes.rich_ui.DominoesRichUI


Module Contents
---------------

.. py:class:: DominoesRichUI(console: rich.console.Console | None = None)

   Enhanced Rich UI for Dominoes game visualization.

   This class provides a visually appealing terminal UI for Dominoes games,
   with styled components, animations, and comprehensive game information.

   Features:
       - Beautiful domino tile visualization with ASCII art
       - Game board with clear indication of playable ends
       - Player hands with pip count and tile organization
       - Game information and score tracking
       - Move history and player analysis
       - Thinking animations and move visualizations

   .. attribute:: console

      Rich console for output

      :type: Console

   .. attribute:: layout

      Layout manager for UI components

      :type: Layout

   .. attribute:: colors

      Color schemes for different UI elements

      :type: dict

   .. rubric:: Examples

   >>> ui = DominoesRichUI()
   >>> state = DominoesState.initialize()
   >>> ui.display_state(state)  # Display the initial game state

   Initialize the UI.

   :param console: Optional Rich console instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DominoesRichUI
      :collapse:

   .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

      Check if a dict contains the required fields for DominoesState.

      :param data: Dictionary to check

      :returns: True if the dict appears to be a valid game state


      .. autolink-examples:: _is_valid_game_state_dict
         :collapse:


   .. py:method:: animate_move(state_before: haive.games.dominoes.state.DominoesState, state_after: haive.games.dominoes.state.DominoesState, delay: float = 0.5) -> None

      Animate a move being made.

      Shows a smooth transition between the before and after states with
      visual indicators of what changed.

      :param state_before: Game state before the move
      :param state_after: Game state after the move
      :param delay: Delay in seconds for the animation

      :returns: None


      .. autolink-examples:: animate_move
         :collapse:


   .. py:method:: create_analysis_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a panel showing the latest analysis.

      :param game_state: Current game state

      :returns: Rich panel with analysis info


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_board_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a visual representation of the dominoes board.

      :param game_state: Current game state

      :returns: Rich panel representing the board


      .. autolink-examples:: create_board_panel
         :collapse:


   .. py:method:: create_domino_tile_art(tile: haive.games.dominoes.models.DominoTile, open_end: bool = False) -> rich.text.Text

      Create ASCII art representation of a domino tile.

      :param tile: The domino tile to represent
      :param open_end: Whether this tile is at an open end of the board

      :returns: Rich Text object with tile representation


      .. autolink-examples:: create_domino_tile_art
         :collapse:


   .. py:method:: create_game_info_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a panel with game information.

      :param game_state: Current game state

      :returns: Rich panel with game info


      .. autolink-examples:: create_game_info_panel
         :collapse:


   .. py:method:: create_layout(game_state: haive.games.dominoes.state.DominoesState) -> rich.layout.Layout

      Create the complete rich UI layout.

      :param game_state: Current game state

      :returns: Complete rich layout


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: create_move_history_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a panel showing move history.

      :param game_state: Current game state

      :returns: Rich panel with move history


      .. autolink-examples:: create_move_history_panel
         :collapse:


   .. py:method:: create_player_hand_panel(game_state: haive.games.dominoes.state.DominoesState, player: str) -> rich.panel.Panel

      Create a panel showing a player's hand.

      :param game_state: Current game state
      :param player: Player whose hand to display

      :returns: Rich panel with player's hand


      .. autolink-examples:: create_player_hand_panel
         :collapse:


   .. py:method:: display_final_results(final_state: Any) -> None

      Display final game results.

      :param final_state: Final game state


      .. autolink-examples:: display_final_results
         :collapse:


   .. py:method:: display_game_with_animation(state_sequence: list[haive.games.dominoes.state.DominoesState], delay: float = 1.0) -> None

      Display a sequence of game states with smooth transitions.

      This is useful for replaying a game or showing a sequence of moves with
      visual transitions between states.

      :param state_sequence: List of game states in sequence
      :param delay: Delay in seconds between states

      :returns: None


      .. autolink-examples:: display_game_with_animation
         :collapse:


   .. py:method:: display_state(state_data: Any) -> bool

      Display the game state using rich UI.

      :param state_data: State data in various formats

      :returns: True if display was successful, False otherwise


      .. autolink-examples:: display_state
         :collapse:


   .. py:method:: display_welcome() -> None

      Display welcome message.


      .. autolink-examples:: display_welcome
         :collapse:


   .. py:method:: extract_game_state(state_data: Any) -> haive.games.dominoes.state.DominoesState | None

      Extract DominoesState from various input formats.

      :param state_data: State data in various formats

      :returns: DominoesState instance or None if extraction fails


      .. autolink-examples:: extract_game_state
         :collapse:


   .. py:method:: run_game_with_ui(agent, delay: float = 1.0) -> haive.games.dominoes.state.DominoesState

      Run a complete game with UI visualization.

      This method handles the entire game flow, including initialization,
      move animation, and final results display.

      :param agent: The game agent that manages the game logic
      :param delay: Delay in seconds between game states

      :returns: Final game state


      .. autolink-examples:: run_game_with_ui
         :collapse:


   .. py:method:: show_move(move: haive.games.dominoes.models.DominoMove | str, player: str) -> None

      Display a move being made.

      Shows a formatted message indicating which player made which move,
      whether it's playing a tile or passing.

      :param move: The move being made ("pass" or DominoMove)
      :type move: Union[DominoMove, str]
      :param player: Player making the move ("player1" or "player2")
      :type player: str

      :returns: None


      .. autolink-examples:: show_move
         :collapse:


   .. py:method:: show_thinking(player: str, message: str = 'Thinking...') -> None

      Display a thinking animation for the current player.

      Shows a spinner animation with player-colored text to indicate
      that the player is thinking about their move.

      :param player: Current player ("player1" or "player2")
      :type player: str
      :param message: Custom message to display. Defaults to "Thinking...".
      :type message: str, optional

      :returns: None


      .. autolink-examples:: show_thinking
         :collapse:


   .. py:attribute:: colors


   .. py:attribute:: console


.. py:data:: logger

