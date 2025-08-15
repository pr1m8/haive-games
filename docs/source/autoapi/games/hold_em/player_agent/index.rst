games.hold_em.player_agent
==========================

.. py:module:: games.hold_em.player_agent

.. autoapi-nested-parse::

   Texas Hold'em Player Agent module for LLM-powered poker players.

   This module implements the player decision-making system for Texas Hold'em poker,
   providing a complete workflow for analyzing the game state and making strategic decisions.
   The player agent is implemented as a subgraph in the main game graph, with each player
   having their own autonomous decision-making process.

   Key components:
       - PlayerSubgraphState: State model for player decision-making
       - HoldemPlayerAgentConfig: Configuration for player agents
       - HoldemPlayerAgent: The player agent implementation with decision workflow
       - Decision pipeline: Situation analysis -> Hand analysis -> Opponent analysis -> Decision

   The agent uses a multi-step analysis process, with each step handled by a specialized
   LLM engine to generate the final poker decision. This design allows for detailed reasoning
   about poker strategy based on the current game state.

   .. rubric:: Example

   >>> from haive.games.hold_em.player_agent import HoldemPlayerAgent, HoldemPlayerAgentConfig
   >>> from haive.games.hold_em.engines import build_player_engines
   >>>
   >>> # Create a player configuration
   >>> player_engines = build_player_engines("Alice", "balanced")
   >>> player_config = HoldemPlayerAgentConfig(
   ...     name="player_alice",
   ...     player_name="Alice",
   ...     player_style="balanced",
   ...     engines=player_engines
   ... )
   >>>
   >>> # Create the player agent
   >>> player_agent = HoldemPlayerAgent(player_config)


   .. autolink-examples:: games.hold_em.player_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.hold_em.player_agent.logger


Classes
-------

.. autoapisummary::

   games.hold_em.player_agent.HoldemPlayerAgent
   games.hold_em.player_agent.HoldemPlayerAgentConfig
   games.hold_em.player_agent.PlayerSubgraphState


Module Contents
---------------

