games.monopoly.game.game
========================

.. py:module:: games.monopoly.game.game

.. autoapi-nested-parse::

   Monopoly Game Engine - Core implementation optimized for AI agent experimentation.
   This module contains the core game rules and state management without UI dependencies.


   .. autolink-examples:: games.monopoly.game.game
      :collapse:


Attributes
----------

.. autoapisummary::

   games.monopoly.game.game.logger


Classes
-------

.. autoapisummary::

   games.monopoly.game.game.MonopolyGame


Module Contents
---------------

.. py:class:: MonopolyGame(player_names: list[str], board_config: list[tuple] | None = None, starting_cash: int = 1500, max_rounds: int = 100, free_parking_money: bool = False, auction_properties: bool = True)

   Core Monopoly game engine without UI dependencies.

   Designed for AI agent experimentation.


   Initialize a new Monopoly game.

   :param player_names: List of player names
   :param board_config: Optional custom board configuration
   :param starting_cash: Starting cash for each player
   :param max_rounds: Maximum number of rounds to play
   :param free_parking_money: Whether Free Parking collects money
   :param auction_properties: Whether to auction unsold properties


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MonopolyGame
      :collapse:

   .. py:method:: _advance_to_next_player() -> None

      Advance to the next player who isn't bankrupt.


      .. autolink-examples:: _advance_to_next_player
         :collapse:


   .. py:method:: _check_game_over() -> bool

      Check if the game is over.


      .. autolink-examples:: _check_game_over
         :collapse:


   .. py:method:: _create_chance_cards() -> list[haive.games.monopoly.game.card.Card]

      Create the standard Chance cards.


      .. autolink-examples:: _create_chance_cards
         :collapse:


   .. py:method:: _create_community_chest_cards() -> list[haive.games.monopoly.game.card.Card]

      Create the standard Community Chest cards.


      .. autolink-examples:: _create_community_chest_cards
         :collapse:


   .. py:method:: _draw_chance_card(player: haive.games.monopoly.game.player.Player) -> None

      Draw a Chance card.


      .. autolink-examples:: _draw_chance_card
         :collapse:


   .. py:method:: _draw_community_chest_card(player: haive.games.monopoly.game.player.Player) -> None

      Draw a Community Chest card.


      .. autolink-examples:: _draw_community_chest_card
         :collapse:


   .. py:method:: _end_game() -> None

      End the game due to round limit.


      .. autolink-examples:: _end_game
         :collapse:


   .. py:method:: _find_nearest_property(position: int, property_type: str) -> int | None

      Find the nearest property of a specific type.


      .. autolink-examples:: _find_nearest_property
         :collapse:


   .. py:method:: _handle_auction_action(property_position: int) -> bool

      Handle auctioning a property.


      .. autolink-examples:: _handle_auction_action
         :collapse:


   .. py:method:: _handle_bankruptcy(player: haive.games.monopoly.game.player.Player, creditor: haive.games.monopoly.game.player.Player | None, amount: int) -> None

      Handle a player going bankrupt.


      .. autolink-examples:: _handle_bankruptcy
         :collapse:


   .. py:method:: _handle_build_house_action(player: haive.games.monopoly.game.player.Player, property_position: int) -> bool

      Handle building a house on a property.


      .. autolink-examples:: _handle_build_house_action
         :collapse:


   .. py:method:: _handle_buy_action(player: haive.games.monopoly.game.player.Player, property_position: int) -> bool

      Handle buying a property.


      .. autolink-examples:: _handle_buy_action
         :collapse:


   .. py:method:: _handle_card(player: haive.games.monopoly.game.player.Player, card: haive.games.monopoly.game.card.Card) -> None

      Handle the effects of a card.


      .. autolink-examples:: _handle_card
         :collapse:


   .. py:method:: _handle_end_turn_action(player: haive.games.monopoly.game.player.Player) -> bool

      Handle ending a player's turn.


      .. autolink-examples:: _handle_end_turn_action
         :collapse:


   .. py:method:: _handle_landing(player: haive.games.monopoly.game.player.Player, position: int) -> None

      Handle a player landing on a space.


      .. autolink-examples:: _handle_landing
         :collapse:


   .. py:method:: _handle_mortgage_action(player: haive.games.monopoly.game.player.Player, property_position: int) -> bool

      Handle mortgaging a property.


      .. autolink-examples:: _handle_mortgage_action
         :collapse:


   .. py:method:: _handle_pay_jail_fee_action(player: haive.games.monopoly.game.player.Player) -> bool

      Handle paying the jail fee.


      .. autolink-examples:: _handle_pay_jail_fee_action
         :collapse:


   .. py:method:: _handle_roll_action(player: haive.games.monopoly.game.player.Player) -> bool

      Handle rolling the dice and moving.


      .. autolink-examples:: _handle_roll_action
         :collapse:


   .. py:method:: _handle_roll_for_jail_action(player: haive.games.monopoly.game.player.Player) -> bool

      Handle rolling for doubles to get out of jail.


      .. autolink-examples:: _handle_roll_for_jail_action
         :collapse:


   .. py:method:: _handle_sell_house_action(player: haive.games.monopoly.game.player.Player, property_position: int) -> bool

      Handle selling a house from a property.


      .. autolink-examples:: _handle_sell_house_action
         :collapse:


   .. py:method:: _handle_special_square(player: haive.games.monopoly.game.player.Player, prop: haive.games.monopoly.game.property.Property) -> None

      Handle landing on a special square.


      .. autolink-examples:: _handle_special_square
         :collapse:


   .. py:method:: _handle_trade_action(player: haive.games.monopoly.game.player.Player, other_player_idx: int, give_properties: list[int], take_properties: list[int], give_money: int, take_money: int) -> bool

      Handle trading between players.


      .. autolink-examples:: _handle_trade_action
         :collapse:


   .. py:method:: _handle_unmortgage_action(player: haive.games.monopoly.game.player.Player, property_position: int) -> bool

      Handle unmortgaging a property.


      .. autolink-examples:: _handle_unmortgage_action
         :collapse:


   .. py:method:: _handle_use_jail_card_action(player: haive.games.monopoly.game.player.Player) -> bool

      Handle using a Get Out of Jail Free card.


      .. autolink-examples:: _handle_use_jail_card_action
         :collapse:


   .. py:method:: _send_to_jail(player: haive.games.monopoly.game.player.Player) -> bool

      Send a player to jail.


      .. autolink-examples:: _send_to_jail
         :collapse:


   .. py:method:: can_build_house(property_position: int) -> bool

      Check if a house can be built on a property.

      :param property_position: Position of the property

      :returns: True if a house can be built


      .. autolink-examples:: can_build_house
         :collapse:


   .. py:method:: can_mortgage(property_position: int) -> bool

      Check if a property can be mortgaged.

      :param property_position: Position of the property

      :returns: True if the property can be mortgaged


      .. autolink-examples:: can_mortgage
         :collapse:


   .. py:method:: can_sell_house(property_position: int) -> bool

      Check if a house can be sold from a property.

      :param property_position: Position of the property

      :returns: True if a house can be sold


      .. autolink-examples:: can_sell_house
         :collapse:


   .. py:method:: can_unmortgage(property_position: int, player: haive.games.monopoly.game.player.Player) -> bool

      Check if a property can be unmortgaged.

      :param property_position: Position of the property
      :param player: Player attempting to unmortgage

      :returns: True if the property can be unmortgaged


      .. autolink-examples:: can_unmortgage
         :collapse:


   .. py:method:: get_current_player() -> haive.games.monopoly.game.player.Player

      Get the current player.

      :returns: Current Player object


      .. autolink-examples:: get_current_player
         :collapse:


   .. py:method:: get_game_state() -> dict[str, Any]

      Get the current game state.

      :returns: Dictionary with the game state


      .. autolink-examples:: get_game_state
         :collapse:


   .. py:method:: get_properties_by_group(color_group: str) -> list[haive.games.monopoly.game.property.Property]

      Get all properties in a color group.

      :param color_group: Name of the color group

      :returns: List of Property objects


      .. autolink-examples:: get_properties_by_group
         :collapse:


   .. py:method:: get_properties_owned_by_player(player_idx: int) -> list[haive.games.monopoly.game.property.Property]

      Get all properties owned by a player.

      :param player_idx: Index of the player

      :returns: List of Property objects


      .. autolink-examples:: get_properties_owned_by_player
         :collapse:


   .. py:method:: get_property_at(position: int) -> haive.games.monopoly.game.property.Property | None

      Get the property at a specific position.

      :param position: Board position

      :returns: Property object or None if not found


      .. autolink-examples:: get_property_at
         :collapse:


   .. py:method:: log_event(event: str) -> None

      Add an event to the game log.

      :param event: Description of the event


      .. autolink-examples:: log_event
         :collapse:


   .. py:method:: perform_action(action_type: haive.games.monopoly.game.types.ActionType, player_idx: int, **kwargs) -> bool

      Perform an action for a player.

      :param action_type: Type of action to perform
      :param player_idx: Index of the player performing the action
      :param \*\*kwargs: Action-specific parameters

      :returns: True if the action was successful


      .. autolink-examples:: perform_action
         :collapse:


   .. py:method:: player_owns_all_in_group(player_idx: int, color_group: str) -> bool

      Check if a player owns all properties in a group.

      :param player_idx: Index of the player
      :param color_group: Name of the color group

      :returns: True if player owns all properties in the group


      .. autolink-examples:: player_owns_all_in_group
         :collapse:


   .. py:method:: print_game_state() -> None

      Print the current game state to the console.


      .. autolink-examples:: print_game_state
         :collapse:


   .. py:method:: roll_dice() -> tuple[int, int]

      Roll two dice.

      :returns: Tuple of (die1, die2)


      .. autolink-examples:: roll_dice
         :collapse:


   .. py:attribute:: DEFAULT_BOARD


   .. py:attribute:: GO_SALARY
      :value: 200



   .. py:attribute:: INCOME_TAX
      :value: 200



   .. py:attribute:: JAIL_FEE
      :value: 50



   .. py:attribute:: JAIL_POSITION
      :value: 10



   .. py:attribute:: LUXURY_TAX
      :value: 100



   .. py:attribute:: MAX_HOUSES_PER_PROPERTY
      :value: 5



   .. py:attribute:: auction_properties
      :value: True



   .. py:attribute:: chance_cards


   .. py:attribute:: community_chest_cards


   .. py:attribute:: current_player_idx
      :value: 0



   .. py:attribute:: current_round
      :value: 0



   .. py:attribute:: doubles_count
      :value: 0



   .. py:attribute:: event_log
      :value: []



   .. py:attribute:: free_parking_money
      :value: False



   .. py:attribute:: free_parking_pot
      :value: 0



   .. py:attribute:: game_over
      :value: False



   .. py:attribute:: has_rolled
      :value: False



   .. py:attribute:: last_dice_roll
      :value: (0, 0)



   .. py:attribute:: max_players


   .. py:attribute:: max_rounds
      :value: 100



   .. py:attribute:: players


   .. py:attribute:: properties
      :value: []



   .. py:attribute:: properties_to_auction
      :value: []



   .. py:attribute:: winner
      :value: None



.. py:data:: logger

