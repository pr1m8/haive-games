games.monopoly.utils
====================

.. py:module:: games.monopoly.utils

Monopoly game utilities and board logic.

This module provides utility functions for the monopoly game, including:
    - Board setup and property definitions
    - Game logic calculations
    - Card definitions and handling
    - Rent calculations



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">12 functions</span> • <span class="module-stat">4 attributes</span>   </div>

.. autoapi-nested-parse::

   Monopoly game utilities and board logic.

   This module provides utility functions for the monopoly game, including:
       - Board setup and property definitions
       - Game logic calculations
       - Card definitions and handling
       - Rent calculations



      

.. admonition:: Attributes (4)
   :class: tip

   .. autoapisummary::

      games.monopoly.utils.BOARD_PROPERTIES
      games.monopoly.utils.CHANCE_CARDS
      games.monopoly.utils.COLOR_GROUPS
      games.monopoly.utils.COMMUNITY_CHEST_CARDS

            
            
            

.. admonition:: Functions (12)
   :class: info

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

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: calculate_rent(property: haive.games.monopoly.models.Property, state: haive.games.monopoly.state.MonopolyState, dice_roll: int | None = None) -> int

            Calculate rent for a property.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: can_trade_properties(prop1: haive.games.monopoly.models.Property, prop2: haive.games.monopoly.models.Property, state: haive.games.monopoly.state.MonopolyState) -> bool

            Check if two properties can be traded.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: check_game_end(state: haive.games.monopoly.state.MonopolyState) -> tuple[bool, str | None]

            Check if the game should end.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_board() -> dict[str, haive.games.monopoly.models.Property]

            Create the initial board with all properties.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_players(player_names: list[str]) -> list[haive.games.monopoly.models.Player]

            Create initial players.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_building_cost(property: haive.games.monopoly.models.Property, buildings: int, is_hotel: bool = False) -> int

            Calculate cost to build houses or hotel.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_properties_by_color(color: haive.games.monopoly.models.PropertyColor) -> list[str]

            Get all property names for a color group.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_property_at_position(position: int) -> dict[str, Any] | None

            Get property information at a board position.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: handle_special_position(position: int, player: haive.games.monopoly.models.Player, state: haive.games.monopoly.state.MonopolyState) -> str

            Handle special board positions like GO, Jail, etc.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: move_player(player: haive.games.monopoly.models.Player, dice_roll: haive.games.monopoly.models.DiceRoll) -> tuple[int, bool]

            Move a player based on dice roll.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: roll_dice() -> haive.games.monopoly.models.DiceRoll

            Roll two dice.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: shuffle_cards() -> tuple[list[str], list[str]]

            Shuffle and return chance and community chest cards.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: BOARD_PROPERTIES


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: CHANCE_CARDS
            :value: ['Advance to GO (Collect $200)', 'Advance to Illinois Avenue', 'Advance to St. Charles Place',...



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: COLOR_GROUPS


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: COMMUNITY_CHEST_CARDS
            :value: ['Advance to GO (Collect $200)', 'Bank error in your favor', "Doctor's fee", 'From sale of stock...





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.utils import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

