"""State manager for the Risk game.

This module defines the RiskStateManager class that manages game state
transitions, rule enforcement, and game progression.
"""

import random

from pydantic import BaseModel, Field

from haive.games.risk.config import RiskConfig
from haive.games.risk.models import CardType, GameStatus, MoveType, PhaseType, RiskMove
from haive.games.risk.state import RiskState


class RiskStateManager(BaseModel):
    """Manages state transitions and rule enforcement for the Risk game.

    This class is responsible for applying moves to the game state,
    enforcing game rules, and managing game progression through different phases.

    Attributes:
        state: The current game state.
        config: Configuration settings for the game.
        move_history: History of all moves made in the game.
    """

    state: RiskState
    config: RiskConfig = Field(default_factory=RiskConfig.classic)
    move_history: list[RiskMove] = Field(default_factory=list)

    @classmethod
    def initialize(
        cls, player_names: list[str], config: RiskConfig | None = None
    ) -> "RiskStateManager":
        """Initialize a new Risk game state manager.

        Args:
            player_names: List of player names.
            config: Optional configuration for the game.
                If not provided, classic Risk rules will be used.

        Returns:
            A new RiskStateManager with initialized state.

        Raises:
            ValueError: If the number of players is invalid.
        """
        # Use default config if none provided
        if config is None:
            config = RiskConfig.classic()

        # Validate player count
        if len(player_names) < 2 or len(player_names) > 6:
            raise ValueError("Risk requires 2-6 players")

        # Initialize state
        state = RiskState.initialize(player_names)

        return cls(state=state, config=config)

    def apply_move(self, move: RiskMove) -> RiskState:
        """Apply a move to the current game state.

        Args:
            move: The move to apply.

        Returns:
            The updated game state after applying the move.

        Raises:
            ValueError: If the move is invalid or violates game rules.
        """
        # Validate move
        self._validate_move(move)

        # Apply the move based on its type
        if move.move_type == MoveType.PLACE_ARMIES:
            self._apply_place_armies(move)
        elif move.move_type == MoveType.ATTACK:
            self._apply_attack(move)
        elif move.move_type == MoveType.FORTIFY:
            self._apply_fortify(move)
        elif move.move_type == MoveType.TRADE_CARDS:
            self._apply_trade_cards(move)

        # Add move to history
        self.move_history.append(move)

        # Check if game is over
        self._check_game_over()

        return self.state

    def _validate_move(self, move: RiskMove) -> None:
        """Validate that a move is legal according to the game rules.

        Args:
            move: The move to validate.

        Raises:
            ValueError: If the move is invalid.
        """
        # Check if it's the player's turn
        if move.player != self.state.current_player:
            raise ValueError(f"Not {move.player}'s turn")

        # Check if player is eliminated
        if self.state.players[move.player].eliminated:
            raise ValueError(f"Player {move.player} is eliminated")

        # Validate based on move type
        if move.move_type == MoveType.PLACE_ARMIES:
            self._validate_place_armies(move)
        elif move.move_type == MoveType.ATTACK:
            self._validate_attack(move)
        elif move.move_type == MoveType.FORTIFY:
            self._validate_fortify(move)
        elif move.move_type == MoveType.TRADE_CARDS:
            self._validate_trade_cards(move)

    def _validate_place_armies(self, move: RiskMove) -> None:
        """Validate a place armies move.

        Args:
            move: The move to validate.

        Raises:
            ValueError: If the move is invalid.
        """
        # Check if to_territory is specified
        if not move.to_territory:
            raise ValueError("Territory to place armies on not specified")

        # Check if territory exists
        if move.to_territory not in self.state.territories:
            raise ValueError(f"Territory {move.to_territory} does not exist")

        # Check if player controls the territory
        if self.state.territories[move.to_territory].owner != move.player:
            raise ValueError(
                f"Player {move.player} does not control {move.to_territory}"
            )

        # Check if player has enough unplaced armies
        if move.armies is None or move.armies <= 0:
            raise ValueError("Must place at least 1 army")

        if self.state.players[move.player].unplaced_armies < move.armies:
            raise ValueError(
                f"Player {move.player} only has {self.state.players[move.player].unplaced_armies} unplaced armies"
            )

    def _validate_attack(self, move: RiskMove) -> None:
        """Validate an attack move.

        Args:
            move: The move to validate.

        Raises:
            ValueError: If the move is invalid.
        """
        # Check if from_territory and to_territory are specified
        if not move.from_territory:
            raise ValueError("Territory to attack from not specified")

        if not move.to_territory:
            raise ValueError("Territory to attack not specified")

        # Check if territories exist
        if move.from_territory not in self.state.territories:
            raise ValueError(f"Territory {move.from_territory} does not exist")

        if move.to_territory not in self.state.territories:
            raise ValueError(f"Territory {move.to_territory} does not exist")

        # Check if player controls the from_territory
        if self.state.territories[move.from_territory].owner != move.player:
            raise ValueError(
                f"Player {move.player} does not control {move.from_territory}"
            )

        # Check if player does not control the to_territory
        if self.state.territories[move.to_territory].owner == move.player:
            raise ValueError(f"Cannot attack your own territory {move.to_territory}")

        # Check if territories are adjacent
        if (
            move.to_territory
            not in self.state.territories[move.from_territory].adjacent
        ):
            raise ValueError(
                f"{move.to_territory} is not adjacent to {move.from_territory}"
            )

        # Check if there are enough armies to attack
        if self.state.territories[move.from_territory].armies < 2:
            raise ValueError(
                f"Need at least 2 armies in {move.from_territory} to attack"
            )

        # Validate attack dice
        if not move.attack_dice or move.attack_dice < 1:
            raise ValueError("Must attack with at least 1 die")

        if move.attack_dice > min(
            3, self.state.territories[move.from_territory].armies - 1
        ):
            raise ValueError(
                f"Cannot attack with {move.attack_dice} dice, maximum is {min(3, self.state.territories[move.from_territory].armies - 1)}"
            )

    def _validate_fortify(self, move: RiskMove) -> None:
        """Validate a fortify move.

        Args:
            move: The move to validate.

        Raises:
            ValueError: If the move is invalid.
        """
        # Skip validation for empty fortify (end turn)
        if not move.from_territory and not move.to_territory:
            return

        # Check if from_territory and to_territory are specified
        if not move.from_territory:
            raise ValueError("Territory to fortify from not specified")

        if not move.to_territory:
            raise ValueError("Territory to fortify not specified")

        # Check if territories exist
        if move.from_territory not in self.state.territories:
            raise ValueError(f"Territory {move.from_territory} does not exist")

        if move.to_territory not in self.state.territories:
            raise ValueError(f"Territory {move.to_territory} does not exist")

        # Check if player controls both territories
        if self.state.territories[move.from_territory].owner != move.player:
            raise ValueError(
                f"Player {move.player} does not control {move.from_territory}"
            )

        if self.state.territories[move.to_territory].owner != move.player:
            raise ValueError(
                f"Player {move.player} does not control {move.to_territory}"
            )

        # Check if territories are adjacent
        if (
            move.to_territory
            not in self.state.territories[move.from_territory].adjacent
        ):
            raise ValueError(
                f"{move.to_territory} is not adjacent to {move.from_territory}"
            )

        # Check if there are enough armies to fortify
        if not move.armies or move.armies <= 0:
            raise ValueError("Must fortify with at least 1 army")

        if self.state.territories[move.from_territory].armies <= move.armies:
            raise ValueError(f"Must leave at least 1 army in {move.from_territory}")

    def _validate_trade_cards(self, move: RiskMove) -> None:
        """Validate a trade cards move.

        Args:
            move: The move to validate.

        Raises:
            ValueError: If the move is invalid.
        """
        # Check if cards are specified
        if not move.cards or len(move.cards) != 3:
            raise ValueError("Must trade exactly 3 cards")

        # Check if player has the cards
        player = self.state.players[move.player]
        for card in move.cards:
            if card not in player.cards:
                raise ValueError(f"Player {move.player} does not have {card}")

        # Check if the set is valid (3 of a kind, 1 of each, or includes a
        # wild)
        card_types = [card.card_type for card in move.cards]
        has_wild = CardType.WILD in card_types

        if has_wild:
            # Any set with a wild card is valid
            pass
        elif len(set(card_types)) == 1:
            # 3 of a kind (all infantry, all cavalry, or all artillery)
            pass
        elif len(set(card_types)) == 3:
            # 1 of each (infantry, cavalry, artillery)
            pass
        else:
            raise ValueError(
                "Invalid card set: must be 3 of a kind, 1 of each type, or include a wild card"
            )

    def _apply_place_armies(self, move: RiskMove) -> None:
        """Apply a place armies move to the game state.

        Args:
            move: The place armies move to apply.
        """
        # Add armies to territory
        territory = self.state.territories[move.to_territory]
        territory.armies += move.armies

        # Reduce player's unplaced armies
        player = self.state.players[move.player]
        player.unplaced_armies -= move.armies

        # If all armies are placed and in setup phase, advance to next player
        if self.state.phase == PhaseType.SETUP and player.unplaced_armies == 0:
            self._advance_to_next_player()

        # If all players have placed initial armies, transition to
        # reinforcement phase
        if self.state.phase == PhaseType.SETUP and all(
            p.unplaced_armies == 0 for p in self.state.players.values()
        ):
            self.state.phase = PhaseType.REINFORCE

    def _apply_attack(self, move: RiskMove) -> None:
        """Apply an attack move to the game state.

        Args:
            move: The attack move to apply.
        """
        # Simulate dice rolls
        attacker_territory = self.state.territories[move.from_territory]
        defender_territory = self.state.territories[move.to_territory]

        attacker_dice = move.attack_dice
        defender_dice = min(2, defender_territory.armies)

        # Roll attacker dice
        attacker_rolls = [random.randint(1, 6) for _ in range(attacker_dice)]
        attacker_rolls.sort(reverse=True)

        # Roll defender dice
        defender_rolls = [random.randint(1, 6) for _ in range(defender_dice)]
        defender_rolls.sort(reverse=True)

        # Compare dice and calculate casualties
        attacker_casualties = 0
        defender_casualties = 0

        for i in range(min(len(attacker_rolls), len(defender_rolls))):
            if attacker_rolls[i] > defender_rolls[i]:
                defender_casualties += 1
            else:
                attacker_casualties += 1

        # Apply casualties
        attacker_territory.armies -= attacker_casualties
        defender_territory.armies -= defender_casualties

        # Check if defender is defeated
        if defender_territory.armies == 0:
            # Transfer ownership
            defender_player = defender_territory.owner
            defender_territory.owner = move.player

            # Move attacking armies
            min_armies = 1  # At least 1 army must be moved
            max_armies = attacker_territory.armies - 1  # At least 1 army must remain
            armies_to_move = min(min_armies, max_armies)  # Default to minimum

            attacker_territory.armies -= armies_to_move
            defender_territory.armies = armies_to_move

            # Mark that attacker captured a territory this turn
            self.state.attacker_captured_territory = True

            # Check if defender is eliminated
            defender_territories = self.state.get_controlled_territories(
                defender_player
            )
            if not defender_territories:
                self.state.players[defender_player].eliminated = True

                # Transfer cards from defender to attacker
                defender_cards = self.state.players[defender_player].cards
                self.state.players[move.player].cards.extend(defender_cards)
                self.state.players[defender_player].cards = []

                # Force attacker to trade cards if they have too many
                if len(self.state.players[move.player].cards) >= 5:
                    # This would trigger a card trade prompt in a real
                    # implementation
                    pass

    def _apply_fortify(self, move: RiskMove) -> None:
        """Apply a fortify move to the game state.

        Args:
            move: The fortify move to apply.
        """
        # Skip for empty fortify (end turn)
        if not move.from_territory and not move.to_territory:
            self._end_turn()
            return

        # Move armies
        from_territory = self.state.territories[move.from_territory]
        to_territory = self.state.territories[move.to_territory]

        from_territory.armies -= move.armies
        to_territory.armies += move.armies

        # End turn after fortification
        self._end_turn()

    def _apply_trade_cards(self, move: RiskMove) -> None:
        """Apply a trade cards move to the game state.

        Args:
            move: The trade cards move to apply.
        """
        # Calculate armies received
        armies_received = self.state.next_card_set_value

        # Update next card set value if using escalating values
        if self.config.escalating_card_values:
            if self.state.next_card_set_value < 12:
                self.state.next_card_set_value += 2
            else:
                self.state.next_card_set_value += 5

        # Give armies to player
        player = self.state.players[move.player]
        player.unplaced_armies += armies_received

        # Remove cards from player's hand
        for card in move.cards:
            player.cards.remove(card)

        # Add cards back to deck
        self.state.deck.extend(move.cards)
        random.shuffle(self.state.deck)

    def _end_turn(self) -> None:
        """End the current player's turn and prepare for the next player."""
        # Give card if territory was captured
        if self.state.attacker_captured_territory:
            if self.state.deck:
                card = self.state.deck.pop(0)
                self.state.players[self.state.current_player].cards.append(card)
            self.state.attacker_captured_territory = False

        # Move to next player
        self._advance_to_next_player()

        # Calculate reinforcements for the new player
        self._calculate_reinforcements()

        # Set phase to reinforce
        self.state.phase = PhaseType.REINFORCE

    def _advance_to_next_player(self) -> None:
        """Advance to the next active player."""
        player_names = list(self.state.players.keys())
        current_index = player_names.index(self.state.current_player)

        # Find next non-eliminated player
        for i in range(1, len(player_names) + 1):
            next_index = (current_index + i) % len(player_names)
            next_player = player_names[next_index]
            if not self.state.players[next_player].eliminated:
                self.state.current_player = next_player
                break

        # Increment turn number when returning to first player
        if next_index < current_index:
            self.state.turn_number += 1

    def _calculate_reinforcements(self) -> None:
        """Calculate reinforcements for the current player."""
        player = self.state.players[self.state.current_player]

        # Base reinforcements (minimum 3)
        territories = self.state.get_controlled_territories(player.name)
        base_reinforcements = max(3, len(territories) // 3)

        # Continent bonuses
        continent_bonus = 0
        for continent in self.state.get_controlled_continents(player.name):
            continent_bonus += continent.bonus

        # Total reinforcements
        total_reinforcements = base_reinforcements + continent_bonus

        # Add to player's unplaced armies
        player.unplaced_armies += total_reinforcements

    def _check_game_over(self) -> None:
        """Check if the game is over."""
        active_players = [
            p.name for p in self.state.players.values() if not p.eliminated
        ]

        if len(active_players) == 1:
            self.state.game_status = GameStatus.FINISHED
            self.state.phase = PhaseType.GAME_OVER
