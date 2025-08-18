games.among_us.demo
===================

.. py:module:: games.among_us.demo

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">11 functions</span> • <span class="module-stat">1 attributes</span>   </div>

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



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.among_us.demo.parser

            
            
            

.. admonition:: Functions (11)
   :class: info

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

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: format_action(move, verbose=False)

            Format an action for display.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_role_color(role)

            Get color for a player role.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_meeting_discussion(agent, state, console, interactive, speed)

            Process a meeting's discussion phase with enhanced visibility.

            :param agent: The AmongUsAgent instance
            :param state: Current game state
            :param console: Rich console for display
            :param interactive: Whether in interactive mode
            :param speed: Simulation speed multiplier

            :returns: Updated state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_meeting_discussion_enhanced(agent, state, ui, interactive, speed)

            Process a meeting's discussion phase with enhanced UI.

            :param agent: The AmongUsAgent instance
            :param state: Current game state
            :param ui: Enhanced UI instance
            :param interactive: Whether in interactive mode
            :param speed: Simulation speed multiplier

            :returns: Updated state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_player_turn(agent, state, player_id, console, interactive, speed)

            Process a single player's turn with enhanced visibility into AI thoughts.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_player_turn_enhanced(agent, state, player_id, ui, interactive, speed)

            Process a single player's turn with enhanced UI.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_random_events(agent, state, console, interactive, speed)

            Process random events that might occur during the task phase.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_random_events_enhanced(agent, state, ui, interactive, speed)

            Process random events that might occur during the task phase with enhanced UI.

            :param agent: The AmongUsAgent instance
            :param state: Current game state
            :param ui: Enhanced UI instance
            :param interactive: Whether in interactive mode
            :param speed: Simulation speed multiplier

            :returns: Updated state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_voting_phase(agent, state, console, interactive, speed)

            Process a meeting's voting phase with enhanced visibility.

            :param agent: The AmongUsAgent instance
            :param state: Current game state
            :param console: Rich console for display
            :param interactive: Whether in interactive mode
            :param speed: Simulation speed multiplier

            :returns: Updated state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: process_voting_phase_enhanced(agent, state, ui, interactive, speed)

            Process a meeting's voting phase with enhanced UI.

            :param agent: The AmongUsAgent instance
            :param state: Current game state
            :param ui: Enhanced UI instance
            :param interactive: Whether in interactive mode
            :param speed: Simulation speed multiplier

            :returns: Updated state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: parser




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.demo import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

