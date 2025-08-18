games.monopoly.simple_demo
==========================

.. py:module:: games.monopoly.simple_demo

Simple demo for testing the Monopoly game without LangGraph integration.

This script demonstrates the core functionality of the Monopoly game:
- Board setup
- Player movement
- Property purchasing
- Rent payments
- Game events

Usage:
    python simple_demo.py



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">6 functions</span> • <span class="module-stat">1 attributes</span>   </div>

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



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.monopoly.simple_demo.console

            
            
            

.. admonition:: Functions (6)
   :class: info

   .. autoapisummary::

      games.monopoly.simple_demo.handle_property_landing
      games.monopoly.simple_demo.print_divider
      games.monopoly.simple_demo.print_player_status
      games.monopoly.simple_demo.print_property
      games.monopoly.simple_demo.print_recent_events
      games.monopoly.simple_demo.run_demo

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: handle_property_landing(state: haive.games.monopoly.state.MonopolyState, position: int) -> list[haive.games.monopoly.models.GameEvent]

            Handle a player landing on a property.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: print_divider()

            Print a divider line.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: print_player_status(state: haive.games.monopoly.state.MonopolyState)

            Print current status of all players.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: print_property(property_obj: haive.games.monopoly.models.Property)

            Print property details.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: print_recent_events(events: list[haive.games.monopoly.models.GameEvent], count: int = 5)

            Print recent game events.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_demo(turns: int = 20)

            Run a simple Monopoly game demo.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: console




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.simple_demo import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

