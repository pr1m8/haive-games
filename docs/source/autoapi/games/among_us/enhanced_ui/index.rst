games.among_us.enhanced_ui
==========================

.. py:module:: games.among_us.enhanced_ui

Enhanced Rich UI module for Among Us game visualization.

This module provides an enhanced rich console UI for visualizing the Among Us game, with
better styling, animated visualizations, and improved game information display.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Enhanced Rich UI module for Among Us game visualization.

   This module provides an enhanced rich console UI for visualizing the Among Us game, with
   better styling, animated visualizations, and improved game information display.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.among_us.enhanced_ui.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.among_us.enhanced_ui.EnhancedAmongUsUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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


            .. py:method:: _format_move_description(move: dict[str, Any], player_id: str, state: haive.games.among_us.state.AmongUsState) -> str

               Format a move description for display.

               :param move: Move details
               :param player_id: ID of the player making the move
               :param state: Current game state

               :returns: Formatted move description



            .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

               Check if a dict contains the required fields for AmongUsState.

               :param data: Dictionary to check

               :returns: True if the dict appears to be a valid game state



            .. py:method:: animate_move(move: dict[str, Any], state_before: haive.games.among_us.state.AmongUsState, state_after: haive.games.among_us.state.AmongUsState, player_id: str, delay: float = 0.5) -> None

               Animate a move being made.

               :param move: Move details
               :param state_before: State before the move
               :param state_after: State after the move
               :param player_id: ID of the player making the move
               :param delay: Delay for animation

               :returns: None



            .. py:method:: create_game_info_panel(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

               Create a panel with general game information.

               :param state: Current game state

               :returns: Rich panel containing game information



            .. py:method:: create_game_over_panel(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

               Create a panel for the game over screen.

               :param state: Current game state

               :returns: Rich panel for game over



            .. py:method:: create_layout(state: haive.games.among_us.state.AmongUsState, player_id: str | None = None, legal_moves: list[dict[str, Any]] | None = None) -> rich.layout.Layout

               Create the complete layout for the game UI.

               :param state: Current game state
               :param player_id: Optional ID of the current player's perspective
               :param legal_moves: Optional list of legal moves for the player

               :returns: Complete rich layout



            .. py:method:: create_legal_moves_panel(legal_moves: list[dict[str, Any]]) -> rich.panel.Panel

               Create a panel showing legal moves.

               :param legal_moves: List of legal moves for the player

               :returns: Rich panel showing legal moves



            .. py:method:: create_map_visualization(state: haive.games.among_us.state.AmongUsState, player_id: str | None = None) -> rich.panel.Panel

               Create a visual representation of the map with rooms, vents, and players.

               :param state: Current game state
               :param player_id: Optional ID of the player whose perspective to show

               :returns: Rich panel containing the map visualization



            .. py:method:: create_meeting_panel(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

               Create a panel for the meeting phase.

               :param state: Current game state

               :returns: Rich panel for the meeting



            .. py:method:: create_other_players_panel(state: haive.games.among_us.state.AmongUsState, player_id: str) -> rich.panel.Panel

               Create a panel showing information about other players.

               :param state: Current game state
               :param player_id: ID of the current player

               :returns: Rich panel containing other player information



            .. py:method:: create_player_info_panel(state: haive.games.among_us.state.AmongUsState, player_id: str) -> rich.panel.Panel

               Create a panel with detailed information about the player.

               :param state: Current game state
               :param player_id: ID of the player to show info for

               :returns: Rich panel containing player information



            .. py:method:: create_sabotage_panel(state: haive.games.among_us.state.AmongUsState, player_id: str | None = None) -> rich.panel.Panel | None

               Create a panel showing active sabotage information if any.

               :param state: Current game state
               :param player_id: Optional ID of the current player

               :returns: Rich panel for sabotage or None if no active sabotage



            .. py:method:: display_final_results(final_state: Any) -> None

               Display enhanced final game results.

               :param final_state: Final game state

               :returns: None



            .. py:method:: display_state(state_data: Any, player_id: str | None = None, legal_moves: list[dict[str, Any]] | None = None) -> bool

               Display the game state using enhanced rich UI.

               :param state_data: State data in various formats
               :param player_id: Optional ID of the player whose perspective to show
               :param legal_moves: Optional list of legal moves for the player

               :returns: True if display was successful, False otherwise



            .. py:method:: display_welcome() -> None

               Display welcome message and game introduction.

               :returns: None



            .. py:method:: extract_game_state(state_data: Any) -> haive.games.among_us.state.AmongUsState | None

               Extract AmongUsState from various input formats.

               :param state_data: State data in various formats

               :returns: AmongUsState instance or None if extraction fails



            .. py:method:: run_among_us_game(agent, delay: float = 1.0) -> haive.games.among_us.state.AmongUsState

               Run a complete Among Us game with UI visualization.

               :param agent: The game agent that manages the game logic
               :param delay: Delay between game states

               :returns: Final game state



            .. py:method:: show_thinking(player_id: str, message: str = 'Thinking...') -> None

               Display a thinking animation for the player.

               :param player_id: ID of the player who is thinking
               :param message: Message to display during thinking

               :returns: None



            .. py:attribute:: colors


            .. py:attribute:: console


            .. py:attribute:: map_symbols


            .. py:attribute:: symbols



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.enhanced_ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

