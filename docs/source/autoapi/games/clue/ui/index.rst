games.clue.ui
=============

.. py:module:: games.clue.ui

Clue rich UI visualization module.

This module provides a visually appealing terminal UI for Clue games,
with styled components, animations, and comprehensive game information.

It uses the Rich library to create a console-based UI with:
    - Game board visualization with players, suspects, weapons, and rooms
    - Guess history with detailed responses
    - Player cards and deduction notes
    - Game status and information
    - Thinking animations and guess visualization

.. rubric:: Example

>>> from haive.games.clue.ui import ClueUI
>>> from haive.games.clue.state import ClueState
>>>
>>> ui = ClueUI()
>>> state = ClueState.initialize()
>>> ui.display_state(state)  # Display the initial game state
>>>
>>> # Show thinking animation for player
>>> ui.show_thinking("player1")
>>>
>>> # Display a guess
>>> from haive.games.clue.models import ClueGuess, ValidSuspect, ValidWeapon, ValidRoom
>>> guess = ClueGuess(
>>>     suspect=ValidSuspect.COLONEL_MUSTARD,
>>>     weapon=ValidWeapon.KNIFE,
>>>     room=ValidRoom.KITCHEN
>>> )
>>> ui.show_guess(guess, "player1")



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Clue rich UI visualization module.

   This module provides a visually appealing terminal UI for Clue games,
   with styled components, animations, and comprehensive game information.

   It uses the Rich library to create a console-based UI with:
       - Game board visualization with players, suspects, weapons, and rooms
       - Guess history with detailed responses
       - Player cards and deduction notes
       - Game status and information
       - Thinking animations and guess visualization

   .. rubric:: Example

   >>> from haive.games.clue.ui import ClueUI
   >>> from haive.games.clue.state import ClueState
   >>>
   >>> ui = ClueUI()
   >>> state = ClueState.initialize()
   >>> ui.display_state(state)  # Display the initial game state
   >>>
   >>> # Show thinking animation for player
   >>> ui.show_thinking("player1")
   >>>
   >>> # Display a guess
   >>> from haive.games.clue.models import ClueGuess, ValidSuspect, ValidWeapon, ValidRoom
   >>> guess = ClueGuess(
   >>>     suspect=ValidSuspect.COLONEL_MUSTARD,
   >>>     weapon=ValidWeapon.KNIFE,
   >>>     room=ValidRoom.KITCHEN
   >>> )
   >>> ui.show_guess(guess, "player1")



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.clue.ui.ClueUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueUI

            Rich UI for beautiful Clue game visualization.

            This class provides a visually appealing terminal UI for Clue games,
            with styled components, animations, and comprehensive game information.

            Features:
                - Game board visualization with suspects, weapons, and rooms
                - Guess history with detailed responses
                - Player cards and deduction notes
                - Game status and information
                - Thinking animations and guess visualization

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

            >>> ui = ClueUI()
            >>> state = ClueState.initialize()
            >>> ui.display_state(state)  # Display the initial game state

            Initialize the Clue UI with default settings.


            .. py:method:: _render_deductions(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render deductions and analysis panel.

               :param state: Current game state

               :returns: Deductions panel
               :rtype: Panel



            .. py:method:: _render_game_info(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render game information panel.

               :param state: Current game state

               :returns: Game information panel
               :rtype: Panel



            .. py:method:: _render_guess_history(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render the guess history panel.

               :param state: Current game state

               :returns: Guess history panel
               :rtype: Panel



            .. py:method:: _render_header(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render the game header with title and status.

               :param state: Current game state

               :returns: Styled header panel
               :rtype: Panel



            .. py:method:: _render_player_cards(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render player cards panel.

               :param state: Current game state

               :returns: Player cards panel
               :rtype: Panel



            .. py:method:: _render_rooms(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render the rooms panel.

               :param state: Current game state

               :returns: Rooms panel
               :rtype: Panel



            .. py:method:: _render_suspects(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render the suspects panel.

               :param state: Current game state

               :returns: Suspects panel
               :rtype: Panel



            .. py:method:: _render_weapons(state: haive.games.clue.state.ClueState) -> rich.panel.Panel

               Render the weapons panel.

               :param state: Current game state

               :returns: Weapons panel
               :rtype: Panel



            .. py:method:: _setup_layout()

               Set up the layout structure for the UI.



            .. py:method:: display_state(state: haive.games.clue.state.ClueState | dict[str, Any]) -> None

               Display the current game state with rich formatting.

               Renders the complete game state including suspects, weapons, rooms,
               guess history, player cards, and game information in a formatted layout.

               :param state: Current game state
               :type state: Union[ClueState, Dict[str, Any]]

               :returns: None

               .. rubric:: Example

               >>> ui = ClueUI()
               >>> state = ClueState.initialize()
               >>> ui.display_state(state)



            .. py:method:: show_game_over(state: haive.games.clue.state.ClueState) -> None

               Display game over message with result.

               Shows a game over panel with the winner highlighted in their color,
               and reveals the solution.

               :param state: Final game state
               :type state: ClueState

               :returns: None

               .. rubric:: Example

               >>> ui = ClueUI()
               >>> state = ClueState.initialize()
               >>> state.game_status = "player1_win"
               >>> state.winner = "player1"
               >>> ui.show_game_over(state)



            .. py:method:: show_guess(guess: haive.games.clue.models.ClueGuess, player: str) -> None

               Display a guess being made.

               Shows a formatted message indicating which player made a guess,
               including the suspect, weapon, and room.

               :param guess: The guess being made
               :type guess: ClueGuess
               :param player: Player making the guess ("player1" or "player2")
               :type player: str

               :returns: None

               .. rubric:: Example

               >>> ui = ClueUI()
               >>> guess = ClueGuess(
               ...     suspect=ValidSuspect.COLONEL_MUSTARD,
               ...     weapon=ValidWeapon.KNIFE,
               ...     room=ValidRoom.KITCHEN
               ... )
               >>> ui.show_guess(guess, "player1")



            .. py:method:: show_response(response: haive.games.clue.models.ClueResponse, player: str) -> None

               Display a response to a guess.

               Shows a formatted message indicating the response to a guess,
               including which player responded and what card was shown.

               :param response: The response to the guess
               :type response: ClueResponse
               :param player: Player who made the guess ("player1" or "player2")
               :type player: str

               :returns: None

               .. rubric:: Example

               >>> ui = ClueUI()
               >>> response = ClueResponse(
               ...     is_correct=False,
               ...     responding_player="player2",
               ...     refuting_card=ClueCard(name="Knife", card_type=CardType.WEAPON)
               ... )
               >>> ui.show_response(response, "player1")



            .. py:method:: show_thinking(player: str, message: str = 'Thinking...') -> None

               Display a thinking animation for the current player.

               Shows a spinner animation with player-colored text to indicate
               that the player is thinking about their guess.

               :param player: Current player ("player1" or "player2")
               :type player: str
               :param message: Custom message to display. Defaults to "Thinking...".
               :type message: str, optional

               :returns: None

               .. rubric:: Example

               >>> ui = ClueUI()
               >>> ui.show_thinking("player1", "Analyzing clues...")



            .. py:attribute:: colors


            .. py:attribute:: console


            .. py:attribute:: layout





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