.. py:class:: HoldemPlayerAgent(config: HoldemPlayerAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`HoldemPlayerAgentConfig`\ ]


   Player agent for Texas Hold'em poker games.

   This agent implements the complete decision-making pipeline for a poker player,
   analyzing the game state and making betting decisions based on a multi-step process:

   1. Situation analysis - Evaluate position, pot odds, betting action, etc.
   2. Hand analysis - Assess hole cards and community cards strength
   3. Opponent analysis - Model opponents' tendencies and likely holdings
   4. Final decision - Synthesize analyses into a concrete betting action

   Each step is handled by a specialized LLM engine configured with poker-specific prompts.
   The agent supports different playing styles (tight, loose, aggressive, etc.) and can
   adapt its risk tolerance and strategy based on configuration.

   This agent does not include fallback mechanisms, allowing for clear error exposure
   and debugging of decision-making issues.



   .. autolink-examples:: HoldemPlayerAgent
      :collapse:

   .. py:method:: _calculate_pot_odds(game_state: haive.games.hold_em.state.HoldemState, player: haive.games.hold_em.state.PlayerState) -> float

      Calculate pot odds for the player's current decision.

      Pot odds represent the ratio between the current call amount and the
      potential pot after calling. This is a key factor in making mathematically
      sound poker decisions, especially for drawing hands.

      :param game_state: Current game state
      :type game_state: HoldemState
      :param player: Player to calculate odds for
      :type player: PlayerState

      :returns:

                Pot odds as a ratio (0.0 to 1.0), where lower values are better.
                      Returns 0.0 if no call is required.
      :rtype: float


      .. autolink-examples:: _calculate_pot_odds
         :collapse:


   .. py:method:: _get_available_actions(game_state: haive.games.hold_em.state.HoldemState, player: haive.games.hold_em.state.PlayerState) -> list[str]

      Get list of available legal actions for the player in the current game state.

      This method determines which poker actions are legally available to the player
      based on the current game state, betting situation, and player's chip stack.
      It prevents the agent from attempting illegal actions like checking when there's
      a bet to call.

      :param game_state: Current game state
      :type game_state: HoldemState
      :param player: Player to determine actions for
      :type player: PlayerState

      :returns:

                List of available action strings that may include:
                    - "fold": Always available unless already all-in
                    - "check": Available if no current bet to call
                    - "call": Available if there's a bet and player has chips
                    - "bet": Available if no current bet and player has chips
                    - "raise": Available if there's a bet and player has enough chips
                    - "all_in": Always available if player has chips
      :rtype: List[str]


      .. autolink-examples:: _get_available_actions
         :collapse:


   .. py:method:: _normalize_decision(decision: Any) -> dict[str, Any]

      Normalize different decision model formats to a consistent dictionary.
      structure.

      This method handles the conversion of various structured output formats into
      a standardized decision dictionary that can be used by the game agent. It's
      necessary because different LLM engines may return different structured output models.

      Handles:
      - BettingDecision model (primary_action, bet_size, etc.)
      - PlayerDecisionModel (action, amount, etc.)
      - Raw dictionaries with various field names

      :param decision: The decision object from the LLM engine
      :type decision: Any

      :returns:

                Normalized decision dictionary with standardized fields:
                    - action: The poker action (fold, check, call, bet, raise, all_in)
                    - amount: The bet/raise amount (if applicable)
                    - reasoning: Explanation for the decision
                    - confidence: Confidence level (0-1)
                    - Additional fields may be included depending on the source format
      :rtype: Dict[str, Any]

      :raises RuntimeError: If the decision cannot be converted to a dictionary


      .. autolink-examples:: _normalize_decision
         :collapse:


   .. py:method:: _prepare_opponent_context(game_state, opponents) -> dict[str, str]

      Prepare context dictionary for opponent analysis with error handling.


      .. autolink-examples:: _prepare_opponent_context
         :collapse:


   .. py:method:: _validate_decision(decision: dict[str, Any], game_state: haive.games.hold_em.state.HoldemState, player: haive.games.hold_em.state.PlayerState) -> dict[str, Any]

      Validate and correct a decision to ensure it's legal in the current game.
      state.

      This method ensures that the LLM-generated decision is valid and legal according
      to poker rules. It checks that the chosen action is available, and that bet
      amounts are within allowed ranges. If issues are found, it corrects them to
      maintain game integrity.

      Corrections include:
      - Ensuring the action is in the available actions list
      - Adjusting bet/raise amounts to meet minimum requirements
      - Adjusting call amounts to match the current bet
      - Converting actions to all-in when the amount exceeds player chips

      :param decision: The normalized decision dictionary
      :type decision: Dict[str, Any]
      :param game_state: Current game state
      :type game_state: HoldemState
      :param player: Player making the decision
      :type player: PlayerState

      :returns: Validated and potentially corrected decision dictionary
      :rtype: Dict[str, Any]

      :raises RuntimeError: If the action is invalid and cannot be corrected


      .. autolink-examples:: _validate_decision
         :collapse:


   .. py:method:: _validate_required_engines() -> None

      Validate that all required LLM engines are present and properly configured.

      This method checks that all the necessary engines for the player's decision
      pipeline exist and have the required attributes (structured_output_model and
      prompt_template). It raises ValueError with detailed messages if any engines
      are missing or misconfigured.

      Required engines:
          - situation_analyzer: Analyzes game situation (position, pot, betting)
          - hand_analyzer: Evaluates hand strength and potential
          - opponent_analyzer: Models opponent behavior and tendencies
          - decision_maker: Makes final betting decisions

      :raises ValueError: If any required engines are missing or misconfigured


      .. autolink-examples:: _validate_required_engines
         :collapse:


   .. py:method:: analyze_hand(state: PlayerSubgraphState) -> langgraph.types.Command[Literal['analyze_opponents']]

      Analyze the player's hand strength and potential.

      This node evaluates the strength of the player's hole cards in combination
      with the community cards, calculating hand rankings, draw potential, and
      relative strength against likely opponent ranges.

      The analysis is performed by the 'hand_analyzer' LLM engine, which considers:
      - Current made hand (pair, two pair, etc.)
      - Drawing possibilities (flush draws, straight draws)
      - Pot odds vs. hand equity
      - Hand strength at current game phase

      :param state: The current state containing game information,
                    player identity, and situation analysis.
      :type state: PlayerSubgraphState

      :returns: State update with hand analysis results
      :rtype: Command

      :raises RuntimeError: If player not found or analysis fails


      .. autolink-examples:: analyze_hand
         :collapse:


   .. py:method:: analyze_opponents(state: PlayerSubgraphState) -> langgraph.types.Command[Literal['make_decision']]

      Analyze opponent behavior, tendencies, and likely holdings.

      This node models opponents' play styles, betting patterns, and probable
      hand ranges based on their actions in the current hand and previous history.
      It helps inform strategic decisions by understanding opponent tendencies.

      The analysis is performed by the 'opponent_analyzer' LLM engine, which considers:
      - Betting patterns and sizing tells
      - Position-based tendencies
      - Aggression levels
      - Likely hand ranges based on actions
      - Exploitable tendencies

      :param state: The current state containing game information,
                    player identity, situation analysis, and hand analysis.
      :type state: PlayerSubgraphState

      :returns: State update with opponent analysis results
      :rtype: Command

      :raises RuntimeError: If analysis fails


      .. autolink-examples:: analyze_opponents
         :collapse:


   .. py:method:: analyze_situation(state: PlayerSubgraphState) -> langgraph.types.Command[Literal['analyze_hand']]

      Analyze the current game situation and table dynamics.

      This node in the decision graph evaluates the overall poker situation including
      position, pot size, betting action, stack sizes, and game phase. It forms the
      foundation for subsequent decision-making steps.

      The analysis is performed by the 'situation_analyzer' LLM engine and the results
      are added to the state for use in later decision steps.

      :param state: The current state containing game information
                    and player identity.
      :type state: PlayerSubgraphState

      :returns: State update with situation analysis results
      :rtype: Command

      :raises RuntimeError: If player not found in game state or analysis fails


      .. autolink-examples:: analyze_situation
         :collapse:


   .. py:method:: make_decision(state: PlayerSubgraphState) -> langgraph.types.Command[Literal[langgraph.graph.END]]

      Make the final betting decision based on all previous analyses.

      This is the final node in the decision graph that synthesizes all previous
      analyses (situation, hand, opponents) into a concrete poker action: fold,
      check, call, bet, raise, or all-in. It handles validation and correction
      of decisions to ensure they're legal within the game rules.

      The decision is made by the 'decision_maker' LLM engine, which produces a
      structured betting decision with:
      - The primary action to take
      - Bet/raise amount if applicable
      - Detailed reasoning for the decision
      - Confidence level

      This method handles both PlayerDecisionModel and BettingDecision model formats
      by normalizing them to a consistent structure.

      :param state: The complete state with all analysis results
      :type state: PlayerSubgraphState

      :returns: Final state update with the betting decision
      :rtype: Command

      :raises RuntimeError: If player lookup fails or decision making fails


      .. autolink-examples:: make_decision
         :collapse:


   .. py:method:: save_debug_logs(timestamp: str | None = None)

      Save debug logs for this player agent to JSON files.

      This method saves three types of debug logs to help with debugging and
      analyzing player agent behavior:
      - Analysis log: Records details of situation, hand, and opponent analyses
      - Decision log: Records betting decisions and their reasoning
      - Error log: Records any errors encountered during decision-making

      :param timestamp: Timestamp string for log filenames.
                        If None, current datetime will be used.
      :type timestamp: str, optional

      :returns:

                Files are saved to the current directory with names like:
                    player_analysis_{player_name}_{timestamp}.json
                    player_decisions_{player_name}_{timestamp}.json
                    player_errors_{player_name}_{timestamp}.json
      :rtype: None


      .. autolink-examples:: save_debug_logs
         :collapse:


   .. py:method:: setup_workflow() -> None

      Setup the player decision workflow graph.

      This method configures the LangGraph workflow for player decision-making,
      establishing the sequence of analysis steps and their dependencies.

      The workflow follows a linear sequence:
      1. START → analyze_situation: Evaluate the current game situation
      2. analyze_situation → analyze_hand: Assess the player's hand strength
      3. analyze_hand → analyze_opponents: Analyze opponent tendencies
      4. analyze_opponents → make_decision: Make the final betting decision
      5. make_decision → END: Return the final decision

      Each step must complete successfully in sequence for the decision to be made.



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: analysis_log
      :value: []



   .. py:attribute:: decision_log
      :value: []



   .. py:attribute:: engines


   .. py:attribute:: error_log
      :value: []



