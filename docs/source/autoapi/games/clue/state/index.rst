games.clue.state
================

.. py:module:: games.clue.state

.. autoapi-nested-parse::

   Comprehensive state management for the Clue (Cluedo) mystery game.

   This module defines the state model for the Clue game, providing complete
   tracking of game progression, player cards, hypotheses, and game status.
   The state system supports both two-player and multi-player configurations
   with full game rule enforcement.

   The state model handles:
   - Secret solution management (murderer, weapon, room)
   - Player card distribution and tracking
   - Guess and response history
   - AI hypothesis generation and tracking
   - Turn management and game flow
   - Win condition evaluation
   - Game status and completion handling

   Key Features:
       - Immutable solution hidden from players
       - Dynamic card dealing and distribution
       - Comprehensive guess and response logging
       - AI hypothesis tracking for strategic play
       - Turn-based progression with validation
       - Multiple win conditions and game ending scenarios

   .. rubric:: Examples

   Initializing a new game::

       from haive.games.clue.state import ClueState

       # Create a new game with random solution
       state = ClueState.initialize()

       # Create a game with specific solution
       from haive.games.clue.models import ClueSolution, ValidSuspect, ValidWeapon, ValidRoom

       solution = ClueSolution(
           suspect=ValidSuspect.COLONEL_MUSTARD,
           weapon=ValidWeapon.KNIFE,
           room=ValidRoom.KITCHEN
       )
       state = ClueState.initialize(solution=solution)

   Checking game status::

       if state.is_game_over:
           print(f"Game ended! Winner: {state.winner}")
       else:
           print(f"Turn {state.current_turn_number}: {state.current_player}'s turn")

   Accessing player information::

       player1_cards = state.player1_cards
       player2_cards = state.player2_cards
       print(f"Player 1 has {len(player1_cards)} cards")
       print(f"Player 2 has {len(player2_cards)} cards")

   The state model integrates seamlessly with the game agent system and provides
   all necessary information for AI decision-making and strategic gameplay.


   .. autolink-examples:: games.clue.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.clue.state.ClueState


Module Contents
---------------

