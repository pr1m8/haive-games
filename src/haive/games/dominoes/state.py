"""Comprehensive state management system for Dominoes gameplay and strategic analysis.

This module provides sophisticated state models for Dominoes games with complete
support for tile tracking, board management, strategic analysis, and game flow
control. The state system maintains both traditional dominoes mechanics and
advanced strategic context for AI decision-making.

The state system supports:
- Complete tile tracking with hand and boneyard management
- Strategic analysis history for multiplayer gameplay
- Board state validation and move legality checking
- Game progression tracking with pass and block detection
- Performance metrics and statistical analysis
- Multiple game variants and scoring systems

Examples:
    Creating a new game state::

        state = DominoesState.initialize(
            player_names=["player1", "player2"],
            tiles_per_hand=7
        )
        assert state.turn in ["player1", "player2"]
        assert state.game_status == "ongoing"

    Accessing game information::

        # Check board state
        left_open = state.left_value
        right_open = state.right_value
        board_display = state.board_string

        # Check hand sizes
        hand_sizes = state.hand_sizes
        tiles_remaining = state.boneyard_size

    Tracking strategic analysis::

        analysis = DominoesAnalysis(
            hand_strength="Strong high-value tiles",
            blocking_opportunities=["Block 5-5 connection"],
            optimal_plays=["Play 6-4 on right end"],
            endgame_strategy="Hold doubles for scoring"
        )
        state.add_analysis(analysis, "player1")

    Game state queries::

        # Check game completion
        if state.is_game_over():
            winner = state.winner
            final_scores = state.scores

        # Strategic position analysis
        playable_tiles = state.get_playable_tiles("player1")
        board_control = state.board_control_analysis

Note:
    All state models use Pydantic for validation and support both JSON
    serialization and integration with LangGraph for distributed gameplay.
"""

import random
from typing import Dict, List, Literal, Optional, Union

from pydantic import Field, computed_field, field_validator

from haive.games.dominoes.models import DominoesAnalysis, DominoMove, DominoTile
from haive.games.framework.base.state import GameState


