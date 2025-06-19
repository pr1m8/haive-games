"""Battleship game state representation module.

This module defines the state models for the Battleship game, including:
    - Player state with board and analysis tracking
    - Complete game state with turn management
    - Game phase transitions
    - Public and private state views
"""

from typing import Annotated, Any, Literal

from pydantic import BaseModel, Field

from haive.games.battleship.models import (
    GamePhase,
    MoveOutcome,
    PlayerBoard,
    ShipPlacement,
)


class PlayerState(BaseModel):
    """Complete state for a player including board and analysis.

    This class maintains the state for a single player, tracking their board,
    ship placements, and strategic analysis history.

    Attributes:
        board (PlayerBoard): The player's game board with ships and attack history
        strategic_analysis (list[str]): History of strategic analyses for the player
        has_placed_ships (bool): Flag indicating if the player has completed ship placement
        ship_placements (list[ShipPlacement]): Record of all ship placement commands

    Examples:
        >>> player_state = PlayerState()
        >>> player_state.has_placed_ships = True
        >>> player_state.strategic_analysis.append("Focus attacks on the center")
    """

    board: PlayerBoard = Field(default_factory=PlayerBoard)
    strategic_analysis: list[str] = Field(default_factory=list)

    has_placed_ships: bool = Field(default=False)
    ship_placements: list[ShipPlacement] = Field(default_factory=list)


class BattleshipState(BaseModel):
    """Complete game state for Battleship.

    Represents the entire game state, including both players' boards,
    turn management, game phase, and move history.

    Attributes:
        player1_state (PlayerState): Complete state for player 1
        player2_state (PlayerState): Complete state for player 2
        current_player (str): Which player's turn it is ("player1" or "player2")
        game_phase (GamePhase): Current phase of the game (setup, playing, ended)
        winner (str, optional): Which player won the game, if any
        move_history (list): History of all moves made in the game
        error_message (str, optional): Any error message from the last operation

    Examples:
        >>> state = BattleshipState()
        >>> state.current_player = "player1"
        >>> state.game_phase = GamePhase.PLAYING
        >>> state.is_game_over()
        False
    """

    # Player states - using Annotated for accumulation
    player1_state: Annotated[PlayerState, "accumulate"] = Field(
        default_factory=PlayerState
    )
    player2_state: Annotated[PlayerState, "accumulate"] = Field(
        default_factory=PlayerState
    )

    # Game state
    current_player: Literal["player1", "player2"] = Field(default="player1")
    game_phase: GamePhase = Field(default=GamePhase.SETUP)
    winner: Literal["player1", "player2"] | None = Field(default=None)

    # Move history
    move_history: list[tuple[str, MoveOutcome]] = Field(default_factory=list)

    # Error state
    error_message: str | None = Field(default=None)

    def get_player_state(self, player: str) -> PlayerState:
        """Get a player's state by name.

        Args:
            player: Player identifier ("player1" or "player2")

        Returns:
            PlayerState: The requested player's state

        Raises:
            ValueError: If an invalid player identifier is provided

        Examples:
            >>> state = BattleshipState()
            >>> player1 = state.get_player_state("player1")
            >>> player1.has_placed_ships = True
        """
        if player == "player1":
            return self.player1_state
        if player == "player2":
            return self.player2_state
        raise ValueError(f"Invalid player: {player}")

    def get_opponent(self, player: str) -> str:
        """Get the name of a player's opponent.

        Args:
            player: Player identifier ("player1" or "player2")

        Returns:
            str: The opponent's identifier

        Examples:
            >>> state = BattleshipState()
            >>> state.get_opponent("player1")
            'player2'
        """
        return "player2" if player == "player1" else "player1"

    def is_setup_complete(self) -> bool:
        """Check if setup phase is complete.

        Returns:
            bool: True if both players have placed their ships

        Examples:
            >>> state = BattleshipState()
            >>> state.player1_state.has_placed_ships = True
            >>> state.player2_state.has_placed_ships = True
            >>> state.is_setup_complete()
            True
        """
        return (
            self.player1_state.has_placed_ships and self.player2_state.has_placed_ships
        )

    def is_game_over(self) -> bool:
        """Check if the game is over.

        The game is over if either:
        1. The game phase is explicitly set to ENDED
        2. All ships of either player are sunk

        Returns:
            bool: True if the game is over

        Examples:
            >>> state = BattleshipState()
            >>> state.game_phase = GamePhase.ENDED
            >>> state.is_game_over()
            True
        """
        return (
            self.game_phase == GamePhase.ENDED
            or self.player1_state.board.all_ships_sunk()
            or self.player2_state.board.all_ships_sunk()
        )

    def get_public_state_for_player(self, player: str) -> dict[str, Any]:
        """Get a public view of the game state for a player.

        Creates a sanitized view of the game state that hides the opponent's
        ship positions and other private information, showing only what the
        specified player should know.

        Args:
            player: Player identifier ("player1" or "player2")

        Returns:
            dict[str, Any]: Dictionary containing the public game state

        Examples:
            >>> state = BattleshipState()
            >>> public_state = state.get_public_state_for_player("player1")
            >>> public_state["is_your_turn"]
            True
        """
        opponent = self.get_opponent(player)
        player_state = self.get_player_state(player)
        opponent_state = self.get_player_state(opponent)

        # Ensure strategic thoughts are available
        strategic_thoughts = (
            player_state.strategic_analysis[-1]
            if player_state.strategic_analysis
            else "No previous strategic analysis."
        )

        return {
            # Game status information
            "game_phase": self.game_phase,
            "current_player": self.current_player,
            "is_your_turn": self.current_player == player,
            # Hits, misses, and sunk ships
            "your_hits": [c.model_dump() for c in player_state.board.successful_hits],
            "your_misses": [c.model_dump() for c in player_state.board.failed_attacks],
            "your_sunk_ships": [ship.value for ship in player_state.board.sunk_ships],
            "opponent_hits": [
                c.model_dump() for c in opponent_state.board.successful_hits
            ],
            "opponent_misses": [
                c.model_dump() for c in opponent_state.board.failed_attacks
            ],
            "opponent_sunk_ships": [
                ship.value for ship in opponent_state.board.sunk_ships
            ],
            # Strategic information
            "strategic_thoughts": strategic_thoughts,
            # Optional extras for debugging/logging
            "move_history": [(p, m.model_dump()) for p, m in self.move_history],
            "your_analysis": player_state.strategic_analysis,
            # Ensure structured output compatibility
            "row": None,  # Add this to match prompt template expectations
            "col": None,
        }
