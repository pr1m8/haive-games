games.dominoes.agent
====================

.. py:module:: games.dominoes.agent


Attributes
----------

.. autoapisummary::

   games.dominoes.agent.UI_AVAILABLE
   games.dominoes.agent.agent
   games.dominoes.agent.logger


Classes
-------

.. autoapisummary::

   games.dominoes.agent.DominoesAgent


Module Contents
---------------

.. py:class:: DominoesAgent(config: haive.games.dominoes.config.DominoesAgentConfig | None = None)

   Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.dominoes.config.DominoesAgentConfig`\ ]


   Agent for playing dominoes.


   .. autolink-examples:: DominoesAgent
      :collapse:

   .. py:method:: _extract_analysis(response: Any) -> haive.games.dominoes.models.DominoesAnalysis

      Extract analysis from engine response.


      .. autolink-examples:: _extract_analysis
         :collapse:


   .. py:method:: analyze_player1(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

      Analyze position for player1.

      :param state: The current game state.
      :type state: DominoesState

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: analyze_player1
         :collapse:


   .. py:method:: analyze_player2(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

      Analyze position for player2.

      :param state: The current game state.
      :type state: DominoesState

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: analyze_player2
         :collapse:


   .. py:method:: analyze_position(state: haive.games.dominoes.state.DominoesState, player: str) -> langgraph.types.Command

      Analyze the current position for the specified player.

      :param state: The current game state.
      :type state: DominoesState
      :param player: The player to analyze the position for.
      :type player: str

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: check_game_status(state: haive.games.dominoes.state.DominoesState) -> str

      Check if the game is over.

      :param state: The current game state.
      :type state: DominoesState

      :returns: Next node to go to.
      :rtype: str


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: extract_move(response: Any) -> haive.games.dominoes.models.DominoMove | Literal['pass']

      Extract move from engine response.


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Dominoes game.

      :param state: The initial state.
      :type state: Dict[str, Any]

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: make_move(state: haive.games.dominoes.state.DominoesState, player: str) -> langgraph.types.Command

      Make a move for the specified player.

      :param state: The current game state.
      :type state: DominoesState
      :param player: The player to make the move for.
      :type player: str

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: make_player1_move(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

      Make a move for player1.

      :param state: The current game state.
      :type state: DominoesState

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: make_player1_move
         :collapse:


   .. py:method:: make_player2_move(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

      Make a move for player2.

      :param state: The current game state.
      :type state: DominoesState

      :returns: Command with updated state.
      :rtype: Command


      .. autolink-examples:: make_player2_move
         :collapse:


   .. py:method:: prepare_analysis_context(state: haive.games.dominoes.state.DominoesState, player: str) -> dict[str, Any]

      Prepare context for position analysis.


      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.dominoes.state.DominoesState, player: str) -> dict[str, Any]

      Prepare context for move generation.


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

      Run the full game, optionally visualizing each step.


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: run_game_with_ui(delay: float = 1.5) -> dict[str, Any]

      Run the full game with Rich UI visualization.

      :param delay: Delay between moves in seconds

      :returns: Final game state


      .. autolink-examples:: run_game_with_ui
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the game workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current game state.


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: console


   .. py:attribute:: state_manager


   .. py:attribute:: ui


.. py:data:: UI_AVAILABLE
   :value: True


.. py:data:: agent

.. py:data:: logger

