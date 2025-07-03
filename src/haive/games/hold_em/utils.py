"""Texas Hold'em utility functions.

This module provides utility functions for the Hold'em game, including:
    - Card and hand evaluation
    - Game state utilities
    - Poker calculations
"""

import random

from haive.games.hold_em.models import HandRank
from haive.games.hold_em.state import HoldemState, PlayerState, PlayerStatus


def create_standard_deck() -> list[str]:
    """Create a standard 52-card deck."""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suits = ["h", "d", "c", "s"]  # hearts, diamonds, clubs, spades
    return [f"{rank}{suit}" for rank in ranks for suit in suits]


def shuffle_deck(deck: list[str]) -> list[str]:
    """Shuffle a deck of cards."""
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled


def deal_cards(deck: list[str], num_cards: int) -> tuple[list[str], list[str]]:
    """Deal cards from deck, returning (dealt_cards, remaining_deck)."""
    if len(deck) < num_cards:
        raise ValueError(
            f"Not enough cards in deck. Need {num_cards}, have {len(deck)}"
        )

    dealt = deck[:num_cards]
    remaining = deck[num_cards:]
    return dealt, remaining


def card_to_rank_value(card: str) -> int:
    """Convert card rank to numeric value for comparison."""
    rank = card[0]
    rank_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    return rank_values.get(rank, 0)


def card_to_suit(card: str) -> str:
    """Extract suit from card."""
    return card[1] if len(card) >= 2 else ""


def format_cards(cards: list[str]) -> str:
    """Format cards for display with suit symbols."""
    suit_symbols = {"h": "♥", "d": "♦", "c": "♣", "s": "♠"}

    formatted = []
    for card in cards:
        if len(card) >= 2:
            rank = card[0]
            suit = suit_symbols.get(card[1], card[1])
            formatted.append(f"{rank}{suit}")
        else:
            formatted.append(card)

    return " ".join(formatted)


