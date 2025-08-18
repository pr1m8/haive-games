games.among_us.state_manager
============================

.. py:module:: games.among_us.state_manager

Comprehensive state management mixin for Among Us social deduction gameplay.

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

.. rubric:: Examples

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

.. note::

   This is a mixin class designed to be inherited by game agents,
   providing state management capabilities without agent-specific behavior.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive state management mixin for Among Us social deduction gameplay.

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

   .. rubric:: Examples

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

   .. note::

      This is a mixin class designed to be inherited by game agents,
      providing state management capabilities without agent-specific behavior.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.among_us.state_manager.AmongUsStateManagerMixin

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsStateManagerMixin

            Bases: :py:obj:`haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager`\ [\ :py:obj:`haive.games.among_us.state.AmongUsState`\ ]


            Comprehensive state management mixin for Among Us social deduction gameplay.

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

            .. rubric:: Examples

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

            .. note::

               This mixin is designed to be inherited by game agents, providing
               state management capabilities without imposing specific agent behaviors.


            .. py:method:: _generate_task_description(task_type: haive.games.among_us.models.TaskType, location: str) -> str
               :classmethod:


               Generate a realistic task description based on type and location.

               Creates authentic Among Us task descriptions that match the game's
               actual tasks, providing immersive gameplay experiences.

               :param task_type: Type of task (VISUAL, COMMON, SHORT, LONG).
               :param location: Room where the task is located.

               :returns: Human-readable task description.
               :rtype: str

               .. rubric:: Examples

               Visual task generation::

                   desc = cls._generate_task_description(TaskType.VISUAL, "medbay")
                   # Returns: "Submit scan"

               Common task generation::

                   desc = cls._generate_task_description(TaskType.COMMON, "admin")
                   # Returns: "Swipe card"

               Fallback generation::

                   desc = cls._generate_task_description(TaskType.SHORT, "unknown_room")
                   # Returns: "Complete short task in unknown_room"



            .. py:method:: _get_potential_targets(state: haive.games.among_us.state.AmongUsState, player_id: str) -> list[str]
               :classmethod:


               Get potential kill targets for an impostor with witness validation.

               Analyzes the current game state to find valid kill targets for an
               impostor, considering location, role, witness presence, and other
               constraints.

               :param state: Current game state.
               :param player_id: ID of the impostor player.

               :returns: List of valid target player IDs.
               :rtype: List[str]

               .. rubric:: Examples

               Isolated target::

                   targets = cls._get_potential_targets(state, "Eve")
                   # Returns ["Alice"] if Alice is alone with Eve

               No valid targets::

                   targets = cls._get_potential_targets(state, "Eve")
                   # Returns [] if all crewmates have witnesses

               Multiple targets::

                   targets = cls._get_potential_targets(state, "Eve")
                   # Returns ["Alice", "Bob"] if both are isolated



            .. py:method:: _handle_complete_task_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle task completion with role validation and visual task detection.

               Processes task completion for crewmates, validates task location and
               status, and generates appropriate observations for other players.
               Handles visual tasks specially for crewmate confirmation.

               :param state: Current game state.
               :param player_id: ID of the player completing the task.
               :param move: Move dictionary with task ID.

               :returns: Updated state with completed task.
               :rtype: AmongUsState

               .. rubric:: Examples

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



            .. py:method:: _handle_discussion_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle discussion contributions with automatic phase progression.

               Processes player discussion messages, records them in discussion history,
               and automatically transitions to voting phase when all players have
               contributed to the discussion.

               :param state: Current game state.
               :param player_id: ID of the discussing player.
               :param move: Move dictionary with discussion message.

               :returns: Updated state with discussion recorded.
               :rtype: AmongUsState

               .. rubric:: Examples

               Discussion contribution::

                   move = {"action": "discuss", "message": "I saw Alice near the body!"}
                   new_state = cls._handle_discussion_action(state, "Bob", move)

               Auto-transition to voting::

                   # When all players have discussed
                   move = {"action": "discuss", "message": "Let's vote!"}
                   new_state = cls._handle_discussion_action(state, "Eve", move)
                   # State transitions to voting phase



            .. py:method:: _handle_emergency_meeting_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle emergency meeting calls with location validation.

               Processes emergency meeting calls, validates the player is in the
               cafeteria, transitions to meeting phase, and forces all players
               out of vents.

               :param state: Current game state.
               :param player_id: ID of the player calling the meeting.
               :param move: Move dictionary (emergency meeting requires no parameters).

               :returns: Updated state in meeting phase.
               :rtype: AmongUsState

               .. rubric:: Examples

               Valid emergency meeting::

                   move = {"action": "call_emergency_meeting"}
                   new_state = cls._handle_emergency_meeting_action(state, "Alice", move)
                   # Game transitions to meeting phase

               Invalid location::

                   # If player is not in cafeteria
                   move = {"action": "call_emergency_meeting"}
                   new_state = cls._handle_emergency_meeting_action(state, "Alice", move)
                   # Returns state with location error



            .. py:method:: _handle_exit_vent_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle impostor vent exit with location validation.

               Processes impostor vent exit actions, validates the player is
               actually in a vent, and properly sets their location to the
               vent's room.

               :param state: Current game state.
               :param player_id: ID of the exiting impostor.
               :param move: Move dictionary (exit vent requires no parameters).

               :returns: Updated state with player out of vent.
               :rtype: AmongUsState

               .. rubric:: Examples

               Exiting a vent::

                   move = {"action": "exit_vent"}
                   new_state = cls._handle_exit_vent_action(state, "Eve", move)
                   # Player exits vent into current room

               Invalid exit::

                   # If player is not in a vent
                   move = {"action": "exit_vent"}
                   new_state = cls._handle_exit_vent_action(state, "Eve", move)
                   # Returns state with error message



            .. py:method:: _handle_kill_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle impostor elimination with cooldown and witness validation.

               Processes impostor kill actions with comprehensive validation including
               role verification, cooldown checks, location validation, and witness
               detection. Updates player counts and applies kill cooldown.

               :param state: Current game state.
               :param player_id: ID of the impostor player.
               :param move: Move dictionary with target player ID.

               :returns: Updated state with eliminated player.
               :rtype: AmongUsState

               .. rubric:: Examples

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



            .. py:method:: _handle_move_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle player movement with connection and sabotage validation.

               Validates and processes player movement between rooms, checking for
               room connections, blocked doors, and updating player location with
               proper observation generation.

               :param state: Current game state.
               :param player_id: ID of the moving player.
               :param move: Move dictionary with target location.

               :returns: Updated state with new player location.
               :rtype: AmongUsState

               .. rubric:: Examples

               Valid movement::

                   move = {"action": "move", "location": "electrical"}
                   new_state = cls._handle_move_action(state, "Alice", move)

               Invalid movement (blocked door)::

                   # If doors are sabotaged
                   move = {"action": "move", "location": "electrical"}
                   new_state = cls._handle_move_action(state, "Alice", move)
                   # Returns state with error_message set



            .. py:method:: _handle_report_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle body reporting with meeting initiation and vent management.

               Processes body report actions, validates dead body presence, transitions
               to meeting phase, and forces all players out of vents for the meeting.

               :param state: Current game state.
               :param player_id: ID of the reporting player.
               :param move: Move dictionary (body reporting requires no parameters).

               :returns: Updated state in meeting phase.
               :rtype: AmongUsState

               .. rubric:: Examples

               Successful body report::

                   move = {"action": "report_body"}
                   new_state = cls._handle_report_action(state, "Alice", move)
                   # Game transitions to meeting phase

               Failed report (no body)::

                   # If no dead body in current location
                   move = {"action": "report_body"}
                   new_state = cls._handle_report_action(state, "Alice", move)
                   # Returns state with error_message



            .. py:method:: _handle_resolve_sabotage_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle sabotage resolution with multi-point validation.

               Processes sabotage resolution actions, validates player location
               against resolution points, handles multi-point sabotages (like
               reactor and O2), and manages door unblocking.

               :param state: Current game state.
               :param player_id: ID of the resolving player.
               :param move: Move dictionary with sabotage and resolution point IDs.

               :returns: Updated state with sabotage resolved (if complete).
               :rtype: AmongUsState

               .. rubric:: Examples

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



            .. py:method:: _handle_sabotage_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle sabotage actions with complex resolution system management.

               Processes impostor sabotage actions, creates appropriate resolution
               points, handles different sabotage types (critical and non-critical),
               and manages door locking mechanics.

               :param state: Current game state.
               :param player_id: ID of the sabotaging impostor.
               :param move: Move dictionary with sabotage type and location.

               :returns: Updated state with active sabotage.
               :rtype: AmongUsState

               .. rubric:: Examples

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



            .. py:method:: _handle_vent_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle impostor vent usage with connection validation.

               Processes impostor vent actions, handling both entering vents and
               traveling between connected vents. Validates vent connectivity and
               updates player location appropriately.

               :param state: Current game state.
               :param player_id: ID of the venting impostor.
               :param move: Move dictionary with target vent ID.

               :returns: Updated state with player in vent system.
               :rtype: AmongUsState

               .. rubric:: Examples

               Entering a vent::

                   move = {"action": "vent", "vent_id": "electrical_vent"}
                   new_state = cls._handle_vent_action(state, "Eve", move)
                   # Player enters vent in current room

               Traveling between vents::

                   # When already in a vent
                   move = {"action": "vent", "vent_id": "cafeteria_vent"}
                   new_state = cls._handle_vent_action(state, "Eve", move)
                   # Player travels to connected vent



            .. py:method:: _handle_vote_action(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Handle voting with ejection processing and phase transition.

               Processes player votes, counts votes when all players have voted,
               handles ejection logic including tie resolution, and transitions
               back to task phase for the next round.

               :param state: Current game state.
               :param player_id: ID of the voting player.
               :param move: Move dictionary with vote target.

               :returns: Updated state with vote processed.
               :rtype: AmongUsState

               .. rubric:: Examples

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



            .. py:method:: advance_phase(state: haive.games.among_us.state.AmongUsState) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Advance the game to the next phase in the game cycle.

               Progresses the game through its phases: TASKS -> MEETING -> VOTING -> TASKS.
               Updates related state variables and resets phase-specific data.

               :param state: Current game state to advance.

               :returns: Updated state in the next phase.
               :rtype: AmongUsState

               .. rubric:: Examples

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



            .. py:method:: apply_move(state: haive.games.among_us.state.AmongUsState, player_id: str, move: dict[str, Any]) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Apply a player's move to the game state with comprehensive validation.

               Processes and validates player moves, updating the game state accordingly.
               Handles all move types across different game phases with proper error
               handling and state consistency maintenance.

               :param state: Current game state to modify.
               :param player_id: ID of the player making the move.
               :param move: Move dictionary containing action and parameters.

               :returns: Updated game state after applying the move.
               :rtype: AmongUsState

               .. rubric:: Examples

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

               .. note::

                  The method creates a deep copy of the state to avoid modifying
                  the original, ensuring state immutability.



            .. py:method:: check_game_status(state: haive.games.among_us.state.AmongUsState) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Check and update game status with win condition evaluation.

               Evaluates the current game state to determine if any win conditions
               have been met and updates the game status accordingly.

               :param state: Current game state to check.

               :returns: Updated state with current game status.
               :rtype: AmongUsState

               .. rubric:: Examples

               Ongoing game::

                   updated_state = cls.check_game_status(state)
                   # Returns state with game_status="ongoing"

               Crewmate victory::

                   updated_state = cls.check_game_status(state)
                   # Returns state with game_status="ended", winner="crewmates"

               Impostor victory::

                   updated_state = cls.check_game_status(state)
                   # Returns state with game_status="ended", winner="impostors"



            .. py:method:: filter_state_for_player(state: haive.games.among_us.state.AmongUsState, player_id: str) -> dict[str, Any]
               :classmethod:


               Filter game state to include only information visible to a specific player.

               Creates a filtered view of the game state that includes only information
               the specified player should have access to, implementing proper information
               hiding for authentic social deduction gameplay.

               :param state: Complete game state to filter.
               :param player_id: ID of the player to create filtered state for.

               :returns: Filtered state dictionary with player-visible information.
               :rtype: Dict[str, Any]

               .. rubric:: Examples

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



            .. py:method:: get_legal_moves(state: haive.games.among_us.state.AmongUsState, player_id: str) -> list[dict[str, Any]]
               :classmethod:


               Generate comprehensive legal moves for a player based on game state.

               Analyzes the current game state and player situation to generate
               all valid moves available to the player, considering their role,
               location, game phase, and current constraints.

               :param state: Current game state.
               :param player_id: ID of the player to generate moves for.

               :returns: List of legal move dictionaries.
               :rtype: List[Dict[str, Any]]

               .. rubric:: Examples

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



            .. py:method:: initialize(player_names: list[str], **kwargs) -> haive.games.among_us.state.AmongUsState
               :classmethod:


               Initialize a new Among Us game state with intelligent defaults.

               Creates a complete game state with role assignments, task generation,
               map initialization, and all necessary game components. The initialization
               process follows standard Among Us rules for balanced gameplay.

               :param player_names: List of player identifiers (4-15 players).
               :param \*\*kwargs: Additional configuration options.
                                  map_name (str): Map to use (default: "skeld").
                                  num_impostors (int): Number of impostors (auto-calculated if None).
                                  tasks_per_player (int): Tasks per crewmate (default: 5).
                                  kill_cooldown (int): Impostor kill cooldown in seconds (default: 45).
                                  seed: Random seed for reproducible games.

               :returns: Fully initialized game state ready for gameplay.
               :rtype: AmongUsState

               .. rubric:: Examples

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

               .. note::

                  The initialization automatically balances impostor count based on
                  player count following standard Among Us ratios.



            .. py:attribute:: model_config





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

