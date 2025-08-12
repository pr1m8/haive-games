
:py:mod:`games.monopoly.standalone_demo`
========================================

.. py:module:: games.monopoly.standalone_demo

Standalone Monopoly demo with minimal dependencies.

This script provides a self-contained demonstration of the Monopoly game
without relying on external dependencies like langchain.

Usage:
    python standalone_demo.py


.. autolink-examples:: games.monopoly.standalone_demo
   :collapse:

Classes
-------

.. autoapisummary::

   games.monopoly.standalone_demo.Color
   games.monopoly.standalone_demo.DiceRoll
   games.monopoly.standalone_demo.GameEvent
   games.monopoly.standalone_demo.GameState
   games.monopoly.standalone_demo.Player
   games.monopoly.standalone_demo.Property
   games.monopoly.standalone_demo.PropertyColor
   games.monopoly.standalone_demo.PropertyType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Color:

   .. graphviz::
      :align: center

      digraph inheritance_Color {
        node [shape=record];
        "Color" [label="Color"];
      }

.. autoclass:: games.monopoly.standalone_demo.Color
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DiceRoll:

   .. graphviz::
      :align: center

      digraph inheritance_DiceRoll {
        node [shape=record];
        "DiceRoll" [label="DiceRoll"];
      }

.. autoclass:: games.monopoly.standalone_demo.DiceRoll
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameEvent:

   .. graphviz::
      :align: center

      digraph inheritance_GameEvent {
        node [shape=record];
        "GameEvent" [label="GameEvent"];
      }

.. autoclass:: games.monopoly.standalone_demo.GameEvent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameState:

   .. graphviz::
      :align: center

      digraph inheritance_GameState {
        node [shape=record];
        "GameState" [label="GameState"];
      }

.. autoclass:: games.monopoly.standalone_demo.GameState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Player:

   .. graphviz::
      :align: center

      digraph inheritance_Player {
        node [shape=record];
        "Player" [label="Player"];
      }

.. autoclass:: games.monopoly.standalone_demo.Player
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Property:

   .. graphviz::
      :align: center

      digraph inheritance_Property {
        node [shape=record];
        "Property" [label="Property"];
      }

.. autoclass:: games.monopoly.standalone_demo.Property
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PropertyColor:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyColor {
        node [shape=record];
        "PropertyColor" [label="PropertyColor"];
        "str" -> "PropertyColor";
        "enum.Enum" -> "PropertyColor";
      }

.. autoclass:: games.monopoly.standalone_demo.PropertyColor
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PropertyColor** is an Enum defined in ``games.monopoly.standalone_demo``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PropertyType:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyType {
        node [shape=record];
        "PropertyType" [label="PropertyType"];
        "str" -> "PropertyType";
        "enum.Enum" -> "PropertyType";
      }

.. autoclass:: games.monopoly.standalone_demo.PropertyType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PropertyType** is an Enum defined in ``games.monopoly.standalone_demo``.



Functions
---------

.. autoapisummary::

   games.monopoly.standalone_demo.calculate_rent
   games.monopoly.standalone_demo.create_board
   games.monopoly.standalone_demo.create_players
   games.monopoly.standalone_demo.get_property_at_position
   games.monopoly.standalone_demo.handle_property_landing
   games.monopoly.standalone_demo.move_player
   games.monopoly.standalone_demo.print_divider
   games.monopoly.standalone_demo.print_player_status
   games.monopoly.standalone_demo.print_property
   games.monopoly.standalone_demo.print_recent_events
   games.monopoly.standalone_demo.roll_dice
   games.monopoly.standalone_demo.run_demo

.. py:function:: calculate_rent(property_obj: Property, state: GameState, dice_roll: int | None = None) -> int

   Calculate rent for a property.


   .. autolink-examples:: calculate_rent
      :collapse:

.. py:function:: create_board() -> dict[str, Property]

   Create the initial board with all properties.


   .. autolink-examples:: create_board
      :collapse:

.. py:function:: create_players(player_names: list[str]) -> list[Player]

   Create initial players.


   .. autolink-examples:: create_players
      :collapse:

.. py:function:: get_property_at_position(position: int) -> dict | None

   Get property information at a board position.


   .. autolink-examples:: get_property_at_position
      :collapse:

.. py:function:: handle_property_landing(state: GameState, position: int) -> list[GameEvent]

   Handle a player landing on a property.


   .. autolink-examples:: handle_property_landing
      :collapse:

.. py:function:: move_player(player: Player, dice_roll: DiceRoll) -> tuple[int, bool]

   Move a player based on dice roll.


   .. autolink-examples:: move_player
      :collapse:

.. py:function:: print_divider()

   Print a divider line.


   .. autolink-examples:: print_divider
      :collapse:

.. py:function:: print_player_status(state: GameState)

   Print current status of all players.


   .. autolink-examples:: print_player_status
      :collapse:

.. py:function:: print_property(property_obj: Property)

   Print property details.


   .. autolink-examples:: print_property
      :collapse:

.. py:function:: print_recent_events(events: list[GameEvent], count: int = 5)

   Print recent game events.


   .. autolink-examples:: print_recent_events
      :collapse:

.. py:function:: roll_dice() -> DiceRoll

   Roll two dice.


   .. autolink-examples:: roll_dice
      :collapse:

.. py:function:: run_demo(turns: int = 10)

   Run a simple Monopoly game demo.


   .. autolink-examples:: run_demo
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.monopoly.standalone_demo
   :collapse:
   
.. autolink-skip:: next
