games.monopoly.simple_demo
==========================

.. py:module:: games.monopoly.simple_demo

.. autoapi-nested-parse::

   Simple demo for testing the Monopoly game without LangGraph integration.

   This script demonstrates the core functionality of the Monopoly game:
   - Board setup
   - Player movement
   - Property purchasing
   - Rent payments
   - Game events

   Usage:
       python simple_demo.py



Attributes
----------

.. autoapisummary::

   games.monopoly.simple_demo.console


Functions
---------

.. autoapisummary::

   games.monopoly.simple_demo.handle_property_landing
   games.monopoly.simple_demo.print_divider
   games.monopoly.simple_demo.print_player_status
   games.monopoly.simple_demo.print_property
   games.monopoly.simple_demo.print_recent_events
   games.monopoly.simple_demo.run_demo


Module Contents
---------------

.. py:function:: handle_property_landing(state: haive.games.monopoly.state.MonopolyState, position: int) -> list[haive.games.monopoly.models.GameEvent]

   Handle a player landing on a property.


.. py:function:: print_divider()

   Print a divider line.


.. py:function:: print_player_status(state: haive.games.monopoly.state.MonopolyState)

   Print current status of all players.


.. py:function:: print_property(property_obj: haive.games.monopoly.models.Property)

   Print property details.


.. py:function:: print_recent_events(events: list[haive.games.monopoly.models.GameEvent], count: int = 5)

   Print recent game events.


.. py:function:: run_demo(turns: int = 20)

   Run a simple Monopoly game demo.


.. py:data:: console

