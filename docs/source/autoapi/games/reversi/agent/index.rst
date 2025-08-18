games.reversi.agent
===================

.. py:module:: games.reversi.agent

Module documentation for games.reversi.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.reversi.agent.ReversiAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ReversiAgent(config: haive.games.reversi.config.ReversiConfig = ReversiConfig())

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.reversi.config.ReversiConfig`\ ]


            Agent for playing Reversi/Othello.

            Initialize the Reversi agent with game configuration and state manager.

            :param config: Configuration object defining player settings,
                           engines, first player, visualization preference, and analysis options.
            :type config: ReversiConfig


            .. py:method:: analyze_B(state: haive.games.reversi.state.ReversiState) -> langgraph.types.Command

               Analyze position for player B (Black).

               :param state: The current game state.
               :type state: ReversiState

               :returns: Command containing the updated ReversiState.
               :rtype: Command



            .. py:method:: analyze_W(state: haive.games.reversi.state.ReversiState) -> langgraph.types.Command

               Analyze position for player W (White).

               :param state: The current game state.
               :type state: ReversiState

               :returns: Command containing the updated ReversiState.
               :rtype: Command



            .. py:method:: extract_move(response: Any) -> haive.games.reversi.models.ReversiMove

               Extract a ReversiMove object from an engine response.

               :param response: Output returned from the LLM engine. Assumed to already be
                                parsed into a ReversiMove object via structured output.
               :type response: Any

               :returns: The move selected by the engine.
               :rtype: ReversiMove



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new Reversi game by constructing the initial game state.

               :param state: Placeholder for incoming LangGraph state (not used directly).
               :type state: Dict[str, Any]

               :returns: Command containing the serialized initial ReversiState.
               :rtype: Command



            .. py:method:: make_B_move(state: haive.games.reversi.state.ReversiState) -> langgraph.types.Command

               Make a move for player B (Black).

               :param state: The current game state.
               :type state: ReversiState

               :returns: Command containing the updated ReversiState.
               :rtype: Command



            .. py:method:: make_W_move(state: haive.games.reversi.state.ReversiState) -> langgraph.types.Command

               Make a move for player W (White).

               :param state: The current game state.
               :type state: ReversiState

               :returns: Command containing the updated ReversiState.
               :rtype: Command



            .. py:method:: prepare_analysis_context(state: haive.games.reversi.state.ReversiState, symbol: str) -> dict[str, Any]

               Prepare the prompt context for board analysis by the strategy engine.

               :param state: The current game state.
               :type state: ReversiState
               :param symbol: Player symbol ('B' or 'W') for whom to analyze the board.
               :type symbol: str

               :returns:

                         A dictionary of analysis context including:
                             - board string
                             - player/opponent symbols
                             - color labels
                             - legal moves
                             - current disc counts
               :rtype: Dict[str, Any]



            .. py:method:: prepare_move_context(state: haive.games.reversi.state.ReversiState) -> dict[str, Any]

               Prepare the prompt context used by the move generation engine.

               :param state: The current game state.
               :type state: ReversiState

               :returns:

                         A dictionary containing the board string, legal move list,
                                         current player turn, and the player's last analysis (if any).
               :rtype: Dict[str, Any]



            .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

               Run a complete Reversi game with visualization.

               :param visualize: Whether to visualize each game state

               :returns: Final game state



            .. py:method:: setup_workflow() -> None

               Set up the game workflow.

               :returns: None



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state.

               :param state: The current game state.
               :type state: Dict[str, Any]

               :returns: None



            .. py:attribute:: state_manager





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.reversi.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

