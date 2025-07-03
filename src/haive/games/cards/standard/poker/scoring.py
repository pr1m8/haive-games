# haive/packages/haive-games/src/haive/games/card/poker/scoring.py

from collections import Counter
from enum import IntEnum

from haive.games.cards.card.components.scoring import HandEvaluator, HandRank
from haive.games.cards.card.components.standard import StandardCard, StandardRank


class PokerHandType(IntEnum):
    """Poker hand rankings in ascending order."""

    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class PokerHandRank(HandRank[StandardCard]):
    """Detailed poker hand ranking."""

    hand_type: PokerHandType
    hand_cards: list[StandardCard] = []
    kicker_cards: list[StandardCard] = []

    def __str__(self) -> str:
        """Human-readable description of the hand."""
        hand_names = {
            PokerHandType.HIGH_CARD: "High Card",
            PokerHandType.PAIR: "Pair",
            PokerHandType.TWO_PAIR: "Two Pair",
            PokerHandType.THREE_OF_A_KIND: "Three of a Kind",
            PokerHandType.STRAIGHT: "Straight",
            PokerHandType.FLUSH: "Flush",
            PokerHandType.FULL_HOUSE: "Full House",
            PokerHandType.FOUR_OF_A_KIND: "Four of a Kind",
            PokerHandType.STRAIGHT_FLUSH: "Straight Flush",
            PokerHandType.ROYAL_FLUSH: "Royal Flush",
        }

        description = hand_names.get(self.hand_type, "Unknown")

        if self.hand_type == PokerHandType.HIGH_CARD and self.hand_cards:
            description += f" {self.hand_cards[0].rank.value}"
        elif self.hand_type == PokerHandType.PAIR and self.hand_cards:
            description += f" of {self.hand_cards[0].rank.value}s"
        elif self.hand_type == PokerHandType.TWO_PAIR and len(self.hand_cards) >= 4:
            description += f" of {self.hand_cards[0].rank.value}s and {self.hand_cards[2].rank.value}s"
        elif self.hand_type == PokerHandType.THREE_OF_A_KIND and self.hand_cards:
            description += f" of {self.hand_cards[0].rank.value}s"
        elif self.hand_type == PokerHandType.FULL_HOUSE and len(self.hand_cards) >= 5:
            description += f" {self.hand_cards[0].rank.value}s full of {self.hand_cards[3].rank.value}s"
        elif self.hand_type == PokerHandType.FOUR_OF_A_KIND and self.hand_cards:
            description += f" of {self.hand_cards[0].rank.value}s"

        return description


