games.hold_em.utils
===================

.. py:module:: games.hold_em.utils

.. autoapi-nested-parse::

   Texas Hold'em utility functions.

   This module provides utility functions for the Hold'em game, including:
       - Card and hand evaluation
       - Game state utilities
       - Poker calculations


   .. autolink-examples:: games.hold_em.utils
      :collapse:


Functions
---------

.. autoapisummary::

   games.hold_em.utils.calculate_effective_stack
   games.hold_em.utils.calculate_pot_odds
   games.hold_em.utils.card_to_rank_value
   games.hold_em.utils.card_to_suit
   games.hold_em.utils.count_players_in_phase
   games.hold_em.utils.create_standard_deck
   games.hold_em.utils.deal_cards
   games.hold_em.utils.evaluate_hand_simple
   games.hold_em.utils.format_cards
   games.hold_em.utils.format_game_summary
   games.hold_em.utils.get_board_texture_description
   games.hold_em.utils.get_next_active_player
   games.hold_em.utils.get_position_name
   games.hold_em.utils.is_position_early
   games.hold_em.utils.is_position_late
   games.hold_em.utils.shuffle_deck
   games.hold_em.utils.validate_game_state


Module Contents
---------------

.. py:function:: calculate_effective_stack(player: haive.games.hold_em.state.PlayerState, opponent: haive.games.hold_em.state.PlayerState) -> int

   Calculate effective stack between two players.


   .. autolink-examples:: calculate_effective_stack
      :collapse:

.. py:function:: calculate_pot_odds(pot_size: int, bet_to_call: int) -> float

   Calculate pot odds as a ratio.


   .. autolink-examples:: calculate_pot_odds
      :collapse:

.. py:function:: card_to_rank_value(card: str) -> int

   Convert card rank to numeric value for comparison.


   .. autolink-examples:: card_to_rank_value
      :collapse:

.. py:function:: card_to_suit(card: str) -> str

   Extract suit from card.


   .. autolink-examples:: card_to_suit
      :collapse:

.. py:function:: count_players_in_phase(game_state: haive.games.hold_em.state.HoldemState, statuses: list[haive.games.hold_em.state.PlayerStatus]) -> int

   Count players with specific statuses.


   .. autolink-examples:: count_players_in_phase
      :collapse:

.. py:function:: create_standard_deck() -> list[str]

   Create a standard 52-card deck.


   .. autolink-examples:: create_standard_deck
      :collapse:

.. py:function:: deal_cards(deck: list[str], num_cards: int) -> tuple[list[str], list[str]]

   Deal cards from deck, returning (dealt_cards, remaining_deck).


   .. autolink-examples:: deal_cards
      :collapse:

.. py:function:: evaluate_hand_simple(hole_cards: list[str], community_cards: list[str]) -> dict[str, any]

   Simple hand evaluation (placeholder for production poker evaluator).

   Returns hand rank, strength score, and description.



   .. autolink-examples:: evaluate_hand_simple
      :collapse:

.. py:function:: format_cards(cards: list[str]) -> str

   Format cards for display with suit symbols.


   .. autolink-examples:: format_cards
      :collapse:

.. py:function:: format_game_summary(game_state: haive.games.hold_em.state.HoldemState) -> str

   Format a summary of the current game state.


   .. autolink-examples:: format_game_summary
      :collapse:

.. py:function:: get_board_texture_description(community_cards: list[str]) -> str

   Describe the board texture.


   .. autolink-examples:: get_board_texture_description
      :collapse:

.. py:function:: get_next_active_player(game_state: haive.games.hold_em.state.HoldemState, start_position: int) -> int | None

   Get the next active player starting from a position.


   .. autolink-examples:: get_next_active_player
      :collapse:

.. py:function:: get_position_name(position: int, num_players: int, dealer_pos: int) -> str

   Get position name based on seat and dealer position.


   .. autolink-examples:: get_position_name
      :collapse:

.. py:function:: is_position_early(position: int, num_players: int, dealer_pos: int) -> bool

   Check if position is early.


   .. autolink-examples:: is_position_early
      :collapse:

.. py:function:: is_position_late(position: int, num_players: int, dealer_pos: int) -> bool

   Check if position is late.


   .. autolink-examples:: is_position_late
      :collapse:

.. py:function:: shuffle_deck(deck: list[str]) -> list[str]

   Shuffle a deck of cards.


   .. autolink-examples:: shuffle_deck
      :collapse:

.. py:function:: validate_game_state(game_state: haive.games.hold_em.state.HoldemState) -> list[str]

   Validate game state and return list of issues.


   .. autolink-examples:: validate_game_state
      :collapse:

