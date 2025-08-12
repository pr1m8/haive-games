
:py:mod:`games.clue.models`
===========================

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


.. autolink-examples:: games.clue.models
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CardType:

   .. graphviz::
      :align: center

      digraph inheritance_CardType {
        node [shape=record];
        "CardType" [label="CardType"];
        "enum.Enum" -> "CardType";
      }

.. autoclass:: games.clue.models.CardType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CardType** is an Enum defined in ``games.clue.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueCard:

   .. graphviz::
      :align: center

      digraph inheritance_ClueCard {
        node [shape=record];
        "ClueCard" [label="ClueCard"];
      }

.. autoclass:: games.clue.models.ClueCard
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueGuess:

   .. graphviz::
      :align: center

      digraph inheritance_ClueGuess {
        node [shape=record];
        "ClueGuess" [label="ClueGuess"];
      }

.. autoclass:: games.clue.models.ClueGuess
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueHypothesis:

   .. graphviz::
      :align: center

      digraph inheritance_ClueHypothesis {
        node [shape=record];
        "ClueHypothesis" [label="ClueHypothesis"];
      }

.. autoclass:: games.clue.models.ClueHypothesis
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueResponse:

   .. graphviz::
      :align: center

      digraph inheritance_ClueResponse {
        node [shape=record];
        "ClueResponse" [label="ClueResponse"];
      }

.. autoclass:: games.clue.models.ClueResponse
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ClueSolution {
        node [shape=record];
        "ClueSolution" [label="ClueSolution"];
      }

.. autoclass:: games.clue.models.ClueSolution
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameStatus:

   .. graphviz::
      :align: center

      digraph inheritance_GameStatus {
        node [shape=record];
        "GameStatus" [label="GameStatus"];
        "enum.Enum" -> "GameStatus";
      }

.. autoclass:: games.clue.models.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``games.clue.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ValidRoom:

   .. graphviz::
      :align: center

      digraph inheritance_ValidRoom {
        node [shape=record];
        "ValidRoom" [label="ValidRoom"];
        "enum.Enum" -> "ValidRoom";
      }

.. autoclass:: games.clue.models.ValidRoom
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ValidRoom** is an Enum defined in ``games.clue.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ValidSuspect:

   .. graphviz::
      :align: center

      digraph inheritance_ValidSuspect {
        node [shape=record];
        "ValidSuspect" [label="ValidSuspect"];
        "enum.Enum" -> "ValidSuspect";
      }

.. autoclass:: games.clue.models.ValidSuspect
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ValidSuspect** is an Enum defined in ``games.clue.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ValidWeapon:

   .. graphviz::
      :align: center

      digraph inheritance_ValidWeapon {
        node [shape=record];
        "ValidWeapon" [label="ValidWeapon"];
        "enum.Enum" -> "ValidWeapon";
      }

.. autoclass:: games.clue.models.ValidWeapon
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ValidWeapon** is an Enum defined in ``games.clue.models``.





.. rubric:: Related Links

.. autolink-examples:: games.clue.models
   :collapse:
   
.. autolink-skip:: next
