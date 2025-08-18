games.cards.standard.bs.agent
=============================

.. py:module:: games.cards.standard.bs.agent

Module documentation for games.cards.standard.bs.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.cards.standard.bs.agent.final_state

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.cards.standard.bs.agent.BullshitAgent

            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.cards.standard.bs.agent.create_bullshit_agent
      games.cards.standard.bs.agent.run_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BullshitAgent(config: haive.games.cards.standard.bs.config.BullshitAgentConfig = BullshitAgentConfig())

            Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.cards.standard.bs.config.BullshitAgentConfig`\ ]


            Multi-player Bullshit (BS) card game agent.

            Initialize the Bullshit agent.


            .. py:method:: calculate_challenge_probability(state: haive.games.cards.standard.bs.state.BullshitGameState) -> float

               Calculate the probability of challenging based on game state.

               :param state: Current game state

               :returns: Probability of challenging



            .. py:method:: decide_challenge(state: haive.games.cards.standard.bs.state.BullshitGameState) -> str

               Decide whether to challenge the previous player's claim.

               :param state: Current game state

               :returns: Next node in the graph



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new Bullshit game.

               :param state: Initial state dictionary (typically empty)

               :returns: Command to set up the game



            .. py:method:: player_turn(state: dict[str, Any]) -> langgraph.types.Command

               Manage a player's turn in the Bullshit game.

               :param state: Current game state

               :returns: Command for next phase



            .. py:method:: prepare_challenge_context(state: haive.games.cards.standard.bs.state.BullshitGameState) -> dict[str, Any]

               Prepare context for a challenge decision.

               :param state: Current game state

               :returns: Context dictionary for challenge decision



            .. py:method:: prepare_claim_context(state: haive.games.cards.standard.bs.state.BullshitGameState) -> dict[str, Any]

               Prepare context for a player's claim.

               :param state: Current game state

               :returns: Context dictionary for claim decision



            .. py:method:: setup_workflow() -> None

               Set up the workflow for the Bullshit game.



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state.

               :param state: Current game state



            .. py:attribute:: challenge_probability
               :value: 0.3



            .. py:attribute:: current_round
               :value: 0



            .. py:attribute:: state_manager



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_bullshit_agent(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> BullshitAgent

            Create a Bullshit agent with customizable parameters.

            :param num_players: Number of players in the game
            :param max_rounds: Maximum number of rounds to play
            :param visualize: Whether to visualize the game state

            :returns: Configured BullshitAgent



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_game(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> dict

            Convenience function to create and run a Bullshit game.

            :param num_players: Number of players in the game
            :param max_rounds: Maximum number of rounds to play
            :param visualize: Whether to visualize the game state during play

            :returns: Final game state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: final_state




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.bs.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

