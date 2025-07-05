"""Test cases for Risk game state manager.

This module tests the RiskStateManager class and its methods for managing
game state transitions, rule enforcement, and move validation.
"""

import pytest

from haive.games.risk.config import RiskConfig
from haive.games.risk.models import (
    Card,
    CardType,
    GameStatus,
    MoveType,
    PhaseType,
    RiskMove,
)
from haive.games.risk.state_manager import RiskStateManager


class TestRiskStateManagerInitialization:
    """Test cases for RiskStateManager initialization."""

    def test_initialization_valid_players(self) -> None:
        """Test initializing state manager with valid players."""
        player_names = ["Alice", "Bob", "Charlie"]
        manager = RiskStateManager.initialize(player_names)

        assert len(manager.state.players) == 3
        assert manager.state.current_player == "Alice"
        assert manager.config is not None
        assert manager.move_history == []

    def test_initialization_with_custom_config(self) -> None:
        """Test initializing state manager with custom config."""
        player_names = ["Alice", "Bob"]
        config = RiskConfig.modern()
        manager = RiskStateManager.initialize(player_names, config)

        assert manager.config == config
        assert manager.config.use_mission_cards is True

    def test_initialization_invalid_players(self) -> None:
        """Test that initialization fails with invalid player count."""
        with pytest.raises(ValueError, match="Risk requires 2-6 players"):
            RiskStateManager.initialize(["Alice"])

        with pytest.raises(ValueError, match="Risk requires 2-6 players"):
            RiskStateManager.initialize(
                ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
            )


