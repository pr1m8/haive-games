"""Comprehensive state management mixin for Among Us social deduction gameplay.

This module provides the core state management functionality for Among Us games,
handling complex game mechanics including role assignments, task management,
sabotage systems, meeting coordination, and win condition evaluation. The state
manager coordinates all gameplay elements for authentic Among Us experiences.

The state manager handles:
- Game initialization with role assignments and task generation
- Move validation and application for all player actions
- Complex sabotage mechanics with resolution systems
- Meeting and voting coordination
- Win condition evaluation and game progression
- Player state filtering for information hiding
- Legal move generation for AI decision-making

Examples:
    Initializing a game::

        state = AmongUsStateManagerMixin.initialize(
            player_names=["Alice", "Bob", "Charlie", "David", "Eve"],
            map_name="skeld",
            num_impostors=1
        )

    Applying player moves::

        move = {"action": "move", "location": "electrical"}
        new_state = AmongUsStateManagerMixin.apply_move(state, "Alice", move)

    Checking game status::

        updated_state = AmongUsStateManagerMixin.check_game_status(state)
        if updated_state.game_status == "ended":
            print(f"Game over! Winner: {updated_state.winner}")

Note:
    This is a mixin class designed to be inherited by game agents,
    providing state management capabilities without agent-specific behavior.

"""

import random
from datetime import datetime
from typing import Any

from haive.games.among_us.models import (
    AmongUsGamePhase,
    PlayerMemory,
    PlayerRole,
    PlayerState,
    SabotageEvent,
    SabotageResolutionPoint,
    SabotageType,
    Task,
    TaskStatus,
    TaskType,
)
from haive.games.among_us.state import AmongUsState
from haive.games.framework.multi_player.state_manager import MultiPlayerGameStateManager


