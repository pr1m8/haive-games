from typing import Annotated, Any, Literal

from pydantic import BaseModel, Field, computed_field

from haive.games.battleship.models import (
    GamePhase,
    MoveOutcome,
    PlayerBoard,
    ShipPlacement,
)

r"""Comprehensive state management system for Battleship game mechanics and
player tracking.

This module provides sophisticated state models for the Battleship game, supporting
complete game state tracking, turn management, strategic analysis, and secure state
transitions. The state system maintains both private game information and public
views for strategic decision-making.

The state models support:
- Individual player state with board management and strategic analysis
- Complete game state with turn-based mechanics and phase transitions
- Secure public/private state views for AI decision-making
- Comprehensive move history and error tracking
- Ship placement validation and game completion detection

Examples:
    Creating a new game state::\n

        state = BattleshipState()
        state.current_player = "player1"
        state.game_phase = GamePhase.SETUP

    Managing player state::\n

        player1 = state.get_player_state("player1")
        player1.has_placed_ships = True
        player1.strategic_analysis.append("Focus on center quadrant")

    Checking game completion::\n

        if state.is_game_over():
            winner = state.winner
            print(f"Game completed, winner: {winner}")

    Getting public state for AI::\n

        public_state = state.get_public_state_for_player("player1")
        # Contains only information player1 should know

    Tracking move history::\n

        move_count = len(state.move_history)
        last_move = state.move_history[-1] if state.move_history else None

Note:
    All state models use Pydantic for validation and serialization, ensuring
    type safety and data integrity throughout the game lifecycle.
"""


class PlayerState(BaseModel):
    r"""Comprehensive state model for individual player tracking and strategic analysis.

    This class maintains complete state information for a single player in the
    Battleship game, including their board configuration, ship placements, attack
    history, and strategic analysis data. The state supports both active gameplay
    and post-game analysis.

    The player state tracks:
    - Board state with ship positions and attack results
    - Strategic analysis history for decision-making
    - Ship placement records and validation
    - Performance metrics and game statistics
    - Error tracking and state validation

    Attributes:
        board (PlayerBoard): The player's game board containing ship positions,
            attack history, successful hits, failed attacks, and sunk ships.
        strategic_analysis (List[str]): Complete history of strategic analyses
            performed for this player, used for learning and adaptation.
        has_placed_ships (bool): Flag indicating whether the player has completed
            the ship placement phase of the game.
        ship_placements (List[ShipPlacement]): Complete record of all ship
            placement commands executed for this player.

    Examples:
        Creating a new player state::\n

            player_state = PlayerState()
            assert not player_state.has_placed_ships
            assert len(player_state.strategic_analysis) == 0

        Managing ship placement::\n

            placement = ShipPlacement(
                ship_type=ShipType.DESTROYER,
                start_row=0, start_col=0,
                orientation=Orientation.HORIZONTAL
            )
            player_state.ship_placements.append(placement)
            player_state.has_placed_ships = True

        Adding strategic analysis::\n

            analysis = "Enemy likely has carrier in top-left quadrant"
            player_state.strategic_analysis.append(analysis)

            # Access latest analysis
            latest_analysis = player_state.strategic_analysis[-1]

        Checking board state::\n

            if player_state.board.all_ships_sunk():
                print("Player has lost the game")

            hits = len(player_state.board.successful_hits)
            misses = len(player_state.board.failed_attacks)
            accuracy = hits / (hits + misses) if (hits + misses) > 0 else 0

    Note:
        Player state is designed to be serializable and thread-safe, supporting
        both local gameplay and distributed game systems.

    """

    board: PlayerBoard = Field(
        default_factory=PlayerBoard,
        description="Player's game board with ship positions and attack history",
    )

    strategic_analysis: list[str] = Field(
        default_factory=list,
        description="Complete history of strategic analyses for decision-making and learning",
    )

    has_placed_ships: bool = Field(
        default=False,
        description="Flag indicating completion of ship placement phase",
    )

    ship_placements: list[ShipPlacement] = Field(
        default_factory=list,
        description="Complete record of all ship placement commands executed",
    )