.. py:class:: ClueState

   Bases: :py:obj:`haive.games.framework.base.state.GameState`


   Comprehensive state model for Clue game sessions.

   This class manages all aspects of a Clue game state, including the secret
   solution, player cards, game progression, and AI reasoning. It provides
   methods for game initialization, turn management, and win condition
   evaluation.

   The state model supports strategic gameplay by tracking player hypotheses,
   guess history, and response patterns. This enables sophisticated AI
   decision-making and deduction logic.

   .. attribute:: solution

      The secret solution that players are trying to discover.
      Contains the murderer (suspect), weapon, and room.

   .. attribute:: guesses

      Complete history of all guesses made during the game.
      Each guess contains a suspect, weapon, and room combination.

   .. attribute:: responses

      Responses to each guess, indicating whether cards were shown
      and which player responded.

   .. attribute:: player1_cards

      List of cards held by player 1.
      Used for responding to guesses and making deductions.

   .. attribute:: player2_cards

      List of cards held by player 2.
      Used for responding to guesses and making deductions.

   .. attribute:: current_player

      The player whose turn it is to make a guess.
      Alternates between "player1" and "player2".

   .. attribute:: max_turns

      Maximum number of turns before the game ends in a draw.
      Prevents infinite games and ensures completion.

   .. attribute:: game_status

      Current status of the game (ongoing, player1_win, player2_win).
      Used to determine if the game has ended and who won.

   .. attribute:: winner

      The winning player, if any.
      Set when a player makes a correct accusation.

   .. attribute:: player1_hypotheses

      List of AI-generated hypotheses for player 1.
      Tracks the AI's reasoning and deduction process.

   .. attribute:: player2_hypotheses

      List of AI-generated hypotheses for player 2.
      Tracks the AI's reasoning and deduction process.

   .. rubric:: Examples

   Creating a new game state::

       state = ClueState.initialize()
       print(f"Solution: {state.solution}")
       print(f"Player 1 cards: {state.player1_cards}")
       print(f"Player 2 cards: {state.player2_cards}")

   Checking game progress::

       if state.is_game_over:
           print(f"Game ended! Winner: {state.winner}")
       else:
           print(f"Turn {state.current_turn_number}: {state.current_player}'s turn")

   Accessing game history::

       for i, (guess, response) in enumerate(zip(state.guesses, state.responses)):
           print(f"Turn {i+1}: {guess.suspect}, {guess.weapon}, {guess.room}")
           print(f"Response: {response.responding_player}")

   .. note::

      The solution is hidden from players during normal gameplay but is
      accessible to the game engine for validation and scoring purposes.


   .. autolink-examples:: ClueState
      :collapse:

   .. py:method:: initialize(**kwargs) -> ClueState
      :classmethod:


      Initialize a new Clue game state.

      Creates a new game state with a random or specified solution, deals cards
      to players, and sets up the initial game conditions. The solution is
      kept secret and the remaining cards are distributed between players.

      :param \*\*kwargs: Keyword arguments for customization:
                         solution (ClueSolution, optional): Predefined solution. If not provided,
                             a random solution will be generated.
                         first_player (str, optional): Which player goes first ("player1" or "player2").
                             Defaults to "player1".
                         max_turns (int, optional): Maximum number of turns before game ends.
                             Defaults to 20.

      :returns: A new initialized game state ready for play.
      :rtype: ClueState

      .. rubric:: Examples

      Creating a random game::

          state = ClueState.initialize()
          print(f"Game initialized with random solution")
          print(f"Player 1 has {len(state.player1_cards)} cards")
          print(f"Player 2 has {len(state.player2_cards)} cards")

      Creating a game with specific solution::

          from haive.games.clue.models import ClueSolution, ValidSuspect, ValidWeapon, ValidRoom

          solution = ClueSolution(
              suspect=ValidSuspect.COLONEL_MUSTARD,
              weapon=ValidWeapon.KNIFE,
              room=ValidRoom.KITCHEN
          )
          state = ClueState.initialize(
              solution=solution,
              first_player="player2",
              max_turns=15
          )

      Checking initialization results::

          state = ClueState.initialize()

          # Verify solution is set
          assert state.solution.suspect in ValidSuspect
          assert state.solution.weapon in ValidWeapon
          assert state.solution.room in ValidRoom

          # Verify cards are distributed
          total_cards = len(state.player1_cards) + len(state.player2_cards)
          assert total_cards == 18  # 21 total cards - 3 solution cards

          # Verify initial state
          assert state.current_player == "player1"  # Default first player
          assert state.game_status == "ongoing"
          assert len(state.guesses) == 0
          assert len(state.responses) == 0

      .. note::

         The solution cards are automatically removed from the deck before
         dealing to players, ensuring they remain hidden. Card distribution
         is as even as possible, with any extra cards going to player1.


      .. autolink-examples:: initialize
         :collapse:


   .. py:property:: board_string
      :type: str


      Get a string representation of the game board.

      Creates a formatted string showing the history of guesses and responses,
      useful for display purposes and debugging.

      :returns: Formatted string representation of the game history.
      :rtype: str

      .. rubric:: Examples

      Displaying game history::

          state = ClueState.initialize()
          # After some guesses...
          print(state.board_string)
          # Output:
          # Turn 1: Colonel Mustard, Knife, Kitchen | Response: Alice
          # Turn 2: Professor Plum, Candlestick, Library | Response: No card shown

      .. autolink-examples:: board_string
         :collapse:


   .. py:attribute:: current_player
      :type:  Literal['player1', 'player2']
      :value: None



   .. py:property:: current_turn_number
      :type: int


      Get the current turn number.

      The turn number is calculated based on the number of guesses made so far,
      starting from 1 for the first turn.

      :returns: The current turn number (1-based).
      :rtype: int

      .. rubric:: Examples

      Checking turn number::

          state = ClueState.initialize()
          print(f"Turn {state.current_turn_number}")  # "Turn 1"

          # After first guess
          state.guesses.append(guess)
          print(f"Turn {state.current_turn_number}")  # "Turn 2"

      .. autolink-examples:: current_turn_number
         :collapse:


   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'player1_win', 'player2_win']
      :value: None



   .. py:attribute:: guesses
      :type:  list[haive.games.clue.models.ClueGuess]
      :value: None



   .. py:property:: is_game_over
      :type: bool


      Check if the game is over.

      The game is over when the status is no longer "ongoing", which happens
      when a player wins or the maximum turns are reached.

      :returns: True if the game has ended, False otherwise.
      :rtype: bool

      .. rubric:: Examples

      Checking game status::

          state = ClueState.initialize()
          if state.is_game_over:
              print(f"Game ended! Winner: {state.winner}")
          else:
              print("Game is still in progress")

      .. autolink-examples:: is_game_over
         :collapse:


   .. py:attribute:: max_turns
      :type:  int
      :value: None



   .. py:attribute:: player1_cards
      :type:  list[str]
      :value: None



   .. py:attribute:: player1_hypotheses
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: player2_cards
      :type:  list[str]
      :value: None



   .. py:attribute:: player2_hypotheses
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: responses
      :type:  list[haive.games.clue.models.ClueResponse]
      :value: None



   .. py:attribute:: solution
      :type:  haive.games.clue.models.ClueSolution
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



