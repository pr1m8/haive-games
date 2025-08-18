games.clue.models
=================

.. py:module:: games.clue.models

Comprehensive data models and enumerations for the Clue (Cluedo) mystery game.
implementation.

This module defines the core data structures, enumerations, and models used
throughout the Clue game implementation. It includes the traditional game
elements (suspects, weapons, rooms) as well as game state representations,
player data structures, and action models following the classic board game rules.

The models follow the classic Clue game rules and include:
- Six suspects (Colonel Mustard, Professor Plum, etc.)
- Six weapons (Knife, Candlestick, Revolver, etc.)
- Nine rooms (Kitchen, Ballroom, Conservatory, etc.)
- Card types and game state tracking
- Player actions and game moves
- Deduction and hypothesis systems

Key Classes:
    ValidSuspect: Enumeration of all possible suspect characters
    ValidWeapon: Enumeration of all possible murder weapons
    ValidRoom: Enumeration of all possible locations
    CardType: Types of cards in the game (Suspect, Weapon, Room)
    ClueCard: Individual card representation with type information
    ClueSolution: The secret solution to the mystery
    ClueGuess: Player suggestions and accusations
    ClueResponse: Responses to player guesses
    ClueHypothesis: AI-generated deduction and reasoning
    GameStatus: Current state of the game progression

.. rubric:: Examples

Creating game elements::

    from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

    # Create a suggestion
    suspect = ValidSuspect.COLONEL_MUSTARD
    weapon = ValidWeapon.KNIFE
    room = ValidRoom.KITCHEN

    # Use in game logic
    suggestion = (suspect, weapon, room)

Working with cards::

    from haive.games.clue.models import ClueCard, CardType

    # Create cards from enums
    suspect_card = ClueCard.from_suspect(ValidSuspect.PROFESSOR_PLUM)
    weapon_card = ClueCard.from_weapon(ValidWeapon.CANDLESTICK)
    room_card = ClueCard.from_room(ValidRoom.BALLROOM)

    # Check card types
    assert suspect_card.card_type == CardType.SUSPECT
    assert weapon_card.card_type == CardType.WEAPON
    assert room_card.card_type == CardType.ROOM

Creating game solutions::

    from haive.games.clue.models import ClueSolution

    # Define the mystery solution
    solution = ClueSolution(
        suspect=ValidSuspect.MRS_PEACOCK,
        weapon=ValidWeapon.REVOLVER,
        room=ValidRoom.LIBRARY
    )

    # Convert to dictionary for serialization
    solution_dict = solution.to_dict()

AI hypothesis generation::

    from haive.games.clue.models import ClueHypothesis

    # Create AI deduction
    hypothesis = ClueHypothesis(
        prime_suspect=ValidSuspect.COLONEL_MUSTARD,
        prime_weapon=ValidWeapon.KNIFE,
        prime_room=ValidRoom.KITCHEN,
        confidence=0.75,
        excluded_suspects=[ValidSuspect.PROFESSOR_PLUM],
        reasoning="Colonel Mustard has not been seen by any player..."
    )