.. py:class:: HoldemPlayerAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for Hold'em player agent.

   This configuration class defines the parameters for a Texas Hold'em player agent,
   including player identity, playing style, risk tolerance, and the LLM engines used
   for different aspects of decision-making.

   The configuration is used to initialize a player agent with specific characteristics
   and behavior patterns. Different combinations of style and risk_tolerance create
   varied player behaviors from conservative to aggressive play.



   .. autolink-examples:: HoldemPlayerAgentConfig
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: player_name
      :type:  str
      :value: None



   .. py:attribute:: player_style
      :type:  str
      :value: None



   .. py:attribute:: risk_tolerance
      :type:  float
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



.. py:class:: PlayerSubgraphState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State model for the player decision subgraph.

   This model represents the complete state for a player's decision- making process,
   including the inputs from the main game, intermediate analysis results, and the
   final decision output. It tracks the entire decision pipeline from situation
   analysis through hand analysis and opponent modeling to the final betting decision.

   The state is passed between nodes in the player's decision graph and accumulates
   information at each step, ultimately producing a final poker action decision.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerSubgraphState
      :collapse:

   .. py:attribute:: debug_info
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: decision
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: game_state
      :type:  haive.games.hold_em.state.HoldemState
      :value: None



   .. py:attribute:: hand_analysis
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: opponent_analysis
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: player_id
      :type:  str
      :value: None



   .. py:attribute:: situation_analysis
      :type:  dict[str, Any] | None
      :value: None



.. py:data:: logger

