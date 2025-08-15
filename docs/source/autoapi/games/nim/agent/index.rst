games.nim.agent
===============

.. py:module:: games.nim.agent

.. autoapi-nested-parse::

   Agent for playing Nim.

   This module defines the Nim agent, which uses language models to generate moves and
   analyze positions in the game.


   .. autolink-examples:: games.nim.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.nim.agent.RICH_AVAILABLE
   games.nim.agent.logger


Classes
-------

.. autoapisummary::

   games.nim.agent.NimAgent


Functions
---------

.. autoapisummary::

   games.nim.agent.ensure_game_state


Module Contents
---------------

.. py:class:: NimAgent(config: haive.games.nim.config.NimConfig = NimConfig())

   Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.nim.config.NimConfig`\ ]


   Agent for playing Nim.

   Initialize the Nim agent.

   :param config: The configuration for the game.
   :type config: NimConfig


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NimAgent
      :collapse:

   .. py:method:: analyze_player1(state: haive.games.nim.state.NimState) -> langgraph.types.Command

      Analyze position for player1.

      :param state: The current game state.
      :type state: NimState

      :returns: The command to analyze the position.
      :rtype: Command


      .. autolink-examples:: analyze_player1
         :collapse:


   .. py:method:: analyze_player2(state: haive.games.nim.state.NimState) -> langgraph.types.Command

      Analyze position for player2.

      :param state: The current game state.
      :type state: NimState

      :returns: The command to analyze the position.
      :rtype: Command


      .. autolink-examples:: analyze_player2
         :collapse:


   .. py:method:: analyze_position(state: haive.games.nim.state.NimState | dict[str, Any] | langgraph.types.Command, player: str) -> langgraph.types.Command

      Analyze the current position for the specified player.

      :param state: The current game state.
      :param player: The player to analyze the position for.

      :returns: The command to analyze the position.
      :rtype: Command


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: extract_move(response: Any) -> Any

      Extract move from engine response.

      :param response: The response from the engine.
      :type response: Any

      :returns: The move from the engine.
      :rtype: Any


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any] | haive.games.nim.state.NimState | langgraph.types.Command) -> langgraph.types.Command

      Initialize a new Nim game with configured pile sizes.

      :param state: The initial state of the game.

      :returns: The command to initialize the game.
      :rtype: Command


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: make_move(state: haive.games.nim.state.NimState | dict[str, Any] | langgraph.types.Command, player: str) -> langgraph.types.Command

      Make a move for the specified player.

      :param state: The current game state.
      :param player: The player to make the move for.

      :returns: The command to make the move.
      :rtype: Command


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: make_player1_move(state: haive.games.nim.state.NimState) -> langgraph.types.Command

      Make a move for player1.

      :param state: The current game state.
      :type state: NimState

      :returns: The command to make the move.
      :rtype: Command


      .. autolink-examples:: make_player1_move
         :collapse:


   .. py:method:: make_player2_move(state: haive.games.nim.state.NimState) -> langgraph.types.Command

      Make a move for player2.

      :param state: The current game state.
      :type state: NimState

      :returns: The command to make the move.
      :rtype: Command


      .. autolink-examples:: make_player2_move
         :collapse:


   .. py:method:: prepare_analysis_context(state: haive.games.nim.state.NimState, player: str) -> dict[str, Any]

      Prepare context for position analysis.

      :param state: The current game state.
      :type state: NimState
      :param player: The player to prepare the context for.
      :type player: str

      :returns: The context for the position analysis.
      :rtype: Dict[str, Any]


      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.nim.state.NimState, player: str) -> dict[str, Any]

      Prepare context for move generation.

      :param state: The current game state.
      :type state: NimState
      :param player: The player to prepare the context for.
      :type player: str

      :returns: The context for the move generation.
      :rtype: Dict[str, Any]


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

      Run a complete Nim game with optional visualization.

      :param visualize: Whether to visualize each game state.
      :type visualize: bool

      :returns: The final game state.
      :rtype: Dict[str, Any]


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: run_game_with_ui(show_analysis: bool = True) -> dict[str, Any]

      Run a complete Nim game with Rich UI.

      This method runs a Nim game with Rich UI visualization, showing
      the game state after each move. It optionally includes analysis.

      :param show_analysis: Whether to include analysis in the game.

      :returns: The final game state.
      :rtype: Dict[str, Any]


      .. autolink-examples:: run_game_with_ui
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the game workflow.

      :returns: None


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current game state.

      :param state: The current game state.
      :type state: Dict[str, Any]


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: state_manager


   .. py:attribute:: ui


.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.nim.state.NimState | langgraph.types.Command) -> haive.games.nim.state.NimState

   Ensure input is converted to NimState.

   This helper function ensures that the input state is properly converted to a NimState
   object, handling various input types (dict, NimState, Command).

   :param state_input: The state to convert, which can be a dictionary, NimState, or Command.

   :returns: The converted state.
   :rtype: NimState


   .. autolink-examples:: ensure_game_state
      :collapse:

.. py:data:: RICH_AVAILABLE
   :value: False


.. py:data:: logger

