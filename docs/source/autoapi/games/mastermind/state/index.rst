games.mastermind.state
======================

.. py:module:: games.mastermind.state

Module documentation for games.mastermind.state


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mastermind.state.MastermindState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MastermindState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.state.GameState`


            Comprehensive state management for Mastermind code-breaking games.

            This class manages the complete state of a Mastermind game, including the
            secret code, guess history, feedback tracking, and game progression. The
            state supports both traditional codemaker/codebreaker roles and maintains
            detailed analytics for AI decision-making.

            The state tracks the classic Mastermind game flow:
            - Secret code generation and protection
            - Sequential guess validation and feedback
            - Turn-based progression with role separation
            - Win condition evaluation and game termination
            - Strategic analysis for AI players

            .. attribute:: secret_code

               The hidden 4-color code that players attempt to guess.
               Kept secret from the codebreaker throughout the game.

            .. attribute:: guesses

               Complete history of all guesses made during the game.
               Maintains chronological order for analysis and replay.

            .. attribute:: feedback

               Corresponding feedback for each guess made.
               Provides positional and color correctness information.

            .. attribute:: turn

               Current player's turn (the active codebreaker).
               Alternates between players in multi-player scenarios.

            .. attribute:: codemaker

               Player who created the secret code.
               Remains constant throughout the game session.

            .. attribute:: max_turns

               Maximum number of guesses allowed before game ends.
               Typically 10-12 turns in standard Mastermind.

            .. attribute:: game_status

               Current state of the game progression.
               Tracks ongoing play, completion, and winner determination.

            .. attribute:: winner

               The victorious player, if any.
               Set when code is cracked or maximum turns reached.

            .. attribute:: player1_analysis

               AI analysis history for player 1.
               Tracks strategic reasoning and decision-making process.

            .. attribute:: player2_analysis

               AI analysis history for player 2.
               Tracks strategic reasoning and decision-making process.

            .. rubric:: Examples

            Game initialization::

                from haive.games.mastermind.state import MastermindState

                # Initialize with random secret code
                state = MastermindState.initialize(
                    codemaker="player1",
                    colors=None,  # Random generation
                    max_turns=10
                )

                # Initialize with specific code
                state = MastermindState.initialize(
                    codemaker="player1",
                    colors=["red", "blue", "green", "yellow"],
                    max_turns=12
                )

            Game progression tracking::

                # Check current game state
                if state.is_game_over:
                    print(f"Game ended! Winner: {state.winner}")
                else:
                    print(f"Turn {state.current_turn}: {state.turn} to guess")
                    print(f"Guesses remaining: {state.turns_remaining}")

            Strategic analysis::

                # Access game statistics
                stats = state.game_statistics
                print(f"Guess accuracy: {stats['accuracy']:.2%}")
                print(f"Information gain: {stats['information_efficiency']:.2f}")

            .. note::

               The secret code is accessible to the game engine for validation
               but should remain hidden from the codebreaker during gameplay.
               The state maintains immutability for core game data while
               supporting dynamic updates for game progression.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: initialize(codemaker: str = 'player1', colors: list[str] | None = None, code_length: int = 4, max_turns: int = 10, secret_code: list[str] | haive.games.mastermind.models.ColorCode | dict | None = None) -> MastermindState
               :classmethod:


               Abstract method that all subclasses must implement to initialize the game.
               state.

               :returns: A fully initialized game state object.
               :rtype: GameState

               .. rubric:: Example

               >>> return Connect4State.initialize(first_player="red")



            .. py:property:: board_string
               :type: str


               Get a string representation of the board.


            .. py:attribute:: codemaker
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:property:: current_turn_number
               :type: int


               Get the current turn number.


            .. py:attribute:: feedback
               :type:  Annotated[list[haive.games.mastermind.models.MastermindFeedback], operator.add]
               :value: None



            .. py:attribute:: game_status
               :type:  Literal['ongoing', 'player1_win', 'player2_win']
               :value: None



            .. py:attribute:: guesses
               :type:  Annotated[list[haive.games.mastermind.models.MastermindGuess], operator.add]
               :value: None



            .. py:property:: is_game_over
               :type: bool


               Check if the game is over.


            .. py:property:: last_feedback
               :type: haive.games.mastermind.models.MastermindFeedback | None


               Get the feedback for the last guess.


            .. py:property:: last_guess
               :type: haive.games.mastermind.models.MastermindGuess | None


               Get the last guess made.


            .. py:attribute:: max_turns
               :type:  int
               :value: None



            .. py:attribute:: player1_analysis
               :type:  Annotated[list[haive.games.mastermind.models.MastermindAnalysis], operator.add]
               :value: None



            .. py:attribute:: player2_analysis
               :type:  Annotated[list[haive.games.mastermind.models.MastermindAnalysis], operator.add]
               :value: None



            .. py:attribute:: secret_code
               :type:  list[str]
               :value: None



            .. py:attribute:: turn
               :type:  Literal['player1', 'player2']
               :value: None



            .. py:property:: turns_remaining
               :type: int


               Get the number of turns remaining.


            .. py:attribute:: winner
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mastermind.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

