"""State manager for the Mancala game.

This module defines the state manager for the Mancala game,
which manages the state of the game and provides methods for initializing,
updating, and analyzing the game state.
"""

import json
from typing import Any, List

from haive.games.framework.base.state_manager import GameStateManager
from haive.games.mancala.models import MancalaAnalysis, MancalaMove
from haive.games.mancala.state import MancalaState


class MancalaStateManager(GameStateManager[MancalaState]):
    """Manager for Mancala game state.

    This class provides methods for initializing, updating, and analyzing the game state.
    """

    @classmethod
    def initialize(cls, **kwargs) -> MancalaState:
        """Initialize a new Mancala game with a fresh board and default settings.

        Args:
            **kwargs: Keyword arguments for game initialization.
                stones_per_pit: Number of stones per pit initially. Defaults to 4.
                Other keyword arguments are passed to the MancalaState constructor.

        Returns:
            MancalaState: A new Mancala game state ready to play.

        Note:
            The board is initialized with the following layout:
            - Indices 0-5: Player 1's pits (bottom row, left to right)
            - Index 6: Player 1's store (right)
            - Indices 7-12: Player 2's pits (top row, right to left)
            - Index 13: Player 2's store (left)
        """
        stones_per_pit = kwargs.get("stones_per_pit", 4)

        # Create the initial board with the proper layout
        # - Indices 0-5: Player 1's pits (bottom row)
        # - Index 6: Player 1's store (right)
        # - Indices 7-12: Player 2's pits (top row)
        # - Index 13: Player 2's store (left)
        board = [stones_per_pit] * 14
        board[6] = 0  # Player 1's store
        board[13] = 0  # Player 2's store

        return MancalaState(
            board=board,
            turn="player1",  # Player 1 starts
            game_status="ongoing",
            move_history=[],
            free_turn=False,
        )

    @classmethod
    def get_legal_moves(cls, state: MancalaState) -> list[MancalaMove]:
        """Get all legal moves for the current player in the given state.

        Args:
            state: The current game state.

        Returns:
            List[MancalaMove]: A list of all legal moves for the current player.
            Each move is represented as a MancalaMove object with pit_index (0-5)
            and player fields.

        Note:
            Pit indices are always 0-5 for both players, representing the six pits
            on their side of the board (not including their store).
        """
        legal_moves = []
        player = state.turn

        # Determine which pits to check based on the current player
        if player == "player1":
            # Player 1's pits are indices 0-5
            for i in range(6):
                if state.board[i] > 0:
                    legal_moves.append(MancalaMove(pit_index=i, player=player))
        else:
            # Player 2's pits are indices 7-12
            for i in range(7, 13):
                if state.board[i] > 0:
                    # Convert to 0-5 for consistent interface
                    pit_index = i - 7
                    legal_moves.append(MancalaMove(pit_index=pit_index, player=player))

        return legal_moves

    @classmethod
    def apply_move(cls, state: MancalaState, move: MancalaMove) -> MancalaState:
        """Apply a move to the current state according to Mancala rules.

        This method distributes stones from the selected pit, handles captures,
        checks for free turns, and updates the game status.

        Args:
            state: The current game state.
            move: The move to apply, containing pit_index (0-5) and player.

        Returns:
            MancalaState: A new game state after applying the move.

        Raises:
            ValueError: If the move is invalid (wrong player's turn, empty pit, etc.).

        Game Rules Implemented:
            1. Stones are distributed counterclockwise, one per pit.
            2. Player's own store is included; opponent's store is skipped.
            3. If the last stone lands in the player's store, they get another turn.
            4. If the last stone lands in an empty pit on the player's side, they
               capture that stone and all stones in the opposite pit.
            5. Game ends when all pits on one side are empty.
        """
        # Validate player's turn
        if move.player != state.turn:
            raise ValueError(f"Not {move.player}'s turn")

        # Convert to actual board index
        start_pit = move.pit_index if move.player == "player1" else move.pit_index + 7

        # Validate the move
        if state.board[start_pit] == 0:
            raise ValueError(f"Pit {move.pit_index} is empty")

        # Create a new state
        new_state = state.model_copy()
        new_state.free_turn = False  # Reset free turn flag

        # Get stones from the starting pit
        stones = new_state.board[start_pit]
        new_state.board[start_pit] = 0

        # Sow the stones
        current_pit = start_pit
        player_store = 6 if move.player == "player1" else 13
        opponent_store = 13 if move.player == "player1" else 6

        while stones > 0:
            current_pit = (current_pit + 1) % 14

            # Skip opponent's store
            if current_pit == opponent_store:
                continue

            # Add a stone to the current pit
            new_state.board[current_pit] += 1
            stones -= 1

        # Check for capture
        last_pit = current_pit
        if last_pit != player_store and new_state.board[last_pit] == 1:
            # The last stone landed in an empty pit on the player's side
            if (move.player == "player1" and 0 <= last_pit < 6) or (
                move.player == "player2" and 7 <= last_pit < 13
            ):
                # Calculate the opposite pit (12 - last_pit)
                # This works because:
                # - Pit 0 is opposite to pit 12
                # - Pit 1 is opposite to pit 11
                # ... and so on
                opposite_pit = 12 - last_pit

                # If the opposite pit has stones, capture them
                if new_state.board[opposite_pit] > 0:
                    # Add the stones from both pits to the player's store
                    new_state.board[player_store] += (
                        new_state.board[last_pit] + new_state.board[opposite_pit]
                    )
                    new_state.board[last_pit] = 0
                    new_state.board[opposite_pit] = 0

        # Check for free turn
        if last_pit == player_store:
            new_state.free_turn = True

        # Add move to history
        new_state.move_history.append(move)

        # Switch turns if no free turn
        if not new_state.free_turn:
            new_state.turn = "player2" if move.player == "player1" else "player1"

        # Check game status
        return cls.check_game_status(new_state)

    @classmethod
    def check_game_status(cls, state: MancalaState) -> MancalaState:
        """Check and update the game status.

        Args:
            state: The current game state.

        Returns:
            MancalaState: The game state with updated status.
        """
        # Check if any player's side is empty
        player1_empty = all(state.board[i] == 0 for i in range(6))
        player2_empty = all(state.board[i] == 0 for i in range(7, 13))

        if player1_empty or player2_empty:
            # Game is over, collect remaining stones
            if player1_empty:
                # Add player2's stones to their store
                for i in range(7, 13):
                    state.board[13] += state.board[i]
                    state.board[i] = 0
            else:
                # Add player1's stones to their store
                for i in range(6):
                    state.board[6] += state.board[i]
                    state.board[i] = 0

            # Determine the winner
            if state.player1_score > state.player2_score:
                state.game_status = "player1_win"
                state.winner = "player1"
            elif state.player2_score > state.player1_score:
                state.game_status = "player2_win"
                state.winner = "player2"
            else:
                state.game_status = "draw"
                state.winner = None

        return state

    @classmethod
    def get_winner(cls, state: MancalaState) -> str | None:
        """Get the winner of the game, if any.

        Args:
            state: The current game state.

        Returns:
            Optional[str]: The winner, or None if the game is ongoing or a draw.
        """
        if state.game_status == "player1_win":
            return "player1"
        if state.game_status == "player2_win":
            return "player2"
        return None

    @classmethod
    def add_analysis(
        cls, state: MancalaState, player: str, analysis: Any
    ) -> MancalaState:
        """Add an analysis to the state.

        Args:
            state: The current game state.
            player: The player who performed the analysis.
            analysis: The analysis to add.

        Returns:
            MancalaState: Updated state with the analysis added.
        """
        from haive.games.mancala.models import MancalaAnalysis

        # Create a copy of the state
        new_state = state.model_copy()

        # Ensure analysis is of the correct type
        if not isinstance(analysis, MancalaAnalysis):
            import json

            from langchain_core.messages import AIMessage

            # Try to convert AIMessage to MancalaAnalysis
            if isinstance(analysis, AIMessage):
                try:
                    # Check additional_kwargs for tool_calls
                    if (
                        hasattr(analysis, "additional_kwargs")
                        and "tool_calls" in analysis.additional_kwargs
                    ):
                        tool_calls = analysis.additional_kwargs["tool_calls"]
                        if tool_calls and len(tool_calls) > 0:
                            # Get the first tool call
                            tool_call = tool_calls[0]
                            # Parse the arguments from the function
                            if (
                                "function" in tool_call
                                and "arguments" in tool_call["function"]
                            ):
                                # Parse the JSON string in arguments
                                args = json.loads(tool_call["function"]["arguments"])
                                analysis = MancalaAnalysis(**args)
                except Exception as e:
                    # If conversion fails, log error but continue
                    print(f"Error converting AIMessage to MancalaAnalysis: {e}")
                    # Return state unchanged
                    return state

        # Add analysis field if it doesn't exist
        if not hasattr(new_state, f"{player}_analysis"):
            setattr(new_state, f"{player}_analysis", [])

        # Add the analysis
        getattr(new_state, f"{player}_analysis").append(analysis)

        return new_state
