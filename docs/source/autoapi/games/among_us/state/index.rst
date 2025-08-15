games.among_us.state
====================

.. py:module:: games.among_us.state

.. autoapi-nested-parse::

   Comprehensive state management for Among Us social deduction gameplay.

   This module provides the core state model for managing Among Us game sessions,
   tracking player positions, tasks, sabotages, and game progression. The state
   system supports complex spatial navigation, role-based mechanics, and real-time
   event handling for authentic social deduction experiences.

   The state management includes:
   - Dynamic map initialization with rooms and vents
   - Player position and status tracking
   - Task completion monitoring
   - Sabotage event management
   - Meeting and voting mechanics
   - Win condition evaluation
   - Observation and memory systems

   .. rubric:: Examples

   Initializing a game state::

       state = AmongUsState()
       state.initialize_map()  # Creates Skeld map by default

       # Add players
       state.player_states["player1"] = PlayerState(
           id="player1",
           role=PlayerRole.CREWMATE,
           location="cafeteria"
       )

   Checking win conditions::

       winner = state.check_win_condition()
       if winner == "crewmates":
           print("All tasks completed!")
       elif winner == "impostors":
           print("Impostors have taken control!")

   Managing sabotages::

       # Create reactor meltdown
       sabotage = SabotageEvent(
           type="reactor",
           location="reactor",
           timer=30
       )
       state.sabotages.append(sabotage)

       # Check if critical
       active = state.get_active_sabotage()
       if active and active.is_critical():
           print(f"Emergency! {active.timer}s remaining!")

   .. note::

      The state model extends MultiPlayerGameState and integrates with
      LangGraph for distributed game session management.


   .. autolink-examples:: games.among_us.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.among_us.state.AmongUsState


Module Contents
---------------