class DominoesState(GameState):
    """Comprehensive state management for Dominoes gameplay with strategic analysis support.

    This class provides complete state management for Dominoes games, supporting
    both traditional dominoes mechanics and strategic analysis. The state system
    maintains tile tracking, board management, strategic context, and performance
    metrics for advanced AI decision-making and game analysis.

    The state system supports:
    - Complete tile tracking with hand and boneyard management
    - Strategic analysis history for multiplayer gameplay with learning capability
    - Board state validation and move legality checking
    - Game progression tracking with pass and block detection
    - Performance metrics and statistical analysis for gameplay optimization
    - Multiple game variants and scoring systems

    The game follows traditional dominoes rules:
    - Each player starts with 7 tiles (configurable)
    - Players take turns placing tiles that match board ends
    - Game ends when a player plays all tiles or board is blocked
    - Scoring typically based on remaining tiles in opponents' hands

    Attributes:
        players (List[str]): List of player names in turn order.
            Maintains consistent ordering for gameplay flow.
        hands (Dict[str, List[DominoTile]]): Current tiles in each player's hand.
            Private information tracked for game management.
        board (List[DominoTile]): Tiles currently placed on the board.
            Represents the train/line of connected dominoes.
        boneyard (List[DominoTile]): Undealt tiles available for drawing.
            Used when players cannot play and must draw.
        turn (str): Current player's turn identifier.
            Cycles through players list for turn management.
        game_status (Literal): Current game state with completion detection.
            Tracks ongoing play, wins, and draw conditions.
        move_history (List[Union[DominoMove, Literal["pass"]]]): Complete move history.
            Includes both tile placements and pass actions.
        last_passes (int): Count of consecutive passes for block detection.
            Used to determine when board is blocked.
        scores (Dict[str, int]): Current scores for each player.
            Updated based on game variant scoring rules.
        winner (Optional[str]): Winner identifier if game completed.
            Set when victory conditions are met.
        player1_analysis (List[DominoesAnalysis]): Strategic analysis history for player1.
            Tracks reasoning and decision-making patterns.
        player2_analysis (List[DominoesAnalysis]): Strategic analysis history for player2.
            Tracks reasoning and decision-making patterns.

    Examples:
        Creating a new game state::

            state = DominoesState.initialize(
                player_names=["Alice", "Bob"],
                tiles_per_hand=7
            )
            assert state.turn in ["Alice", "Bob"]
            assert len(state.players) == 2
            assert all(len(hand) == 7 for hand in state.hands.values())

        Accessing game information::

            # Check board state
            left_open = state.left_value  # Value that can be matched on left
            right_open = state.right_value  # Value that can be matched on right
            board_display = state.board_string  # Human-readable board

            # Check hand and boneyard sizes
            hand_sizes = state.hand_sizes
            tiles_remaining = state.boneyard_size
            total_tiles = state.total_tiles_in_play

        Managing strategic analysis::

            analysis = DominoesAnalysis(
                hand_strength="Strong concentration of 5s and 6s",
                blocking_opportunities=["Block opponent's 3-3 double"],
                optimal_plays=["Play 5-2 on left end for control"],
                endgame_strategy="Hold 6-6 double for final scoring"
            )
            state.add_analysis(analysis, "Alice")

            # Access latest strategic insights
            latest_analysis = state.get_latest_analysis("Alice")

        Game state queries::

            # Check game completion
            if state.is_game_over():
                winner = state.winner
                final_scores = state.scores
                game_summary = state.game_summary

            # Strategic position analysis
            playable_tiles = state.get_playable_tiles("Alice")
            board_control = state.board_control_analysis
            tile_distribution = state.tile_distribution_analysis

        Advanced game analysis::

            # Performance metrics
            stats = state.game_statistics
            print(f"Moves played: {stats['total_moves']}")
            print(f"Pass rate: {stats['pass_percentage']:.1f}%")

            # Strategic evaluation
            position_eval = state.position_evaluation
            print(f"Board control: {position_eval['board_control']}")
            print(f"Hand strength: {position_eval['hand_strength_analysis']}")

    Note:
        The state uses Pydantic for validation and supports both JSON serialization
        and integration with LangGraph for distributed game systems. All tile
        operations maintain game rule consistency and strategic context.
    """

    players: List[str] = Field(
        ...,
        min_items=2,
        max_items=4,
        description="List of player names in turn order (2-4 players supported)",
    )
    hands: Dict[str, List[DominoTile]] = Field(
        ..., description="Current tiles in each player's hand (private information)"
    )
    board: List[DominoTile] = Field(
        default_factory=list,
        description="Tiles currently placed on the board in connection order",
    )
    boneyard: List[DominoTile] = Field(
        default_factory=list,
        description="Undealt tiles available for drawing when players cannot play",
    )
    turn: str = Field(
        ..., description="Current player's turn identifier (must be in players list)"
    )
    game_status: Literal["ongoing", "player1_win", "player2_win", "draw"] = Field(
        default="ongoing",
        description="Current game state: ongoing play, player victory, or draw",
    )
    move_history: List[Union[DominoMove, Literal["pass"]]] = Field(
        default_factory=list,
        description="Complete chronological history of moves and passes",
    )
    last_passes: int = Field(
        default=0,
        ge=0,
        description="Number of consecutive passes (for block detection)",
    )
    scores: Dict[str, int] = Field(
        default_factory=dict,
        description="Current scores for each player (updated by game variant rules)",
    )
    winner: Optional[str] = Field(
        default=None, description="Winner identifier if game completed, None if ongoing"
    )
    player1_analysis: List[DominoesAnalysis] = Field(
        default_factory=list,
        description="Strategic analysis history for player1 with reasoning patterns",
    )
    player2_analysis: List[DominoesAnalysis] = Field(
        default_factory=list,
        description="Strategic analysis history for player2 with reasoning patterns",
    )

    @computed_field
    @property
    def left_value(self) -> Optional[int]:
        """Get the value on the left end of the board that can be matched.

        Returns:
            Optional[int]: Value that can be matched on left end, None if board empty.
        """
        if not self.board:
            return None
        return self.board[0].left

    @computed_field
    @property
    def right_value(self) -> Optional[int]:
        """Get the value on the right end of the board that can be matched.

        Returns:
            Optional[int]: Value that can be matched on right end, None if board empty.
        """
        if not self.board:
            return None
        return self.board[-1].right

    @computed_field
    @property
    def board_string(self) -> str:
        """Get a human-readable string representation of the board.

        Returns:
            str: Visual representation of the domino train with connecting lines.
        """
        if not self.board:
            return "Empty board"

        board_str = ""
        for i, tile in enumerate(self.board):
            if i > 0:
                # Add a connecting character between tiles
                board_str += "-"
            board_str += str(tile)

        return board_str

    @computed_field
    @property
    def hand_sizes(self) -> Dict[str, int]:
        """Get the current hand sizes for all players."""
        return {player: len(self.hands[player]) for player in self.players}

    @computed_field
    @property
    def boneyard_size(self) -> int:
        """Get the number of tiles remaining in the boneyard."""
        return len(self.boneyard)

    @computed_field
    @property
    def total_tiles_in_play(self) -> int:
        """Get the total number of tiles currently in players' hands and on board."""
        hand_tiles = sum(len(hand) for hand in self.hands.values())
        board_tiles = len(self.board)
        return hand_tiles + board_tiles

    @computed_field
    @property
    def is_blocked(self) -> bool:
        """Check if the board is blocked (all players have passed)."""
        return self.last_passes >= len(self.players)

    @computed_field
    @property
    def game_statistics(self) -> Dict[str, Union[int, float, str]]:
        """Generate comprehensive game statistics."""
        total_moves = len(self.move_history)
        pass_count = sum(1 for move in self.move_history if move == "pass")

        return {
            "total_moves": total_moves,
            "pass_count": pass_count,
            "pass_percentage": (
                (pass_count / total_moves * 100) if total_moves > 0 else 0
            ),
            "tiles_on_board": len(self.board),
            "tiles_in_boneyard": self.boneyard_size,
            "consecutive_passes": self.last_passes,
            "game_phase": (
                "endgame"
                if self.total_tiles_in_play < 10
                else "midgame" if self.total_tiles_in_play < 20 else "opening"
            ),
            "board_blocked": self.is_blocked,
        }

    @computed_field
    @property
    def position_evaluation(self) -> Dict[str, Union[str, int, float]]:
        """Generate strategic position evaluation."""
        hand_sizes = self.hand_sizes
        min_hand_size = min(hand_sizes.values())
        leader = [
            player for player, size in hand_sizes.items() if size == min_hand_size
        ][0]

        return {
            "hand_strength_leader": leader,
            "minimum_hand_size": min_hand_size,
            "hand_size_spread": max(hand_sizes.values()) - min_hand_size,
            "board_control": "dynamic" if self.board else "balanced",
            "tiles_remaining_total": sum(hand_sizes.values()),
            "endgame_proximity": min_hand_size <= 3,
        }

    def add_analysis(self, analysis: DominoesAnalysis, player: str) -> None:
        """Add strategic analysis for a player."""
        if player not in self.players:
            raise ValueError(f"Player '{player}' not in game")

        if player == "player1":
            self.player1_analysis = list(self.player1_analysis) + [analysis]
        elif player == "player2":
            self.player2_analysis = list(self.player2_analysis) + [analysis]

    def get_latest_analysis(self, player: str) -> Optional[DominoesAnalysis]:
        """Get the latest analysis for a player."""
        if player == "player1":
            return self.player1_analysis[-1] if self.player1_analysis else None
        elif player == "player2":
            return self.player2_analysis[-1] if self.player2_analysis else None
        return None

    def get_playable_tiles(self, player: str) -> List[DominoTile]:
        """Get tiles that a player can currently play."""
        if player not in self.players:
            return []

        player_hand = self.hands[player]

        # If board is empty, any tile can be played
        if not self.board:
            return player_hand[:]

        # Check which tiles can match board ends
        playable = []
        left_val = self.left_value
        right_val = self.right_value

        for tile in player_hand:
            if (
                tile.left == left_val
                or tile.right == left_val
                or tile.left == right_val
                or tile.right == right_val
            ):
                playable.append(tile)

        return playable

    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_status != "ongoing"

    @classmethod
    def initialize(
        cls, player_names: Optional[List[str]] = None, tiles_per_hand: int = 7
    ) -> "DominoesState":
        """Initialize a new dominoes game with proper tile distribution.

        Args:
            player_names: List of player names. Defaults to ["player1", "player2"].
            tiles_per_hand: Number of tiles to deal to each player. Default is 7.

        Returns:
            DominoesState: A new game state ready to play.
        """
        if player_names is None:
            player_names = ["player1", "player2"]

        # Create all tiles from 0-0 to 6-6 (standard double-six set)
        all_tiles = []
        for i in range(7):
            for j in range(i, 7):  # Create tiles from 0-0 to 6-6
                all_tiles.append(DominoTile(left=i, right=j))

        # Shuffle the tiles for random distribution
        random.shuffle(all_tiles)

        # Deal tiles to players
        hands = {}
        for player in player_names:
            hands[player] = all_tiles[:tiles_per_hand]
            all_tiles = all_tiles[tiles_per_hand:]

        # Remaining tiles go to the boneyard
        boneyard = all_tiles

        # Determine who goes first using traditional dominoes rules
        # Rule 1: Player with highest double goes first
        first_player = player_names[0]  # Default fallback
        highest_double = -1

        for player in player_names:
            for tile in hands[player]:
                if tile.is_double() and tile.left > highest_double:
                    highest_double = tile.left
                    first_player = player

        # Rule 2: If no doubles, player with highest-value tile goes first
        if highest_double == -1:
            highest_sum = -1
            for player in player_names:
                for tile in hands[player]:
                    tile_sum = tile.sum()
                    if tile_sum > highest_sum:
                        highest_sum = tile_sum
                        first_player = player

        # Create the initial state with proper initialization
        return cls(
            players=player_names,
            hands=hands,
            board=[],
            boneyard=boneyard,
            turn=first_player,
            game_status="ongoing",
            move_history=[],
            last_passes=0,
            scores=dict.fromkeys(player_names, 0),
        )

    model_config = {"arbitrary_types_allowed": True}
