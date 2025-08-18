games.cards.standard.blackjack.agent
====================================

.. py:module:: games.cards.standard.blackjack.agent

Module documentation for games.cards.standard.blackjack.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.cards.standard.blackjack.agent.BlackjackAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BlackjackAgent(config: haive.games.cards.standard.blackjack.config.BlackjackAgentConfig = BlackjackAgentConfig())

            Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.cards.standard.blackjack.config.BlackjackAgentConfig`\ ]


            Multi-player Blackjack game agent.

            Initialize the Blackjack agent.


            .. py:method:: betting_phase(state: dict[str, Any]) -> langgraph.types.Command

               Manage the betting phase for all players.

               :param state: Current game state

               :returns: Command for next phase



            .. py:method:: deal_cards(state: dict[str, Any]) -> langgraph.types.Command

               Deal initial cards to all players and dealer.

               :param state: Current game state

               :returns: Command for player turns



            .. py:method:: dealer_turn(state: dict[str, Any]) -> langgraph.types.Command

               Execute dealer's turn.

               :param state: Current game state

               :returns: Command for game conclusion



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new Blackjack game.

               :param state: Initial state dictionary (typically empty)

               :returns: Command to set up the game



            .. py:method:: player_turns(state: dict[str, Any]) -> langgraph.types.Command

               Manage player turns for decision making.

               :param state: Current game state

               :returns: Command for next phase



            .. py:method:: setup_workflow() -> None

               Set up the workflow for the Blackjack game.



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state.

               :param state: Current game state



            .. py:attribute:: current_round
               :value: 0



            .. py:attribute:: previous_round_summary
               :value: 'New game started'



            .. py:attribute:: state_manager





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.blackjack.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