.. py:class:: AmongUsState

   Bases: :py:obj:`haive.games.framework.multi_player.state.MultiPlayerGameState`


   Comprehensive state model for Among Us game sessions.

   This class manages all aspects of an Among Us game state, including
   spatial layout, player tracking, task management, and game progression.
   It provides methods for querying game state, updating player positions,
   managing events, and evaluating win conditions.

   The state model supports:
   - Multiple map layouts (currently Skeld, with Polus/Mira HQ planned)
   - Real-time player position and status tracking
   - Task assignment and completion monitoring
   - Sabotage event lifecycle management
   - Emergency meeting and voting systems
   - Observation and memory tracking for deduction
   - Flexible win condition evaluation

   .. attribute:: map_locations

      List of valid room IDs for the current map.
      Used for movement validation and spawn points.

   .. attribute:: map_name

      Name of the current map (e.g., "skeld", "polus").
      Determines room layout and task locations.

   .. attribute:: rooms

      Mapping of room IDs to Room objects.
      Defines spatial layout and connections.

   .. attribute:: vents

      Mapping of vent IDs to Vent objects.
      Enables impostor movement through vent network.

   .. attribute:: player_states

      Mapping of player IDs to PlayerState objects.
      Tracks all player information including role and position.

   .. attribute:: tasks

      Mapping of task IDs to Task objects.
      Defines available tasks and their completion status.

   .. attribute:: sabotages

      List of active and resolved sabotage events.
      Tracks sabotage history and current emergencies.

   .. attribute:: eliminated_players

      List of player IDs who have been eliminated.
      Used for ghost mechanics and win conditions.

   .. attribute:: meeting_active

      Whether an emergency meeting is in progress.
      Pauses gameplay and enables discussion/voting.

   .. attribute:: meeting_caller

      Player ID who called the current meeting.
      None if meeting was triggered by body report.

   .. attribute:: reported_body

      Player ID of body that triggered meeting.
      None if meeting was called via emergency button.

   .. attribute:: votes

      Mapping of voter ID to target ID for current meeting.
      Tracks voting progress and determines ejection.

   .. attribute:: game_phase

      Current phase of gameplay.
      Controls available actions and UI state.

   .. attribute:: impostor_count

      Number of living impostors.
      Cached for efficient win condition checks.

   .. attribute:: crewmate_count

      Number of living crewmates.
      Cached for efficient win condition checks.

   .. attribute:: discussion_history

      List of discussion events and messages.
      Provides context for AI decision-making.

   .. attribute:: kill_cooldowns

      Mapping of impostor ID to remaining cooldown.
      Prevents rapid elimination chains.

   .. rubric:: Examples

   Creating a new game state::

       state = AmongUsState(
           map_name="skeld",
           impostor_count=2,
           crewmate_count=8
       )
       state.initialize_map()

   Checking task progress::

       progress = state.get_task_completion_percentage()
       if progress >= 100:
           print("Crewmates win by tasks!")

   Managing meetings::

       state.meeting_active = True
       state.meeting_caller = "player1"
       state.votes["player1"] = "player3"  # Voting for player3
       state.votes["player2"] = "skip"     # Voting to skip


   .. autolink-examples:: AmongUsState
      :collapse:

   .. py:method:: add_observation(player_id: str, observation: str) -> None

      Add an observation to a player's memory.

      Observations form the basis of deduction in Among Us. This method
      records what a player has witnessed for later analysis.

      :param player_id: ID of the observing player.
      :param observation: Description of what was observed.

      .. rubric:: Examples

      Witnessing movement::

          state.add_observation(
              "player1",
              "Saw player3 enter electrical at 14:32"
          )

      Task verification::

          state.add_observation(
              "player2",
              "Watched player4 complete medbay scan"
          )


      .. autolink-examples:: add_observation
         :collapse:


   .. py:method:: add_observation_to_all_in_room(room_id: str, observation: str, exclude_players: list[str] | None = None) -> None

      Add an observation to all players in a specific room.

      Used for events that are visible to everyone in a location,
      such as sabotages, eliminations, or visual tasks.

      :param room_id: Room where the event occurred.
      :param observation: Description of the observed event.
      :param exclude_players: Optional list of player IDs to exclude.
                              Typically used to exclude the actor from observations.

      .. rubric:: Examples

      Elimination witnessed::

          state.add_observation_to_all_in_room(
              "electrical",
              "Player5 eliminated player2!",
              exclude_players=["player5"]  # Killer doesn't observe self
          )

      Visual task::

          state.add_observation_to_all_in_room(
              "medbay",
              "Player3 completed scan (confirmed crewmate)"
          )


      .. autolink-examples:: add_observation_to_all_in_room
         :collapse:


   .. py:method:: check_win_condition() -> Literal['crewmates', 'impostors'] | None

      Check if either side has achieved victory.

      Evaluates all win conditions for both teams:

      Crewmate victories:
      - All tasks completed
      - All impostors eliminated

      Impostor victories:
      - Impostor count >= crewmate count
      - Critical sabotage timer expired

      :returns: Winning team or None.
      :rtype: Optional[Literal["crewmates", "impostors"]]

      .. rubric:: Examples

      Task victory::

          # All tasks done
          winner = state.check_win_condition()
          assert winner == "crewmates"

      Impostor majority::

          # 2 impostors, 2 crewmates remaining
          winner = state.check_win_condition()
          assert winner == "impostors"

      Sabotage victory::

          # Reactor meltdown timer reaches 0
          winner = state.check_win_condition()
          assert winner == "impostors"


      .. autolink-examples:: check_win_condition
         :collapse:


   .. py:method:: decrement_cooldowns() -> None

      Decrement all active kill cooldowns by 1 second.

      Should be called each game tick/second to update cooldowns.
      Automatically removes cooldowns that reach 0.

      .. rubric:: Examples

      Game loop integration::

          # In game tick handler
          state.decrement_cooldowns()

          # Check if any impostors can now kill
          for impostor_id in impostor_ids:
              if state.get_player_cooldown(impostor_id) == 0:
                  # Enable kill button in UI
                  pass


      .. autolink-examples:: decrement_cooldowns
         :collapse:


   .. py:method:: get_active_sabotage() -> haive.games.among_us.models.SabotageEvent | None

      Get the currently active sabotage event.

      Only one sabotage can be active at a time. This method returns
      the first unresolved sabotage found.

      :returns: Active sabotage or None.
      :rtype: Optional[SabotageEvent]

      .. rubric:: Examples

      Emergency response::

          sabotage = state.get_active_sabotage()
          if sabotage and sabotage.is_critical():
              print(f"EMERGENCY: {sabotage.type} - {sabotage.timer}s left!")

      Checking if sabotage is possible::

          if state.get_active_sabotage() is None:
              # Impostors can trigger new sabotage
              pass


      .. autolink-examples:: get_active_sabotage
         :collapse:


   .. py:method:: get_alive_players() -> list[str]

      Get list of alive player IDs.

      Returns only players who have not been eliminated, useful for
      voting counts, task assignments, and win condition checks.

      :returns: IDs of all living players.
      :rtype: List[str]

      .. rubric:: Examples

      During meeting::

          alive = state.get_alive_players()
          print(f"{len(alive)} players can vote")

      Win condition check::

          alive = state.get_alive_players()
          if len(alive) <= 2:
              # Check for impostor majority
              pass


      .. autolink-examples:: get_alive_players
         :collapse:


   .. py:method:: get_connected_rooms(room_id: str) -> list[str]

      Get all rooms directly connected to the given room.

      Returns only accessible connections (not blocked by sabotage).
      Used for pathfinding and movement validation.

      :param room_id: Source room to check connections from.

      :returns: IDs of all accessible connected rooms.
      :rtype: List[str]

      .. rubric:: Examples

      Movement options::

          adjacent = state.get_connected_rooms("cafeteria")
          print(f"Can move to: {', '.join(adjacent)}")

      Sabotage effects::

          # During O2 sabotage, some doors may be sealed
          rooms = state.get_connected_rooms("admin")
          if len(rooms) < normal_count:
              print("Some exits are blocked!")


      .. autolink-examples:: get_connected_rooms
         :collapse:


   .. py:method:: get_connected_vents(vent_id: str) -> list[str]

      Get all vents connected to the given vent.

      Used for impostor movement through the vent network.
      All vent connections are always accessible (no blocking).

      :param vent_id: Source vent to check connections from.

      :returns: IDs of all connected vents.
      :rtype: List[str]

      .. rubric:: Examples

      Vent navigation::

          connected = state.get_connected_vents("electrical_vent")
          for vent_id in connected:
              vent = state.get_vent(vent_id)
              print(f"Can emerge in: {vent.location}")


      .. autolink-examples:: get_connected_vents
         :collapse:


   .. py:method:: get_player_cooldown(player_id: str) -> int

      Get a player's kill cooldown in seconds.

      :param player_id: ID of the player (impostor) to check.

      :returns: Remaining cooldown seconds (0 if can kill).
      :rtype: int

      .. rubric:: Examples

      Checking kill availability::

          cooldown = state.get_player_cooldown("impostor1")
          if cooldown == 0:
              print("Kill ability ready")
          else:
              print(f"Kill on cooldown: {cooldown}s")


      .. autolink-examples:: get_player_cooldown
         :collapse:


   .. py:method:: get_room(room_id: str) -> haive.games.among_us.models.Room | None

      Get a room by its unique identifier.

      :param room_id: Unique room identifier (e.g., "cafeteria").

      :returns: Room object if found, None otherwise.
      :rtype: Optional[Room]

      .. rubric:: Examples

      Checking room properties::

          room = state.get_room("electrical")
          if room and room.has_security_camera:
              print("This room is monitored")


      .. autolink-examples:: get_room
         :collapse:


   .. py:method:: get_task_completion_percentage() -> float

      Calculate overall task completion percentage.

      Computes the percentage of all tasks that have been completed
      across all crewmates. This is a primary win condition - crewmates
      win immediately when this reaches 100%.

      :returns: Percentage of completed tasks (0-100).
      :rtype: float

      .. rubric:: Examples

      Progress tracking::

          progress = state.get_task_completion_percentage()
          print(f"Tasks: {progress:.1f}% complete")

      Win condition::

          if state.get_task_completion_percentage() >= 100:
              return "crewmates_win_by_tasks"

      .. note:: Returns 100.0 if no tasks exist (edge case handling).


      .. autolink-examples:: get_task_completion_percentage
         :collapse:


   .. py:method:: get_vent(vent_id: str) -> haive.games.among_us.models.Vent | None

      Get a vent by its unique identifier.

      :param vent_id: Unique vent identifier (e.g., "electrical_vent").

      :returns: Vent object if found, None otherwise.
      :rtype: Optional[Vent]

      .. rubric:: Examples

      Checking vent connections::

          vent = state.get_vent("cafeteria_vent")
          if vent:
              connected = [c.target_vent_id for c in vent.connections]
              print(f"Can travel to: {connected}")


      .. autolink-examples:: get_vent
         :collapse:


   .. py:method:: get_vents_in_room(room_id: str) -> list[haive.games.among_us.models.Vent]

      Get all vents located in a specific room.

      Used for impostor movement options and vent camping detection.

      :param room_id: Room to search for vents.

      :returns: All vents in the specified room.
      :rtype: List[Vent]

      .. rubric:: Examples

      Impostor options::

          vents = state.get_vents_in_room("electrical")
          if vents and player.role == PlayerRole.IMPOSTOR:
              print(f"Can enter {len(vents)} vent(s) here")


      .. autolink-examples:: get_vents_in_room
         :collapse:


   .. py:method:: initialize_map() -> None

      Initialize the map with rooms and vents based on the map name.

      Creates the spatial layout for the selected map, including all rooms,
      connections, and vent networks. Currently supports the Skeld map with
      plans for Polus and Mira HQ.

      The initialization includes:
      - Room creation with connections and properties
      - Vent network setup with travel times
      - Map location list for spawn points

      .. rubric:: Examples

      Default Skeld initialization::

          state = AmongUsState(map_name="skeld")
          state.initialize_map()
          assert "cafeteria" in state.rooms
          assert len(state.vents) == 10  # Skeld has 10 vents

      Future map support::

          state = AmongUsState(map_name="polus")
          state.initialize_map()  # Will support Polus layout

      .. note::

         This method clears any existing rooms and vents before
         creating the new map layout.


      .. autolink-examples:: initialize_map
         :collapse:


   .. py:method:: set_player_cooldown(player_id: str, cooldown: int) -> None

      Set a player's kill cooldown.

      Typically called after an impostor eliminates someone.

      :param player_id: ID of the player (impostor).
      :param cooldown: Cooldown duration in seconds.

      .. rubric:: Examples

      After elimination::

          # Standard 30 second cooldown
          state.set_player_cooldown("impostor1", 30)

      Custom game settings::

          # Fast-paced game with 10s cooldown
          state.set_player_cooldown("impostor1", 10)


      .. autolink-examples:: set_player_cooldown
         :collapse:


   .. py:method:: validate_map_name(v: str) -> str
      :classmethod:


      Validate map name is supported.

      :param v: Map name to validate.

      :returns: Validated map name in lowercase.
      :rtype: str

      :raises ValueError: If map name is not supported.


      .. autolink-examples:: validate_map_name
         :collapse:


   .. py:attribute:: crewmate_count
      :type:  int
      :value: None



   .. py:attribute:: discussion_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: eliminated_players
      :type:  list[str]
      :value: None



   .. py:attribute:: game_phase
      :type:  haive.games.among_us.models.AmongUsGamePhase
      :value: None



   .. py:property:: game_statistics
      :type: dict[str, Any]


      Calculate comprehensive game statistics.

      :returns: Statistics including player counts, progress, etc.
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      Displaying game stats::

          stats = state.game_statistics
          print(f"Tasks: {stats['task_progress']:.1f}%")
          print(f"Impostors: {stats['alive_impostors']}/{stats['total_impostors']}")

      .. autolink-examples:: game_statistics
         :collapse:


   .. py:attribute:: impostor_count
      :type:  int
      :value: None



   .. py:attribute:: kill_cooldowns
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: map_locations
      :type:  list[str]
      :value: None



   .. py:attribute:: map_name
      :type:  str
      :value: None



   .. py:attribute:: meeting_active
      :type:  bool
      :value: None



   .. py:attribute:: meeting_caller
      :type:  str | None
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: player_states
      :type:  dict[str, haive.games.among_us.models.PlayerState]
      :value: None



   .. py:attribute:: reported_body
      :type:  str | None
      :value: None



   .. py:attribute:: rooms
      :type:  dict[str, haive.games.among_us.models.Room]
      :value: None



   .. py:attribute:: sabotages
      :type:  list[haive.games.among_us.models.SabotageEvent]
      :value: None



   .. py:attribute:: tasks
      :type:  dict[str, haive.games.among_us.models.Task]
      :value: None



   .. py:attribute:: vents
      :type:  dict[str, haive.games.among_us.models.Vent]
      :value: None



   .. py:attribute:: votes
      :type:  dict[str, str]
      :value: None



