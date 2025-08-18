games.hold_em.utils
===================

.. py:module:: games.hold_em.utils

Texas Hold'em utility functions.

This module provides utility functions for the Hold'em game, including:
    - Card and hand evaluation
    - Game state utilities
    - Poker calculations



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">17 functions</span>   </div>

.. autoapi-nested-parse::

   Texas Hold'em utility functions.

   This module provides utility functions for the Hold'em game, including:
       - Card and hand evaluation
       - Game state utilities
       - Poker calculations



      
            
            
            

.. admonition:: Functions (17)
   :class: info

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

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: calculate_effective_stack(player: haive.games.hold_em.state.PlayerState, opponent: haive.games.hold_em.state.PlayerState) -> int

            Calculate effective stack between two players.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: calculate_pot_odds(pot_size: int, bet_to_call: int) -> float

            Calculate pot odds as a ratio.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: card_to_rank_value(card: str) -> int

            Convert card rank to numeric value for comparison.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: card_to_suit(card: str) -> str

            Extract suit from card.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: count_players_in_phase(game_state: haive.games.hold_em.state.HoldemState, statuses: list[haive.games.hold_em.state.PlayerStatus]) -> int

            Count players with specific statuses.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_standard_deck() -> list[str]

            Create a standard 52-card deck.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: deal_cards(deck: list[str], num_cards: int) -> tuple[list[str], list[str]]

            Deal cards from deck, returning (dealt_cards, remaining_deck).



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: evaluate_hand_simple(hole_cards: list[str], community_cards: list[str]) -> dict[str, any]

            Simple hand evaluation (placeholder for production poker evaluator).

            Returns hand rank, strength score, and description.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: format_cards(cards: list[str]) -> str

            Format cards for display with suit symbols.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: format_game_summary(game_state: haive.games.hold_em.state.HoldemState) -> str

            Format a summary of the current game state.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_board_texture_description(community_cards: list[str]) -> str

            Describe the board texture.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_next_active_player(game_state: haive.games.hold_em.state.HoldemState, start_position: int) -> int | None

            Get the next active player starting from a position.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_position_name(position: int, num_players: int, dealer_pos: int) -> str

            Get position name based on seat and dealer position.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: is_position_early(position: int, num_players: int, dealer_pos: int) -> bool

            Check if position is early.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: is_position_late(position: int, num_players: int, dealer_pos: int) -> bool

            Check if position is late.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: shuffle_deck(deck: list[str]) -> list[str]

            Shuffle a deck of cards.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: validate_game_state(game_state: haive.games.hold_em.state.HoldemState) -> list[str]

            Validate game state and return list of issues.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.utils import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