class TestMoveValidation:
    """Test cases for move validation."""

    @pytest.fixture
    def manager(self) -> RiskStateManager:
        """Create a basic state manager for testing."""
        player_names = ["Alice", "Bob", "Charlie"]
        manager = RiskStateManager.initialize(player_names)

        # Set up some basic territory ownership
        manager.state.territories["Alaska"].owner = "Alice"
        manager.state.territories["Alaska"].armies = 5
        manager.state.territories["Alberta"].owner = "Bob"
        manager.state.territories["Alberta"].armies = 3
        manager.state.territories["Quebec"].owner = "Alice"
        manager.state.territories["Quebec"].armies = 2

        return manager

    def test_validate_move_wrong_player(self, manager: RiskStateManager) -> None:
        """Test validation fails when it's not the player's turn."""
        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Bob",  # Not current player
            to_territory="Alberta",
            armies=1,
        )

        with pytest.raises(ValueError, match="Not Bob's turn"):
            manager._validate_move(move)

    def test_validate_move_eliminated_player(self, manager: RiskStateManager) -> None:
        """Test validation fails for eliminated player."""
        manager.state.players["Alice"].eliminated = True

        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="Alaska",
            armies=1,
        )

        with pytest.raises(ValueError, match="Player Alice is eliminated"):
            manager._validate_move(move)

    def test_validate_place_armies_valid(self, manager: RiskStateManager) -> None:
        """Test valid place armies move validation."""
        manager.state.players["Alice"].unplaced_armies = 5

        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="Alaska",
            armies=3,
        )

        # Should not raise an exception
        manager._validate_move(move)

    def test_validate_place_armies_no_territory(
        self, manager: RiskStateManager
    ) -> None:
        """Test place armies validation fails without territory."""
        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            armies=1,
        )

        with pytest.raises(
            ValueError, match="Territory to place armies on not specified"
        ):
            manager._validate_move(move)

    def test_validate_place_armies_invalid_territory(
        self, manager: RiskStateManager
    ) -> None:
        """Test place armies validation fails with invalid territory."""
        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="InvalidTerritory",
            armies=1,
        )

        with pytest.raises(
            ValueError, match="Territory InvalidTerritory does not exist"
        ):
            manager._validate_move(move)

    def test_validate_place_armies_not_owned(self, manager: RiskStateManager) -> None:
        """Test place armies validation fails if player doesn't own territory."""
        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="Alberta",  # Owned by Bob
            armies=1,
        )

        with pytest.raises(ValueError, match="Player Alice does not control Alberta"):
            manager._validate_move(move)

    def test_validate_place_armies_insufficient_armies(
        self, manager: RiskStateManager
    ) -> None:
        """Test place armies validation fails with insufficient armies."""
        manager.state.players["Alice"].unplaced_armies = 1

        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="Alaska",
            armies=3,  # More than available
        )

        with pytest.raises(ValueError, match="only has 1 unplaced armies"):
            manager._validate_move(move)

    def test_validate_attack_valid(self, manager: RiskStateManager) -> None:
        """Test valid attack move validation."""
        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Alice",
            from_territory="Alaska",
            to_territory="Alberta",
            attack_dice=2,
        )

        # Should not raise an exception
        manager._validate_move(move)

    def test_validate_attack_same_territory(self, manager: RiskStateManager) -> None:
        """Test attack validation fails when attacking own territory."""
        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Alice",
            from_territory="Alaska",
            to_territory="Quebec",  # Also owned by Alice
            attack_dice=1,
        )

        with pytest.raises(ValueError, match="Cannot attack your own territory"):
            manager._validate_move(move)

    def test_validate_attack_not_adjacent(self, manager: RiskStateManager) -> None:
        """Test attack validation fails when territories not adjacent."""
        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Alice",
            from_territory="Alaska",
            to_territory="Brazil",  # Not adjacent to Alaska
            attack_dice=1,
        )

        with pytest.raises(ValueError, match="Brazil is not adjacent to Alaska"):
            manager._validate_move(move)

    def test_validate_attack_insufficient_armies(
        self, manager: RiskStateManager
    ) -> None:
        """Test attack validation fails with insufficient armies."""
        manager.state.territories["Alaska"].armies = 1  # Need at least 2 to attack

        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Alice",
            from_territory="Alaska",
            to_territory="Alberta",
            attack_dice=1,
        )

        with pytest.raises(
            ValueError, match="Need at least 2 armies in Alaska to attack"
        ):
            manager._validate_move(move)

    def test_validate_attack_too_many_dice(self, manager: RiskStateManager) -> None:
        """Test attack validation fails with too many dice."""
        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Alice",
            from_territory="Alaska",  # Has 5 armies, can attack with max 3 dice
            to_territory="Alberta",
            attack_dice=4,  # Too many
        )

        with pytest.raises(ValueError, match="Cannot attack with 4 dice"):
            manager._validate_move(move)

    def test_validate_fortify_valid(self, manager: RiskStateManager) -> None:
        """Test valid fortify move validation."""
        # Quebec is adjacent to Ontario, and Alice should own both
        manager.state.territories["Ontario"].owner = "Alice"
        manager.state.territories["Ontario"].armies = 1

        move = RiskMove(
            move_type=MoveType.FORTIFY,
            player="Alice",
            from_territory="Quebec",
            to_territory="Ontario",
            armies=1,
        )

        # Should not raise an exception
        manager._validate_move(move)

    def test_validate_fortify_empty_move(self, manager: RiskStateManager) -> None:
        """Test empty fortify move (end turn) validation."""
        move = RiskMove(
            move_type=MoveType.FORTIFY,
            player="Alice",
        )

        # Should not raise an exception
        manager._validate_move(move)

    def test_validate_trade_cards_valid(self, manager: RiskStateManager) -> None:
        """Test valid trade cards move validation."""
        cards = [
            Card(card_type=CardType.INFANTRY),
            Card(card_type=CardType.CAVALRY),
            Card(card_type=CardType.ARTILLERY),
        ]
        manager.state.players["Alice"].cards = cards

        move = RiskMove(
            move_type=MoveType.TRADE_CARDS,
            player="Alice",
            cards=cards,
        )

        # Should not raise an exception
        manager._validate_move(move)

    def test_validate_trade_cards_wrong_count(self, manager: RiskStateManager) -> None:
        """Test trade cards validation fails with wrong card count."""
        cards = [Card(card_type=CardType.INFANTRY)]

        move = RiskMove(
            move_type=MoveType.TRADE_CARDS,
            player="Alice",
            cards=cards,
        )

        with pytest.raises(ValueError, match="Must trade exactly 3 cards"):
            manager._validate_move(move)

    def test_validate_trade_cards_player_doesnt_have(
        self, manager: RiskStateManager
    ) -> None:
        """Test trade cards validation fails when player doesn't have cards."""
        cards = [
            Card(card_type=CardType.INFANTRY),
            Card(card_type=CardType.CAVALRY),
            Card(card_type=CardType.ARTILLERY),
        ]
        # Don't give cards to Alice

        move = RiskMove(
            move_type=MoveType.TRADE_CARDS,
            player="Alice",
            cards=cards,
        )

        with pytest.raises(ValueError, match="Player Alice does not have"):
            manager._validate_move(move)

    def test_validate_trade_cards_invalid_set(self, manager: RiskStateManager) -> None:
        """Test trade cards validation fails with invalid card set."""
        cards = [
            Card(card_type=CardType.INFANTRY),
            Card(card_type=CardType.INFANTRY),
            Card(card_type=CardType.CAVALRY),
        ]
        manager.state.players["Alice"].cards = cards

        move = RiskMove(
            move_type=MoveType.TRADE_CARDS,
            player="Alice",
            cards=cards,
        )

        with pytest.raises(ValueError, match="Invalid card set"):
            manager._validate_move(move)


