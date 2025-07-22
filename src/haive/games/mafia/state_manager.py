"""State management for the Mafia game.

This module provides the core state management functionality for the Mafia game,
handling game state transitions, move validation, and game progression logic.

The state manager is responsible for:
    - Game initialization and setup
    - Phase transitions (day/night cycles)
    - Move validation and application
    - Game state filtering for information hiding
    - Win condition checking
"""

import random
from typing import Any

from loguru import logger

from .framework.multi_player.state_manager import MultiPlayerGameStateManager
from .mafia.models import (
    ActionType,
    GamePhase,
    MafiaAction,
    NarratorAction,
    PlayerRole,
    PlayerState,
)
from .mafia.state import MafiaGameState


class MafiaStateManager(MultiPlayerGameStateManager[MafiaGameState]):
    """Manager for the Mafia game state.

    This class extends MultiPlayerGameStateManager to provide Mafia-specific
    state management functionality. It handles game progression, move validation,
    and state transitions.

    The manager maintains game state including:
        - Player roles and alive/dead status
        - Day/night cycle progression
        - Vote tracking and resolution
        - Night action resolution (kills, saves, investigations)
        - Win condition checking

    Note:
        This class is designed to be used statically, with all methods being
        class methods that take and return game states.
    """

    @classmethod
    def advance_phase(cls, state: MafiaGameState) -> MafiaGameState:
        """Advance the game to the next phase.

        This method handles the transition between game phases, including:
            - Setup → Night (first night)
            - Night → Day Discussion (with night action resolution)
            - Day Discussion → Day Voting
            - Day Voting → Night (with vote resolution)
            - Game Over checks at appropriate points

        Args:
            state: Current game state

        Returns:
            Updated game state with new phase and relevant changes
        """
        # Create a deep copy of the state to avoid modifying the original
        new_state = state.model_copy(deep=True)

        # Get the current phase
        current_phase = new_state.game_phase

        logger.debug(f"Advancing phase from {current_phase}")

        # Phase transition logic
        if current_phase == GamePhase.SETUP:
            # From SETUP, transition to NIGHT for the first night
            new_state.game_phase = GamePhase.NIGHT
            new_state.day_number = 1
            new_state.round_number += 1

            new_state.add_public_announcement(
                f"Night {new_state.day_number} falls upon the village. The residents go to sleep."
            )

        elif current_phase == GamePhase.NIGHT:
            # From NIGHT, transition to DAY_DISCUSSION
            new_state.game_phase = GamePhase.DAY_DISCUSSION
            new_state.add_public_announcement(
                f"Day {new_state.day_number} begins. The village awakens."
            )

            # Process night actions (usually done by narrator in their turn)
            # This is a fallback if narrator didn't process them
            if (
                new_state.killed_at_night
                and new_state.killed_at_night != new_state.saved_at_night
            ):
                victim_id = new_state.killed_at_night
                if victim_id in new_state.player_states:
                    new_state.player_states[victim_id].is_alive = False
                    new_state.add_public_announcement(
                        f"{victim_id} was found dead this morning!"
                    )

                    # Update alive counts
                    role = new_state.roles.get(victim_id)
                    if role == PlayerRole.MAFIA:
                        new_state.alive_mafia_count = max(
                            0, new_state.alive_mafia_count - 1
                        )
                    else:
                        new_state.alive_village_count = max(
                            0, new_state.alive_village_count - 1
                        )

        elif current_phase == GamePhase.DAY_DISCUSSION:
            # From DAY_DISCUSSION, transition to DAY_VOTING
            new_state.game_phase = GamePhase.DAY_VOTING
            new_state.votes = {}  # Reset votes
            new_state.add_public_announcement(
                "The discussion period has ended. Time to vote!"
            )

        elif current_phase == GamePhase.DAY_VOTING:
            # From DAY_VOTING, transition to NIGHT (or GAME_OVER if end conditions met)
            # Process votes first
            if new_state.votes:
                # Count votes
                vote_count: dict[str, int] = {}
                for _, voted_for in new_state.votes.items():
                    vote_count[voted_for] = vote_count.get(voted_for, 0) + 1

                # Find player with most votes (handle ties by random selection)
                max_votes = max(vote_count.values()) if vote_count else 0
                tied_players = [
                    player for player, count in vote_count.items() if count == max_votes
                ]

                # Eliminate the chosen player
                if tied_players:
                    eliminated_player = (
                        random.choice(tied_players)
                        if len(tied_players) > 1
                        else tied_players[0]
                    )
                    if eliminated_player in new_state.player_states:
                        new_state.player_states[eliminated_player].is_alive = False
                        new_state.add_public_announcement(
                            f"{eliminated_player} has been eliminated by the village vote!"
                        )

                        # Update alive counts
                        role = new_state.roles.get(eliminated_player)
                        if role == PlayerRole.MAFIA:
                            new_state.alive_mafia_count = max(
                                0, new_state.alive_mafia_count - 1
                            )
                        else:
                            new_state.alive_village_count = max(
                                0, new_state.alive_village_count - 1
                            )

            # Check game end conditions
            if new_state.alive_mafia_count == 0:
                new_state.game_phase = GamePhase.GAME_OVER
                new_state.winner = "village"
                new_state.game_status = "ended"
                new_state.add_public_announcement(
                    "All mafia members have been eliminated! The village wins!"
                )
                return new_state

            if new_state.alive_mafia_count >= new_state.alive_village_count:
                new_state.game_phase = GamePhase.GAME_OVER
                new_state.winner = "mafia"
                new_state.game_status = "ended"
                new_state.add_public_announcement(
                    "The mafia now equals or outnumbers the villagers! The mafia wins!"
                )
                return new_state

            # Continue to next night
            new_state.game_phase = GamePhase.NIGHT
            new_state.day_number += 1
            new_state.round_number += 1
            new_state.killed_at_night = None
            new_state.saved_at_night = None
            new_state.add_public_announcement(
                f"Night {new_state.day_number} falls. The village sleeps."
            )

        elif current_phase == GamePhase.GAME_OVER:
            # Game is already over, do nothing
            pass

        # Reset current player to the first alive player for the new phase
        if current_phase != GamePhase.GAME_OVER:
            alive_players = [
                idx
                for idx, pid in enumerate(new_state.players)
                if pid in new_state.player_states
                and new_state.player_states[pid].is_alive
            ]
            if alive_players:
                new_state.current_player_idx = alive_players[0]

        return new_state

    @classmethod
    def resolve_night_actions(cls, state: MafiaGameState) -> MafiaGameState:
        """Resolve night actions and determine outcomes.

        This method processes all night actions in the correct order:
            1. Mafia kill attempt
            2. Doctor save attempt
            3. Detective investigation results

        Args:
            state: Current game state with night actions recorded

        Returns:
            Updated state with night actions resolved
        """
        new_state = state.model_copy(deep=True)

        # Check for mafia kill
        killed_player = new_state.killed_at_night
        saved_player = new_state.saved_at_night

        # Log night actions for debugging
        logger.info(f"Night actions - Kill: {killed_player}, Save: {saved_player}")

        # If doctor saved the target, they survive
        if killed_player and saved_player and killed_player == saved_player:
            logger.info(f"Doctor saved {saved_player} from being killed!")
            # Reset night action tracking
            new_state.killed_at_night = None
            new_state.saved_at_night = None
            return new_state

        # If kill wasn't prevented
        if killed_player and killed_player in new_state.player_states:
            # Mark player as dead
            new_state.player_states[killed_player].is_alive = False

            # Track night deaths
            new_state.night_deaths.append(killed_player)

            # Update alive counts
            role = new_state.roles.get(killed_player)
            if role == PlayerRole.MAFIA:
                new_state.alive_mafia_count = max(0, new_state.alive_mafia_count - 1)
                logger.info(f"Mafia member {killed_player} was killed at night")
            elif role and role != PlayerRole.NARRATOR:
                new_state.alive_village_count = max(
                    0, new_state.alive_village_count - 1
                )
                logger.info(f"Villager {killed_player} was killed at night")

        # Reset night action tracking
        new_state.killed_at_night = None
        new_state.saved_at_night = None

        return new_state

    @classmethod
    def handle_phase_transition(cls, state: MafiaGameState) -> MafiaGameState:
        """Handle phase transition with error handling.

        This method safely transitions the game phase, handling any errors
        that might occur during the transition.

        Args:
            state: Current game state

        Returns:
            Updated state after phase transition

        Raises:
            ValueError: If critical game state fields are missing
        """
        logger.debug(f"Handling phase transition for state: {state.game_phase}")

        try:
            # Use the state manager to advance the phase
            new_state = cls.advance_phase(state)

            # Set current player to the first alive player for the new phase
            alive_players = [
                idx
                for idx, pid in enumerate(new_state.players)
                if pid in new_state.player_states
                and new_state.player_states[pid].is_alive
            ]
            if alive_players:
                new_state.current_player_idx = alive_players[0]
            else:
                new_state.current_player_idx = 0

            return new_state

        except Exception as e:
            error_msg = f"Error in phase transition: {e!s}"
            logger.error(error_msg, exc_info=True)

            # Try to set error on state
            try:
                error_state = state.model_copy(deep=True)
                error_state.error_message = error_msg
                error_state.game_status = "ended"
                return error_state
            except:
                # If we can't even copy the state, create a minimal error state
                return MafiaGameState(
                    players=state.players if hasattr(state, "players") else [],
                    current_player_idx=0,
                    roles={},
                    player_states={},
                    game_phase=GamePhase.GAME_OVER,
                    game_status="ended",
                    error_message=error_msg,
                    alive_mafia_count=0,
                    alive_village_count=0,
                )

    @classmethod
    def apply_move(
        cls,
        state: MafiaGameState,
        player_id: str,
        move: MafiaAction | NarratorAction,
    ) -> MafiaGameState:
        """Apply a move to the game state.

        This method validates and applies a player's move or narrator's action
        to the game state, updating all relevant state fields.

        Args:
            state: Current game state
            player_id: ID of the player making the move
            move: Move to apply

        Returns:
            Updated game state after applying the move
        """
        # Create a copy of state
        new_state = state.model_copy(deep=True)

        # Handle MafiaAction
        if isinstance(move, MafiaAction):
            # Add action to history
            new_state.action_history.append(move)

            # Handle different action types
            if move.action_type == ActionType.SPEAK:
                # Add message to public announcements
                if move.message:
                    new_state.add_public_announcement(f"{player_id}: {move.message}")

            elif move.action_type == ActionType.VOTE:
                # Record vote
                if move.target_id:
                    new_state.votes[player_id] = move.target_id
                    # Add to public announcements
                    new_state.add_public_announcement(
                        f"{player_id} has voted for {move.target_id}."
                    )

            elif (
                move.action_type == ActionType.KILL
                and new_state.game_phase == GamePhase.NIGHT
            ):
                # Record kill target
                if move.target_id:
                    new_state.killed_at_night = move.target_id

            elif (
                move.action_type == ActionType.INVESTIGATE
                and new_state.game_phase == GamePhase.NIGHT
            ):
                # Perform investigation
                if move.target_id:
                    target_id = move.target_id
                    is_mafia = new_state.roles.get(target_id) == PlayerRole.MAFIA

                    # Store investigation result
                    if player_id in new_state.player_states:
                        if not hasattr(
                            new_state.player_states[player_id], "investigation_results"
                        ):
                            new_state.player_states[player_id].investigation_results = (
                                {}
                            )

                        new_state.player_states[player_id].investigation_results[
                            target_id
                        ] = is_mafia

            elif (
                move.action_type == ActionType.SAVE
                and new_state.game_phase == GamePhase.NIGHT
            ):
                # Record save target
                if move.target_id:
                    new_state.saved_at_night = move.target_id

        # Handle NarratorAction
        elif isinstance(move, NarratorAction):
            # Add action to history
            new_state.action_history.append(move)

            # Add announcement to public announcements
            if move.announcement:
                new_state.add_public_announcement(move.announcement)

            # Handle phase transition if requested
            if move.phase_transition:
                new_state = cls.handle_phase_transition(new_state)

        return new_state

    @classmethod
    def initialize(cls, player_names: list[str], **kwargs) -> MafiaGameState:
        """Initialize a new Mafia game with the given players.

        This method sets up a new game state with:
            - Random role assignment
            - Initial player states
            - Game phase setup
            - Role knowledge distribution

        Args:
            player_names: List of player names/IDs
            **kwargs: Additional configuration options
                include_all_roles: Force inclusion of all special roles

        Returns:
            Initial game state

        Raises:
            ValueError: If there aren't enough players (minimum 4)
        """
        # Ensure player_names is a non-None iterable
        if player_names is None:
            logger.warning("Received None for player_names, using default list")
            player_names = ["Player_1", "Player_2", "Player_3", "Narrator"]

        # Ensure player_names is a list
        if not isinstance(player_names, list):
            try:
                player_names = list(player_names)
            except TypeError:
                logger.warning("Could not convert player_names to list, using default")
                player_names = ["Player_1", "Player_2", "Player_3", "Narrator"]

        # Ensure player_names is not empty
        if not player_names:
            logger.warning("Received empty player_names list, using default")
            player_names = ["Player_1", "Player_2", "Player_3", "Narrator"]

        # Ensure we have enough players (at least 3 plus narrator)
        if len(player_names) < 4:
            logger.warning("Not enough players provided, using minimum 4 players")
            # Add default players to reach minimum count
            current_count = len(player_names)
            for i in range(current_count, 4):
                player_names.append(f"Player_{i+1}")
            # Ensure the last player is the narrator
            if "Narrator" not in player_names:
                player_names[-1] = "Narrator"

        # Separate regular players from narrator
        narrator_id = player_names[-1]
        regular_players = player_names[:-1]
        num_regular_players = len(regular_players)

        # Calculate role counts based on player count
        num_mafia = max(1, num_regular_players // 4)
        num_detectives = 1 if num_regular_players >= 6 else 0
        num_doctors = 1 if num_regular_players >= 7 else 0

        # Override for testing/debugging
        if kwargs.get("include_all_roles", False) and num_regular_players >= 3:
            num_mafia = max(1, min(num_regular_players // 3, num_mafia))
            num_detectives = min(1, num_regular_players - num_mafia - 1)
            num_doctors = min(1, num_regular_players - num_mafia - num_detectives - 1)

        # Initialize roles dictionary
        roles: dict[str, PlayerRole] = {narrator_id: PlayerRole.NARRATOR}

        # Shuffle players for random role assignment
        shuffled_players = list(regular_players)
        random.shuffle(shuffled_players)

        # Assign roles
        role_idx = 0

        # Assign mafia
        for i in range(num_mafia):
            if role_idx < len(shuffled_players):
                roles[shuffled_players[role_idx]] = PlayerRole.MAFIA
                role_idx += 1

        # Assign detective
        for i in range(num_detectives):
            if role_idx < len(shuffled_players):
                roles[shuffled_players[role_idx]] = PlayerRole.DETECTIVE
                role_idx += 1

        # Assign doctor
        for i in range(num_doctors):
            if role_idx < len(shuffled_players):
                roles[shuffled_players[role_idx]] = PlayerRole.DOCTOR
                role_idx += 1

        # Assign villager to remaining players
        while role_idx < len(shuffled_players):
            roles[shuffled_players[role_idx]] = PlayerRole.VILLAGER
            role_idx += 1

        # Initialize player states
        player_states: dict[str, PlayerState] = {}
        for player_id in player_names:
            role = roles.get(player_id, PlayerRole.VILLAGER)

            # Initialize known roles
            known_roles = {player_id: role}

            # Mafia know who other mafia are
            if role == PlayerRole.MAFIA:
                for pid, r in roles.items():
                    if r == PlayerRole.MAFIA:
                        known_roles[pid] = r

            # Narrator knows all roles
            if role == PlayerRole.NARRATOR:
                known_roles = roles.copy()

            player_states[player_id] = PlayerState(
                player_id=player_id,
                role=role,
                is_alive=True,
                known_roles=known_roles,
                investigation_results={},
            )

        # Count alive players by role
        alive_mafia_count = sum(
            1 for role in roles.values() if role == PlayerRole.MAFIA
        )
        alive_village_count = sum(
            1
            for role in roles.values()
            if role not in [PlayerRole.MAFIA, PlayerRole.NARRATOR]
        )

        # Create the initial state
        state = MafiaGameState(
            players=player_names,
            current_player_idx=0,
            roles=roles,
            player_states=player_states,
            game_phase=GamePhase.SETUP,
            game_status="ongoing",
            move_history=[],
            action_history=[],
            public_announcements=["The game of Mafia begins!"],
            alive_mafia_count=alive_mafia_count,
            alive_village_count=alive_village_count,
            votes={},
            day_number=0,
            round_number=0,
            killed_at_night=None,
            saved_at_night=None,
            night_deaths=[],
            winner=None,
            error_message=None,
        )

        return state

    @classmethod
    def get_legal_moves(
        cls, state: MafiaGameState, player_id: str
    ) -> list[MafiaAction | NarratorAction]:
        """Get legal moves for a specific player.

        This method determines what moves are legal for a player based on:
            - Current game phase
            - Player's role
            - Player's alive/dead status
            - Previous actions in the current phase

        Args:
            state: Current game state
            player_id: ID of the player to get moves for

        Returns:
            List of legal moves (MafiaAction or NarratorAction)
        """
        legal_moves: list[MafiaAction | NarratorAction] = []

        # Check if player exists
        if player_id not in state.player_states:
            return legal_moves

        player_state = state.player_states[player_id]
        player_role = state.roles.get(player_id)

        # Check if player is alive (except for narrator)
        if not player_state.is_alive and player_role != PlayerRole.NARRATOR:
            return legal_moves

        # Narrator moves
        if player_role == PlayerRole.NARRATOR:
            # Narrator can always make announcements
            legal_moves.append(
                NarratorAction(
                    announcement="[Example announcement]",
                    player_state_updates={},
                    phase_transition=False,
                    round_number=state.round_number,
                )
            )

            # Narrator can transition phases if appropriate
            if state.game_phase in [
                GamePhase.SETUP,
                GamePhase.NIGHT,
                GamePhase.DAY_DISCUSSION,
                GamePhase.DAY_VOTING,
            ]:
                legal_moves.append(
                    NarratorAction(
                        announcement="Transitioning to next phase...",
                        player_state_updates={},
                        phase_transition=True,
                        round_number=state.round_number,
                    )
                )

            return legal_moves

        # Player moves based on game phase
        if state.game_phase in [GamePhase.DAY_DISCUSSION, GamePhase.DAY_VOTING]:
            # All players can speak during the day
            legal_moves.append(
                MafiaAction(
                    player_id=player_id,
                    action_type=ActionType.SPEAK,
                    message="[Your message here]",
                    phase=state.game_phase,
                    round_number=state.round_number,
                )
            )

        if state.game_phase == GamePhase.DAY_VOTING:
            # All players can vote during voting phase
            for target_id, target_state in state.player_states.items():
                # Can only vote for alive players other than yourself
                if (
                    target_state.is_alive
                    and target_id != player_id
                    and state.roles.get(target_id) != PlayerRole.NARRATOR
                ):
                    legal_moves.append(
                        MafiaAction(
                            player_id=player_id,
                            action_type=ActionType.VOTE,
                            target_id=target_id,
                            phase=state.game_phase,
                            round_number=state.round_number,
                        )
                    )

        if state.game_phase == GamePhase.NIGHT:
            # Night actions based on roles
            if player_role == PlayerRole.MAFIA:
                # Mafia can kill during the night
                for target_id, target_state in state.player_states.items():
                    # Can only kill alive non-mafia players
                    if target_state.is_alive and state.roles.get(target_id) not in [
                        PlayerRole.MAFIA,
                        PlayerRole.NARRATOR,
                    ]:
                        legal_moves.append(
                            MafiaAction(
                                player_id=player_id,
                                action_type=ActionType.KILL,
                                target_id=target_id,
                                phase=state.game_phase,
                                round_number=state.round_number,
                            )
                        )

            elif player_role == PlayerRole.DOCTOR:
                # Doctor can save during the night
                for target_id, target_state in state.player_states.items():
                    # Can save any alive player except narrator
                    if (
                        target_state.is_alive
                        and state.roles.get(target_id) != PlayerRole.NARRATOR
                    ):
                        legal_moves.append(
                            MafiaAction(
                                player_id=player_id,
                                action_type=ActionType.SAVE,
                                target_id=target_id,
                                phase=state.game_phase,
                                round_number=state.round_number,
                            )
                        )

            elif player_role == PlayerRole.DETECTIVE:
                # Detective can investigate during the night
                for target_id, target_state in state.player_states.items():
                    # Can investigate any alive player other than themselves and narrator
                    if (
                        target_state.is_alive
                        and target_id != player_id
                        and state.roles.get(target_id) != PlayerRole.NARRATOR
                    ):
                        legal_moves.append(
                            MafiaAction(
                                player_id=player_id,
                                action_type=ActionType.INVESTIGATE,
                                target_id=target_id,
                                phase=state.game_phase,
                                round_number=state.round_number,
                            )
                        )

        return legal_moves

    @classmethod
    def check_game_status(cls, state: MafiaGameState) -> MafiaGameState:
        """Check if the game has ended and determine the winner.

        This method checks win conditions:
            - Village wins if all mafia are dead
            - Mafia wins if they equal/outnumber villagers

        Args:
            state: Current game state

        Returns:
            Updated state with game status and winner if game is over
        """
        new_state = state.model_copy(deep=True)

        # Game ends if all mafia are dead (village wins)
        if new_state.alive_mafia_count == 0:
            new_state.game_status = "ended"
            new_state.winner = "village"
            new_state.game_phase = GamePhase.GAME_OVER
            new_state.add_public_announcement(
                "All mafia members have been eliminated! The village wins!"
            )
            logger.info("Game over: Village wins (all mafia eliminated)")

        # Game ends if mafia equals or outnumbers villagers (mafia wins)
        elif new_state.alive_mafia_count >= new_state.alive_village_count:
            new_state.game_status = "ended"
            new_state.winner = "mafia"
            new_state.game_phase = GamePhase.GAME_OVER
            new_state.add_public_announcement(
                "The mafia has won! They now equal or outnumber the villagers."
            )
            logger.info("Game over: Mafia wins (villagers outnumbered)")

        return new_state

    @classmethod
    def filter_state_for_player(
        cls, state: MafiaGameState, player_id: str
    ) -> dict[str, Any]:
        """Filter the state to include only information visible to a specific player.

        This method implements information hiding, ensuring players only see
        information they should have access to based on their role and the
        game phase.

        Args:
            state: Full game state
            player_id: ID of the player to filter for

        Returns:
            Filtered state containing only visible information
        """
        # Create a filtered copy of the state
        filtered_state: dict[str, Any] = {}

        # Basic game information visible to all
        filtered_state["players"] = state.players
        filtered_state["game_phase"] = state.game_phase.value
        filtered_state["day_number"] = state.day_number
        filtered_state["round_number"] = state.round_number
        filtered_state["public_announcements"] = state.public_announcements
        filtered_state["game_status"] = state.game_status

        # Information about who is alive
        filtered_state["alive_players"] = [
            pid for pid, p_state in state.player_states.items() if p_state.is_alive
        ]
        filtered_state["dead_players"] = [
            pid for pid, p_state in state.player_states.items() if not p_state.is_alive
        ]

        # Player's own information
        if player_id in state.player_states:
            player_state = state.player_states[player_id]
            filtered_state["my_role"] = state.roles.get(
                player_id, PlayerRole.VILLAGER
            ).value
            filtered_state["known_roles"] = {
                pid: role.value for pid, role in player_state.known_roles.items()
            }

            # Add investigation results for detectives
            if state.roles.get(player_id) == PlayerRole.DETECTIVE:
                filtered_state["investigation_results"] = (
                    player_state.investigation_results
                )

        # During voting, everyone can see the votes
        if state.game_phase == GamePhase.DAY_VOTING:
            filtered_state["votes"] = state.votes

        # Game over information
        if state.game_phase == GamePhase.GAME_OVER:
            filtered_state["winner"] = state.winner
            # Reveal all roles at game end
            filtered_state["all_roles"] = {
                pid: role.value for pid, role in state.roles.items()
            }

        # Narrator can see everything
        if state.roles.get(player_id) == PlayerRole.NARRATOR:
            filtered_state["full_state"] = {
                "roles": {pid: role.value for pid, role in state.roles.items()},
                "player_states": {
                    pid: {
                        "is_alive": p_state.is_alive,
                        "role": state.roles.get(pid, PlayerRole.VILLAGER).value,
                        "known_roles": {
                            k: v.value for k, v in p_state.known_roles.items()
                        },
                        "investigation_results": getattr(
                            p_state, "investigation_results", {}
                        ),
                    }
                    for pid, p_state in state.player_states.items()
                },
                "killed_at_night": state.killed_at_night,
                "saved_at_night": state.saved_at_night,
                "alive_mafia_count": state.alive_mafia_count,
                "alive_village_count": state.alive_village_count,
            }

        return filtered_state
