games.among_us.demo
===================

.. py:module:: games.among_us.demo

.. autoapi-nested-parse::

   Among Us social deduction game demo using the Haive framework.

   This module demonstrates an implementation of the popular social deduction game
   Among Us, where crewmates try to complete tasks while impostors attempt to
   eliminate them. The game features AI-powered players that engage in discussion,
   voting, and strategic deception.

   The demo showcases:
       - Multi-player social deduction gameplay with AI agents
       - Task completion and sabotage mechanics
       - Emergency meetings and discussion phases
       - Voting system with accusations and defenses
       - Rich terminal UI with game state visualization
       - Different AI personalities (suspicious, trusting, analytical)
       - Victory conditions for both crewmates and impostors

   Game Flow:
       1. Players are assigned roles (crewmate or impostor)
       2. Crewmates complete tasks while impostors sabotage
       3. Emergency meetings are called when bodies are found
       4. Players discuss and vote to eject suspected impostors
       5. Game ends when all tasks complete or impostors outnumber crew

   Usage:
       Basic game (5 players, 1 impostor):
           $ python demo.py

       Custom configuration:
           $ python demo.py --players 8 --impostors 2 --difficulty hard

       With specific map:
           $ python demo.py --map skeld --tasks 10

   .. rubric:: Example

   >>> # Run a standard Among Us game
   >>> from haive.games.among_us.demo import run_among_us_demo
   >>> run_among_us_demo(num_players=7, num_impostors=2)


   .. autolink-examples:: games.among_us.demo
      :collapse:


Attributes
----------

.. autoapisummary::

   games.among_us.demo.parser


Functions
---------

.. autoapisummary::

   games.among_us.demo.format_action
   games.among_us.demo.get_role_color
   games.among_us.demo.process_meeting_discussion
   games.among_us.demo.process_meeting_discussion_enhanced
   games.among_us.demo.process_player_turn
   games.among_us.demo.process_player_turn_enhanced
   games.among_us.demo.process_random_events
   games.among_us.demo.process_random_events_enhanced
   games.among_us.demo.process_voting_phase
   games.among_us.demo.process_voting_phase_enhanced
   games.among_us.demo.run_among_us_demo


Module Contents
---------------

.. py:function:: format_action(move, verbose=False)

   Format an action for display.


   .. autolink-examples:: format_action
      :collapse:

.. py:function:: get_role_color(role)

   Get color for a player role.


   .. autolink-examples:: get_role_color
      :collapse:

.. py:function:: process_meeting_discussion(agent, state, console, interactive, speed)

   Process a meeting's discussion phase with enhanced visibility.

   :param agent: The AmongUsAgent instance
   :param state: Current game state
   :param console: Rich console for display
   :param interactive: Whether in interactive mode
   :param speed: Simulation speed multiplier

   :returns: Updated state


   .. autolink-examples:: process_meeting_discussion
      :collapse:

.. py:function:: process_meeting_discussion_enhanced(agent, state, ui, interactive, speed)

   Process a meeting's discussion phase with enhanced UI.

   :param agent: The AmongUsAgent instance
   :param state: Current game state
   :param ui: Enhanced UI instance
   :param interactive: Whether in interactive mode
   :param speed: Simulation speed multiplier

   :returns: Updated state


   .. autolink-examples:: process_meeting_discussion_enhanced
      :collapse:

.. py:function:: process_player_turn(agent, state, player_id, console, interactive, speed)

   Process a single player's turn with enhanced visibility into AI thoughts.


   .. autolink-examples:: process_player_turn
      :collapse:

.. py:function:: process_player_turn_enhanced(agent, state, player_id, ui, interactive, speed)

   Process a single player's turn with enhanced UI.


   .. autolink-examples:: process_player_turn_enhanced
      :collapse:

.. py:function:: process_random_events(agent, state, console, interactive, speed)

   Process random events that might occur during the task phase.


   .. autolink-examples:: process_random_events
      :collapse:

.. py:function:: process_random_events_enhanced(agent, state, ui, interactive, speed)

   Process random events that might occur during the task phase with enhanced UI.

   :param agent: The AmongUsAgent instance
   :param state: Current game state
   :param ui: Enhanced UI instance
   :param interactive: Whether in interactive mode
   :param speed: Simulation speed multiplier

   :returns: Updated state


   .. autolink-examples:: process_random_events_enhanced
      :collapse:

.. py:function:: process_voting_phase(agent, state, console, interactive, speed)

   Process a meeting's voting phase with enhanced visibility.

   :param agent: The AmongUsAgent instance
   :param state: Current game state
   :param console: Rich console for display
   :param interactive: Whether in interactive mode
   :param speed: Simulation speed multiplier

   :returns: Updated state


   .. autolink-examples:: process_voting_phase
      :collapse:

.. py:function:: process_voting_phase_enhanced(agent, state, ui, interactive, speed)

   Process a meeting's voting phase with enhanced UI.

   :param agent: The AmongUsAgent instance
   :param state: Current game state
   :param ui: Enhanced UI instance
   :param interactive: Whether in interactive mode
   :param speed: Simulation speed multiplier

   :returns: Updated state


   .. autolink-examples:: process_voting_phase_enhanced
      :collapse:

.. py:function:: run_among_us_demo(player_count: int = 6, impostor_count: int = 1, map_name: str = 'skeld', save_path: str = None, load_path: str = None, interactive: bool = True, max_rounds: int = 15, speed: float = 1.0, use_enhanced_ui: bool = True)

   Run a demo of the Among Us game with AI agents and enhanced visibility.

   :param player_count: Number of players (4-10)
   :param impostor_count: Number of impostors (1-3)
   :param map_name: Name of map to use
   :param save_path: Path to save game at the end
   :param load_path: Path to load a saved game
   :param interactive: Whether to run in interactive mode
   :param max_rounds: Maximum number of rounds
   :param speed: Simulation speed multiplier
   :param use_enhanced_ui: Whether to use the enhanced UI (recommended)


   .. autolink-examples:: run_among_us_demo
      :collapse:

.. py:data:: parser