def evaluate_hand_simple(
    hole_cards: list[str], community_cards: list[str]
) -> dict[str, any]:
    """Simple hand evaluation (placeholder for production poker evaluator).
    Returns hand rank, strength score, and description.
    """
    all_cards = hole_cards + community_cards
    if len(all_cards) < 5:
        return {
            "rank": HandRank.HIGH_CARD,
            "strength": 0.1,
            "description": "Insufficient cards",
            "made_hand": [],
            "kickers": [],
        }

    # Get ranks and suits
    ranks = [card[0] for card in all_cards]
    suits = [card[1] for card in all_cards]

    # Count ranks and suits
    rank_counts = {}
    suit_counts = {}

    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    for suit in suits:
        suit_counts[suit] = suit_counts.get(suit, 0) + 1

    # Sort ranks by count and value
    sorted_ranks = sorted(
        rank_counts.items(),
        key=lambda x: (x[1], card_to_rank_value(x[0])),
        reverse=True,
    )

    # Check for flush
    has_flush = max(suit_counts.values()) >= 5
    flush_suit = None
    if has_flush:
        flush_suit = max(suit_counts.items(), key=lambda x: x[1])[0]

    # Check for straight
    rank_values = sorted(
        [card_to_rank_value(rank) for rank in set(ranks)], reverse=True
    )
    has_straight = False
    straight_high = 0

    # Check for regular straight
    for i in range(len(rank_values) - 4):
        if rank_values[i] - rank_values[i + 4] == 4:
            has_straight = True
            straight_high = rank_values[i]
            break

    # Check for A-2-3-4-5 straight (wheel)
    if not has_straight and set([14, 2, 3, 4, 5]).issubset(set(rank_values)):
        has_straight = True
        straight_high = 5  # 5-high straight

    # Determine hand rank
    counts = [count for rank, count in sorted_ranks]

    if has_straight and has_flush:
        if straight_high == 14:  # A-K-Q-J-T
            return {
                "rank": HandRank.ROYAL_FLUSH,
                "strength": 1.0,
                "description": "Royal Flush",
                "made_hand": all_cards[:5],
                "kickers": [],
            }
        return {
            "rank": HandRank.STRAIGHT_FLUSH,
            "strength": 0.95,
            "description": f"Straight Flush, {straight_high} high",
            "made_hand": all_cards[:5],
            "kickers": [],
        }

    if counts[0] == 4:
        return {
            "rank": HandRank.FOUR_OF_A_KIND,
            "strength": 0.9,
            "description": f"Four of a Kind, {sorted_ranks[0][0]}s",
            "made_hand": [card for card in all_cards if card[0] == sorted_ranks[0][0]],
            "kickers": [sorted_ranks[1][0]],
        }

    if counts[0] == 3 and counts[1] == 2:
        return {
            "rank": HandRank.FULL_HOUSE,
            "strength": 0.85,
            "description": f"Full House, {sorted_ranks[0][0]}s over {sorted_ranks[1][0]}s",
            "made_hand": all_cards[:5],
            "kickers": [],
        }

    if has_flush:
        return {
            "rank": HandRank.FLUSH,
            "strength": 0.75,
            "description": f"Flush, {flush_suit}",
            "made_hand": [card for card in all_cards if card[1] == flush_suit][:5],
            "kickers": [],
        }

    if has_straight:
        return {
            "rank": HandRank.STRAIGHT,
            "strength": 0.65,
            "description": f"Straight, {straight_high} high",
            "made_hand": all_cards[:5],
            "kickers": [],
        }

    if counts[0] == 3:
        return {
            "rank": HandRank.THREE_OF_A_KIND,
            "strength": 0.55,
            "description": f"Three of a Kind, {sorted_ranks[0][0]}s",
            "made_hand": [card for card in all_cards if card[0] == sorted_ranks[0][0]],
            "kickers": [rank for rank, count in sorted_ranks[1:3]],
        }

    if counts[0] == 2 and counts[1] == 2:
        return {
            "rank": HandRank.TWO_PAIR,
            "strength": 0.35,
            "description": f"Two Pair, {sorted_ranks[0][0]}s and {sorted_ranks[1][0]}s",
            "made_hand": [
                card
                for card in all_cards
                if card[0] in [sorted_ranks[0][0], sorted_ranks[1][0]]
            ],
            "kickers": [sorted_ranks[2][0]],
        }

    if counts[0] == 2:
        return {
            "rank": HandRank.PAIR,
            "strength": 0.25,
            "description": f"Pair of {sorted_ranks[0][0]}s",
            "made_hand": [card for card in all_cards if card[0] == sorted_ranks[0][0]],
            "kickers": [rank for rank, count in sorted_ranks[1:4]],
        }

    high_card = sorted_ranks[0][0]
    return {
        "rank": HandRank.HIGH_CARD,
        "strength": 0.1 + (card_to_rank_value(high_card) / 100),
        "description": f"High Card, {high_card}",
        "made_hand": [card for card in all_cards if card[0] == high_card][:1],
        "kickers": [rank for rank, count in sorted_ranks[1:5]],
    }


def calculate_pot_odds(pot_size: int, bet_to_call: int) -> float:
    """Calculate pot odds as a ratio."""
    if bet_to_call <= 0:
        return 0.0
    total_pot = pot_size + bet_to_call
    return bet_to_call / total_pot if total_pot > 0 else 0.0


def calculate_effective_stack(player: PlayerState, opponent: PlayerState) -> int:
    """Calculate effective stack between two players."""
    return min(player.chips, opponent.chips)


def get_position_name(position: int, num_players: int, dealer_pos: int) -> str:
    """Get position name based on seat and dealer position."""
    if num_players == 2:
        return "Dealer" if position == dealer_pos else "Big Blind"

    relative_pos = (position - dealer_pos) % num_players

    if relative_pos == 0:
        return "Dealer"
    if relative_pos == 1:
        return "Small Blind"
    if relative_pos == 2:
        return "Big Blind"
    if relative_pos == 3:
        return "Under the Gun"
    if relative_pos == num_players - 1:
        return "Cutoff"
    if relative_pos == num_players - 2:
        return "Hijack"
    return f"Middle Position {relative_pos - 2}"