The models are designed to be immutable where possible and include comprehensive
validation to ensure game rules are properly enforced throughout the implementation.
All models support serialization to dictionaries for persistence and network
communication.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">10 classes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive data models and enumerations for the Clue (Cluedo) mystery game.
   implementation.

   This module defines the core data structures, enumerations, and models used
   throughout the Clue game implementation. It includes the traditional game
   elements (suspects, weapons, rooms) as well as game state representations,
   player data structures, and action models following the classic board game rules.

   The models follow the classic Clue game rules and include:
   - Six suspects (Colonel Mustard, Professor Plum, etc.)
   - Six weapons (Knife, Candlestick, Revolver, etc.)
   - Nine rooms (Kitchen, Ballroom, Conservatory, etc.)
   - Card types and game state tracking
   - Player actions and game moves
   - Deduction and hypothesis systems

   Key Classes:
       ValidSuspect: Enumeration of all possible suspect characters
       ValidWeapon: Enumeration of all possible murder weapons
       ValidRoom: Enumeration of all possible locations
       CardType: Types of cards in the game (Suspect, Weapon, Room)
       ClueCard: Individual card representation with type information
       ClueSolution: The secret solution to the mystery
       ClueGuess: Player suggestions and accusations
       ClueResponse: Responses to player guesses
       ClueHypothesis: AI-generated deduction and reasoning
       GameStatus: Current state of the game progression

   .. rubric:: Examples

   Creating game elements::

       from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

       # Create a suggestion
       suspect = ValidSuspect.COLONEL_MUSTARD
       weapon = ValidWeapon.KNIFE
       room = ValidRoom.KITCHEN

       # Use in game logic
       suggestion = (suspect, weapon, room)

   Working with cards::

       from haive.games.clue.models import ClueCard, CardType

       # Create cards from enums
       suspect_card = ClueCard.from_suspect(ValidSuspect.PROFESSOR_PLUM)
       weapon_card = ClueCard.from_weapon(ValidWeapon.CANDLESTICK)
       room_card = ClueCard.from_room(ValidRoom.BALLROOM)

       # Check card types
       assert suspect_card.card_type == CardType.SUSPECT
       assert weapon_card.card_type == CardType.WEAPON
       assert room_card.card_type == CardType.ROOM

   Creating game solutions::

       from haive.games.clue.models import ClueSolution

       # Define the mystery solution
       solution = ClueSolution(
           suspect=ValidSuspect.MRS_PEACOCK,
           weapon=ValidWeapon.REVOLVER,
           room=ValidRoom.LIBRARY
       )

       # Convert to dictionary for serialization
       solution_dict = solution.to_dict()

   AI hypothesis generation::

       from haive.games.clue.models import ClueHypothesis

       # Create AI deduction
       hypothesis = ClueHypothesis(
           prime_suspect=ValidSuspect.COLONEL_MUSTARD,
           prime_weapon=ValidWeapon.KNIFE,
           prime_room=ValidRoom.KITCHEN,
           confidence=0.75,
           excluded_suspects=[ValidSuspect.PROFESSOR_PLUM],
           reasoning="Colonel Mustard has not been seen by any player..."
       )

   The models are designed to be immutable where possible and include comprehensive
   validation to ensure game rules are properly enforced throughout the implementation.
   All models support serialization to dictionaries for persistence and network
   communication.



      
            
            

