games.checkers.ui
=================

.. py:module:: games.checkers.ui

Checkers game UI module.

This module provides a rich text-based UI for the checkers game, including:
    - Beautiful board visualization with colors
    - Game information display
    - Move history tracking
    - Captured pieces visualization
    - Position analysis display
    - Game status and winner announcements
    - Move and thinking animations

The UI uses the rich library to create a visually appealing terminal interface
that makes the game more engaging and easier to follow.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Checkers game UI module.

   This module provides a rich text-based UI for the checkers game, including:
       - Beautiful board visualization with colors
       - Game information display
       - Move history tracking
       - Captured pieces visualization
       - Position analysis display
       - Game status and winner announcements
       - Move and thinking animations

   The UI uses the rich library to create a visually appealing terminal interface
   that makes the game more engaging and easier to follow.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.checkers.ui.CheckersUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CheckersUI

            Rich UI for beautiful checkers game visualization.

            This class provides a visually appealing terminal UI for checkers games,
            with styled components, animations, and comprehensive game information.

            Features:
                - Colorful board display with piece symbols
                - Move history panel
                - Captured pieces tracking
                - Game status and information
                - Position analysis display
                - Move and thinking animations
                - Game over screen

            .. attribute:: console

               Rich console for output

               :type: Console

            .. attribute:: layout

               Layout manager for UI components

               :type: Layout

            .. attribute:: colors

               Color schemes for different UI elements

               :type: dict

            .. attribute:: pieces

               Unicode symbols for different piece types

               :type: dict

            .. attribute:: game_log

               Log of game events

               :type: List[str]

            .. attribute:: move_count

               Counter for moves

               :type: int

            .. attribute:: start_time

               Game start time

               :type: datetime

            .. rubric:: Examples

            >>> ui = CheckersUI()
            >>> state = CheckersState.initialize()
            >>> ui.display_state(state)  # Display the initial board
            >>>
            >>> # Show thinking animation during move generation
            >>> ui.show_thinking("red")
            >>>
            >>> # Display a move
            >>> move = CheckersMove(from_position="a3", to_position="b4", player="red")
            >>> ui.show_move(move)

            Initialize the checkers UI.

            Sets up the console, layout, color schemes, piece symbols, and tracking
            variables for the UI.



            .. py:method:: _create_analysis_panel(state: haive.games.checkers.state.CheckersState) -> rich.panel.Panel

               Create analysis panel showing latest analysis.

               Creates a panel with the latest position analysis for the current player,
               including material advantage, center control, and suggested moves.

               :param state: Current game state
               :type state: CheckersState

               :returns: A styled panel with position analysis
               :rtype: Panel



            .. py:method:: _create_board_display(state: haive.games.checkers.state.CheckersState, last_move: haive.games.checkers.models.CheckersMove | None = None) -> rich.panel.Panel

               Create a beautiful board visualization.

               Generates a rich Panel containing the styled checkers board with
               pieces, coordinates, and optional highlighting for the last move.

               :param state: Current game state
               :type state: CheckersState
               :param last_move: Last move to highlight.
                                 Defaults to None.
               :type last_move: Optional[CheckersMove], optional

               :returns: A styled panel containing the board visualization
               :rtype: Panel



            .. py:method:: _create_captured_pieces(state: haive.games.checkers.state.CheckersState) -> rich.panel.Panel

               Create captured pieces display.

               Creates a panel showing pieces captured by each player.

               :param state: Current game state
               :type state: CheckersState

               :returns: A styled panel showing captured pieces
               :rtype: Panel



            .. py:method:: _create_footer(message: str = '') -> rich.panel.Panel

               Create footer with status message.

               Creates a footer panel with a status message or default controls.

               :param message: Custom message to display. Defaults to "".
               :type message: str, optional

               :returns: A styled footer panel
               :rtype: Panel



            .. py:method:: _create_game_info(state: haive.games.checkers.state.CheckersState) -> rich.panel.Panel

               Create game information panel.

               Creates a panel with game status, move count, winner (if any),
               and piece counts.

               :param state: Current game state
               :type state: CheckersState

               :returns: A styled panel with game information
               :rtype: Panel



            .. py:method:: _create_header(state: haive.games.checkers.state.CheckersState) -> rich.panel.Panel

               Create the header panel.

               Creates a styled header with the game title, current turn, and elapsed time.

               :param state: Current game state
               :type state: CheckersState

               :returns: A styled panel for the header
               :rtype: Panel



            .. py:method:: _create_move_history(state: haive.games.checkers.state.CheckersState) -> rich.panel.Panel

               Create move history panel.

               Creates a panel showing the recent moves made in the game.

               :param state: Current game state
               :type state: CheckersState

               :returns: A styled panel with move history
               :rtype: Panel



            .. py:method:: _get_piece_display(piece_value: int, last_move_player: str = '') -> str

               Get styled piece display.

               Converts a numeric piece value to a styled Unicode symbol.

               :param piece_value: Piece value (0-4)
               :type piece_value: int
               :param last_move_player: Player color for last move highlighting.
                                        Defaults to "".
               :type last_move_player: str, optional

               :returns: Styled Unicode representation of the piece
               :rtype: str

               .. note::

                  Piece values:
                  - 0: Empty square
                  - 1: Red piece
                  - 2: Red king
                  - 3: Black piece
                  - 4: Black king



            .. py:method:: _notation_to_index(notation: str) -> tuple[int, int]

               Convert algebraic notation to board indices.

               Converts algebraic notation (e.g., "a3") to zero-based row and column indices.

               :param notation: Position in algebraic notation (e.g., "a3")
               :type notation: str

               :returns: (row, col) indices
               :rtype: tuple[int, int]

               .. rubric:: Examples

               >>> ui = CheckersUI()
               >>> ui._notation_to_index("a8")
               (0, 0)
               >>> ui._notation_to_index("h1")
               (7, 7)



            .. py:method:: _setup_layout()

               Setup the main layout structure.

               Creates a layout with the following components:
               - Header: Game title and current turn
               - Main area: Board and sidebars
               - Footer: Status messages and controls
               - Left sidebar: Game info and captured pieces
               - Right sidebar: Analysis and move history




            .. py:method:: display_state(state: haive.games.checkers.state.CheckersState, message: str = '')

               Display the complete game state.

               Updates and displays all UI components with the current game state.

               :param state: Current game state
               :type state: CheckersState
               :param message: Custom message for the footer. Defaults to "".
               :type message: str, optional

               .. rubric:: Examples

               >>> ui = CheckersUI()
               >>> state = CheckersState.initialize()
               >>> ui.display_state(state)
               >>>
               >>> # Display with a custom message
               >>> ui.display_state(state, "Red is thinking...")



            .. py:method:: show_game_over(state: haive.games.checkers.state.CheckersState)

               Show game over screen.

               Displays a game over message with the winner when the game ends.

               :param state: Final game state
               :type state: CheckersState

               .. rubric:: Examples

               >>> ui = CheckersUI()
               >>> state = CheckersState(game_status="game_over", winner="red")
               >>> ui.show_game_over(state)  # Shows "RED WINS!" message



            .. py:method:: show_move(move: haive.games.checkers.models.CheckersMove)

               Show move animation.

               Displays a brief animation/message when a move is made.

               :param move: The move that was made
               :type move: CheckersMove

               .. rubric:: Examples

               >>> ui = CheckersUI()
               >>> move = CheckersMove(from_position="a3", to_position="b4", player="red")
               >>> ui.show_move(move)  # Shows move message



            .. py:method:: show_thinking(player: str)

               Show thinking animation.

               Displays a spinner animation while a player is thinking about a move.

               :param player: Player who is thinking ("red" or "black")
               :type player: str

               .. rubric:: Examples

               >>> ui = CheckersUI()
               >>> ui.show_thinking("red")  # Shows a spinner for red's thinking



            .. py:attribute:: colors


            .. py:attribute:: console


            .. py:attribute:: game_log
               :type:  list[str]
               :value: []



            .. py:attribute:: layout


            .. py:attribute:: move_count
               :value: 0



            .. py:attribute:: pieces


            .. py:attribute:: start_time





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.checkers.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

