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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/clue/state/ClueState

.. autoapisummary::

   games.clue.state.ClueState


