games.dominoes.agent
====================

.. py:module:: games.dominoes.agent

Module documentation for games.dominoes.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">3 attributes</span>   </div>


      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.dominoes.agent.UI_AVAILABLE
      games.dominoes.agent.agent
      games.dominoes.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.dominoes.agent.DominoesAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesAgent(config: haive.games.dominoes.config.DominoesAgentConfig | None = None)

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.dominoes.config.DominoesAgentConfig`\ ]


            Agent for playing dominoes.

            Initialize the game agent.

            :param config: Configuration for the game agent.
                           Defaults to GameConfig().
            :type config: GameConfig, optional


            .. py:method:: _extract_analysis(response: Any) -> haive.games.dominoes.models.DominoesAnalysis

               Extract analysis from engine response.



            .. py:method:: analyze_player1(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

               Analyze position for player1.

               :param state: The current game state.
               :type state: DominoesState

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: analyze_player2(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

               Analyze position for player2.

               :param state: The current game state.
               :type state: DominoesState

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: analyze_position(state: haive.games.dominoes.state.DominoesState, player: str) -> langgraph.types.Command

               Analyze the current position for the specified player.

               :param state: The current game state.
               :type state: DominoesState
               :param player: The player to analyze the position for.
               :type player: str

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: check_game_status(state: haive.games.dominoes.state.DominoesState) -> str

               Check if the game is over.

               :param state: The current game state.
               :type state: DominoesState

               :returns: Next node to go to.
               :rtype: str



            .. py:method:: extract_move(response: Any) -> haive.games.dominoes.models.DominoMove | Literal['pass']

               Extract move from engine response.



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new Dominoes game.

               :param state: The initial state.
               :type state: Dict[str, Any]

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: make_move(state: haive.games.dominoes.state.DominoesState, player: str) -> langgraph.types.Command

               Make a move for the specified player.

               :param state: The current game state.
               :type state: DominoesState
               :param player: The player to make the move for.
               :type player: str

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: make_player1_move(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

               Make a move for player1.

               :param state: The current game state.
               :type state: DominoesState

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: make_player2_move(state: haive.games.dominoes.state.DominoesState) -> langgraph.types.Command

               Make a move for player2.

               :param state: The current game state.
               :type state: DominoesState

               :returns: Command with updated state.
               :rtype: Command



            .. py:method:: prepare_analysis_context(state: haive.games.dominoes.state.DominoesState, player: str) -> dict[str, Any]

               Prepare context for position analysis.



            .. py:method:: prepare_move_context(state: haive.games.dominoes.state.DominoesState, player: str) -> dict[str, Any]

               Prepare context for move generation.



            .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

               Run the full game, optionally visualizing each step.



            .. py:method:: run_game_with_ui(delay: float = 1.5) -> dict[str, Any]

               Run the full game with Rich UI visualization.

               :param delay: Delay between moves in seconds

               :returns: Final game state



            .. py:method:: setup_workflow() -> None

               Set up the game workflow.



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state.



            .. py:attribute:: console


            .. py:attribute:: state_manager


            .. py:attribute:: ui



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: UI_AVAILABLE
            :value: True



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: agent


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.dominoes.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

