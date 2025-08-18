games.mastermind.agent
======================

.. py:module:: games.mastermind.agent

Module documentation for games.mastermind.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">2 attributes</span>   </div>


      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.mastermind.agent.UI_AVAILABLE
      games.mastermind.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mastermind.agent.MastermindAgent

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.mastermind.agent.ensure_game_state

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MastermindAgent(config: haive.games.mastermind.config.MastermindConfig = MastermindConfig())

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.mastermind.config.MastermindConfig`\ ]


            Agent for playing Mastermind.

            This class implements the Mastermind game agent, which uses language models to
            generate guesses and analyze positions in the game.


            Initialize the Mastermind agent.

            :param config: The configuration for the Mastermind game.
            :type config: MastermindConfig


            .. py:method:: analyze_player1(state: haive.games.mastermind.state.MastermindState) -> langgraph.types.Command

               Run analysis for player1 if they are the codebreaker.

               :param state: Current game state.
               :type state: MastermindState

               :returns: Updated state with appended analysis or passthrough.
               :rtype: Command



            .. py:method:: analyze_player2(state: haive.games.mastermind.state.MastermindState) -> langgraph.types.Command

               Run analysis for player2 if they are the codebreaker.

               :param state: Current game state.
               :type state: MastermindState

               :returns: Updated state with appended analysis or passthrough.
               :rtype: Command



            .. py:method:: analyze_position(state: haive.games.mastermind.state.MastermindState, player: str) -> langgraph.types.Command

               Invoke the analysis engine to evaluate the current position.

               :param state: Current game state.
               :type state: MastermindState
               :param player: 'player1' or 'player2'.
               :type player: str

               :returns: Updated state including the newly generated analysis.
               :rtype: Command



            .. py:method:: extract_guess(response: Any) -> haive.games.mastermind.models.MastermindGuess

               Extract a structured MastermindGuess object from the engine response.

               :param response: Response from the guess engine.
               :type response: Any

               :returns: Parsed guess object.
               :rtype: MastermindGuess



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize the Mastermind game.

               If a secret code is not already configured, this method uses the codemaker engine
               to generate one. It then constructs the initial game state with the given parameters.

               :param state: Initial state dictionary (unused here but required for interface).
               :type state: Dict[str, Any]

               :returns: Initialization command containing the new game state.
               :rtype: Command



            .. py:method:: make_guess(state: haive.games.mastermind.state.MastermindState, player: str) -> langgraph.types.Command

               Invoke the appropriate guess engine and apply the resulting move.

               Skips if it is not the player's turn or the game is no longer ongoing.

               :param state: Current game state.
               :type state: MastermindState
               :param player: 'player1' or 'player2'.
               :type player: str

               :returns: Updated game state with the new guess applied.
               :rtype: Command



            .. py:method:: make_player1_guess(state: haive.games.mastermind.state.MastermindState) -> langgraph.types.Command

               Handle player1's guess if they are the codebreaker.

               Returns immediately if player1 is the codemaker.

               :param state: Current game state.
               :type state: MastermindState

               :returns: Updated game state after the guess or passthrough if not allowed.
               :rtype: Command



            .. py:method:: make_player2_guess(state: haive.games.mastermind.state.MastermindState) -> langgraph.types.Command

               Handle player2's guess if they are the codebreaker.

               Returns immediately if player2 is the codemaker.

               :param state: Current game state.
               :type state: MastermindState

               :returns: Updated game state after the guess or passthrough if not allowed.
               :rtype: Command



            .. py:method:: prepare_analysis_context(state: haive.games.mastermind.state.MastermindState, player: str) -> dict[str, Any]

               Build input context for position analysis engine.

               Includes history of guesses with feedback and turn metadata.

               :param state: Current game state.
               :type state: MastermindState
               :param player: The analyzing player ('player1' or 'player2').
               :type player: str

               :returns: Context dictionary for analysis.
               :rtype: Dict[str, Any]



            .. py:method:: prepare_guess_context(state: haive.games.mastermind.state.MastermindState, player: str) -> dict[str, Any]

               Build input context for the guess engine.

               Includes the current board string, turn info, past guesses with feedback,
               and any previous analysis by the current codebreaker.

               :param state: Current game state.
               :type state: MastermindState
               :param player: The guessing player ('player1' or 'player2').
               :type player: str

               :returns: Context dictionary for guess generation.
               :rtype: Dict[str, Any]



            .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

               Run the full Mastermind game, optionally visualizing each step.

               :param visualize: Whether to visualize the game state.
               :type visualize: bool

               :returns: Final game state after completion.
               :rtype: Dict[str, Any]



            .. py:method:: run_game_with_ui(delay: float = 1.0) -> dict[str, Any]

               Run the Mastermind game with Rich UI visualization.

               :param delay: Delay between game state updates in seconds.

               :returns: Final game state after completion.
               :rtype: Dict[str, Any]



            .. py:method:: setup_workflow() -> None

               Set up the game workflow.

               Creates a dynamic graph with nodes for game initialization, guess making, and
               analysis. Adds edges between nodes based on the codemaker's role.




            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Print a visual summary of the current game state.

               Shows the board, guesses, codemaker, game status, and most recent analysis.

               :param state: The state dictionary to render.
               :type state: Dict[str, Any]



            .. py:attribute:: console


            .. py:attribute:: state_manager


            .. py:attribute:: ui



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mastermind.state.MastermindState | langgraph.types.Command) -> haive.games.mastermind.state.MastermindState

            Ensure input is converted to MastermindState.

            :param state_input: State input as dict, MastermindState, or Command

            :returns: MastermindState instance



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

      from games.mastermind.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

