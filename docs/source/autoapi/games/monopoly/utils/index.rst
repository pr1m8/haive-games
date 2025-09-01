games.monopoly.utils
====================

.. py:module:: games.monopoly.utils

.. autoapi-nested-parse::

   Monopoly game utilities and board logic.

   This module provides utility functions for the monopoly game, including:
       - Board setup and property definitions
       - Game logic calculations
       - Card definitions and handling
       - Rent calculations



Attributes
----------

.. autoapisummary::

   games.monopoly.utils.BOARD_PROPERTIES
   games.monopoly.utils.CHANCE_CARDS
   games.monopoly.utils.COLOR_GROUPS
   games.monopoly.utils.COMMUNITY_CHEST_CARDS


Functions
---------

.. autoapisummary::

   games.monopoly.utils.calculate_rent
   games.monopoly.utils.can_trade_properties
   games.monopoly.utils.check_game_end
   games.monopoly.utils.create_board
   games.monopoly.utils.create_players
   games.monopoly.utils.get_building_cost
   games.monopoly.utils.get_properties_by_color
   games.monopoly.utils.get_property_at_position
   games.monopoly.utils.handle_special_position
   games.monopoly.utils.move_player
   games.monopoly.utils.roll_dice
   games.monopoly.utils.shuffle_cards


Module Contents
---------------

.. py:function:: calculate_rent(property: haive.games.monopoly.models.Property, state: haive.games.monopoly.state.MonopolyState, dice_roll: int | None = None) -> int

   Calculate rent for a property.


.. py:function:: can_trade_properties(prop1: haive.games.monopoly.models.Property, prop2: haive.games.monopoly.models.Property, state: haive.games.monopoly.state.MonopolyState) -> bool

   Check if two properties can be traded.


.. py:function:: check_game_end(state: haive.games.monopoly.state.MonopolyState) -> tuple[bool, str | None]

   Check if the game should end.


.. py:function:: create_board() -> dict[str, haive.games.monopoly.models.Property]

   Create the initial board with all properties.


.. py:function:: create_players(player_names: list[str]) -> list[haive.games.monopoly.models.Player]

   Create initial players.


.. py:function:: get_building_cost(property: haive.games.monopoly.models.Property, buildings: int, is_hotel: bool = False) -> int

   Calculate cost to build houses or hotel.


.. py:function:: get_properties_by_color(color: haive.games.monopoly.models.PropertyColor) -> list[str]

   Get all property names for a color group.


.. py:function:: get_property_at_position(position: int) -> dict[str, Any] | None

   Get property information at a board position.


.. py:function:: handle_special_position(position: int, player: haive.games.monopoly.models.Player, state: haive.games.monopoly.state.MonopolyState) -> str

   Handle special board positions like GO, Jail, etc.


.. py:function:: move_player(player: haive.games.monopoly.models.Player, dice_roll: haive.games.monopoly.models.DiceRoll) -> tuple[int, bool]

   Move a player based on dice roll.


.. py:function:: roll_dice() -> haive.games.monopoly.models.DiceRoll

   Roll two dice.


.. py:function:: shuffle_cards() -> tuple[list[str], list[str]]

   Shuffle and return chance and community chest cards.


.. py:data:: BOARD_PROPERTIES

.. py:data:: CHANCE_CARDS
   :value: ['Advance to GO (Collect $200)', 'Advance to Illinois Avenue', 'Advance to St. Charles Place',...


.. py:data:: COLOR_GROUPS

.. py:data:: COMMUNITY_CHEST_CARDS
   :value: ['Advance to GO (Collect $200)', 'Bank error in your favor', "Doctor's fee", 'From sale of stock...