class PokerHandEvaluator(HandEvaluator[StandardCard]):
    """Evaluator for poker hands."""

    @classmethod
    def evaluate(
        cls, cards: list[StandardCard], context: dict | None = None
    ) -> PokerHandRank:
        """Evaluate a poker hand to determine its rank."""
        context = context or {}
        aces_high = context.get("aces_high", True)

        # Need at least 5 cards for a proper poker hand
        if len(cards) < 5:
            # Return high card for hands with fewer than 5 cards
            sorted_cards = sorted(
                cards,
                key=lambda card: (
                    14 if aces_high and card.rank == StandardRank.ACE else card.value
                ),
                reverse=True,
            )
            return PokerHandRank(
                rank_name="Incomplete Hand",
                rank_value=0,
                hand_type=PokerHandType.HIGH_CARD,
                primary_cards=sorted_cards[:1],
                secondary_cards=sorted_cards[1:],
                hand_cards=sorted_cards[:1],
                kicker_cards=sorted_cards[1:],
            )

        # Sort cards by rank for evaluation
        sorted_cards = sorted(
            cards,
            key=lambda card: (
                14 if aces_high and card.rank == StandardRank.ACE else card.value
            ),
            reverse=True,
        )

        # Check for each hand type from highest to lowest
        if result := cls._check_royal_flush(sorted_cards, aces_high):
            return result
        if result := cls._check_straight_flush(sorted_cards, aces_high):
            return result
        if result := cls._check_four_of_a_kind(sorted_cards):
            return result
        if result := cls._check_full_house(sorted_cards):
            return result
        if result := cls._check_flush(sorted_cards):
            return result
        if result := cls._check_straight(sorted_cards, aces_high):
            return result
        if result := cls._check_three_of_a_kind(sorted_cards):
            return result
        if result := cls._check_two_pair(sorted_cards):
            return result
        if result := cls._check_pair(sorted_cards):
            return result

        # Default to high card
        return cls._check_high_card(sorted_cards)

    @classmethod
    def _check_royal_flush(
        cls, cards: list[StandardCard], aces_high: bool
    ) -> PokerHandRank | None:
        """Check for a royal flush (A-K-Q-J-10 of same suit)."""
        # First check if there's a straight flush
        straight_flush = cls._check_straight_flush(cards, aces_high)
        if not straight_flush:
            return None

        # Check if it's A-high
        if aces_high and any(
            c.rank == StandardRank.ACE for c in straight_flush.hand_cards
        ):
            high_card = straight_flush.hand_cards[0]
            if high_card.rank == StandardRank.ACE:
                return PokerHandRank(
                    rank_name="Royal Flush",
                    rank_value=PokerHandType.ROYAL_FLUSH,
                    hand_type=PokerHandType.ROYAL_FLUSH,
                    primary_cards=straight_flush.hand_cards,
                    secondary_cards=[],
                    hand_cards=straight_flush.hand_cards,
                    kicker_cards=[],
                )
        return None

    @classmethod
    def _check_straight_flush(
        cls, cards: list[StandardCard], aces_high: bool
    ) -> PokerHandRank | None:
        """Check for a straight flush."""
        # Group by suit
        by_suit = {}
        for card in cards:
            if card.suit not in by_suit:
                by_suit[card.suit] = []
            by_suit[card.suit].append(card)

        # Check each suit group for a straight
        for _suit, suited_cards in by_suit.items():
            if len(suited_cards) >= 5:
                # Sort cards by rank
                sorted_suited = sorted(
                    suited_cards,
                    key=lambda card: (
                        14
                        if aces_high and card.rank == StandardRank.ACE
                        else card.value
                    ),
                    reverse=True,
                )

                # Check for straight
                straight = cls._find_straight(sorted_suited, aces_high)
                if straight:
                    return PokerHandRank(
                        rank_name="Straight Flush",
                        rank_value=PokerHandType.STRAIGHT_FLUSH,
                        hand_type=PokerHandType.STRAIGHT_FLUSH,
                        primary_cards=straight,
                        secondary_cards=[],
                        hand_cards=straight,
                        kicker_cards=[],
                    )
        return None

    @classmethod
    def _check_four_of_a_kind(cls, cards: list[StandardCard]) -> PokerHandRank | None:
        """Check for four of a kind."""
        # Count cards by rank
        rank_counts = Counter(card.rank for card in cards)

        # Find any rank with 4 cards
        four_kind_rank = None
        for rank, count in rank_counts.items():
            if count >= 4:
                four_kind_rank = rank
                break

        if not four_kind_rank:
            return None

        # Get the four cards and kickers
        four_cards = [card for card in cards if card.rank == four_kind_rank][:4]
        kickers = [card for card in cards if card.rank != four_kind_rank][:1]

        return PokerHandRank(
            rank_name=f"Four of a Kind of {four_kind_rank.value}s",
            rank_value=PokerHandType.FOUR_OF_A_KIND,
            hand_type=PokerHandType.FOUR_OF_A_KIND,
            primary_cards=four_cards,
            secondary_cards=kickers,
            hand_cards=four_cards,
            kicker_cards=kickers,
        )

    @classmethod
    def _check_full_house(cls, cards: list[StandardCard]) -> PokerHandRank | None:
        """Check for a full house (three of a kind + pair)."""
        # Count cards by rank
        rank_counts = Counter(card.rank for card in cards)

        # Find a three of a kind
        three_kind_rank = None
        for rank, count in rank_counts.items():
            if count >= 3:
                three_kind_rank = rank
                break

        if not three_kind_rank:
            return None

        # Find a pair that's different from the three of a kind
        pair_rank = None
        for rank, count in rank_counts.items():
            if rank != three_kind_rank and count >= 2:
                pair_rank = rank
                break

        if not pair_rank:
            return None

        # Get the three cards and the pair
        three_cards = [card for card in cards if card.rank == three_kind_rank][:3]
        pair_cards = [card for card in cards if card.rank == pair_rank][:2]

        return PokerHandRank(
            rank_name=f"Full House {three_kind_rank.value}s full of {pair_rank.value}s",
            rank_value=PokerHandType.FULL_HOUSE,
            hand_type=PokerHandType.FULL_HOUSE,
            primary_cards=three_cards + pair_cards,
            secondary_cards=[],
            hand_cards=three_cards + pair_cards,
            kicker_cards=[],
        )

    @classmethod
    def _check_flush(cls, cards: list[StandardCard]) -> PokerHandRank | None:
        """Check for a flush (5+ cards of same suit)."""
        # Group by suit
        by_suit = {}
        for card in cards:
            if card.suit not in by_suit:
                by_suit[card.suit] = []
            by_suit[card.suit].append(card)

        # Find any suit with 5+ cards
        for suit, suited_cards in by_suit.items():
            if len(suited_cards) >= 5:
                # Sort by rank
                sorted_suited = sorted(
                    suited_cards, key=lambda card: card.value, reverse=True
                )
                flush_cards = sorted_suited[:5]

                return PokerHandRank(
                    rank_name=f"Flush of {suit.value}",
                    rank_value=PokerHandType.FLUSH,
                    hand_type=PokerHandType.FLUSH,
                    primary_cards=flush_cards,
                    secondary_cards=[],
                    hand_cards=flush_cards,
                    kicker_cards=[],
                )
        return None

    @classmethod
    def _find_straight(
        cls, sorted_cards: list[StandardCard], aces_high: bool
    ) -> list[StandardCard] | None:
        """Find a straight in a sorted list of cards."""
        if len(sorted_cards) < 5:
            return None

        # Handle ace-low straight (A-2-3-4-5)
        if aces_high and any(card.rank == StandardRank.ACE for card in sorted_cards):
            # Copy cards and add low ace if needed
            with_low_ace = sorted_cards.copy()
            ace_card = next(
                (card for card in sorted_cards if card.rank == StandardRank.ACE), None
            )
            if ace_card:
                # Count ace as value 1 for low straight
                low_ace = StandardCard(
                    id=ace_card.id,
                    name=ace_card.name,
                    suit=ace_card.suit,
                    rank=ace_card.rank,
                    value=1,  # Low ace value
                    face_up=ace_card.face_up,
                    owner_id=ace_card.owner_id,
                )
                with_low_ace.append(low_ace)

                # Re-sort with low ace
                with_low_ace = sorted(
                    with_low_ace, key=lambda card: card.value, reverse=True
                )
        else:
            with_low_ace = sorted_cards

        # Look for 5 consecutive cards by value
        straight = []
        prev_value = None

        for card in with_low_ace:
            if prev_value is None or card.value == prev_value - 1:
                straight.append(card)
                if len(straight) == 5:
                    return straight
            elif card.value != prev_value:  # Skip duplicates
                straight = [card]
            prev_value = card.value

        return None

    @classmethod
    def _check_straight(
        cls, cards: list[StandardCard], aces_high: bool
    ) -> PokerHandRank | None:
        """Check for a straight (5 consecutive ranked cards)."""
        straight_cards = cls._find_straight(cards, aces_high)

        if straight_cards:
            return PokerHandRank(
                rank_name=f"Straight to {straight_cards[0].rank.value}",
                rank_value=PokerHandType.STRAIGHT,
                hand_type=PokerHandType.STRAIGHT,
                primary_cards=straight_cards,
                secondary_cards=[],
                hand_cards=straight_cards,
                kicker_cards=[],
            )
        return None

    @classmethod
    def _check_three_of_a_kind(cls, cards: list[StandardCard]) -> PokerHandRank | None:
        """Check for three of a kind."""
        # Count cards by rank
        rank_counts = Counter(card.rank for card in cards)

        # Find any rank with 3 cards
        three_kind_rank = None
        for rank, count in rank_counts.items():
            if count >= 3:
                three_kind_rank = rank
                break

        if not three_kind_rank:
            return None

        # Get the three cards and kickers
        three_cards = [card for card in cards if card.rank == three_kind_rank][:3]
        kickers = [card for card in cards if card.rank != three_kind_rank][:2]

        return PokerHandRank(
            rank_name=f"Three of a Kind of {three_kind_rank.value}s",
            rank_value=PokerHandType.THREE_OF_A_KIND,
            hand_type=PokerHandType.THREE_OF_A_KIND,
            primary_cards=three_cards,
            secondary_cards=kickers,
            hand_cards=three_cards,
            kicker_cards=kickers,
        )

    @classmethod
    def _check_two_pair(cls, cards: list[StandardCard]) -> PokerHandRank | None:
        """Check for two pair."""
        # Count cards by rank
        rank_counts = Counter(card.rank for card in cards)

        # Find ranks with pairs
        pair_ranks = [rank for rank, count in rank_counts.items() if count >= 2]

        if len(pair_ranks) < 2:
            return None

        # Sort pairs by rank
        pair_ranks.sort(key=lambda r: r.value, reverse=True)
        pair_ranks = pair_ranks[:2]  # Take highest two pairs

        # Get the pair cards and kickers
        first_pair = [card for card in cards if card.rank == pair_ranks[0]][:2]
        second_pair = [card for card in cards if card.rank == pair_ranks[1]][:2]
        kickers = [card for card in cards if card.rank not in pair_ranks][:1]

        return PokerHandRank(
            rank_name=f"Two Pair {pair_ranks[0].value}s and {pair_ranks[1].value}s",
            rank_value=PokerHandType.TWO_PAIR,
            hand_type=PokerHandType.TWO_PAIR,
            primary_cards=first_pair + second_pair,
            secondary_cards=kickers,
            hand_cards=first_pair + second_pair,
            kicker_cards=kickers,
        )

    @classmethod
    def _check_pair(cls, cards: list[StandardCard]) -> PokerHandRank | None:
        """Check for a pair."""
        # Count cards by rank
        rank_counts = Counter(card.rank for card in cards)

        # Find any rank with 2 cards
        pair_rank = None
        for rank, count in rank_counts.items():
            if count >= 2:
                pair_rank = rank
                break

        if not pair_rank:
            return None

        # Get the pair cards and kickers
        pair_cards = [card for card in cards if card.rank == pair_rank][:2]
        kickers = [card for card in cards if card.rank != pair_rank][:3]

        return PokerHandRank(
            rank_name=f"Pair of {pair_rank.value}s",
            rank_value=PokerHandType.PAIR,
            hand_type=PokerHandType.PAIR,
            primary_cards=pair_cards,
            secondary_cards=kickers,
            hand_cards=pair_cards,
            kicker_cards=kickers,
        )

    @classmethod
    def _check_high_card(cls, cards: list[StandardCard]) -> PokerHandRank:
        """Return high card evaluation."""
        high_card = [cards[0]]
        kickers = cards[1:5]

        return PokerHandRank(
            rank_name=f"High Card {cards[0].rank.value}",
            rank_value=PokerHandType.HIGH_CARD,
            hand_type=PokerHandType.HIGH_CARD,
            primary_cards=high_card,
            secondary_cards=kickers,
            hand_cards=high_card,
            kicker_cards=kickers,
        )
