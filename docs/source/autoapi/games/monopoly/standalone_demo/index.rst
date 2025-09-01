games.monopoly.standalone_demo
==============================

.. py:module:: games.monopoly.standalone_demo

.. autoapi-nested-parse::

   Standalone Monopoly demo with minimal dependencies.

   This script provides a self-contained demonstration of the Monopoly game
   without relying on external dependencies like langchain.

   Usage:
       python standalone_demo.py



Attributes
----------

.. autoapisummary::

   games.monopoly.standalone_demo.BOARD_PROPERTIES


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/monopoly/standalone_demo/Color
   /autoapi/games/monopoly/standalone_demo/DiceRoll
   /autoapi/games/monopoly/standalone_demo/GameEvent
   /autoapi/games/monopoly/standalone_demo/GameState
   /autoapi/games/monopoly/standalone_demo/Player
   /autoapi/games/monopoly/standalone_demo/Property
   /autoapi/games/monopoly/standalone_demo/PropertyColor
   /autoapi/games/monopoly/standalone_demo/PropertyType

.. autoapisummary::

   games.monopoly.standalone_demo.Color
   games.monopoly.standalone_demo.DiceRoll
   games.monopoly.standalone_demo.GameEvent
   games.monopoly.standalone_demo.GameState
   games.monopoly.standalone_demo.Player
   games.monopoly.standalone_demo.Property
   games.monopoly.standalone_demo.PropertyColor
   games.monopoly.standalone_demo.PropertyType


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


Module Contents
---------------

.. py:function:: calculate_rent(property_obj: Property, state: GameState, dice_roll: int | None = None) -> int

   Calculate rent for a property.


.. py:function:: create_board() -> dict[str, Property]

   Create the initial board with all properties.


.. py:function:: create_players(player_names: list[str]) -> list[Player]

   Create initial players.


.. py:function:: get_property_at_position(position: int) -> dict | None

   Get property information at a board position.


.. py:function:: handle_property_landing(state: GameState, position: int) -> list[GameEvent]

   Handle a player landing on a property.


.. py:function:: move_player(player: Player, dice_roll: DiceRoll) -> tuple[int, bool]

   Move a player based on dice roll.


.. py:function:: print_divider()

   Print a divider line.


.. py:function:: print_player_status(state: GameState)

   Print current status of all players.


.. py:function:: print_property(property_obj: Property)

   Print property details.


.. py:function:: print_recent_events(events: list[GameEvent], count: int = 5)

   Print recent game events.


.. py:function:: roll_dice() -> DiceRoll

   Roll two dice.


.. py:function:: run_demo(turns: int = 10)

   Run a simple Monopoly game demo.


.. py:data:: BOARD_PROPERTIES

