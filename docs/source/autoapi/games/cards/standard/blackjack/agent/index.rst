games.cards.standard.blackjack.agent
====================================

.. py:module:: games.cards.standard.blackjack.agent


Classes
-------

.. autoapisummary::

   games.cards.standard.blackjack.agent.BlackjackAgent


Module Contents
---------------

.. py:class:: BlackjackAgent(config: haive.games.cards.standard.blackjack.config.BlackjackAgentConfig = BlackjackAgentConfig())

   Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.cards.standard.blackjack.config.BlackjackAgentConfig`\ ]


   Multi-player Blackjack game agent.

   Initialize the Blackjack agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BlackjackAgent
      :collapse:

   .. py:method:: betting_phase(state: dict[str, Any]) -> langgraph.types.Command

      Manage the betting phase for all players.

      :param state: Current game state

      :returns: Command for next phase


      .. autolink-examples:: betting_phase
         :collapse:


   .. py:method:: deal_cards(state: dict[str, Any]) -> langgraph.types.Command

      Deal initial cards to all players and dealer.

      :param state: Current game state

      :returns: Command for player turns


      .. autolink-examples:: deal_cards
         :collapse:


   .. py:method:: dealer_turn(state: dict[str, Any]) -> langgraph.types.Command

      Execute dealer's turn.

      :param state: Current game state

      :returns: Command for game conclusion


      .. autolink-examples:: dealer_turn
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Blackjack game.

      :param state: Initial state dictionary (typically empty)

      :returns: Command to set up the game


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: player_turns(state: dict[str, Any]) -> langgraph.types.Command

      Manage player turns for decision making.

      :param state: Current game state

      :returns: Command for next phase


      .. autolink-examples:: player_turns
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow for the Blackjack game.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current game state.

      :param state: Current game state


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: current_round
      :value: 0



   .. py:attribute:: previous_round_summary
      :value: 'New game started'



   .. py:attribute:: state_manager


