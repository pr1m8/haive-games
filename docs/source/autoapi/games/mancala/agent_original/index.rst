games.mancala.agent_original
============================

.. py:module:: games.mancala.agent_original

Mancala game agent.

This module defines the Mancala game agent, which uses language models to generate moves
and analyze positions in the game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Mancala game agent.

   This module defines the Mancala game agent, which uses language models to generate moves
   and analyze positions in the game.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mancala.agent_original.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mancala.agent_original.MancalaAgent

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.mancala.agent_original.ensure_game_state

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MancalaAgent(config: haive.games.mancala.config.MancalaConfig = MancalaConfig())

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.mancala.config.MancalaConfig`\ ]


            Agent for playing Mancala.

            This class implements the Mancala game agent, which uses language models to generate
            moves and analyze positions in the game.


            Initialize the Mancala agent.

            :param config: The configuration for the Mancala game.
            :type config: MancalaConfig


            .. py:method:: analyze_player1(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

               Analyze position for player1.

               :param state: Current game state.
               :type state: MancalaState

               :returns: Updated game state after the analysis.
               :rtype: Command



            .. py:method:: analyze_player2(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

               Analyze position for player2.

               :param state: Current game state.
               :type state: MancalaState

               :returns: Updated game state after the analysis.
               :rtype: Command



            .. py:method:: analyze_position(state: haive.games.mancala.state.MancalaState, player: str) -> langgraph.types.Command

               Analyze the current position for the specified player.

               :param state: Current game state.
               :type state: MancalaState
               :param player: The player making the analysis ('player1' or 'player2').
               :type player: str

               :returns: Updated game state after the analysis.
               :rtype: Command



            .. py:method:: extract_analysis(response: Any) -> Any

               Extract analysis from engine response.

               :param response: Response from the engine.
               :type response: Any

               :returns: Parsed analysis object.
               :rtype: Any



            .. py:method:: extract_move(response: Any) -> haive.games.mancala.models.MancalaMove

               Extract move from engine response.

               :param response: Response from the engine.
               :type response: Any

               :returns: Parsed move object.
               :rtype: MancalaMove



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new Mancala game with configured stones per pit.

               :param state: Initial state dictionary (unused here but required for interface).
               :type state: Dict[str, Any]

               :returns: Initialization command containing the new game state fields.
               :rtype: Command



            .. py:method:: make_move(state: haive.games.mancala.state.MancalaState, player: str) -> langgraph.types.Command

               Make a move for the specified player.

               :param state: Current game state.
               :type state: MancalaState
               :param player: The player making the move ('player1' or 'player2').
               :type player: str

               :returns: Updated game state after the move.
               :rtype: Command



            .. py:method:: make_player1_move(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

               Make a move for player1.

               :param state: Current game state.
               :type state: MancalaState

               :returns: Updated game state after the move.
               :rtype: Command



            .. py:method:: make_player2_move(state: haive.games.mancala.state.MancalaState) -> langgraph.types.Command

               Make a move for player2.

               :param state: Current game state.
               :type state: MancalaState

               :returns: Updated game state after the move.
               :rtype: Command



            .. py:method:: prepare_analysis_context(state: haive.games.mancala.state.MancalaState, player: str) -> dict[str, Any]

               Prepare context for position analysis.

               :param state: Current game state.
               :type state: MancalaState
               :param player: The player making the analysis ('player1' or 'player2').
               :type player: str

               :returns: Context dictionary for position analysis.
               :rtype: Dict[str, Any]



            .. py:method:: prepare_move_context(state: haive.games.mancala.state.MancalaState, player: str) -> dict[str, Any]

               Prepare context for move generation.

               :param state: Current game state.
               :type state: MancalaState
               :param player: The player making the move ('player1' or 'player2').
               :type player: str

               :returns: Context dictionary for move generation.
               :rtype: Dict[str, Any]



            .. py:method:: run_game(visualize: bool = True, debug: bool = False) -> haive.games.mancala.state.MancalaState

               Run a full Mancala game loop with optional visualization.

               :param visualize: Whether to visualize the game state.
               :type visualize: bool
               :param debug: Whether to run in debug mode.
               :type debug: bool

               :returns: Final game state after completion.
               :rtype: MancalaState



            .. py:method:: setup_workflow() -> None

               Set up the game workflow.

               Creates a dynamic graph with nodes for game initialization, move making, and
               analysis. Adds edges between nodes based on the current player's turn.




            .. py:method:: visualize_state(state)

               Visualize the current game state.

               :param state: Either a MancalaState object or a dictionary with state data



            .. py:attribute:: engines


            .. py:attribute:: state_manager



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

            Ensure input is converted to MancalaState.

            :param state_input: State input as dict, MancalaState, or Command

            :returns: MancalaState instance



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mancala.agent_original import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