class TestMoveApplication:
    """Test cases for applying moves to game state."""

    @pytest.fixture
    def manager(self) -> RiskStateManager:
        """Create a basic state manager for testing."""
        player_names = ["Alice", "Bob", "Charlie"]
        manager = RiskStateManager.initialize(player_names)

        # Set up basic territory ownership
        manager.state.territories["Alaska"].owner = "Alice"
        manager.state.territories["Alaska"].armies = 5
        manager.state.territories["Alberta"].owner = "Bob"
        manager.state.territories["Alberta"].armies = 3
        manager.state.players["Alice"].unplaced_armies = 10

        return manager

    def test_apply_place_armies(self, manager: RiskStateManager) -> None:
        """Test applying place armies move."""
        initial_armies = manager.state.territories["Alaska"].armies
        initial_unplaced = manager.state.players["Alice"].unplaced_armies

        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="Alaska",
            armies=3,
        )

        manager.apply_move(move)

        assert manager.state.territories["Alaska"].armies == initial_armies + 3
        assert manager.state.players["Alice"].unplaced_armies == initial_unplaced - 3
        assert move in manager.move_history

    def test_apply_attack_attacker_wins(self, manager: RiskStateManager) -> None:
        """Test applying attack move where attacker wins."""
        # Set up a scenario where attacker is likely to win
        manager.state.territories["Alaska"].armies = 10
        manager.state.territories["Alberta"].armies = 1

        move = RiskMove(
            move_type=MoveType.ATTACK,
            player="Alice",
            from_territory="Alaska",
            to_territory="Alberta",
            attack_dice=3,
        )

        # Apply the move multiple times until attacker wins (or limit reached)
        attempts = 0
        while manager.state.territories["Alberta"].owner != "Alice" and attempts < 20:
            manager.apply_move(move)
            attempts += 1

        # Eventually Alice should capture Alberta
        if manager.state.territories["Alberta"].owner == "Alice":
            assert manager.state.territories["Alberta"].armies >= 1
            assert manager.state.attacker_captured_territory is True

    def test_apply_fortify(self, manager: RiskStateManager) -> None:
        """Test applying fortify move."""
        # Set up territories for fortification
        manager.state.territories["Quebec"].owner = "Alice"
        manager.state.territories["Quebec"].armies = 5
        manager.state.territories["Ontario"].owner = "Alice"
        manager.state.territories["Ontario"].armies = 2

        move = RiskMove(
            move_type=MoveType.FORTIFY,
            player="Alice",
            from_territory="Quebec",
            to_territory="Ontario",
            armies=3,
        )

        manager.apply_move(move)

        assert manager.state.territories["Quebec"].armies == 2
        assert manager.state.territories["Ontario"].armies == 5

    def test_apply_trade_cards(self, manager: RiskStateManager) -> None:
        """Test applying trade cards move."""
        cards = [
            Card(card_type=CardType.INFANTRY),
            Card(card_type=CardType.CAVALRY),
            Card(card_type=CardType.ARTILLERY),
        ]
        manager.state.players["Alice"].cards = cards.copy()
        initial_unplaced = manager.state.players["Alice"].unplaced_armies

        move = RiskMove(
            move_type=MoveType.TRADE_CARDS,
            player="Alice",
            cards=cards,
        )

        manager.apply_move(move)

        # Player should get armies (first set is worth 4)
        assert manager.state.players["Alice"].unplaced_armies == initial_unplaced + 4
        # Cards should be removed from player's hand
        assert len(manager.state.players["Alice"].cards) == 0
        # Cards should be added back to deck
        assert len(manager.state.deck) > 42  # Original deck size

    def test_game_over_detection(self, manager: RiskStateManager) -> None:
        """Test that game over is detected when only one player remains."""
        # Eliminate all players except Alice
        manager.state.players["Bob"].eliminated = True
        manager.state.players["Charlie"].eliminated = True

        move = RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player="Alice",
            to_territory="Alaska",
            armies=1,
        )

        manager.apply_move(move)

        assert manager.state.game_status == GameStatus.FINISHED
        assert manager.state.phase == PhaseType.GAME_OVER
