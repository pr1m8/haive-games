games.nim.agent
===============

.. py:module:: games.nim.agent

Agent for playing Nim.

This module defines the Nim agent, which uses language models to generate moves and
analyze positions in the game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Agent for playing Nim.

   This module defines the Nim agent, which uses language models to generate moves and
   analyze positions in the game.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.nim.agent.RICH_AVAILABLE
      games.nim.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.nim.agent.NimAgent

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.nim.agent.ensure_game_state

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimAgent(config: haive.games.nim.config.NimConfig = NimConfig())

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.nim.config.NimConfig`\ ]


            Agent for playing Nim.

            Initialize the Nim agent.

            :param config: The configuration for the game.
            :type config: NimConfig


            .. py:method:: analyze_player1(state: haive.games.nim.state.NimState) -> langgraph.types.Command

               Analyze position for player1.

               :param state: The current game state.
               :type state: NimState

               :returns: The command to analyze the position.
               :rtype: Command



            .. py:method:: analyze_player2(state: haive.games.nim.state.NimState) -> langgraph.types.Command

               Analyze position for player2.

               :param state: The current game state.
               :type state: NimState

               :returns: The command to analyze the position.
               :rtype: Command



            .. py:method:: analyze_position(state: haive.games.nim.state.NimState | dict[str, Any] | langgraph.types.Command, player: str) -> langgraph.types.Command

               Analyze the current position for the specified player.

               :param state: The current game state.
               :param player: The player to analyze the position for.

               :returns: The command to analyze the position.
               :rtype: Command



            .. py:method:: extract_move(response: Any) -> Any

               Extract move from engine response.

               :param response: The response from the engine.
               :type response: Any

               :returns: The move from the engine.
               :rtype: Any



            .. py:method:: initialize_game(state: dict[str, Any] | haive.games.nim.state.NimState | langgraph.types.Command) -> langgraph.types.Command

               Initialize a new Nim game with configured pile sizes.

               :param state: The initial state of the game.

               :returns: The command to initialize the game.
               :rtype: Command



            .. py:method:: make_move(state: haive.games.nim.state.NimState | dict[str, Any] | langgraph.types.Command, player: str) -> langgraph.types.Command

               Make a move for the specified player.

               :param state: The current game state.
               :param player: The player to make the move for.

               :returns: The command to make the move.
               :rtype: Command



            .. py:method:: make_player1_move(state: haive.games.nim.state.NimState) -> langgraph.types.Command

               Make a move for player1.

               :param state: The current game state.
               :type state: NimState

               :returns: The command to make the move.
               :rtype: Command



            .. py:method:: make_player2_move(state: haive.games.nim.state.NimState) -> langgraph.types.Command

               Make a move for player2.

               :param state: The current game state.
               :type state: NimState

               :returns: The command to make the move.
               :rtype: Command



            .. py:method:: prepare_analysis_context(state: haive.games.nim.state.NimState, player: str) -> dict[str, Any]

               Prepare context for position analysis.

               :param state: The current game state.
               :type state: NimState
               :param player: The player to prepare the context for.
               :type player: str

               :returns: The context for the position analysis.
               :rtype: Dict[str, Any]



            .. py:method:: prepare_move_context(state: haive.games.nim.state.NimState, player: str) -> dict[str, Any]

               Prepare context for move generation.

               :param state: The current game state.
               :type state: NimState
               :param player: The player to prepare the context for.
               :type player: str

               :returns: The context for the move generation.
               :rtype: Dict[str, Any]



            .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

               Run a complete Nim game with optional visualization.

               :param visualize: Whether to visualize each game state.
               :type visualize: bool

               :returns: The final game state.
               :rtype: Dict[str, Any]



            .. py:method:: run_game_with_ui(show_analysis: bool = True) -> dict[str, Any]

               Run a complete Nim game with Rich UI.

               This method runs a Nim game with Rich UI visualization, showing
               the game state after each move. It optionally includes analysis.

               :param show_analysis: Whether to include analysis in the game.

               :returns: The final game state.
               :rtype: Dict[str, Any]



            .. py:method:: setup_workflow() -> None

               Set up the game workflow.

               :returns: None



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state.

               :param state: The current game state.
               :type state: Dict[str, Any]



            .. py:attribute:: state_manager


            .. py:attribute:: ui



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.nim.state.NimState | langgraph.types.Command) -> haive.games.nim.state.NimState

            Ensure input is converted to NimState.

            This helper function ensures that the input state is properly converted to a NimState
            object, handling various input types (dict, NimState, Command).

            :param state_input: The state to convert, which can be a dictionary, NimState, or Command.

            :returns: The converted state.
            :rtype: NimState



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: RICH_AVAILABLE
            :value: False



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

