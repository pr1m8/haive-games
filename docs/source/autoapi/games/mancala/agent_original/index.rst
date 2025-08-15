games.mancala.agent_original
============================

.. py:module:: games.mancala.agent_original

.. autoapi-nested-parse::

   Mancala game agent.

   This module defines the Mancala game agent, which uses language models to generate moves
   and analyze positions in the game.


   .. autolink-examples:: games.mancala.agent_original
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mancala.agent_original.logger


Classes
-------

.. autoapisummary::

   games.mancala.agent_original.MancalaAgent


Functions
---------

.. autoapisummary::

   games.mancala.agent_original.ensure_game_state


Module Contents
---------------

.. py:class:: MancalaAgent(config: haive.games.mancala.config.MancalaConfig = MancalaConfig())

   Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.mancala.config.MancalaConfig`\ ]


   Agent for playing Mancala.

   This class implements the Mancala game agent, which uses language models to generate
   moves and analyze positions in the game.


   Initialize the Mancala agent.

   :param config: The configuration for the Mancala game.
   :type config: MancalaConfig


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MancalaAgent
      :collapse:

   .. py:method:: analyze_player1(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

      Analyze position for player1.

      :param state: Current game state.
      :type state: MancalaState

      :returns: Updated game state after the analysis.
      :rtype: Command


      .. autolink-examples:: analyze_player1
         :collapse:


   .. py:method:: analyze_player2(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

      Analyze position for player2.

      :param state: Current game state.
      :type state: MancalaState

      :returns: Updated game state after the analysis.
      :rtype: Command


      .. autolink-examples:: analyze_player2
         :collapse:


   .. py:method:: analyze_position(state: haive.games.mancala.state.MancalaState, player: str) -> langgraph.types.Command

      Analyze the current position for the specified player.

      :param state: Current game state.
      :type state: MancalaState
      :param player: The player making the analysis ('player1' or 'player2').
      :type player: str

      :returns: Updated game state after the analysis.
      :rtype: Command


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: extract_analysis(response: Any) -> Any

      Extract analysis from engine response.

      :param response: Response from the engine.
      :type response: Any

      :returns: Parsed analysis object.
      :rtype: Any


      .. autolink-examples:: extract_analysis
         :collapse:


   .. py:method:: extract_move(response: Any) -> haive.games.mancala.models.MancalaMove

      Extract move from engine response.

      :param response: Response from the engine.
      :type response: Any

      :returns: Parsed move object.
      :rtype: MancalaMove


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Mancala game with configured stones per pit.

      :param state: Initial state dictionary (unused here but required for interface).
      :type state: Dict[str, Any]

      :returns: Initialization command containing the new game state fields.
      :rtype: Command


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: make_move(state: haive.games.mancala.state.MancalaState, player: str) -> langgraph.types.Command

      Make a move for the specified player.

      :param state: Current game state.
      :type state: MancalaState
      :param player: The player making the move ('player1' or 'player2').
      :type player: str

      :returns: Updated game state after the move.
      :rtype: Command


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: make_player1_move(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

      Make a move for player1.

      :param state: Current game state.
      :type state: MancalaState

      :returns: Updated game state after the move.
      :rtype: Command


      .. autolink-examples:: make_player1_move
         :collapse:


   .. py:method:: make_player2_move(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

      Make a move for player2.

      :param state: Current game state.
      :type state: MancalaState

      :returns: Updated game state after the move.
      :rtype: Command


      .. autolink-examples:: make_player2_move
         :collapse:


   .. py:method:: prepare_analysis_context(state: haive.games.mancala.state.MancalaState, player: str) -> dict[str, Any]

      Prepare context for position analysis.

      :param state: Current game state.
      :type state: MancalaState
      :param player: The player making the analysis ('player1' or 'player2').
      :type player: str

      :returns: Context dictionary for position analysis.
      :rtype: Dict[str, Any]


      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.mancala.state.MancalaState, player: str) -> dict[str, Any]

      Prepare context for move generation.

      :param state: Current game state.
      :type state: MancalaState
      :param player: The player making the move ('player1' or 'player2').
      :type player: str

      :returns: Context dictionary for move generation.
      :rtype: Dict[str, Any]


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: run_game(visualize: bool = True, debug: bool = False) -> haive.games.mancala.state.MancalaState

      Run a full Mancala game loop with optional visualization.

      :param visualize: Whether to visualize the game state.
      :type visualize: bool
      :param debug: Whether to run in debug mode.
      :type debug: bool

      :returns: Final game state after completion.
      :rtype: MancalaState


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the game workflow.

      Creates a dynamic graph with nodes for game initialization, move making, and
      analysis. Adds edges between nodes based on the current player's turn.



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state)

      Visualize the current game state.

      :param state: Either a MancalaState object or a dictionary with state data


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: engines


   .. py:attribute:: state_manager


.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

   Ensure input is converted to MancalaState.

   :param state_input: State input as dict, MancalaState, or Command

   :returns: MancalaState instance


   .. autolink-examples:: ensure_game_state
      :collapse:

.. py:data:: logger

