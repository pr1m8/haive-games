games.connect4.ui
=================

.. py:module:: games.connect4.ui

Connect4 rich UI visualization module.

This module provides a visually appealing terminal UI for Connect4 games,
with styled components, animations, and comprehensive game information.

It uses the Rich library to create a console-based UI with:
    - Colorful board display with piece symbols
    - Move history panel
    - Game status and information
    - Position analysis display
    - Move and thinking animations

.. rubric:: Example

>>> from haive.games.connect4.ui import Connect4UI
>>> from haive.games.connect4.state import Connect4State
>>>
>>> ui = Connect4UI()
>>> state = Connect4State.initialize()
>>> ui.display_state(state)  # Display the initial board
>>>
>>> # Show thinking animation for player move
>>> ui.show_thinking("red")
>>>
>>> # Display a move
>>> from haive.games.connect4.models import Connect4Move
>>> move = Connect4Move(column=3)
>>> ui.show_move(move, "red")



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Connect4 rich UI visualization module.

   This module provides a visually appealing terminal UI for Connect4 games,
   with styled components, animations, and comprehensive game information.

   It uses the Rich library to create a console-based UI with:
       - Colorful board display with piece symbols
       - Move history panel
       - Game status and information
       - Position analysis display
       - Move and thinking animations

   .. rubric:: Example

   >>> from haive.games.connect4.ui import Connect4UI
   >>> from haive.games.connect4.state import Connect4State
   >>>
   >>> ui = Connect4UI()
   >>> state = Connect4State.initialize()
   >>> ui.display_state(state)  # Display the initial board
   >>>
   >>> # Show thinking animation for player move
   >>> ui.show_thinking("red")
   >>>
   >>> # Display a move
   >>> from haive.games.connect4.models import Connect4Move
   >>> move = Connect4Move(column=3)
   >>> ui.show_move(move, "red")



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.connect4.ui.Connect4UI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Connect4UI

            Rich UI for beautiful Connect4 game visualization.

            This class provides a visually appealing terminal UI for Connect4 games,
            with styled components, animations, and comprehensive game information.

            Features:
                - Colorful board display with piece symbols
                - Move history panel
                - Game status and information
                - Position analysis display
                - Move and thinking animations

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

            >>> ui = Connect4UI()
            >>> state = Connect4State.initialize()
            >>> ui.display_state(state)  # Display the initial board

            Initialize the Connect4 UI with default settings.


            .. py:method:: _render_analysis(state: haive.games.connect4.state.Connect4State) -> rich.panel.Panel

               Render analysis information panel.

               :param state: Current game state

               :returns: Analysis information panel
               :rtype: Panel



            .. py:method:: _render_board(state: haive.games.connect4.state.Connect4State) -> rich.panel.Panel

               Render the Connect4 board with pieces.

               :param state: Current game state

               :returns: Styled board panel
               :rtype: Panel



            .. py:method:: _render_game_info(state: haive.games.connect4.state.Connect4State) -> rich.panel.Panel

               Render game information panel.

               :param state: Current game state

               :returns: Game information panel
               :rtype: Panel



            .. py:method:: _render_header(state: haive.games.connect4.state.Connect4State) -> rich.panel.Panel

               Render the game header with title and status.

               :param state: Current game state

               :returns: Styled header panel
               :rtype: Panel



            .. py:method:: _render_move_history(state: haive.games.connect4.state.Connect4State) -> rich.panel.Panel

               Render move history panel.

               :param state: Current game state

               :returns: Move history panel
               :rtype: Panel



            .. py:method:: _setup_layout()

               Set up the layout structure for the UI.



            .. py:method:: display_state(state: haive.games.connect4.state.Connect4State | dict) -> None

               Display the current game state with rich formatting.

               Renders the complete game state including board, game info,
               analysis, and move history in a formatted layout.

               :param state: Current game state (Connect4State or dict)
               :type state: Union[Connect4State, dict]

               :returns: None

               .. rubric:: Example

               >>> ui = Connect4UI()
               >>> state = Connect4State.initialize()
               >>> ui.display_state(state)



            .. py:method:: show_game_over(winner: str | None = None) -> None

               Display game over message with result.

               Shows a game over panel with the winner highlighted in their color,
               or indicating a draw if there's no winner.

               :param winner: Winning player or None for a draw. Defaults to None.
               :type winner: Optional[str], optional

               :returns: None

               .. rubric:: Example

               >>> ui = Connect4UI()
               >>> ui.show_game_over("red")  # Red player wins
               >>> ui.show_game_over(None)   # Draw



            .. py:method:: show_move(move: haive.games.connect4.models.Connect4Move, player: str) -> None

               Display a move animation.

               Shows a formatted message indicating which player made which move,
               with color-coded player name and piece symbol.

               :param move: The move being made
               :type move: Connect4Move
               :param player: Player making the move ("red" or "yellow")
               :type player: str

               :returns: None

               .. rubric:: Example

               >>> ui = Connect4UI()
               >>> move = Connect4Move(column=3)
               >>> ui.show_move(move, "red")



            .. py:method:: show_thinking(player: str, message: str = 'Thinking...') -> None

               Display a thinking animation for the current player.

               Shows a spinner animation with player-colored text to indicate
               that the player is thinking about their move.

               :param player: Current player ("red" or "yellow")
               :type player: str
               :param message: Custom message to display. Defaults to "Thinking...".
               :type message: str, optional

               :returns: None

               .. rubric:: Example

               >>> ui = Connect4UI()
               >>> ui.show_thinking("red", "Analyzing position...")



            .. py:attribute:: colors


            .. py:attribute:: console


            .. py:attribute:: layout


            .. py:attribute:: move_count
               :value: 0



            .. py:attribute:: move_history
               :type:  list[str]
               :value: []






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.connect4.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

