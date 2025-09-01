games.hold_em.utils
===================

.. py:module:: games.hold_em.utils

.. autoapi-nested-parse::

   Texas Hold'em utility functions.

   This module provides utility functions for the Hold'em game, including:
       - Card and hand evaluation
       - Game state utilities
       - Poker calculations



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


.. py:function:: calculate_pot_odds(pot_size: int, bet_to_call: int) -> float

   Calculate pot odds as a ratio.


.. py:function:: card_to_rank_value(card: str) -> int

   Convert card rank to numeric value for comparison.


.. py:function:: card_to_suit(card: str) -> str

   Extract suit from card.


.. py:function:: count_players_in_phase(game_state: haive.games.hold_em.state.HoldemState, statuses: list[haive.games.hold_em.state.PlayerStatus]) -> int

   Count players with specific statuses.


.. py:function:: create_standard_deck() -> list[str]

   Create a standard 52-card deck.


.. py:function:: deal_cards(deck: list[str], num_cards: int) -> tuple[list[str], list[str]]

   Deal cards from deck, returning (dealt_cards, remaining_deck).


.. py:function:: evaluate_hand_simple(hole_cards: list[str], community_cards: list[str]) -> dict[str, any]

   Simple hand evaluation (placeholder for production poker evaluator).

   Returns hand rank, strength score, and description.



.. py:function:: format_cards(cards: list[str]) -> str

   Format cards for display with suit symbols.


.. py:function:: format_game_summary(game_state: haive.games.hold_em.state.HoldemState) -> str

   Format a summary of the current game state.


.. py:function:: get_board_texture_description(community_cards: list[str]) -> str

   Describe the board texture.


.. py:function:: get_next_active_player(game_state: haive.games.hold_em.state.HoldemState, start_position: int) -> int | None

   Get the next active player starting from a position.


.. py:function:: get_position_name(position: int, num_players: int, dealer_pos: int) -> str

   Get position name based on seat and dealer position.


.. py:function:: is_position_early(position: int, num_players: int, dealer_pos: int) -> bool

   Check if position is early.


.. py:function:: is_position_late(position: int, num_players: int, dealer_pos: int) -> bool

   Check if position is late.


.. py:function:: shuffle_deck(deck: list[str]) -> list[str]

   Shuffle a deck of cards.


.. py:function:: validate_game_state(game_state: haive.games.hold_em.state.HoldemState) -> list[str]

   Validate game state and return list of issues.


