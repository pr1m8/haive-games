games.hold_em.ui
================

.. py:module:: games.hold_em.ui

Texas Hold'em Rich UI for live game display.

This module provides a beautiful Rich-based terminal UI for displaying
Texas Hold'em games in real-time, showing:
    - Player positions and chip stacks
    - Community cards and pot
    - Current action and betting
    - Game phase and status



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Texas Hold'em Rich UI for live game display.

   This module provides a beautiful Rich-based terminal UI for displaying
   Texas Hold'em games in real-time, showing:
       - Player positions and chip stacks
       - Community cards and pot
       - Current action and betting
       - Game phase and status



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.hold_em.ui.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.hold_em.ui.HoldemRichUI

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.hold_em.ui.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HoldemRichUI

            Beautiful Rich UI for displaying a live Texas Hold'em game.


            .. py:method:: _create_initial_state(agent: haive.games.hold_em.game_agent.HoldemGameAgent) -> haive.games.hold_em.state.HoldemState

               Create initial game state from agent config.



            .. py:method:: _format_last_action() -> rich.text.Text

               Format the last action for display.



            .. py:method:: _format_player_short(player: haive.games.hold_em.state.PlayerState, game_state: haive.games.hold_em.state.HoldemState) -> str

               Format player for table display.



            .. py:method:: _get_player_at_position(game_state: haive.games.hold_em.state.HoldemState, position: int) -> haive.games.hold_em.state.PlayerState | None

               Get player at specific position.



            .. py:method:: _get_player_name_by_id(game_state: haive.games.hold_em.state.HoldemState, player_id: str) -> str

               Get player name by ID.



            .. py:method:: _setup_layout()

               Initialize the layout structure.



            .. py:method:: _suit_symbol(suit: str) -> str

               Convert suit letter to symbol.



            .. py:method:: _update_layout()

               Update all layout components with current state.



            .. py:method:: render_action_log() -> rich.panel.Panel

               Render recent actions and decisions.



            .. py:method:: render_community_cards() -> rich.panel.Panel

               Render community cards and board.



            .. py:method:: render_footer() -> rich.panel.Panel

               Render the footer with controls and current action.



            .. py:method:: render_game_stats() -> rich.panel.Panel

               Render game statistics.



            .. py:method:: render_hand_history() -> rich.panel.Panel

               Render hand history summary.



            .. py:method:: render_header() -> rich.panel.Panel

               Render the header with game title and phase.



            .. py:method:: render_player_info() -> rich.panel.Panel

               Render detailed player information.



            .. py:method:: render_pot_info() -> rich.panel.Panel

               Render pot size and betting information.



            .. py:method:: render_table() -> rich.panel.Panel

               Render the poker table with player positions.



            .. py:method:: run(agent: haive.games.hold_em.game_agent.HoldemGameAgent, delay: float = 2.0)

               Run the live UI with the Hold'em agent.

               :param agent: The HoldemGameAgent instance
               :param delay: Delay between updates for readability



            .. py:attribute:: console


            .. py:attribute:: last_action
               :type:  dict[str, Any] | None
               :value: None



            .. py:attribute:: layout


            .. py:attribute:: state
               :type:  dict[str, Any] | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Main function to run the UI demo.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

