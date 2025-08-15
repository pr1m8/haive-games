games.fox_and_geese.rich_ui
===========================

.. py:module:: games.fox_and_geese.rich_ui

.. autoapi-nested-parse::

   Enhanced Rich UI module for Fox and Geese game visualization.

   This module provides an enhanced rich console UI for visualizing the Fox and Geese game,
   with better styling, animated piece movements, and improved game information display.


   .. autolink-examples:: games.fox_and_geese.rich_ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.fox_and_geese.rich_ui.logger


Classes
-------

.. autoapisummary::

   games.fox_and_geese.rich_ui.FoxAndGeeseRichUI


Module Contents
---------------

.. py:class:: FoxAndGeeseRichUI(console: rich.console.Console | None = None)

   Enhanced Rich UI for Fox and Geese game visualization.

   This class provides a visually appealing terminal UI for Fox and Geese games,
   with styled components, animations, and comprehensive game information.

   Features:
       - Beautiful game board visualization with colored squares
       - Animated piece movements for fox and geese
       - Detailed game statistics and turn information
       - Move history tracking with visual indicators
       - Analysis visualization for both fox and geese strategies
       - Thinking animations and move highlights

   .. attribute:: console

      Rich console for output

      :type: Console

   .. attribute:: colors

      Color schemes for different UI elements

      :type: dict

   Initialize the UI.

   :param console: Optional Rich console instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FoxAndGeeseRichUI
      :collapse:

   .. py:method:: _get_square_symbol(row: int, col: int) -> str

      Get the symbol for a board square based on its position.

      In Fox and Geese, pieces can move on any square but we use a checkered pattern
      to make the board more visually appealing.

      :param row: Row index
      :param col: Column index

      :returns: Symbol for the square


      .. autolink-examples:: _get_square_symbol
         :collapse:


   .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

      Check if a dict contains the required fields for FoxAndGeeseState.

      :param data: Dictionary to check

      :returns: True if the dict appears to be a valid game state


      .. autolink-examples:: _is_valid_game_state_dict
         :collapse:


   .. py:method:: animate_move(state_before: haive.games.fox_and_geese.state.FoxAndGeeseState, state_after: haive.games.fox_and_geese.state.FoxAndGeeseState, delay: float = 0.5) -> None

      Animate a move being made.

      Shows a smooth transition between the before and after states with
      visual indicators of what changed.

      :param state_before: Game state before the move
      :param state_after: State after the move
      :param delay: Delay in seconds for the animation

      :returns: None


      .. autolink-examples:: animate_move
         :collapse:


   .. py:method:: create_analysis_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

      Create an enhanced panel showing the latest analysis.

      :param game_state: Current game state

      :returns: Rich panel with detailed analysis


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_board_table(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState, highlight_positions: set[haive.games.fox_and_geese.models.FoxAndGeesePosition] | None = None, capture_position: haive.games.fox_and_geese.models.FoxAndGeesePosition | None = None) -> rich.table.Table

      Create an enhanced visual representation of the board.

      :param game_state: Current game state
      :param highlight_positions: Optional positions to highlight (for showing moves)
      :param capture_position: Optional position to highlight as a capture

      :returns: Rich table representing the board


      .. autolink-examples:: create_board_table
         :collapse:


   .. py:method:: create_game_info_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

      Create an enhanced panel with game information.

      :param game_state: Current game state

      :returns: Rich panel with detailed game info


      .. autolink-examples:: create_game_info_panel
         :collapse:


   .. py:method:: create_layout(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState, highlight_positions: set[haive.games.fox_and_geese.models.FoxAndGeesePosition] | None = None, capture_position: haive.games.fox_and_geese.models.FoxAndGeesePosition | None = None, legal_moves: list[haive.games.fox_and_geese.models.FoxAndGeeseMove] | None = None) -> rich.layout.Layout

      Create the enhanced complete rich UI layout.

      :param game_state: Current game state
      :param highlight_positions: Optional positions to highlight
      :param capture_position: Optional position being captured
      :param legal_moves: Optional list of legal moves

      :returns: Complete rich layout


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: create_legal_moves_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState, legal_moves: list[haive.games.fox_and_geese.models.FoxAndGeeseMove] | None = None) -> rich.panel.Panel

      Create a panel showing legal moves for the current player.

      :param game_state: Current game state
      :param legal_moves: Optional list of legal moves

      :returns: Rich panel with legal moves info


      .. autolink-examples:: create_legal_moves_panel
         :collapse:


   .. py:method:: create_move_history_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

      Create an enhanced panel showing move history.

      :param game_state: Current game state

      :returns: Rich panel with detailed move history


      .. autolink-examples:: create_move_history_panel
         :collapse:


   .. py:method:: display_final_results(final_state: Any) -> None

      Display enhanced final game results.

      :param final_state: Final game state


      .. autolink-examples:: display_final_results
         :collapse:


   .. py:method:: display_game_with_animation(state_sequence: list[haive.games.fox_and_geese.state.FoxAndGeeseState], delay: float = 1.0) -> None

      Display a sequence of game states with smooth transitions.

      This is useful for replaying a game or showing a sequence of moves with
      visual transitions between states.

      :param state_sequence: List of game states in sequence
      :param delay: Delay in seconds between states

      :returns: None


      .. autolink-examples:: display_game_with_animation
         :collapse:


   .. py:method:: display_state(state_data: Any, highlight_positions: set[haive.games.fox_and_geese.models.FoxAndGeesePosition] | None = None, capture_position: haive.games.fox_and_geese.models.FoxAndGeesePosition | None = None, legal_moves: list[haive.games.fox_and_geese.models.FoxAndGeeseMove] | None = None) -> bool

      Display the game state using enhanced rich UI.

      :param state_data: State data in various formats
      :param highlight_positions: Optional positions to highlight
      :param capture_position: Optional position being captured
      :param legal_moves: Optional list of legal moves

      :returns: True if display was successful, False otherwise


      .. autolink-examples:: display_state
         :collapse:


   .. py:method:: display_welcome() -> None

      Display welcome message.


      .. autolink-examples:: display_welcome
         :collapse:


   .. py:method:: extract_game_state(state_data: Any) -> haive.games.fox_and_geese.state.FoxAndGeeseState | None

      Extract FoxAndGeeseState from various input formats.

      :param state_data: State data in various formats

      :returns: FoxAndGeeseState instance or None if extraction fails


      .. autolink-examples:: extract_game_state
         :collapse:


   .. py:method:: run_fox_and_geese_game(agent, delay: float = 1.0) -> haive.games.fox_and_geese.state.FoxAndGeeseState

      Run a complete Fox and Geese game with UI visualization.

      This method handles the entire game flow, including initialization,
      move animation, and final results display.

      :param agent: The game agent that manages the game logic
      :param delay: Delay in seconds between game states

      :returns: Final game state


      .. autolink-examples:: run_fox_and_geese_game
         :collapse:


   .. py:method:: show_move(move: haive.games.fox_and_geese.models.FoxAndGeeseMove, state_before: haive.games.fox_and_geese.state.FoxAndGeeseState, state_after: haive.games.fox_and_geese.state.FoxAndGeeseState) -> None

      Display an animated move being made.

      Shows the move with highlighting of the relevant positions.

      :param move: The move being made
      :param state_before: State before the move
      :param state_after: State after the move

      :returns: None


      .. autolink-examples:: show_move
         :collapse:


   .. py:method:: show_thinking(player: str, message: str = 'Thinking...') -> None

      Display a thinking animation for the current player.

      Shows a spinner animation with player-colored text to indicate
      that the player is thinking about their move.

      :param player: Current player ("fox" or "geese")
      :type player: str
      :param message: Custom message to display. Defaults to "Thinking...".
      :type message: str, optional

      :returns: None


      .. autolink-examples:: show_thinking
         :collapse:


   .. py:attribute:: board_symbols


   .. py:attribute:: colors


   .. py:attribute:: console


.. py:data:: logger

