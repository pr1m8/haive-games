games.among_us.enhanced_ui
==========================

.. py:module:: games.among_us.enhanced_ui

.. autoapi-nested-parse::

   Enhanced Rich UI module for Among Us game visualization.

   This module provides an enhanced rich console UI for visualizing the Among Us game, with
   better styling, animated visualizations, and improved game information display.


   .. autolink-examples:: games.among_us.enhanced_ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.among_us.enhanced_ui.logger


Classes
-------

.. autoapisummary::

   games.among_us.enhanced_ui.EnhancedAmongUsUI


Module Contents
---------------

.. py:class:: EnhancedAmongUsUI(console: rich.console.Console | None = None)

   Enhanced UI for Among Us game with rich terminal graphics.

   This class provides a visually appealing terminal UI for Among Us games,
   with styled components, animations, and comprehensive game information.

   Features:
       - Beautiful game map visualization with colored squares
       - Animated transitions between game states
       - Detailed player status display
       - Vent and sabotage system visualization
       - Meeting and voting interfaces
       - Game over screens with detailed statistics


   Initialize the UI.

   :param console: Optional Rich console instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedAmongUsUI
      :collapse:

   .. py:method:: _format_move_description(move: dict[str, Any], player_id: str, state: haive.games.among_us.state.AmongUsState) -> str

      Format a move description for display.

      :param move: Move details
      :param player_id: ID of the player making the move
      :param state: Current game state

      :returns: Formatted move description


      .. autolink-examples:: _format_move_description
         :collapse:


   .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

      Check if a dict contains the required fields for AmongUsState.

      :param data: Dictionary to check

      :returns: True if the dict appears to be a valid game state


      .. autolink-examples:: _is_valid_game_state_dict
         :collapse:


   .. py:method:: animate_move(move: dict[str, Any], state_before: haive.games.among_us.state.AmongUsState, state_after: haive.games.among_us.state.AmongUsState, player_id: str, delay: float = 0.5) -> None

      Animate a move being made.

      :param move: Move details
      :param state_before: State before the move
      :param state_after: State after the move
      :param player_id: ID of the player making the move
      :param delay: Delay for animation

      :returns: None


      .. autolink-examples:: animate_move
         :collapse:


   .. py:method:: create_game_info_panel(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

      Create a panel with general game information.

      :param state: Current game state

      :returns: Rich panel containing game information


      .. autolink-examples:: create_game_info_panel
         :collapse:


   .. py:method:: create_game_over_panel(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

      Create a panel for the game over screen.

      :param state: Current game state

      :returns: Rich panel for game over


      .. autolink-examples:: create_game_over_panel
         :collapse:


   .. py:method:: create_layout(state: haive.games.among_us.state.AmongUsState, player_id: str | None = None, legal_moves: list[dict[str, Any]] | None = None) -> rich.layout.Layout

      Create the complete layout for the game UI.

      :param state: Current game state
      :param player_id: Optional ID of the current player's perspective
      :param legal_moves: Optional list of legal moves for the player

      :returns: Complete rich layout


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: create_legal_moves_panel(legal_moves: list[dict[str, Any]]) -> rich.panel.Panel

      Create a panel showing legal moves.

      :param legal_moves: List of legal moves for the player

      :returns: Rich panel showing legal moves


      .. autolink-examples:: create_legal_moves_panel
         :collapse:


   .. py:method:: create_map_visualization(state: haive.games.among_us.state.AmongUsState, player_id: str | None = None) -> rich.panel.Panel

      Create a visual representation of the map with rooms, vents, and players.

      :param state: Current game state
      :param player_id: Optional ID of the player whose perspective to show

      :returns: Rich panel containing the map visualization


      .. autolink-examples:: create_map_visualization
         :collapse:


   .. py:method:: create_meeting_panel(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

      Create a panel for the meeting phase.

      :param state: Current game state

      :returns: Rich panel for the meeting


      .. autolink-examples:: create_meeting_panel
         :collapse:


   .. py:method:: create_other_players_panel(state: haive.games.among_us.state.AmongUsState, player_id: str) -> rich.panel.Panel

      Create a panel showing information about other players.

      :param state: Current game state
      :param player_id: ID of the current player

      :returns: Rich panel containing other player information


      .. autolink-examples:: create_other_players_panel
         :collapse:


   .. py:method:: create_player_info_panel(state: haive.games.among_us.state.AmongUsState, player_id: str) -> rich.panel.Panel

      Create a panel with detailed information about the player.

      :param state: Current game state
      :param player_id: ID of the player to show info for

      :returns: Rich panel containing player information


      .. autolink-examples:: create_player_info_panel
         :collapse:


   .. py:method:: create_sabotage_panel(state: haive.games.among_us.state.AmongUsState, player_id: str | None = None) -> rich.panel.Panel | None

      Create a panel showing active sabotage information if any.

      :param state: Current game state
      :param player_id: Optional ID of the current player

      :returns: Rich panel for sabotage or None if no active sabotage


      .. autolink-examples:: create_sabotage_panel
         :collapse:


   .. py:method:: display_final_results(final_state: Any) -> None

      Display enhanced final game results.

      :param final_state: Final game state

      :returns: None


      .. autolink-examples:: display_final_results
         :collapse:


   .. py:method:: display_state(state_data: Any, player_id: str | None = None, legal_moves: list[dict[str, Any]] | None = None) -> bool

      Display the game state using enhanced rich UI.

      :param state_data: State data in various formats
      :param player_id: Optional ID of the player whose perspective to show
      :param legal_moves: Optional list of legal moves for the player

      :returns: True if display was successful, False otherwise


      .. autolink-examples:: display_state
         :collapse:


   .. py:method:: display_welcome() -> None

      Display welcome message and game introduction.

      :returns: None


      .. autolink-examples:: display_welcome
         :collapse:


   .. py:method:: extract_game_state(state_data: Any) -> haive.games.among_us.state.AmongUsState | None

      Extract AmongUsState from various input formats.

      :param state_data: State data in various formats

      :returns: AmongUsState instance or None if extraction fails


      .. autolink-examples:: extract_game_state
         :collapse:


   .. py:method:: run_among_us_game(agent, delay: float = 1.0) -> haive.games.among_us.state.AmongUsState

      Run a complete Among Us game with UI visualization.

      :param agent: The game agent that manages the game logic
      :param delay: Delay between game states

      :returns: Final game state


      .. autolink-examples:: run_among_us_game
         :collapse:


   .. py:method:: show_thinking(player_id: str, message: str = 'Thinking...') -> None

      Display a thinking animation for the player.

      :param player_id: ID of the player who is thinking
      :param message: Message to display during thinking

      :returns: None


      .. autolink-examples:: show_thinking
         :collapse:


   .. py:attribute:: colors


   .. py:attribute:: console


   .. py:attribute:: map_symbols


   .. py:attribute:: symbols


.. py:data:: logger