class BattleshipState(BaseModel):
    r"""Comprehensive state model for managing complete Battleship game sessions.

    This class provides complete state management for Battleship games, supporting
    turn-based gameplay, phase transitions, strategic analysis, and secure state
    views. The state system maintains both public and private information while
    ensuring game rule enforcement and data integrity.

    The game state manages:
    - Complete player states with board and strategic data
    - Turn-based gameplay mechanics and phase transitions
    - Comprehensive move history and outcome tracking
    - Error handling and state validation
    - Public/private state views for AI decision-making
    - Game completion detection and winner determination

    Attributes:
        player1_state (PlayerState): Complete state for the first player,
            including board configuration, ship placements, and strategic analysis.
        player2_state (PlayerState): Complete state for the second player,
            including board configuration, ship placements, and strategic analysis.
        current_player (Literal["player1", "player2"]): Identifier of the player
            whose turn it currently is in the game.
        game_phase (GamePhase): Current phase of the game (SETUP, PLAYING, ENDED),
            determining which actions are valid.
        winner (Optional[Literal["player1", "player2"]]): Identifier of the winning
            player, or None if the game is still in progress.
        move_history (List[Tuple[str, MoveOutcome]]): Complete chronological record
            of all moves made in the game with their outcomes.
        error_message (Optional[str]): Error message from the last operation,
            or None if no error occurred.

    Examples:
        Creating a new game state::\n

            state = BattleshipState()
            assert state.current_player == "player1"
            assert state.game_phase == GamePhase.SETUP
            assert state.winner is None

        Managing turn-based gameplay::\n

            # Start player 1's turn
            state.current_player = "player1"
            player1 = state.get_player_state("player1")

            # After player 1 moves, switch to player 2
            state.current_player = "player2"
            player2 = state.get_player_state("player2")

        Tracking game progress::\n

            # Check if setup is complete
            if state.is_setup_complete():
                state.game_phase = GamePhase.PLAYING

            # Check for game completion
            if state.is_game_over():
                # Determine winner based on remaining ships
                if state.player1_state.board.all_ships_sunk():
                    state.winner = "player2"
                elif state.player2_state.board.all_ships_sunk():
                    state.winner = "player1"

        Managing move history::\n

            # Add a move to history
            move_outcome = MoveOutcome(hit=True, sunk_ship=ShipType.DESTROYER)
            state.move_history.append(("player1", move_outcome))

            # Analyze recent moves
            recent_moves = state.move_history[-5:]  # Last 5 moves

        Getting secure state views::\n

            # Get public state for AI decision-making
            public_state = state.get_public_state_for_player("player1")
            # Contains only information player1 should know

            # Check opponent without revealing private info
            opponent = state.get_opponent("player1")

        Error handling::\n

            try:
                # Attempt game operation
                state.some_operation()
            except Exception as e:
                state.error_message = str(e)
                # Game can continue with error logged

    Note:
        The state uses Pydantic annotations for LangGraph accumulation,
        enabling efficient state updates in distributed game systems.

    """

    # Player states - using Annotated for LangGraph accumulation
    player1_state: Annotated[PlayerState, "accumulate"] = Field(
        default_factory=PlayerState,
        description="Complete state for player 1 including board and strategic analysis",
    )
    player2_state: Annotated[PlayerState, "accumulate"] = Field(
        default_factory=PlayerState,
        description="Complete state for player 2 including board and strategic analysis",
    )

    # Game state management
    current_player: Literal["player1", "player2"] = Field(
        default="player1",
        description="Identifier of the player whose turn it currently is",
    )
    game_phase: GamePhase = Field(
        default=GamePhase.SETUP,
        description="Current phase of the game (SETUP, PLAYING, ENDED)",
    )
    winner: Literal["player1", "player2"] | None = Field(
        default=None,
        description="Identifier of the winning player, or None if game is in progress",
    )

    # Move tracking and history
    move_history: list[tuple[str, MoveOutcome]] = Field(
        default_factory=list,
        description="Complete chronological record of all moves made in the game",
    )

    # Error handling
    error_message: str | None = Field(
        default=None,
        description="Error message from the last operation, or None if no error occurred",
    )

    def get_player_state(self, player: str) -> PlayerState:
        r"""Retrieve a player's complete state by their identifier.

        Provides access to a player's complete state including board configuration,
        ship placements, strategic analysis, and game statistics. This method
        ensures type safety and validates player identifiers.

        Args:
            player (str): Player identifier, must be either "player1" or "player2".

        Returns:
            PlayerState: The complete state object for the specified player,
                containing board, strategic analysis, and placement information.

        Raises:
            ValueError: If the player identifier is not "player1" or "player2".

        Examples:
            Basic player state access::\n

                state = BattleshipState()
                player1 = state.get_player_state("player1")
                player1.has_placed_ships = True

            Accessing player board::\n

                player_state = state.get_player_state("player1")
                hits = len(player_state.board.successful_hits)
                misses = len(player_state.board.failed_attacks)

            Managing strategic analysis::\n

                player_state = state.get_player_state("player2")
                player_state.strategic_analysis.append("Focus on quadrant C")
                latest_analysis = player_state.strategic_analysis[-1]

        """
        if player == "player1":
            return self.player1_state
        if player == "player2":
            return self.player2_state
        raise ValueError(
            f"Invalid player identifier: {player}. Must be 'player1' or 'player2'.",
        )

    def get_opponent(self, player: str) -> str:
        r"""Determine the opponent of a specified player.

        Provides the identifier of the opposing player, essential for turn-based
        game mechanics and strategic analysis. This method ensures consistent
        opponent identification throughout the game.

        Args:
            player (str): Player identifier ("player1" or "player2").

        Returns:
            str: The opponent's identifier ("player2" for "player1", "player1" for "player2").

        Examples:
            Basic opponent identification::\n

                state = BattleshipState()
                opponent = state.get_opponent("player1")
                assert opponent == "player2"

            Turn-based game logic::\n

                current_player = state.current_player
                opponent = state.get_opponent(current_player)

                # Switch turns
                state.current_player = opponent

            Strategic analysis::\n

                player = "player1"
                opponent = state.get_opponent(player)
                opponent_state = state.get_player_state(opponent)

                # Analyze opponent's remaining ships
                opponent_ships = opponent_state.board.sunk_ships

        """
        return "player2" if player == "player1" else "player1"

    def is_setup_complete(self) -> bool:
        r"""Check if the ship placement phase is complete for both players.

        Determines whether both players have successfully placed all their ships
        and the game is ready to transition from the SETUP phase to the PLAYING
        phase. This method is essential for game phase management.

        Returns:
            bool: True if both players have completed ship placement, False otherwise.

        Examples:
            Checking setup completion::\n

                state = BattleshipState()
                state.player1_state.has_placed_ships = True
                state.player2_state.has_placed_ships = True

                if state.is_setup_complete():
                    state.game_phase = GamePhase.PLAYING

            Game phase transition logic::\n

                if state.game_phase == GamePhase.SETUP and state.is_setup_complete():
                    state.game_phase = GamePhase.PLAYING
                    print("Game is ready to begin!")

            Validating game readiness::\n

                if not state.is_setup_complete():
                    players_needed = []
                    if not state.player1_state.has_placed_ships:
                        players_needed.append("player1")
                    if not state.player2_state.has_placed_ships:
                        players_needed.append("player2")
                    print(f"Waiting for ship placement: {players_needed}")

        """
        return (
            self.player1_state.has_placed_ships and self.player2_state.has_placed_ships
        )

    def is_game_over(self) -> bool:
        r"""Determine if the game has reached a terminal state.

        Checks multiple conditions to determine if the game is complete:
        1. Game phase is explicitly set to ENDED
        2. All ships of either player are sunk (victory condition)

        This method is critical for game loop termination and winner determination.

        Returns:
            bool: True if the game is over, False if gameplay should continue.

        Examples:
            Basic game completion check::\n

                state = BattleshipState()
                state.game_phase = GamePhase.ENDED
                assert state.is_game_over() == True

            Victory condition checking::\n

                if state.is_game_over():
                    if state.player1_state.board.all_ships_sunk():
                        state.winner = "player2"
                        print("Player 2 wins!")
                    elif state.player2_state.board.all_ships_sunk():
                        state.winner = "player1"
                        print("Player 1 wins!")

            Game loop integration::\n

                while not state.is_game_over():
                    current_player = state.current_player
                    # Process current player's turn
                    process_turn(state, current_player)

                # Game completed, display results
                winner = state.winner
                print(f"Game over! Winner: {winner}")

        """
        return (
            self.game_phase == GamePhase.ENDED
            or self.player1_state.board.all_ships_sunk()
            or self.player2_state.board.all_ships_sunk()
        )

    def get_public_state_for_player(self, player: str) -> dict[str, Any]:
        r"""Generate a secure public view of the game state for AI decision- making.

        Creates a carefully sanitized view of the game state that provides all
        information a player should legitimately know while hiding opponent secrets
        like ship positions. This method is essential for AI agents to make informed
        decisions without having access to private information.

        The public state includes:
        - Game phase and turn information
        - Player's own hits, misses, and sunk ships
        - Opponent's hits, misses, and sunk ships (but not ship positions)
        - Strategic analysis history for the requesting player
        - Complete move history for pattern analysis
        - Structured output compatibility for LLM processing

        Args:
            player (str): Player identifier ("player1" or "player2") requesting the state.

        Returns:
            Dict[str, Any]: Comprehensive public state dictionary containing:
                - game_phase: Current game phase (setup/playing/ended)
                - current_player: Whose turn it is
                - is_your_turn: Boolean indicating if it's the requesting player's turn
                - your_hits/your_misses: Player's attack results
                - your_sunk_ships: Ships the player has sunk
                - opponent_hits/opponent_misses: Opponent's attack results
                - opponent_sunk_ships: Ships the opponent has sunk
                - strategic_thoughts: Latest strategic analysis
                - move_history: Complete chronological move record
                - your_analysis: Full strategic analysis history
                - row/col: Compatibility fields for structured output

        Examples:
            Getting state for AI decision-making::\n

                state = BattleshipState()
                public_state = state.get_public_state_for_player("player1")

                # Check if it's player's turn
                if public_state["is_your_turn"]:
                    # Use public state to make move decision
                    hits = public_state["your_hits"]
                    misses = public_state["your_misses"]

            Analyzing strategic information::\n

                public_state = state.get_public_state_for_player("player2")
                strategic_thoughts = public_state["strategic_thoughts"]
                analysis_history = public_state["your_analysis"]

                # Use for strategic planning
                if "center quadrant" in strategic_thoughts:
                    # Continue center-focused strategy
                    pass

            Checking game progress::\n

                public_state = state.get_public_state_for_player("player1")

                player_sunk = len(public_state["your_sunk_ships"])
                opponent_sunk = len(public_state["opponent_sunk_ships"])

                print(f"You sunk: {player_sunk}, Opponent sunk: {opponent_sunk}")

            Move history analysis::\n

                public_state = state.get_public_state_for_player("player1")
                recent_moves = public_state["move_history"][-5:]  # Last 5 moves

                # Analyze patterns in recent gameplay
                for player_id, move_outcome in recent_moves:
                    if move_outcome["hit"]:
                        print(f"{player_id} scored a hit!")

        Note:
            This method ensures information security by never exposing opponent
            ship positions or other private game state. All information provided
            is what the player would legitimately know during actual gameplay.

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
            # Player's own attack results
            "your_hits": [c.model_dump() for c in player_state.board.successful_hits],
            "your_misses": [c.model_dump() for c in player_state.board.failed_attacks],
            "your_sunk_ships": [ship.value for ship in player_state.board.sunk_ships],
            # Opponent's attack results (but not ship positions)
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
            # Complete game history for pattern analysis
            "move_history": [(p, m.model_dump()) for p, m in self.move_history],
            "your_analysis": player_state.strategic_analysis,
            # Structured output compatibility for LLM processing
            "row": None,  # Compatibility field for move generation
            "col": None,  # Compatibility field for move generation
        }

    @computed_field
    @property
    def game_statistics(self) -> dict[str, int | float | str]:
        r"""Calculate comprehensive game statistics and metrics.

        Returns:
            Dict[str, Union[int, float, str]]: Dictionary containing game statistics.

        Examples:
            Analyzing game performance::\n

                stats = state.game_statistics
                print(f"Total moves: {stats['total_moves']}")
                print(f"Game duration: {stats['game_phase']}")

        """
        total_moves = len(self.move_history)

        # Calculate hit rates
        p1_hits = len(self.player1_state.board.successful_hits)
        p1_misses = len(self.player1_state.board.failed_attacks)
        p1_total = p1_hits + p1_misses
        p1_hit_rate = (p1_hits / p1_total) if p1_total > 0 else 0.0

        p2_hits = len(self.player2_state.board.successful_hits)
        p2_misses = len(self.player2_state.board.failed_attacks)
        p2_total = p2_hits + p2_misses
        p2_hit_rate = (p2_hits / p2_total) if p2_total > 0 else 0.0

        return {
            "total_moves": total_moves,
            "game_phase": self.game_phase.value,
            "current_player": self.current_player,
            "winner": self.winner or "None",
            "player1_hit_rate": round(p1_hit_rate, 3),
            "player2_hit_rate": round(p2_hit_rate, 3),
            "player1_ships_sunk": len(self.player1_state.board.sunk_ships),
            "player2_ships_sunk": len(self.player2_state.board.sunk_ships),
            "setup_complete": self.is_setup_complete(),
            "game_over": self.is_game_over(),
        }