.. admonition:: Classes (10)
   :class: note

   .. autoapisummary::

      games.clue.models.CardType
      games.clue.models.ClueCard
      games.clue.models.ClueGuess
      games.clue.models.ClueHypothesis
      games.clue.models.ClueResponse
      games.clue.models.ClueSolution
      games.clue.models.GameStatus
      games.clue.models.ValidRoom
      games.clue.models.ValidSuspect
      games.clue.models.ValidWeapon

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardType(*args, **kwds)

            Bases: :py:obj:`enum.Enum`


            Types of cards in the game of Clue.

            Enumeration of the three types of cards that exist in the Clue game:
            suspect cards, weapon cards, and room cards. Each card type represents
            a different category of evidence that players use to solve the mystery.

            The game solution consists of exactly one card from each type, and the
            remaining cards are distributed to players as evidence.

            .. attribute:: SUSPECT

               Cards representing the six possible suspects

            .. attribute:: WEAPON

               Cards representing the six possible murder weapons

            .. attribute:: ROOM

               Cards representing the nine possible crime scene locations

            .. rubric:: Examples

            Using card types for validation::

                from haive.games.clue.models import CardType, ClueCard

                # Check card type
                card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                if card.card_type == CardType.SUSPECT:
                    print("This is a suspect card!")

                # Filter cards by type
                suspect_cards = [card for card in all_cards
                               if card.card_type == CardType.SUSPECT]


            .. py:attribute:: ROOM
               :value: 'Room'



            .. py:attribute:: SUSPECT
               :value: 'Suspect'



            .. py:attribute:: WEAPON
               :value: 'Weapon'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueCard

            A card in the game of Clue.

            Represents an individual card that can be held by players or be part of the
            game solution. Each card has a name and a type (suspect, weapon, or room).

            Cards are the primary evidence in the Clue game - players use them to make
            deductions about the solution and to respond to other players' suggestions.

            .. attribute:: name

               The name of the card (e.g., "Colonel Mustard", "Knife", "Kitchen")

            .. attribute:: card_type

               The type of card (suspect, weapon, or room)

            .. rubric:: Examples

            Creating cards from enums::

                from haive.games.clue.models import ClueCard, ValidSuspect

                # Create a suspect card
                suspect_card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                print(f"Card: {suspect_card.name} ({suspect_card.card_type.value})")

                # Create weapon and room cards
                weapon_card = ClueCard.from_weapon(ValidWeapon.KNIFE)
                room_card = ClueCard.from_room(ValidRoom.KITCHEN)

            Converting to dictionary::

                card_dict = suspect_card.to_dict()
                # Returns: {"name": "Colonel Mustard", "card_type": "Suspect"}

            Using in game logic::

                # Check if player has a specific card
                if card.name == "Colonel Mustard" and card.card_type == CardType.SUSPECT:
                    print("Player has Colonel Mustard suspect card!")


            .. py:method:: from_room(room: ValidRoom) -> ClueCard
               :staticmethod:


               Create a card from a room enum value.

               :param room: The room enum value to convert to a card.

               :returns: A new room card instance.
               :rtype: ClueCard

               .. rubric:: Examples

               Creating room cards::

                   card = ClueCard.from_room(ValidRoom.KITCHEN)
                   assert card.name == "Kitchen"
                   assert card.card_type == CardType.ROOM



            .. py:method:: from_suspect(suspect: ValidSuspect) -> ClueCard
               :staticmethod:


               Create a card from a suspect enum value.

               :param suspect: The suspect enum value to convert to a card.

               :returns: A new suspect card instance.
               :rtype: ClueCard

               .. rubric:: Examples

               Creating suspect cards::

                   card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                   assert card.name == "Colonel Mustard"
                   assert card.card_type == CardType.SUSPECT



            .. py:method:: from_weapon(weapon: ValidWeapon) -> ClueCard
               :staticmethod:


               Create a card from a weapon enum value.

               :param weapon: The weapon enum value to convert to a card.

               :returns: A new weapon card instance.
               :rtype: ClueCard

               .. rubric:: Examples

               Creating weapon cards::

                   card = ClueCard.from_weapon(ValidWeapon.KNIFE)
                   assert card.name == "Knife"
                   assert card.card_type == CardType.WEAPON



            .. py:method:: to_dict() -> dict[str, str]

               Convert the card to a dictionary.

               :returns: Dictionary representation with 'name' and 'card_type' keys.
               :rtype: dict[str, str]

               .. rubric:: Examples

               Converting to dictionary::

                   card = ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                   card_dict = card.to_dict()
                   # Returns: {"name": "Colonel Mustard", "card_type": "Suspect"}



            .. py:attribute:: card_type
               :type:  CardType


            .. py:attribute:: name
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueGuess

            A guess made during a game of Clue.

            Represents a player's suggestion or accusation in the game. A guess consists
            of one suspect, one weapon, and one room. Players use guesses to gather
            information and test hypotheses about the solution.

            There are two types of guesses:
            - Suggestion: Made to gather information from other players
            - Accusation: Made to win the game (if correct) or be eliminated (if wrong)

            .. attribute:: suspect

               The suspect being guessed

            .. attribute:: weapon

               The weapon being guessed

            .. attribute:: room

               The room being guessed

            .. rubric:: Examples

            Creating a guess::

                guess = ClueGuess(
                    suspect=ValidSuspect.PROFESSOR_PLUM,
                    weapon=ValidWeapon.CANDLESTICK,
                    room=ValidRoom.LIBRARY
                )

            Converting to dictionary::

                guess_dict = guess.to_dict()
                # Returns: {
                #     "suspect": "Professor Plum",
                #     "weapon": "Candlestick",
                #     "room": "Library"
                # }

            Comparing guesses::

                guess1 = ClueGuess(ValidSuspect.COLONEL_MUSTARD, ValidWeapon.KNIFE, ValidRoom.KITCHEN)
                guess2 = ClueGuess(ValidSuspect.COLONEL_MUSTARD, ValidWeapon.KNIFE, ValidRoom.KITCHEN)

                same_guess = (
                    guess1.suspect == guess2.suspect and
                    guess1.weapon == guess2.weapon and
                    guess1.room == guess2.room
                )


            .. py:method:: to_dict() -> dict[str, str]

               Convert the guess to a dictionary.

               :returns: Dictionary with 'suspect', 'weapon', and 'room' keys.
               :rtype: dict[str, str]

               .. rubric:: Examples

               Converting guess to dictionary::

                   guess = ClueGuess(
                       suspect=ValidSuspect.PROFESSOR_PLUM,
                       weapon=ValidWeapon.CANDLESTICK,
                       room=ValidRoom.LIBRARY
                   )
                   guess_dict = guess.to_dict()
                   # Returns: {
                   #     "suspect": "Professor Plum",
                   #     "weapon": "Candlestick",
                   #     "room": "Library"
                   # }



            .. py:attribute:: room
               :type:  ValidRoom


            .. py:attribute:: suspect
               :type:  ValidSuspect


            .. py:attribute:: weapon
               :type:  ValidWeapon



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueHypothesis

            A hypothesis about the solution generated by AI analysis.

            Represents an AI player's current best guess about the solution based on
            the information gathered during the game. This includes both positive
            hypotheses (what the AI thinks the solution is) and negative information
            (what has been ruled out).

            The hypothesis system allows AI players to reason about the game state
            and make informed decisions about suggestions and accusations.

            .. attribute:: prime_suspect

               Current best guess for the suspect

            .. attribute:: prime_weapon

               Current best guess for the weapon

            .. attribute:: prime_room

               Current best guess for the room

            .. attribute:: confidence

               Confidence level from 0.0 to 1.0

            .. attribute:: excluded_suspects

               Suspects that have been ruled out

            .. attribute:: excluded_weapons

               Weapons that have been ruled out

            .. attribute:: excluded_rooms

               Rooms that have been ruled out

            .. attribute:: reasoning

               Text explanation of the reasoning

            .. rubric:: Examples

            Creating a hypothesis::

                hypothesis = ClueHypothesis(
                    prime_suspect=ValidSuspect.COLONEL_MUSTARD,
                    prime_weapon=ValidWeapon.KNIFE,
                    prime_room=ValidRoom.KITCHEN,
                    confidence=0.75,
                    excluded_suspects=[ValidSuspect.PROFESSOR_PLUM, ValidSuspect.MR_GREEN],
                    excluded_weapons=[ValidWeapon.CANDLESTICK],
                    excluded_rooms=[ValidRoom.BALLROOM, ValidRoom.LIBRARY],
                    reasoning="Colonel Mustard was never shown by any player, and the knife was suggested multiple times without refutation"
                )

            Converting to dictionary::

                hypothesis_dict = hypothesis.to_dict()
                # Returns: {
                #     "prime_suspect": "Colonel Mustard",
                #     "prime_weapon": "Knife",
                #     "prime_room": "Kitchen",
                #     "confidence": 0.75,
                #     "excluded_suspects": ["Professor Plum", "Mr. Green"],
                #     "excluded_weapons": ["Candlestick"],
                #     "excluded_rooms": ["Ballroom", "Library"],
                #     "reasoning": "Colonel Mustard was never shown..."
                # }

            Using for decision making::

                # AI decides whether to make an accusation
                if hypothesis.confidence > 0.9:
                    # Make accusation with high confidence
                    accusation = ClueGuess(
                        suspect=hypothesis.prime_suspect,
                        weapon=hypothesis.prime_weapon,
                        room=hypothesis.prime_room
                    )


            .. py:method:: to_dict() -> dict[str, Any]

               Convert the hypothesis to a dictionary.

               :returns: Dictionary representation of the hypothesis.
               :rtype: dict[str, Any]

               .. rubric:: Examples

               Converting hypothesis to dictionary::

                   hypothesis = ClueHypothesis(
                       prime_suspect=ValidSuspect.COLONEL_MUSTARD,
                       prime_weapon=ValidWeapon.KNIFE,
                       prime_room=ValidRoom.KITCHEN,
                       confidence=0.75,
                       excluded_suspects=[ValidSuspect.PROFESSOR_PLUM],
                       reasoning="Based on elimination"
                   )
                   hypothesis_dict = hypothesis.to_dict()
                   # Returns: {
                   #     "prime_suspect": "Colonel Mustard",
                   #     "prime_weapon": "Knife",
                   #     "prime_room": "Kitchen",
                   #     "confidence": 0.75,
                   #     "excluded_suspects": ["Professor Plum"],
                   #     "excluded_weapons": [],
                   #     "excluded_rooms": [],
                   #     "reasoning": "Based on elimination"
                   # }



            .. py:attribute:: confidence
               :type:  float
               :value: 0.0



            .. py:attribute:: excluded_rooms
               :type:  list[ValidRoom]
               :value: []



            .. py:attribute:: excluded_suspects
               :type:  list[ValidSuspect]
               :value: []



            .. py:attribute:: excluded_weapons
               :type:  list[ValidWeapon]
               :value: []



            .. py:attribute:: prime_room
               :type:  ValidRoom | None
               :value: None



            .. py:attribute:: prime_suspect
               :type:  ValidSuspect | None
               :value: None



            .. py:attribute:: prime_weapon
               :type:  ValidWeapon | None
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: ''




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueResponse

            A response to a guess in a game of Clue.

            Represents the response given when a player makes a suggestion or accusation.
            The response indicates whether the guess was correct (for accusations) or
            provides information about which player can refute the guess (for suggestions).

            For suggestions, players check their cards to see if they can disprove the
            guess by showing one of the cards mentioned. For accusations, the response
            indicates whether the guess matches the solution exactly.

            .. attribute:: is_correct

               True if the guess matched the solution (accusations only)

            .. attribute:: responding_player

               Name of the player who responded (suggestions only)

            .. attribute:: refuting_card

               The card shown to refute the guess (suggestions only)

            .. rubric:: Examples

            Response to a suggestion::

                # Player can refute with Colonel Mustard card
                response = ClueResponse(
                    is_correct=False,
                    responding_player="Alice",
                    refuting_card=ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                )

            Response to an accusation::

                # Accusation was correct
                response = ClueResponse(
                    is_correct=True,
                    responding_player=None,
                    refuting_card=None
                )

                # Accusation was wrong
                response = ClueResponse(
                    is_correct=False,
                    responding_player=None,
                    refuting_card=None
                )

            Converting to dictionary::

                response_dict = response.to_dict()
                # Returns: {
                #     "is_correct": False,
                #     "responding_player": "Alice",
                #     "refuting_card": {"name": "Colonel Mustard", "card_type": "Suspect"}
                # }


            .. py:method:: to_dict() -> dict[str, Any]

               Convert the response to a dictionary.

               :returns: Dictionary representation of the response.
               :rtype: dict[str, Any]

               .. rubric:: Examples

               Converting response to dictionary::

                   response = ClueResponse(
                       is_correct=False,
                       responding_player="Alice",
                       refuting_card=ClueCard.from_suspect(ValidSuspect.COLONEL_MUSTARD)
                   )
                   response_dict = response.to_dict()
                   # Returns: {
                   #     "is_correct": False,
                   #     "responding_player": "Alice",
                   #     "refuting_card": {"name": "Colonel Mustard", "card_type": "Suspect"}
                   # }



            .. py:attribute:: is_correct
               :type:  bool


            .. py:attribute:: refuting_card
               :type:  ClueCard | None
               :value: None



            .. py:attribute:: responding_player
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueSolution

            The solution to a game of Clue.

            Represents the secret solution to the mystery that players are trying to solve.
            The solution consists of exactly one suspect, one weapon, and one room - these
            are the three cards that are set aside at the beginning of the game.

            Players win by correctly guessing all three elements of the solution through
            an accusation. The solution is hidden from all players until the end of the game.

            .. attribute:: suspect

               The suspect who committed the murder

            .. attribute:: weapon

               The weapon used to commit the murder

            .. attribute:: room

               The room where the murder took place

            .. rubric:: Examples

            Creating a solution::

                solution = ClueSolution(
                    suspect=ValidSuspect.COLONEL_MUSTARD,
                    weapon=ValidWeapon.KNIFE,
                    room=ValidRoom.KITCHEN
                )

            Converting to dictionary::

                solution_dict = solution.to_dict()
                # Returns: {
                #     "suspect": "Colonel Mustard",
                #     "weapon": "Knife",
                #     "room": "Kitchen"
                # }

            Checking accusations::

                player_accusation = (
                    ValidSuspect.COLONEL_MUSTARD,
                    ValidWeapon.KNIFE,
                    ValidRoom.KITCHEN
                )

                is_correct = (
                    solution.suspect == player_accusation[0] and
                    solution.weapon == player_accusation[1] and
                    solution.room == player_accusation[2]
                )


            .. py:method:: to_dict() -> dict[str, str]

               Convert the solution to a dictionary.

               :returns: Dictionary with 'suspect', 'weapon', and 'room' keys.
               :rtype: dict[str, str]

               .. rubric:: Examples

               Converting solution to dictionary::

                   solution = ClueSolution(
                       suspect=ValidSuspect.COLONEL_MUSTARD,
                       weapon=ValidWeapon.KNIFE,
                       room=ValidRoom.KITCHEN
                   )
                   solution_dict = solution.to_dict()
                   # Returns: {
                   #     "suspect": "Colonel Mustard",
                   #     "weapon": "Knife",
                   #     "room": "Kitchen"
                   # }



            .. py:attribute:: room
               :type:  ValidRoom


            .. py:attribute:: suspect
               :type:  ValidSuspect


            .. py:attribute:: weapon
               :type:  ValidWeapon



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameStatus(*args, **kwds)

            Bases: :py:obj:`enum.Enum`


            Status of a Clue game.

            Enumeration of the possible states of a Clue game during its lifecycle.
            Used to track game progression and determine valid actions.

            .. attribute:: NOT_STARTED

               Game has been created but not yet begun

            .. attribute:: IN_PROGRESS

               Game is currently being played

            .. attribute:: COMPLETED

               Game has finished (someone won or all players were eliminated)

            .. rubric:: Examples

            Checking game status::

                from haive.games.clue.models import GameStatus

                # Initialize game
                status = GameStatus.NOT_STARTED

                # Start game
                if status == GameStatus.NOT_STARTED:
                    status = GameStatus.IN_PROGRESS
                    print("Game started!")

                # Check if game is active
                if status == GameStatus.IN_PROGRESS:
                    # Allow players to make moves
                    process_player_turn()

                # Game completed
                if status == GameStatus.COMPLETED:
                    print("Game over!")

            Converting to string::

                status = GameStatus.IN_PROGRESS
                status_str = str(status)  # Returns "IN_PROGRESS"
                status_name = status.value  # Returns "IN_PROGRESS"


            .. py:method:: __str__() -> str

               Return the string representation of the game status.

               :returns: The status value as a string.
               :rtype: str

               .. rubric:: Examples

               Converting status to string::

                   status = GameStatus.IN_PROGRESS
                   print(f"Current status: {status}")  # "Current status: IN_PROGRESS"



            .. py:attribute:: COMPLETED
               :value: 'COMPLETED'



            .. py:attribute:: IN_PROGRESS
               :value: 'IN_PROGRESS'



            .. py:attribute:: NOT_STARTED
               :value: 'NOT_STARTED'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ValidRoom(*args, **kwds)

            Bases: :py:obj:`enum.Enum`


            Valid rooms in the game of Clue.

            Enumeration of all nine possible rooms in the classic Clue board game.
            Each room represents a location where the murder could have taken place
            in the game's solution.

            According to the classic Clue rules, one of these rooms will be the murder
            location in the game's solution, and the others will be distributed as cards
            to players for deduction purposes.

            .. attribute:: KITCHEN

               The food preparation area

            .. attribute:: BALLROOM

               The large dance hall

            .. attribute:: CONSERVATORY

               The greenhouse room

            .. attribute:: BILLIARD_ROOM

               The game room with pool table

            .. attribute:: LIBRARY

               The book-filled study room

            .. attribute:: STUDY

               The private office

            .. attribute:: HALL

               The main entrance hallway

            .. attribute:: LOUNGE

               The comfortable sitting room

            .. attribute:: DINING_ROOM

               The formal eating area

            .. rubric:: Examples

            Using rooms in game logic::

                from haive.games.clue.models import ValidRoom

                # Check if a room is valid
                if room_name == ValidRoom.KITCHEN.value:
                    print("Kitchen is a valid room!")

                # Iterate through all rooms
                for room in ValidRoom:
                    print(f"Room: {room.value}")

                # Use in suggestions
                my_suggestion = (
                    ValidSuspect.MRS_PEACOCK,
                    ValidWeapon.REVOLVER,
                    ValidRoom.LIBRARY
                )


            .. py:attribute:: BALLROOM
               :value: 'Ballroom'



            .. py:attribute:: BILLIARD_ROOM
               :value: 'Billiard Room'



            .. py:attribute:: CONSERVATORY
               :value: 'Conservatory'



            .. py:attribute:: DINING_ROOM
               :value: 'Dining Room'



            .. py:attribute:: HALL
               :value: 'Hall'



            .. py:attribute:: KITCHEN
               :value: 'Kitchen'



            .. py:attribute:: LIBRARY
               :value: 'Library'



            .. py:attribute:: LOUNGE
               :value: 'Lounge'



            .. py:attribute:: STUDY
               :value: 'Study'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ValidSuspect(*args, **kwds)

            Bases: :py:obj:`enum.Enum`


            Valid suspects in the game of Clue.

            Enumeration of all six possible suspects in the classic Clue board game.
            Each suspect is represented by their traditional character name and can
            be used as both a character to play as and a card in the deck.

            According to the classic Clue rules, one of these suspects will be the
            murderer in the game's solution, and the others will be distributed as
            cards to players for deduction purposes.

            .. attribute:: COLONEL_MUSTARD

               The military officer suspect

            .. attribute:: PROFESSOR_PLUM

               The academic suspect

            .. attribute:: MR_GREEN

               The businessman suspect

            .. attribute:: MRS_PEACOCK

               The socialite suspect

            .. attribute:: MISS_SCARLET

               The glamorous suspect

            .. attribute:: MRS_WHITE

               The housekeeper suspect

            .. rubric:: Examples

            Using suspects in game logic::

                from haive.games.clue.models import ValidSuspect

                # Check if a suspect is valid
                if suspect_name == ValidSuspect.COLONEL_MUSTARD.value:
                    print("Colonel Mustard is a valid suspect!")

                # Iterate through all suspects
                for suspect in ValidSuspect:
                    print(f"Suspect: {suspect.value}")

                # Use in game suggestions
                my_suggestion = (
                    ValidSuspect.PROFESSOR_PLUM,
                    ValidWeapon.CANDLESTICK,
                    ValidRoom.LIBRARY
                )


            .. py:attribute:: COLONEL_MUSTARD
               :value: 'Colonel Mustard'



            .. py:attribute:: MISS_SCARLET
               :value: 'Miss Scarlet'



            .. py:attribute:: MRS_PEACOCK
               :value: 'Mrs. Peacock'



            .. py:attribute:: MRS_WHITE
               :value: 'Mrs. White'



            .. py:attribute:: MR_GREEN
               :value: 'Mr. Green'



            .. py:attribute:: PROFESSOR_PLUM
               :value: 'Professor Plum'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ValidWeapon(*args, **kwds)

            Bases: :py:obj:`enum.Enum`


            Valid weapons in the game of Clue.

            Enumeration of all six possible murder weapons in the classic Clue board game.
            Each weapon represents a potential murder weapon that could be used to commit
            the crime in the game's solution.

            According to the classic Clue rules, one of these weapons will be the murder
            weapon in the game's solution, and the others will be distributed as cards
            to players for deduction purposes.

            .. attribute:: KNIFE

               A sharp blade weapon

            .. attribute:: CANDLESTICK

               A heavy decorative candle holder

            .. attribute:: REVOLVER

               A six-shot pistol

            .. attribute:: ROPE

               A length of rope for strangulation

            .. attribute:: LEAD_PIPE

               A heavy metal pipe

            .. attribute:: WRENCH

               A heavy tool weapon

            .. rubric:: Examples

            Using weapons in game logic::

                from haive.games.clue.models import ValidWeapon

                # Check if a weapon is valid
                if weapon_name == ValidWeapon.KNIFE.value:
                    print("Knife is a valid weapon!")

                # Iterate through all weapons
                for weapon in ValidWeapon:
                    print(f"Weapon: {weapon.value}")

                # Use in accusations
                my_accusation = (
                    ValidSuspect.COLONEL_MUSTARD,
                    ValidWeapon.KNIFE,
                    ValidRoom.KITCHEN
                )


            .. py:attribute:: CANDLESTICK
               :value: 'Candlestick'



            .. py:attribute:: KNIFE
               :value: 'Knife'



            .. py:attribute:: LEAD_PIPE
               :value: 'Lead Pipe'



            .. py:attribute:: REVOLVER
               :value: 'Revolver'



            .. py:attribute:: ROPE
               :value: 'Rope'



            .. py:attribute:: WRENCH
               :value: 'Wrench'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

