games.hold_em.ui
================

.. py:module:: games.hold_em.ui

.. autoapi-nested-parse::

   Texas Hold'em Rich UI for live game display.

   This module provides a beautiful Rich-based terminal UI for displaying
   Texas Hold'em games in real-time, showing:
       - Player positions and chip stacks
       - Community cards and pot
       - Current action and betting
       - Game phase and status


   .. autolink-examples:: games.hold_em.ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.hold_em.ui.logger


Classes
-------

.. autoapisummary::

   games.hold_em.ui.HoldemRichUI


Functions
---------

.. autoapisummary::

   games.hold_em.ui.main


Module Contents
---------------

.. py:class:: HoldemRichUI

   Beautiful Rich UI for displaying a live Texas Hold'em game.


   .. autolink-examples:: HoldemRichUI
      :collapse:

   .. py:method:: _create_initial_state(agent: haive.games.hold_em.game_agent.HoldemGameAgent) -> haive.games.hold_em.state.HoldemState

      Create initial game state from agent config.


      .. autolink-examples:: _create_initial_state
         :collapse:


   .. py:method:: _format_last_action() -> rich.text.Text

      Format the last action for display.


      .. autolink-examples:: _format_last_action
         :collapse:


   .. py:method:: _format_player_short(player: haive.games.hold_em.state.PlayerState, game_state: haive.games.hold_em.state.HoldemState) -> str

      Format player for table display.


      .. autolink-examples:: _format_player_short
         :collapse:


   .. py:method:: _get_player_at_position(game_state: haive.games.hold_em.state.HoldemState, position: int) -> haive.games.hold_em.state.PlayerState | None

      Get player at specific position.


      .. autolink-examples:: _get_player_at_position
         :collapse:


   .. py:method:: _get_player_name_by_id(game_state: haive.games.hold_em.state.HoldemState, player_id: str) -> str

      Get player name by ID.


      .. autolink-examples:: _get_player_name_by_id
         :collapse:


   .. py:method:: _setup_layout()

      Initialize the layout structure.


      .. autolink-examples:: _setup_layout
         :collapse:


   .. py:method:: _suit_symbol(suit: str) -> str

      Convert suit letter to symbol.


      .. autolink-examples:: _suit_symbol
         :collapse:


   .. py:method:: _update_layout()

      Update all layout components with current state.


      .. autolink-examples:: _update_layout
         :collapse:


   .. py:method:: render_action_log() -> rich.panel.Panel

      Render recent actions and decisions.


      .. autolink-examples:: render_action_log
         :collapse:


   .. py:method:: render_community_cards() -> rich.panel.Panel

      Render community cards and board.


      .. autolink-examples:: render_community_cards
         :collapse:


   .. py:method:: render_footer() -> rich.panel.Panel

      Render the footer with controls and current action.


      .. autolink-examples:: render_footer
         :collapse:


   .. py:method:: render_game_stats() -> rich.panel.Panel

      Render game statistics.


      .. autolink-examples:: render_game_stats
         :collapse:


   .. py:method:: render_hand_history() -> rich.panel.Panel

      Render hand history summary.


      .. autolink-examples:: render_hand_history
         :collapse:


   .. py:method:: render_header() -> rich.panel.Panel

      Render the header with game title and phase.


      .. autolink-examples:: render_header
         :collapse:


   .. py:method:: render_player_info() -> rich.panel.Panel

      Render detailed player information.


      .. autolink-examples:: render_player_info
         :collapse:


   .. py:method:: render_pot_info() -> rich.panel.Panel

      Render pot size and betting information.


      .. autolink-examples:: render_pot_info
         :collapse:


   .. py:method:: render_table() -> rich.panel.Panel

      Render the poker table with player positions.


      .. autolink-examples:: render_table
         :collapse:


   .. py:method:: run(agent: haive.games.hold_em.game_agent.HoldemGameAgent, delay: float = 2.0)

      Run the live UI with the Hold'em agent.

      :param agent: The HoldemGameAgent instance
      :param delay: Delay between updates for readability


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: console


   .. py:attribute:: last_action
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: layout


   .. py:attribute:: state
      :type:  dict[str, Any] | None
      :value: None



.. py:function:: main()

   Main function to run the UI demo.


   .. autolink-examples:: main
      :collapse:

.. py:data:: logger