class AmongUsStateManagerMixin(MultiPlayerGameStateManager[AmongUsState]):
    """Comprehensive state management mixin for Among Us social deduction gameplay.

    This mixin class provides complete state management functionality for Among Us
    games, handling complex mechanics including role-based gameplay, task systems,
    sabotage mechanics, meeting coordination, and win condition evaluation. The
    class separates state management from agent behavior, allowing any inheriting
    class to gain full Among Us state management capabilities.

    The state manager handles:
    - Game initialization with intelligent role assignment
    - Task generation and completion tracking
    - Complex sabotage systems with resolution mechanics
    - Meeting and voting coordination
    - Move validation and application
    - Win condition evaluation
    - Player state filtering for information hiding
    - Legal move generation for AI systems

    Examples:
        Initializing a new game::

            state = AmongUsStateManagerMixin.initialize(
                player_names=["Alice", "Bob", "Charlie", "David", "Eve"],
                map_name="skeld",
                num_impostors=1,
                tasks_per_player=5
            )

        Applying player actions::

            # Player movement
            move = {"action": "move", "location": "electrical"}
            new_state = AmongUsStateManagerMixin.apply_move(state, "Alice", move)

            # Task completion
            task_move = {"action": "complete_task", "task_id": "Alice_task_1"}
            new_state = AmongUsStateManagerMixin.apply_move(state, "Alice", task_move)

            # Impostor actions
            kill_move = {"action": "kill", "target_id": "Bob"}
            new_state = AmongUsStateManagerMixin.apply_move(state, "Eve", kill_move)

        Checking game progression::

            updated_state = AmongUsStateManagerMixin.check_game_status(state)
            if updated_state.game_status == "ended":
                print(f"Game over! {updated_state.winner} wins!")

    Note:
        This mixin is designed to be inherited by game agents, providing
        state management capabilities without imposing specific agent behaviors.

    """

    @classmethod
    def initialize(cls, player_names: list[str], **kwargs) -> AmongUsState:
        """Initialize a new Among Us game state with intelligent defaults.

        Creates a complete game state with role assignments, task generation,
        map initialization, and all necessary game components. The initialization
        process follows standard Among Us rules for balanced gameplay.

        Args:
            player_names: List of player identifiers (4-15 players).
            **kwargs: Additional configuration options.
                map_name (str): Map to use (default: "skeld").
                num_impostors (int): Number of impostors (auto-calculated if None).
                tasks_per_player (int): Tasks per crewmate (default: 5).
                kill_cooldown (int): Impostor kill cooldown in seconds (default: 45).
                seed: Random seed for reproducible games.

        Returns:
            AmongUsState: Fully initialized game state ready for gameplay.

        Examples:
            Standard initialization::

                state = AmongUsStateManagerMixin.initialize(
                    player_names=["Alice", "Bob", "Charlie", "David", "Eve"],
                    map_name="skeld"
                )
                # Auto-assigns 1 impostor for 5 players

            Custom configuration::

                state = AmongUsStateManagerMixin.initialize(
                    player_names=["Player_" + str(i) for i in range(10)],
                    map_name="polus",
                    num_impostors=2,
                    tasks_per_player=6,
                    kill_cooldown=30,
                    seed=12345
                )

        Note:
            The initialization automatically balances impostor count based on
            player count following standard Among Us ratios.

        """
        # Set default map name
        map_name = kwargs.get("map_name", "skeld")

        # Create initial state with empty rooms and vents
        state = AmongUsState(
            players=player_names,
            current_player_idx=0,
            game_phase=AmongUsGamePhase.TASKS,
            game_status="ongoing",
            move_history=[],
            round_number=0,
            player_data={},  # Will use player_states instead
            public_state={},
            map_name=map_name,
            map_locations=[],  # Will be populated by initialize_map
            player_states={},
            tasks={},
            sabotages=[],
            eliminated_players=[],
            meeting_active=False,
            meeting_caller=None,
            reported_body=None,
            votes={},
            impostor_count=0,
            crewmate_count=0,
            discussion_history=[],
            rooms={},
            vents={},
            kill_cooldowns={},
        )

        # Initialize map rooms and vents
        state.initialize_map()

        # Get updated map locations
        map_locations = state.map_locations

        # Determine number of impostors based on player count
        num_players = len(player_names)
        num_impostors = kwargs.get("num_impostors", max(1, num_players // 5))

        # Randomly assign roles

        random.seed(kwargs.get("seed"))
        impostor_indices = random.sample(
            range(num_players), min(num_impostors, num_players)
        )

        # Create player states
        player_states = {}
        tasks_per_player = kwargs.get("tasks_per_player", 5)
        all_tasks = {}

        for i, player_name in enumerate(player_names):
            role = PlayerRole.IMPOSTOR if i in impostor_indices else PlayerRole.CREWMATE

            # Generate tasks for crewmates (impostors get fake tasks)
            player_tasks = []
            if role == PlayerRole.CREWMATE:
                for j in range(tasks_per_player):
                    task_id = f"{player_name}_task_{j}"
                    location = random.choice(map_locations)
                    task_type = random.choice(list(TaskType))
                    visual = task_type == TaskType.VISUAL

                    task = Task(
                        id=task_id,
                        type=task_type,
                        location=location,
                        description=cls._generate_task_description(task_type, location),
                        status=TaskStatus.NOT_STARTED,
                        visual_indicator=visual,
                    )
                    player_tasks.append(task)
                    all_tasks[task_id] = task
            else:
                # Fake tasks for impostors (not counted in completion)
                for j in range(tasks_per_player):
                    task_id = f"{player_name}_fake_task_{j}"
                    location = random.choice(map_locations)
                    task_type = random.choice(list(TaskType))

                    task = Task(
                        id=task_id,
                        type=task_type,
                        location=location,
                        description=cls._generate_task_description(task_type, location),
                        status=TaskStatus.NOT_STARTED,
                    )
                    player_tasks.append(task)

            # Create player memory
            memory = PlayerMemory(
                observations=[],
                player_suspicions={},
                player_alibis={},
                location_history=["cafeteria"],  # Starting location
            )

            # Create player state
            player_states[player_name] = PlayerState(
                id=player_name,
                role=role,
                location="cafeteria",  # Everyone starts in cafeteria
                tasks=player_tasks,
                is_alive=True,
                observations=[],
                memory=memory,
                in_vent=False,
                current_vent=None,
            )

            # Set kill cooldown for impostors
            if role == PlayerRole.IMPOSTOR:
                state.kill_cooldowns[player_name] = kwargs.get("kill_cooldown", 45)

        # Update state with player states and tasks
        state.player_states = player_states
        state.tasks = all_tasks
        state.impostor_count = num_impostors
        state.crewmate_count = num_players - num_impostors

        return state

    @classmethod
    def _generate_task_description(cls, task_type: TaskType, location: str) -> str:
        """Generate a realistic task description based on type and location.

        Creates authentic Among Us task descriptions that match the game's
        actual tasks, providing immersive gameplay experiences.

        Args:
            task_type: Type of task (VISUAL, COMMON, SHORT, LONG).
            location: Room where the task is located.

        Returns:
            str: Human-readable task description.

        Examples:
            Visual task generation::

                desc = cls._generate_task_description(TaskType.VISUAL, "medbay")
                # Returns: "Submit scan"

            Common task generation::

                desc = cls._generate_task_description(TaskType.COMMON, "admin")
                # Returns: "Swipe card"

            Fallback generation::

                desc = cls._generate_task_description(TaskType.SHORT, "unknown_room")
                # Returns: "Complete short task in unknown_room"

        """
        task_descriptions = {
            TaskType.VISUAL: {
                "medbay": "Submit scan",
                "weapons": "Clear asteroids",
                "shields": "Prime shields",
            },
            TaskType.COMMON: {
                "admin": "Swipe card",
                "electrical": "Divert power",
                "o2": "Empty garbage",
            },
            TaskType.SHORT: {
                "electrical": "Fix wiring",
                "navigation": "Chart course",
                "admin": "Download data",
            },
            TaskType.LONG: {
                "electrical": "Calibrate distributor",
                "navigation": "Stabilize steering",
                "medbay": "Inspect sample",
            },
        }

        # Get possible descriptions for this type and location
        possible_descriptions = task_descriptions.get(task_type, {}).get(location)
        if possible_descriptions:
            return possible_descriptions

        # Fallback descriptions by type
        fallback_by_type = {
            TaskType.VISUAL: "Perform visual task",
            TaskType.COMMON: "Complete common task",
            TaskType.SHORT: "Complete short task",
            TaskType.LONG: "Complete long task",
        }

        return f"{fallback_by_type[task_type]} in {location}"

    @classmethod
    def apply_move(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Apply a player's move to the game state with comprehensive validation.

        Processes and validates player moves, updating the game state accordingly.
        Handles all move types across different game phases with proper error
        handling and state consistency maintenance.

        Args:
            state: Current game state to modify.
            player_id: ID of the player making the move.
            move: Move dictionary containing action and parameters.

        Returns:
            AmongUsState: Updated game state after applying the move.

        Examples:
            Movement action::

                move = {"action": "move", "location": "electrical"}
                new_state = cls.apply_move(state, "Alice", move)

            Task completion::

                move = {"action": "complete_task", "task_id": "Alice_task_1"}
                new_state = cls.apply_move(state, "Alice", move)

            Impostor kill::

                move = {"action": "kill", "target_id": "Bob"}
                new_state = cls.apply_move(state, "Eve", move)

            Voting action::

                move = {"action": "vote", "vote_for": "Charlie"}
                new_state = cls.apply_move(state, "Alice", move)

        Note:
            The method creates a deep copy of the state to avoid modifying
            the original, ensuring state immutability.

        """
        # Create deep copy to avoid modifying original state
        state = state.model_copy(deep=True)

        # Validate player exists
        if player_id not in state.player_states:
            state.error_message = f"Player {player_id} not found"
            return state

        # Record the action in history
        action = {
            "player_id": player_id,
            "action_type": move.get("action"),
            "timestamp": datetime.now().isoformat(),
            "phase": state.game_phase,
            "round_number": state.round_number,
            "details": move,
        }
        state.move_history.append(action)

        # Update player's last action
        state.player_states[player_id].last_action = move.get("action")

        # Handle different action types based on game phase
        action_type = move.get("action")

        # Delegate to appropriate handler
        if state.game_phase == AmongUsGamePhase.TASKS:
            if action_type == "move":
                return cls._handle_move_action(state, player_id, move)
            if action_type == "complete_task":
                return cls._handle_complete_task_action(state, player_id, move)
            if action_type == "kill":
                return cls._handle_kill_action(state, player_id, move)
            if action_type == "report_body":
                return cls._handle_report_action(state, player_id, move)
            if action_type == "call_emergency_meeting":
                return cls._handle_emergency_meeting_action(state, player_id, move)
            if action_type == "sabotage":
                return cls._handle_sabotage_action(state, player_id, move)
            if action_type == "resolve_sabotage":
                return cls._handle_resolve_sabotage_action(state, player_id, move)
            if action_type == "vent":
                return cls._handle_vent_action(state, player_id, move)
            if action_type == "exit_vent":
                return cls._handle_exit_vent_action(state, player_id, move)

        elif state.game_phase == AmongUsGamePhase.MEETING:
            if action_type == "discuss":
                return cls._handle_discussion_action(state, player_id, move)

        elif state.game_phase == AmongUsGamePhase.VOTING:
            if action_type == "vote":
                return cls._handle_vote_action(state, player_id, move)

        # If we get here, the action wasn't handled
        state.error_message = (
            f"Invalid action '{action_type}' for phase '{state.game_phase}'"
        )
        return state

    # Action handlers for different game actions
    @classmethod
    def _handle_move_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle player movement with connection and sabotage validation.

        Validates and processes player movement between rooms, checking for
        room connections, blocked doors, and updating player location with
        proper observation generation.

        Args:
            state: Current game state.
            player_id: ID of the moving player.
            move: Move dictionary with target location.

        Returns:
            AmongUsState: Updated state with new player location.

        Examples:
            Valid movement::

                move = {"action": "move", "location": "electrical"}
                new_state = cls._handle_move_action(state, "Alice", move)

            Invalid movement (blocked door)::

                # If doors are sabotaged
                move = {"action": "move", "location": "electrical"}
                new_state = cls._handle_move_action(state, "Alice", move)
                # Returns state with error_message set

        """
        player_state = state.player_states[player_id]
        target_location = move.get("location")

        # Cannot move while in a vent
        if player_state.in_vent:
            state.error_message = "Cannot move to a new room while in a vent"
            return state

        # Validate location
        if target_location not in state.map_locations:
            state.error_message = f"Invalid location '{target_location}'"
            return state

        # Get current location for observation
        current_location = player_state.location

        # Check if rooms are connected
        current_room = state.get_room(current_location)
        if current_room and not current_room.is_connected_to(target_location):
            state.error_message = f"Cannot move directly from {current_location} to {target_location} - rooms are not connected"
            return state

        # Check if doors are locked between rooms (due to sabotage)
        if current_room:
            connection = current_room.get_connection(target_location)
            if connection and connection.is_blocked:
                state.error_message = (
                    f"The door to {target_location} is currently locked"
                )
                return state

        # Update player location
        player_state.location = target_location

        # Update player's memory location history
        player_state.memory.location_history.append(target_location)
        if len(player_state.memory.location_history) > 10:  # Keep only recent locations
            player_state.memory.location_history.pop(0)

        # Add observation about their movement for other players in
        # source/target
        observation = f"{player_id} moved from {current_location} to {target_location}"

        # Players in the target location observe the arrival
        state.add_observation_to_all_in_room(target_location, observation, [player_id])

        return state

    @classmethod
    def _handle_complete_task_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle task completion with role validation and visual task detection.

        Processes task completion for crewmates, validates task location and
        status, and generates appropriate observations for other players.
        Handles visual tasks specially for crewmate confirmation.

        Args:
            state: Current game state.
            player_id: ID of the player completing the task.
            move: Move dictionary with task ID.

        Returns:
            AmongUsState: Updated state with completed task.

        Examples:
            Crewmate task completion::

                move = {"action": "complete_task", "task_id": "Alice_task_1"}
                new_state = cls._handle_complete_task_action(state, "Alice", move)

            Impostor fake task::

                # Impostor pretending to do tasks
                move = {"action": "complete_task", "task_id": "fake_task"}
                new_state = cls._handle_complete_task_action(state, "Eve", move)
                # Creates fake observation without actually completing task

            Visual task completion::

                # Visual task provides crewmate confirmation
                move = {"action": "complete_task", "task_id": "scan_task"}
                new_state = cls._handle_complete_task_action(state, "Alice", move)
                # Generates "[CONFIRMED CREWMATE]" observation

        """
        player_state = state.player_states[player_id]
        task_id = move.get("task_id")

        # Validate player is a crewmate (impostors can't complete real tasks)
        if player_state.role != PlayerRole.CREWMATE:
            # Impostors pretend to do tasks but don't actually complete them
            # Add fake observation for impostor pretending to do task
            observation = f"{player_id} appears to be working on a task in {
                player_state.location
            }"
            state.add_observation_to_all_in_room(
                player_state.location, observation, [player_id]
            )
            return state

        # Find the task
        player_tasks = [t for t in player_state.tasks if t.id == task_id]
        if not player_tasks:
            state.error_message = f"Task {task_id} not found for player {player_id}"
            return state

        task = player_tasks[0]

        # Validate task is in the player's current location
        if task.location != player_state.location:
            state.error_message = f"Task {task_id} is not in this location"
            return state

        # Update task status
        for i, t in enumerate(player_state.tasks):
            if t.id == task_id:
                player_state.tasks[i].status = TaskStatus.COMPLETED
                break

        if task_id in state.tasks:
            state.tasks[task_id].status = TaskStatus.COMPLETED

        # Add observation for other players in the same location
        observation = (
            f"{player_id} completed a task ({task.description}) in {task.location}"
        )

        # For visual tasks, make it clearer that it was a visual task
        if task.visual_indicator or task.type == TaskType.VISUAL:
            observation = f"{player_id} completed a visual task ({
                task.description
            }) in {task.location} [CONFIRMED CREWMATE]"

        state.add_observation_to_all_in_room(
            player_state.location, observation, [player_id]
        )

        return state

    @classmethod
    def _handle_kill_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle impostor elimination with cooldown and witness validation.

        Processes impostor kill actions with comprehensive validation including
        role verification, cooldown checks, location validation, and witness
        detection. Updates player counts and applies kill cooldown.

        Args:
            state: Current game state.
            player_id: ID of the impostor player.
            move: Move dictionary with target player ID.

        Returns:
            AmongUsState: Updated state with eliminated player.

        Examples:
            Successful kill::

                move = {"action": "kill", "target_id": "Bob"}
                new_state = cls._handle_kill_action(state, "Eve", move)
                # Bob is eliminated, Eve gets cooldown

            Failed kill (witnesses)::

                # If other players are in the room
                move = {"action": "kill", "target_id": "Bob"}
                new_state = cls._handle_kill_action(state, "Eve", move)
                # Returns state with error_message about witnesses

            Failed kill (cooldown)::

                # If impostor is on cooldown
                move = {"action": "kill", "target_id": "Bob"}
                new_state = cls._handle_kill_action(state, "Eve", move)
                # Returns state with cooldown error message

        """
        player_state = state.player_states[player_id]
        target_id = move.get("target_id")

        # Validate player is an impostor
        if not player_state.is_impostor():
            state.error_message = "Only impostors can perform kills"
            return state

        # Check if impostor is in a vent
        if player_state.in_vent:
            state.error_message = "Cannot kill while in a vent"
            return state

        # Check kill cooldown
        kill_cooldown = state.get_player_cooldown(player_id)
        if kill_cooldown > 0:
            state.error_message = (
                f"Kill is on cooldown for {kill_cooldown} more seconds"
            )
            return state

        # Validate target exists and is alive
        if target_id not in state.player_states:
            state.error_message = f"Target {target_id} not found"
            return state

        target_state = state.player_states[target_id]
        if not target_state.is_alive:
            state.error_message = f"Target {target_id} is already dead"
            return state

        # Validate target is in the same location
        if target_state.location != player_state.location:
            state.error_message = f"Target {target_id} is not in the same location"
            return state

        # Check for witnesses (other players in the same location)
        witnesses = [
            pid
            for pid, pstate in state.player_states.items()
            if (
                pid != player_id
                and pid != target_id
                and pstate.is_alive
                and pstate.location == player_state.location
                and pstate.role != PlayerRole.IMPOSTOR
            )  # Other impostors don't count as witnesses
        ]

        if witnesses:
            state.error_message = "Cannot kill when there are witnesses"
            return state

        # Perform the kill
        target_state.is_alive = False
        state.eliminated_players.append(target_id)

        # Update counts
        if target_state.role == PlayerRole.CREWMATE:
            state.crewmate_count -= 1

        # Set kill cooldown
        state.set_player_cooldown(player_id, 45)  # Default 45 second cooldown

        return state

    @classmethod
    def _handle_report_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle body reporting with meeting initiation and vent management.

        Processes body report actions, validates dead body presence, transitions
        to meeting phase, and forces all players out of vents for the meeting.

        Args:
            state: Current game state.
            player_id: ID of the reporting player.
            move: Move dictionary (body reporting requires no parameters).

        Returns:
            AmongUsState: Updated state in meeting phase.

        Examples:
            Successful body report::

                move = {"action": "report_body"}
                new_state = cls._handle_report_action(state, "Alice", move)
                # Game transitions to meeting phase

            Failed report (no body)::

                # If no dead body in current location
                move = {"action": "report_body"}
                new_state = cls._handle_report_action(state, "Alice", move)
                # Returns state with error_message

        """
        player_state = state.player_states[player_id]

        # Cannot report while in a vent
        if player_state.in_vent:
            state.error_message = "Cannot report a body while in a vent"
            return state

        # Check if there's a dead body in the current location
        location = player_state.location
        dead_bodies = [
            pid
            for pid, pstate in state.player_states.items()
            if not pstate.is_alive and pstate.location == location
        ]

        if not dead_bodies:
            state.error_message = "No dead bodies to report"
            return state

        # Transition to meeting phase
        state.game_phase = AmongUsGamePhase.MEETING
        state.meeting_active = True
        state.meeting_caller = player_id
        state.reported_body = dead_bodies[0]

        # Add observation for all alive players
        observation = (
            f"{player_id} reported the dead body of {dead_bodies[0]} in {location}"
        )
        for pid, pstate in state.player_states.items():
            if pstate.is_alive:
                state.add_observation(pid, observation)

        # Force all impostors out of vents when a meeting is called
        for pid, pstate in state.player_states.items():
            if pstate.in_vent:
                pstate.in_vent = False
                pstate.current_vent = None

        return state

    @classmethod
    def _handle_emergency_meeting_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle emergency meeting calls with location validation.

        Processes emergency meeting calls, validates the player is in the
        cafeteria, transitions to meeting phase, and forces all players
        out of vents.

        Args:
            state: Current game state.
            player_id: ID of the player calling the meeting.
            move: Move dictionary (emergency meeting requires no parameters).

        Returns:
            AmongUsState: Updated state in meeting phase.

        Examples:
            Valid emergency meeting::

                move = {"action": "call_emergency_meeting"}
                new_state = cls._handle_emergency_meeting_action(state, "Alice", move)
                # Game transitions to meeting phase

            Invalid location::

                # If player is not in cafeteria
                move = {"action": "call_emergency_meeting"}
                new_state = cls._handle_emergency_meeting_action(state, "Alice", move)
                # Returns state with location error

        """
        player_state = state.player_states[player_id]

        # Validate player is in cafeteria
        if player_state.location != "cafeteria":
            state.error_message = "Emergency meetings can only be called in cafeteria"
            return state

        # Cannot call meeting while in a vent
        if player_state.in_vent:
            state.error_message = "Cannot call a meeting while in a vent"
            return state

        # Transition to meeting phase
        state.game_phase = AmongUsGamePhase.MEETING
        state.meeting_active = True
        state.meeting_caller = player_id

        # Add observation for all alive players
        observation = f"{player_id} called an emergency meeting"
        for pid, pstate in state.player_states.items():
            if pstate.is_alive:
                state.add_observation(pid, observation)

        # Force all impostors out of vents when a meeting is called
        for pid, pstate in state.player_states.items():
            if pstate.in_vent:
                pstate.in_vent = False
                pstate.current_vent = None

        return state

    @classmethod
    def _handle_discussion_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle discussion contributions with automatic phase progression.

        Processes player discussion messages, records them in discussion history,
        and automatically transitions to voting phase when all players have
        contributed to the discussion.

        Args:
            state: Current game state.
            player_id: ID of the discussing player.
            move: Move dictionary with discussion message.

        Returns:
            AmongUsState: Updated state with discussion recorded.

        Examples:
            Discussion contribution::

                move = {"action": "discuss", "message": "I saw Alice near the body!"}
                new_state = cls._handle_discussion_action(state, "Bob", move)

            Auto-transition to voting::

                # When all players have discussed
                move = {"action": "discuss", "message": "Let's vote!"}
                new_state = cls._handle_discussion_action(state, "Eve", move)
                # State transitions to voting phase

        """
        message = move.get("message", "")

        # Record the message in the discussion history
        state.discussion_history.append(
            {
                "player_id": player_id,
                "message": message,
                "timestamp": datetime.now().isoformat(),
            }
        )

        # Check if all alive players have contributed to the discussion
        alive_players = [
            pid for pid, pstate in state.player_states.items() if pstate.is_alive
        ]
        current_round_messages = [
            msg for msg in state.discussion_history if msg["player_id"] in alive_players
        ]

        players_who_discussed = {msg["player_id"] for msg in current_round_messages}

        if len(players_who_discussed) >= len(alive_players):
            # Transition to voting phase
            state.game_phase = AmongUsGamePhase.VOTING

        return state

    @classmethod
    def _handle_vote_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle voting with ejection processing and phase transition.

        Processes player votes, counts votes when all players have voted,
        handles ejection logic including tie resolution, and transitions
        back to task phase for the next round.

        Args:
            state: Current game state.
            player_id: ID of the voting player.
            move: Move dictionary with vote target.

        Returns:
            AmongUsState: Updated state with vote processed.

        Examples:
            Vote for player::

                move = {"action": "vote", "vote_for": "Charlie"}
                new_state = cls._handle_vote_action(state, "Alice", move)

            Skip vote::

                move = {"action": "vote", "vote_for": "skip"}
                new_state = cls._handle_vote_action(state, "Bob", move)

            Final vote triggering ejection::

                # When all players have voted
                move = {"action": "vote", "vote_for": "Charlie"}
                new_state = cls._handle_vote_action(state, "Eve", move)
                # Processes ejection and returns to task phase

        """
        target_id = move.get("vote_for")

        # Validate target exists or is "skip"
        if target_id != "skip" and target_id not in state.player_states:
            state.error_message = f"Invalid vote target: {target_id}"
            return state

        # Record the vote
        state.votes[player_id] = target_id

        # Check if all alive players have voted
        alive_players = [
            pid for pid, pstate in state.player_states.items() if pstate.is_alive
        ]

        if len(state.votes) >= len(alive_players):
            # Count votes and eliminate player if needed
            vote_counts = {}
            for voted_for in state.votes.values():
                vote_counts[voted_for] = vote_counts.get(voted_for, 0) + 1

            # Find the player with the most votes (excluding skip)
            max_votes = 0
            player_to_eject = None

            for pid, count in vote_counts.items():
                if pid != "skip" and count > max_votes:
                    max_votes = count
                    player_to_eject = pid

            # In case of a tie, no one is ejected
            skip_votes = vote_counts.get("skip", 0)

            if player_to_eject and skip_votes < max_votes:
                # Check if anyone else has the same number of votes (tie)
                tied_players = [
                    pid
                    for pid, count in vote_counts.items()
                    if pid != "skip" and pid != player_to_eject and count == max_votes
                ]

                if not tied_players:  # No tie
                    # Eject the player
                    state.player_states[player_to_eject].is_alive = False
                    state.eliminated_players.append(player_to_eject)

                    # Add observation for all players
                    ejected_role = state.player_states[player_to_eject].role
                    role_text = (
                        "an Impostor"
                        if ejected_role == PlayerRole.IMPOSTOR
                        else "a Crewmate"
                    )
                    observation = f"{player_to_eject} was ejected and was {role_text}"
                    for pid, _pstate in state.player_states.items():
                        state.add_observation(pid, observation)

                    # Update counts
                    if ejected_role == PlayerRole.IMPOSTOR:
                        state.impostor_count -= 1
                    else:
                        state.crewmate_count -= 1

            # Reset for next round
            state.votes = {}
            state.meeting_active = False
            state.meeting_caller = None
            state.reported_body = None

            # Transition back to tasks phase
            state.game_phase = AmongUsGamePhase.TASKS
            state.round_number += 1

            # Decrement cooldowns
            state.decrement_cooldowns()

        return state

    @classmethod
    def _handle_sabotage_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle sabotage actions with complex resolution system management.

        Processes impostor sabotage actions, creates appropriate resolution
        points, handles different sabotage types (critical and non-critical),
        and manages door locking mechanics.

        Args:
            state: Current game state.
            player_id: ID of the sabotaging impostor.
            move: Move dictionary with sabotage type and location.

        Returns:
            AmongUsState: Updated state with active sabotage.

        Examples:
            Reactor sabotage::

                move = {"action": "sabotage", "sabotage_type": "reactor"}
                new_state = cls._handle_sabotage_action(state, "Eve", move)
                # Creates critical sabotage with 45s timer

            Lights sabotage::

                move = {"action": "sabotage", "sabotage_type": "lights"}
                new_state = cls._handle_sabotage_action(state, "Eve", move)
                # Creates non-critical sabotage with 120s timer

            Door sabotage::

                move = {
                    "action": "sabotage",
                    "sabotage_type": "doors",
                    "location": "electrical"
                }
                new_state = cls._handle_sabotage_action(state, "Eve", move)
                # Blocks connections to/from electrical

        """
        player_state = state.player_states[player_id]

        # Validate player is an impostor
        if not player_state.is_impostor():
            state.error_message = "Only impostors can sabotage"
            return state

        sabotage_type_str = move.get("sabotage_type")
        location = move.get("location", sabotage_type_str)

        # Validate sabotage type
        try:
            sabotage_type = SabotageType(sabotage_type_str)
        except ValueError:
            state.error_message = f"Invalid sabotage type: {sabotage_type_str}"
            return state

        # Check if a critical sabotage is already active
        active_sabotage = state.get_active_sabotage()
        if (
            active_sabotage
            and active_sabotage.is_critical()
            and sabotage_type in [SabotageType.OXYGEN, SabotageType.REACTOR]
        ):
            state.error_message = (
                "Cannot start a critical sabotage while another is active"
            )
            return state

        # Create resolution points based on sabotage type
        resolution_points = []
        timer = 60  # Default timer

        if sabotage_type == SabotageType.OXYGEN:
            # O2 requires two points to be resolved
            resolution_points = [
                SabotageResolutionPoint(
                    id="o2_panel_1",
                    location="o2",
                    description="Reset O2 panel in O2 room",
                    resolved=False,
                ),
                SabotageResolutionPoint(
                    id="o2_panel_2",
                    location="admin",
                    description="Reset O2 panel in Admin room",
                    resolved=False,
                ),
            ]
            timer = 45  # 45 seconds to resolve O2

        elif sabotage_type == SabotageType.REACTOR:
            # Reactor requires two points to be resolved
            resolution_points = [
                SabotageResolutionPoint(
                    id="reactor_panel_1",
                    location="reactor",
                    description="Stabilize reactor (left panel)",
                    resolved=False,
                ),
                SabotageResolutionPoint(
                    id="reactor_panel_2",
                    location="reactor",
                    description="Stabilize reactor (right panel)",
                    resolved=False,
                ),
            ]
            timer = 45  # 45 seconds to resolve reactor

        elif sabotage_type == SabotageType.LIGHTS:
            # Lights can be resolved at one point
            resolution_points = [
                SabotageResolutionPoint(
                    id="light_panel",
                    location="electrical",
                    description="Reset light panel in Electrical",
                    resolved=False,
                ),
            ]
            timer = 120  # Lights can stay out longer

        elif sabotage_type == SabotageType.COMMS:
            # Comms can be resolved at one point
            resolution_points = [
                SabotageResolutionPoint(
                    id="comms_panel",
                    location="communications",
                    description="Reset communications panel",
                    resolved=False,
                ),
            ]
            timer = 90  # Comms disruption

        elif sabotage_type == SabotageType.DOORS:
            # Door locks require no resolution - they time out automatically
            if location not in state.rooms:
                state.error_message = f"Invalid door lock location: {location}"
                return state

            # Block connections to and from this room
            room = state.rooms[location]
            for connection in room.connections:
                connection.is_blocked = True

            # Add blocked connections from other rooms to this room
            for room_id, other_room in state.rooms.items():
                if room_id != location:
                    for connection in other_room.connections:
                        if connection.target_room == location:
                            connection.is_blocked = True

            timer = 10  # Doors unlock after 10 seconds

            # Add observation for players in the room
            observation = f"The doors to {location} have been locked"
            state.add_observation_to_all_in_room(location, observation, [])

            # Create door sabotage event
            sabotage = SabotageEvent(
                type=sabotage_type_str,
                location=location,
                timer=timer,
                resolved=False,
            )

            state.sabotages.append(sabotage)

            # Schedule automatic resolution after timer
            # In a real implementation, this would be handled by a timer
            # For now, we'll just mark it as resolved immediately
            # TODO: Implement proper timer mechanism

            return state

        # Create the sabotage event for non-door sabotages
        sabotage = SabotageEvent(
            type=sabotage_type_str,
            location=location,
            timer=timer,
            resolved=False,
            resolution_points=resolution_points,
        )

        state.sabotages.append(sabotage)

        # Add observation for all players
        observation = f"ALERT: {sabotage_type_str.upper()} SYSTEM SABOTAGED!"
        for pid, pstate in state.player_states.items():
            if pstate.is_alive:
                state.add_observation(pid, observation)

        return state

    @classmethod
    def _handle_resolve_sabotage_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle sabotage resolution with multi-point validation.

        Processes sabotage resolution actions, validates player location
        against resolution points, handles multi-point sabotages (like
        reactor and O2), and manages door unblocking.

        Args:
            state: Current game state.
            player_id: ID of the resolving player.
            move: Move dictionary with sabotage and resolution point IDs.

        Returns:
            AmongUsState: Updated state with sabotage resolved (if complete).

        Examples:
            Reactor resolution::

                move = {
                    "action": "resolve_sabotage",
                    "sabotage_id": "reactor",
                    "resolution_point_id": "reactor_panel_1"
                }
                new_state = cls._handle_resolve_sabotage_action(state, "Alice", move)
                # Resolves one of two reactor panels

            Complete resolution::

                # After both panels are resolved
                move = {
                    "action": "resolve_sabotage",
                    "sabotage_id": "reactor",
                    "resolution_point_id": "reactor_panel_2"
                }
                new_state = cls._handle_resolve_sabotage_action(state, "Bob", move)
                # Fully resolves reactor sabotage

        """
        player_state = state.player_states[player_id]
        sabotage_id = move.get("sabotage_id")
        resolution_point_id = move.get("resolution_point_id")

        # Find the active sabotage
        active_sabotage = None
        for sabotage in state.sabotages:
            if not sabotage.is_resolved() and (
                not sabotage_id or sabotage.type == sabotage_id
            ):
                active_sabotage = sabotage
                break

        if not active_sabotage:
            state.error_message = "No active sabotage to resolve"
            return state

        # Check if player is in the correct location for resolution
        found_point = False
        for point in active_sabotage.resolution_points:
            if (
                point.id == resolution_point_id
                and point.location == player_state.location
            ):
                found_point = True
                point.resolved = True
                point.resolver_id = player_id
                break

        if not found_point:
            state.error_message = "No resolution point found at this location"
            return state

        # Check if all resolution points are resolved
        if all(point.resolved for point in active_sabotage.resolution_points):
            active_sabotage.resolved = True

            # For door sabotages, unblock connections
            if active_sabotage.type == SabotageType.DOORS.value:
                location = active_sabotage.location
                room = state.rooms.get(location)
                if room:
                    for connection in room.connections:
                        connection.is_blocked = False

                    # Unblock connections from other rooms to this room
                    for room_id, other_room in state.rooms.items():
                        if room_id != location:
                            for connection in other_room.connections:
                                if connection.target_room == location:
                                    connection.is_blocked = False

            # Add observation for all players
            observation = f"{active_sabotage.type.upper()} sabotage has been resolved!"
            for pid, pstate in state.player_states.items():
                if pstate.is_alive:
                    state.add_observation(pid, observation)
        else:
            # Add observation for players in the same room
            observation = (
                f"{player_id} resolved part of the {active_sabotage.type} sabotage"
            )
            state.add_observation_to_all_in_room(player_state.location, observation, [])

        return state

    @classmethod
    def _handle_vent_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle impostor vent usage with connection validation.

        Processes impostor vent actions, handling both entering vents and
        traveling between connected vents. Validates vent connectivity and
        updates player location appropriately.

        Args:
            state: Current game state.
            player_id: ID of the venting impostor.
            move: Move dictionary with target vent ID.

        Returns:
            AmongUsState: Updated state with player in vent system.

        Examples:
            Entering a vent::

                move = {"action": "vent", "vent_id": "electrical_vent"}
                new_state = cls._handle_vent_action(state, "Eve", move)
                # Player enters vent in current room

            Traveling between vents::

                # When already in a vent
                move = {"action": "vent", "vent_id": "cafeteria_vent"}
                new_state = cls._handle_vent_action(state, "Eve", move)
                # Player travels to connected vent

        """
        player_state = state.player_states[player_id]
        vent_id = move.get("vent_id")

        # Validate player is an impostor
        if not player_state.is_impostor():
            state.error_message = "Only impostors can use vents"
            return state

        # If player is already in a vent, this is a travel action
        if player_state.in_vent:
            current_vent = state.get_vent(player_state.current_vent)
            if not current_vent:
                state.error_message = "Current vent not found"
                return state

            # Check if target vent is connected
            connected_vents = state.get_connected_vents(current_vent.id)
            if vent_id not in connected_vents:
                state.error_message = f"Cannot travel from {current_vent.id} to {
                    vent_id
                } - vents are not connected"
                return state

            # Update player's current vent
            player_state.current_vent = vent_id

            # Update player's location to the vent's room
            target_vent = state.get_vent(vent_id)
            if target_vent:
                player_state.location = target_vent.location

            return state

        # Otherwise, this is an enter vent action
        # Check if there is a vent in the current room
        room_vents = state.get_vents_in_room(player_state.location)
        vent_ids = [vent.id for vent in room_vents]

        if not vent_ids or vent_id not in vent_ids:
            state.error_message = (
                f"No vent with ID {vent_id} found in {player_state.location}"
            )
            return state

        # Enter the vent
        player_state.in_vent = True
        player_state.current_vent = vent_id

        return state

    @classmethod
    def _handle_exit_vent_action(
        cls, state: AmongUsState, player_id: str, move: dict[str, Any]
    ) -> AmongUsState:
        """Handle impostor vent exit with location validation.

        Processes impostor vent exit actions, validates the player is
        actually in a vent, and properly sets their location to the
        vent's room.

        Args:
            state: Current game state.
            player_id: ID of the exiting impostor.
            move: Move dictionary (exit vent requires no parameters).

        Returns:
            AmongUsState: Updated state with player out of vent.

        Examples:
            Exiting a vent::

                move = {"action": "exit_vent"}
                new_state = cls._handle_exit_vent_action(state, "Eve", move)
                # Player exits vent into current room

            Invalid exit::

                # If player is not in a vent
                move = {"action": "exit_vent"}
                new_state = cls._handle_exit_vent_action(state, "Eve", move)
                # Returns state with error message

        """
        player_state = state.player_states[player_id]

        # Check if player is actually in a vent
        if not player_state.in_vent or not player_state.current_vent:
            state.error_message = "Not currently in a vent"
            return state

        # Exit the vent
        player_state.in_vent = False
        current_vent = state.get_vent(player_state.current_vent)
        player_state.current_vent = None

        # Location should already be set to the vent's room
        # But make sure it is correct
        if current_vent:
            player_state.location = current_vent.location

        return state

    @classmethod
    def get_legal_moves(
        cls, state: AmongUsState, player_id: str
    ) -> list[dict[str, Any]]:
        """Generate comprehensive legal moves for a player based on game state.

        Analyzes the current game state and player situation to generate
        all valid moves available to the player, considering their role,
        location, game phase, and current constraints.

        Args:
            state: Current game state.
            player_id: ID of the player to generate moves for.

        Returns:
            List[Dict[str, Any]]: List of legal move dictionaries.

        Examples:
            Crewmate in task phase::

                moves = cls.get_legal_moves(state, "Alice")
                # Returns moves like:
                # [{"action": "move", "location": "electrical"},
                #  {"action": "complete_task", "task_id": "Alice_task_1"},
                #  {"action": "report_body"}] (if body present)

            Impostor in task phase::

                moves = cls.get_legal_moves(state, "Eve")
                # Returns moves like:
                # [{"action": "move", "location": "medbay"},
                #  {"action": "kill", "target_id": "Bob"},
                #  {"action": "vent", "vent_id": "electrical_vent"},
                #  {"action": "sabotage", "sabotage_type": "lights"}]

            Player in voting phase::

                moves = cls.get_legal_moves(state, "Alice")
                # Returns moves like:
                # [{"action": "vote", "vote_for": "Charlie"},
                #  {"action": "vote", "vote_for": "skip"}]

        """
        if player_id not in state.player_states:
            return []

        player_state = state.player_states[player_id]

        # Dead players can only observe
        if not player_state.is_alive:
            return [{"action": "observe"}]

        legal_moves = []

        # Handle different game phases
        if state.game_phase == AmongUsGamePhase.TASKS:
            # If player is in a vent, only allow vent travel or exit
            if player_state.in_vent:
                # Exit vent
                legal_moves.append({"action": "exit_vent"})

                # Travel to connected vents
                if player_state.current_vent:
                    connected_vents = state.get_connected_vents(
                        player_state.current_vent
                    )
                    for vent_id in connected_vents:
                        legal_moves.append({"action": "vent", "vent_id": vent_id})

                return legal_moves

            # Normal movement (only to connected rooms)
            current_room = state.get_room(player_state.location)
            if current_room:
                connected_rooms = state.get_connected_rooms(player_state.location)
                for location in connected_rooms:
                    legal_moves.append({"action": "move", "location": location})
            else:
                # Fallback if room data is not available
                for location in state.map_locations:
                    if location != player_state.location:
                        legal_moves.append({"action": "move", "location": location})

            # Task completion (for crewmates)
            if player_state.role == PlayerRole.CREWMATE:
                for task in player_state.tasks:
                    if (
                        task.location == player_state.location
                        and task.status != TaskStatus.COMPLETED
                    ):
                        legal_moves.append(
                            {"action": "complete_task", "task_id": task.id}
                        )

            # Vent usage (for impostors)
            if player_state.role == PlayerRole.IMPOSTOR:
                room_vents = state.get_vents_in_room(player_state.location)
                for vent in room_vents:
                    legal_moves.append({"action": "vent", "vent_id": vent.id})

            # Kill action (for impostors)
            if (
                player_state.role == PlayerRole.IMPOSTOR
                and state.get_player_cooldown(player_id) <= 0
            ):
                targets = cls._get_potential_targets(state, player_id)
                for target_id in targets:
                    legal_moves.append({"action": "kill", "target_id": target_id})

            # Report action
            dead_bodies = [
                pid
                for pid, pstate in state.player_states.items()
                if not pstate.is_alive and pstate.location == player_state.location
            ]
            if dead_bodies:
                legal_moves.append({"action": "report_body"})

            # Emergency meeting
            if player_state.location == "cafeteria":
                legal_moves.append({"action": "call_emergency_meeting"})

            # Sabotage (for impostors)
            if player_state.role == PlayerRole.IMPOSTOR:
                sabotage_types = [st.value for st in SabotageType]
                for sabotage_type in sabotage_types:
                    if sabotage_type == SabotageType.DOORS.value:
                        # Door locks can be applied to any room
                        for room_id in state.rooms:
                            legal_moves.append(
                                {
                                    "action": "sabotage",
                                    "sabotage_type": sabotage_type,
                                    "location": room_id,
                                }
                            )
                    else:
                        legal_moves.append(
                            {
                                "action": "sabotage",
                                "sabotage_type": sabotage_type,
                            }
                        )

            # Resolve sabotage
            active_sabotage = state.get_active_sabotage()
            if active_sabotage:
                for point in active_sabotage.resolution_points:
                    if point.location == player_state.location and not point.resolved:
                        legal_moves.append(
                            {
                                "action": "resolve_sabotage",
                                "sabotage_id": active_sabotage.type,
                                "resolution_point_id": point.id,
                            }
                        )

        elif state.game_phase == AmongUsGamePhase.MEETING:
            # Discussion
            legal_moves.append({"action": "discuss", "message": "[Your message here]"})

        elif state.game_phase == AmongUsGamePhase.VOTING:
            # Voting
            for pid, pstate in state.player_states.items():
                if pstate.is_alive and pid != player_id:
                    legal_moves.append({"action": "vote", "vote_for": pid})

            # Skip vote
            legal_moves.append({"action": "vote", "vote_for": "skip"})

        return legal_moves

    @classmethod
    def _get_potential_targets(cls, state: AmongUsState, player_id: str) -> list[str]:
        """Get potential kill targets for an impostor with witness validation.

        Analyzes the current game state to find valid kill targets for an
        impostor, considering location, role, witness presence, and other
        constraints.

        Args:
            state: Current game state.
            player_id: ID of the impostor player.

        Returns:
            List[str]: List of valid target player IDs.

        Examples:
            Isolated target::

                targets = cls._get_potential_targets(state, "Eve")
                # Returns ["Alice"] if Alice is alone with Eve

            No valid targets::

                targets = cls._get_potential_targets(state, "Eve")
                # Returns [] if all crewmates have witnesses

            Multiple targets::

                targets = cls._get_potential_targets(state, "Eve")
                # Returns ["Alice", "Bob"] if both are isolated

        """
        if player_id not in state.player_states:
            return []

        player_state = state.player_states[player_id]
        if not player_state.is_impostor() or player_state.in_vent:
            return []

        # Find alive crewmates in the same location
        targets = []

        for pid, pstate in state.player_states.items():
            if (
                pid != player_id
                and pstate.is_alive
                and pstate.role == PlayerRole.CREWMATE
                and pstate.location == player_state.location
            ):
                # Check for witnesses
                witnesses = [
                    wpid
                    for wpid, wpstate in state.player_states.items()
                    if (
                        wpid != player_id
                        and wpid != pid
                        and wpstate.is_alive
                        and wpstate.role != PlayerRole.IMPOSTOR
                        and wpstate.location == player_state.location
                    )
                ]

                if not witnesses:
                    targets.append(pid)

        return targets

    @classmethod
    def check_game_status(cls, state: AmongUsState) -> AmongUsState:
        """Check and update game status with win condition evaluation.

        Evaluates the current game state to determine if any win conditions
        have been met and updates the game status accordingly.

        Args:
            state: Current game state to check.

        Returns:
            AmongUsState: Updated state with current game status.

        Examples:
            Ongoing game::

                updated_state = cls.check_game_status(state)
                # Returns state with game_status="ongoing"

            Crewmate victory::

                updated_state = cls.check_game_status(state)
                # Returns state with game_status="ended", winner="crewmates"

            Impostor victory::

                updated_state = cls.check_game_status(state)
                # Returns state with game_status="ended", winner="impostors"

        """
        winner = state.check_win_condition()

        if winner:
            state.game_phase = AmongUsGamePhase.GAME_OVER
            state.game_status = "ended"
            state.winner = winner

        return state

    @classmethod
    def advance_phase(cls, state: AmongUsState) -> AmongUsState:
        """Advance the game to the next phase in the game cycle.

        Progresses the game through its phases: TASKS -> MEETING -> VOTING -> TASKS.
        Updates related state variables and resets phase-specific data.

        Args:
            state: Current game state to advance.

        Returns:
            AmongUsState: Updated state in the next phase.

        Examples:
            Task to meeting transition::

                new_state = cls.advance_phase(state)
                # game_phase changes from TASKS to MEETING

            Meeting to voting transition::

                new_state = cls.advance_phase(state)
                # game_phase changes from MEETING to VOTING

            Voting to tasks transition::

                new_state = cls.advance_phase(state)
                # game_phase changes from VOTING to TASKS
                # round_number increments, votes cleared

        """
        if state.game_phase == AmongUsGamePhase.TASKS:
            # TASKS -> MEETING
            state.game_phase = AmongUsGamePhase.MEETING
            state.meeting_active = True

        elif state.game_phase == AmongUsGamePhase.MEETING:
            # MEETING -> VOTING
            state.game_phase = AmongUsGamePhase.VOTING

        elif state.game_phase == AmongUsGamePhase.VOTING:
            # VOTING -> TASKS
            state.game_phase = AmongUsGamePhase.TASKS
            state.meeting_active = False
            state.votes = {}
            state.round_number += 1

        return state

    # Enhanced filtered state for players
    @classmethod
    def filter_state_for_player(
        cls, state: AmongUsState, player_id: str
    ) -> dict[str, Any]:
        """Filter game state to include only information visible to a specific player.

        Creates a filtered view of the game state that includes only information
        the specified player should have access to, implementing proper information
        hiding for authentic social deduction gameplay.

        Args:
            state: Complete game state to filter.
            player_id: ID of the player to create filtered state for.

        Returns:
            Dict[str, Any]: Filtered state dictionary with player-visible information.

        Examples:
            Crewmate filtered state::

                filtered = cls.filter_state_for_player(state, "Alice")
                # Includes: own location, tasks, observations, connected rooms
                # Excludes: other players' roles, impostor identities

            Impostor filtered state::

                filtered = cls.filter_state_for_player(state, "Eve")
                # Includes: fellow impostors, vent locations, kill cooldown
                # Excludes: crewmate task progress details

            Dead player filtered state::

                filtered = cls.filter_state_for_player(state, "Bob")
                # Includes: basic game information, spectator view
                # Excludes: ability to influence game

        """
        if player_id not in state.player_states:
            return {}

        player_state = state.player_states[player_id]

        # Create a filtered copy of the state
        filtered_state = {
            "game_phase": state.game_phase,
            "map_locations": state.map_locations,
            "meeting_active": state.meeting_active,
            "meeting_caller": state.meeting_caller,
            "round_number": state.round_number,
            # Player-specific info
            "player_id": player_id,
            "location": player_state.location,
            "is_alive": player_state.is_alive,
            "role": player_state.role,
            "tasks": [
                task.dict() if hasattr(task, "dict") else task
                for task in player_state.tasks
            ],
            "observations": player_state.observations,
            "in_vent": player_state.in_vent,
            "current_vent": player_state.current_vent,
        }

        # Add memory if available
        if hasattr(player_state, "memory"):
            filtered_state["memory"] = player_state.memory

        # Add connected rooms
        filtered_state["connected_rooms"] = state.get_connected_rooms(
            player_state.location
        )

        # Add vents in current room
        if player_state.role == PlayerRole.IMPOSTOR:
            filtered_state["room_vents"] = [
                vent.id for vent in state.get_vents_in_room(player_state.location)
            ]

            # Add connected vents if in a vent
            if player_state.in_vent and player_state.current_vent:
                filtered_state["connected_vents"] = state.get_connected_vents(
                    player_state.current_vent
                )

            # Add kill cooldown
            filtered_state["kill_cooldown"] = state.get_player_cooldown(player_id)

        # If player is impostor, add info about other impostors
        if player_state.role == PlayerRole.IMPOSTOR:
            filtered_state["fellow_impostors"] = [
                pid
                for pid, pstate in state.player_states.items()
                if pstate.role == PlayerRole.IMPOSTOR and pid != player_id
            ]

        # Add active sabotage info
        active_sabotage = state.get_active_sabotage()
        if active_sabotage:
            filtered_state["active_sabotage"] = {
                "type": active_sabotage.type,
                "location": active_sabotage.location,
                "timer": active_sabotage.timer,
                "resolution_points": [
                    {
                        "id": point.id,
                        "location": point.location,
                        "description": point.description,
                        "resolved": point.resolved,
                    }
                    for point in active_sabotage.resolution_points
                ],
            }

        # Info about other players
        visible_players = []
        for pid, pstate in state.player_states.items():
            if pid == player_id:
                continue

            # Basic info about all players
            player_info = {"id": pid, "is_alive": pstate.is_alive}

            # Add location if they're visible (same location or meeting)
            if pstate.location == player_state.location or state.game_phase in [
                AmongUsGamePhase.MEETING,
                AmongUsGamePhase.VOTING,
            ]:
                player_info["location"] = pstate.location

            # Add role only if they're a fellow impostor
            if (
                player_state.role == PlayerRole.IMPOSTOR
                and pstate.role == PlayerRole.IMPOSTOR
            ):
                player_info["role"] = "impostor"
            else:
                player_info["role"] = "unknown"

            visible_players.append(player_info)

        filtered_state["visible_players"] = visible_players

        # Meeting and voting info
        if state.game_phase in [AmongUsGamePhase.MEETING, AmongUsGamePhase.VOTING]:
            # Add discussion history
            filtered_state["discussion_history"] = state.discussion_history

            # Add reported body info
            if state.reported_body:
                filtered_state["reported_body"] = state.reported_body
                reported_location = (
                    state.player_states[state.reported_body].location
                    if state.reported_body in state.player_states
                    else None
                )
                filtered_state["reported_body_location"] = reported_location

            if state.game_phase == AmongUsGamePhase.VOTING:
                # Show who has voted but not who they voted for
                filtered_state["voted_players"] = list(state.votes.keys())

                # Show my vote if I've voted
                if player_id in state.votes:
                    filtered_state["my_vote"] = state.votes[player_id]

        return filtered_state

    model_config = {"arbitrary_types_allowed": True}
