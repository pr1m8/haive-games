games.cards.standard.bs.agent
=============================

.. py:module:: games.cards.standard.bs.agent


Attributes
----------

.. autoapisummary::

   games.cards.standard.bs.agent.final_state


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.agent.BullshitAgent


Functions
---------

.. autoapisummary::

   games.cards.standard.bs.agent.create_bullshit_agent
   games.cards.standard.bs.agent.run_game


Module Contents
---------------

.. py:class:: BullshitAgent(config: haive.games.cards.standard.bs.config.BullshitAgentConfig = BullshitAgentConfig())

   Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.cards.standard.bs.config.BullshitAgentConfig`\ ]


   Multi-player Bullshit (BS) card game agent.

   Initialize the Bullshit agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BullshitAgent
      :collapse:

   .. py:method:: calculate_challenge_probability(state: haive.games.cards.standard.bs.state.BullshitGameState) -> float

      Calculate the probability of challenging based on game state.

      :param state: Current game state

      :returns: Probability of challenging


      .. autolink-examples:: calculate_challenge_probability
         :collapse:


   .. py:method:: decide_challenge(state: haive.games.cards.standard.bs.state.BullshitGameState) -> str

      Decide whether to challenge the previous player's claim.

      :param state: Current game state

      :returns: Next node in the graph


      .. autolink-examples:: decide_challenge
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Bullshit game.

      :param state: Initial state dictionary (typically empty)

      :returns: Command to set up the game


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: player_turn(state: dict[str, Any]) -> langgraph.types.Command

      Manage a player's turn in the Bullshit game.

      :param state: Current game state

      :returns: Command for next phase


      .. autolink-examples:: player_turn
         :collapse:


   .. py:method:: prepare_challenge_context(state: haive.games.cards.standard.bs.state.BullshitGameState) -> dict[str, Any]

      Prepare context for a challenge decision.

      :param state: Current game state

      :returns: Context dictionary for challenge decision


      .. autolink-examples:: prepare_challenge_context
         :collapse:


   .. py:method:: prepare_claim_context(state: haive.games.cards.standard.bs.state.BullshitGameState) -> dict[str, Any]

      Prepare context for a player's claim.

      :param state: Current game state

      :returns: Context dictionary for claim decision


      .. autolink-examples:: prepare_claim_context
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow for the Bullshit game.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current game state.

      :param state: Current game state


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: challenge_probability
      :value: 0.3



   .. py:attribute:: current_round
      :value: 0



   .. py:attribute:: state_manager


.. py:function:: create_bullshit_agent(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> BullshitAgent

   Create a Bullshit agent with customizable parameters.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param visualize: Whether to visualize the game state

   :returns: Configured BullshitAgent


   .. autolink-examples:: create_bullshit_agent
      :collapse:

.. py:function:: run_game(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> dict

   Convenience function to create and run a Bullshit game.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param visualize: Whether to visualize the game state during play

   :returns: Final game state


   .. autolink-examples:: run_game
      :collapse:

.. py:data:: final_state