def is_position_early(position: int, num_players: int, dealer_pos: int) -> bool:
    """Check if position is early."""
    relative_pos = (position - dealer_pos) % num_players
    return relative_pos <= 3 and num_players > 3


def is_position_late(position: int, num_players: int, dealer_pos: int) -> bool:
    """Check if position is late."""
    relative_pos = (position - dealer_pos) % num_players
    return relative_pos >= num_players - 2


def get_next_active_player(game_state: HoldemState, start_position: int) -> int | None:
    """Get the next active player starting from a position."""
    for i in range(len(game_state.players)):
        next_pos = (start_position + i) % len(game_state.players)
        player = game_state.players[next_pos]
        if player.status == PlayerStatus.ACTIVE:
            return next_pos
    return None


def count_players_in_phase(
    game_state: HoldemState, statuses: list[PlayerStatus]
) -> int:
    """Count players with specific statuses."""
    return len([p for p in game_state.players if p.status in statuses])


def get_board_texture_description(community_cards: list[str]) -> str:
    """Describe the board texture."""
    if len(community_cards) < 3:
        return "Preflop"

    # Get suits and ranks
    suits = [card[1] for card in community_cards]
    ranks = [card[0] for card in community_cards]
    rank_values = [card_to_rank_value(card) for card in community_cards]

    descriptions = []

    # Check for flush draws
    suit_counts = {}
    for suit in suits:
        suit_counts[suit] = suit_counts.get(suit, 0) + 1

    max_suit_count = max(suit_counts.values()) if suit_counts else 0
    if max_suit_count >= 3:
        descriptions.append("flush draw possible")

    # Check for straight draws
    sorted_values = sorted(set(rank_values))
    gaps = []
    for i in range(len(sorted_values) - 1):
        gaps.append(sorted_values[i + 1] - sorted_values[i])

    if any(gap == 1 for gap in gaps):
        descriptions.append("straight draw possible")

    # Check for pairs
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    pairs = [rank for rank, count in rank_counts.items() if count >= 2]
    if pairs:
        descriptions.append(f"paired board ({pairs[0]})")

    # Board wetness
    if len(descriptions) >= 2:
        texture = "wet"
    elif len(descriptions) == 1:
        texture = "semi-wet"
    else:
        texture = "dry"

    base_description = f"{texture} board"
    if descriptions:
        base_description += f" ({', '.join(descriptions)})"

    return base_description


def format_game_summary(game_state: HoldemState) -> str:
    """Format a summary of the current game state."""
    summary = (
        f"Hand #{game_state.hand_number} - {game_state.current_phase.value.title()}\n"
    )
    summary += f"Pot: {game_state.total_pot} chips\n"

    if game_state.community_cards:
        summary += f"Board: {format_cards(game_state.community_cards)}\n"

    summary += f"Players in hand: {len(game_state.players_in_hand)}\n"

    active_players = [p for p in game_state.players if p.status == PlayerStatus.ACTIVE]
    summary += f"Active players: {len(active_players)}\n"

    if game_state.current_player:
        summary += f"Current player: {game_state.current_player.name}\n"

    return summary


def validate_game_state(game_state: HoldemState) -> list[str]:
    """Validate game state and return list of issues."""
    issues = []

    # Check player count
    if len(game_state.players) < 2:
        issues.append("Need at least 2 players")

    # Check chip counts
    total_chips = sum(p.chips + p.total_bet for p in game_state.players)
    if total_chips <= 0:
        issues.append("No chips in play")

    # Check deck size
    expected_deck_size = (
        52 - len(game_state.community_cards) - len(game_state.burned_cards)
    )
    for player in game_state.players:
        expected_deck_size -= len(player.hole_cards)

    if len(game_state.deck) != expected_deck_size:
        issues.append(
            f"Deck size mismatch: expected {expected_deck_size}, got {len(game_state.deck)}"
        )

    # Check betting consistency
    if game_state.current_bet < 0:
        issues.append("Current bet cannot be negative")

    for player in game_state.players:
        if player.current_bet < 0:
            issues.append(f"Player {player.name} has negative current bet")
        if player.chips < 0:
            issues.append(f"Player {player.name} has negative chips")

    return issues
