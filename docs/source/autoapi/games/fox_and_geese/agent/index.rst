games.fox_and_geese.agent
=========================

.. py:module:: games.fox_and_geese.agent

Fox and Geese game agent with fixed state handling and UI integration.

This module defines the Fox and Geese game agent, which uses language models to generate
moves and analyze positions in the game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Fox and Geese game agent with fixed state handling and UI integration.

   This module defines the Fox and Geese game agent, which uses language models to generate
   moves and analyze positions in the game.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.fox_and_geese.agent.UI_AVAILABLE
      games.fox_and_geese.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.fox_and_geese.agent.FoxAndGeeseAgent

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.fox_and_geese.agent.ensure_game_state

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FoxAndGeeseAgent(config: haive.games.fox_and_geese.config.FoxAndGeeseConfig = FoxAndGeeseConfig())

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.fox_and_geese.config.FoxAndGeeseConfig`\ ]


            Agent for playing Fox and Geese.

            This class implements the Fox and Geese game agent, which uses language models to
            generate moves and analyze positions in the game.


            Initialize the Fox and Geese agent.

            :param config: The configuration for the Fox and Geese game.
            :type config: FoxAndGeeseConfig


            .. py:method:: _extract_analysis_data(response: Any, perspective: str) -> str

               Extract analysis data from LLM response.

               :param response: Response from the LLM
               :param perspective: The perspective of the analysis ('fox' or 'geese')

               :returns: String representation of the analysis



            .. py:method:: _get_legal_move_fallback(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState, piece_type: str) -> haive.games.fox_and_geese.models.FoxAndGeeseMove

               Get a legal move as a fallback when LLM fails.

               :param game_state: Current game state
               :param piece_type: Type of piece ('fox' or 'goose')

               :returns: A legal move
               :rtype: FoxAndGeeseMove



            .. py:method:: analyze_fox_position(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> langgraph.types.Command

               Analyze the current position from the Fox's perspective.

               :param state: Current game state

               :returns: LangGraph command with fox analysis updates
               :rtype: Command



            .. py:method:: analyze_geese_position(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> langgraph.types.Command

               Analyze the current position from the Geese's perspective.

               :param state: Current game state

               :returns: LangGraph command with geese analysis updates
               :rtype: Command



            .. py:method:: analyze_player1(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> langgraph.types.Command

               Analyze position for player 1 (fox).

               :param state: Current game state

               :returns: State updates with analysis
               :rtype: Dict[str, Any]



            .. py:method:: analyze_player2(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> langgraph.types.Command

               Analyze position for player 2 (geese).

               :param state: Current game state

               :returns: State updates with analysis
               :rtype: Dict[str, Any]



            .. py:method:: extract_move(response: Any, piece_type: str = 'fox') -> haive.games.fox_and_geese.models.FoxAndGeeseMove

               Extract move from engine response.

               :param response: Response from the engine
               :param piece_type: Type of piece making the move ('fox' or 'goose')

               :returns: Parsed move object
               :rtype: FoxAndGeeseMove



            .. py:method:: initialize_game(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> dict[str, Any]

               Initialize a new Fox and Geese game.

               :param state: Input state (ignored for initialization)

               :returns: State updates for the new game
               :rtype: Dict[str, Any]



            .. py:method:: make_fox_move(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> haive.games.fox_and_geese.state.FoxAndGeeseState

               Make a move for the fox.

               :param state: Current game state

               :returns: Updated game state after the move
               :rtype: FoxAndGeeseState



            .. py:method:: make_geese_move(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> haive.games.fox_and_geese.state.FoxAndGeeseState

               Make a move for the geese.

               :param state: Current game state

               :returns: Updated game state after the move
               :rtype: FoxAndGeeseState



            .. py:method:: make_player1_move(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> langgraph.types.Command

               Make a move for player 1 (fox).

               :param state: Current game state

               :returns: State updates after the move
               :rtype: Dict[str, Any]



            .. py:method:: make_player2_move(state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> langgraph.types.Command

               Make a move for player 2 (geese).

               :param state: Current game state

               :returns: State updates after the move
               :rtype: Dict[str, Any]



            .. py:method:: prepare_analysis_context(state: haive.games.fox_and_geese.state.FoxAndGeeseState, player: str) -> dict[str, Any]

               Prepare context for position analysis.

               :param state: Current game state
               :param player: The player for whom to prepare the analysis context

               :returns: The context dictionary for position analysis
               :rtype: Dict[str, Any]



            .. py:method:: prepare_move_context(state: haive.games.fox_and_geese.state.FoxAndGeeseState, player: str) -> dict[str, Any]

               Prepare context for move generation.

               :param state: Current game state
               :param player: The player making the move ('fox' or 'geese')

               :returns: Context dictionary for move generation
               :rtype: Dict[str, Any]



            .. py:method:: run(input_data: dict[str, Any] | haive.games.fox_and_geese.state.FoxAndGeeseState | None = None, **kwargs) -> dict[str, Any]

               Run the Fox and Geese game.

               :param input_data: Optional input data for the game (state dict or FoxAndGeeseState)
               :param \*\*kwargs: Additional arguments (e.g., thread_id)

               :returns: The final game state as a dictionary



            .. py:method:: run_game(visualize: bool = True) -> haive.games.fox_and_geese.state.FoxAndGeeseState

               Run the full Fox and Geese game, optionally visualizing each step.

               :param visualize: Whether to visualize the game state

               :returns: Final game state after completion
               :rtype: FoxAndGeeseState



            .. py:method:: run_game_with_ui(delay: float = 2.0) -> haive.games.fox_and_geese.state.FoxAndGeeseState

               Run the full Fox and Geese game with UI visualization.

               :param delay: Delay between moves in seconds

               :returns: Final game state after completion
               :rtype: FoxAndGeeseState



            .. py:method:: setup_workflow() -> None

               Set up the game workflow.

               Creates a dynamic graph with nodes for game initialization, move making, and
               analysis. Uses the base GameAgent workflow pattern.




            .. py:method:: should_continue_game(state: dict | haive.games.fox_and_geese.state.FoxAndGeeseState) -> bool

               Determine if the game should continue.

               :param state: Current game state (dict or FoxAndGeeseState)

               :returns: True if the game should continue, False otherwise
               :rtype: bool



            .. py:attribute:: console


            .. py:attribute:: engines
               :value: None



            .. py:attribute:: game_over
               :value: False



            .. py:attribute:: state_manager


            .. py:attribute:: ui



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.fox_and_geese.state.FoxAndGeeseState) -> haive.games.fox_and_geese.state.FoxAndGeeseState

            Ensure input is converted to FoxAndGeeseState.

            :param state_input: State input as dict or FoxAndGeeseState

            :returns: FoxAndGeeseState instance



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: UI_AVAILABLE
            :value: True



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.fox_and_geese.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

