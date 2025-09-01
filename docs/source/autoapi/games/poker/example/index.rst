games.poker.example
===================

.. py:module:: games.poker.example

.. autoapi-nested-parse::

   Example poker game demonstrating the Haive poker implementation.

   This module provides a comprehensive example of running a poker game with
   AI-powered players using the Haive framework. It demonstrates:
       - Creating and configuring poker agents with different playing styles
       - Running a complete poker game with betting rounds
       - Rich terminal UI with card visualization
       - Hand evaluation and winner determination
       - Game state tracking and analysis

   The example supports various poker configurations including different
   numbers of players, starting chips, blind structures, and AI strategies.

   Usage:
       Basic game:
           $ python example.py

       Custom configuration:
           $ python example.py --players 6 --chips 1000 --blinds 10 20

       With specific AI strategies:
           $ python example.py --strategies aggressive conservative balanced random

   .. rubric:: Examples

   >>> # Run a basic 4-player game
   >>> from haive.games.poker.example import run_poker_game
   >>> run_poker_game(num_players=4, starting_chips=1000)



Attributes
----------

.. autoapisummary::

   games.poker.example.live
   games.poker.example.logger
   games.poker.example.player_names
   games.poker.example.ui


Functions
---------

.. autoapisummary::

   games.poker.example.create_config_from_args
   games.poker.example.format_card
   games.poker.example.get_position_name
   games.poker.example.launch_in_separate_window
   games.poker.example.main
   games.poker.example.run_rich_ui_game
   games.poker.example.run_text_game
   games.poker.example.update_ui
   games.poker.example.visualize_game_state


Module Contents
---------------

.. py:function:: create_config_from_args(args, player_names)

   Create a poker agent config from command line args.


.. py:function:: format_card(card: haive.games.poker.models.Card) -> str

   Format a card with unicode symbols.


.. py:function:: get_position_name(position: int, num_players: int) -> str

   Get the poker position name.


.. py:function:: launch_in_separate_window(args, player_names)

   Launch the poker game in a separate terminal window.


.. py:function:: main()

   Main.


.. py:function:: run_rich_ui_game(config, player_names, delay, max_hands=None)

   Run the game with rich UI visualization.


.. py:function:: run_text_game(config, delay)

   Run the game with text-only visualization.


.. py:function:: update_ui()

   Helper function to update all UI components.


.. py:function:: visualize_game_state(game_state)

   Visualize the current game state in a human-readable format.


.. py:data:: live
   :value: None


.. py:data:: logger

.. py:data:: player_names
   :value: ['Alice', 'Bob']


.. py:data:: ui
   :value: None


