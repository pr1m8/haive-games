games.risk.agent
================

.. py:module:: games.risk.agent

.. autoapi-nested-parse::

   Advanced Risk agent implementation for strategic world domination gameplay.

   This module provides a sophisticated RiskAgent class that uses AI-powered strategic
   reasoning to play the classic Risk board game. The agent analyzes territorial control,
   army positioning, continental bonuses, and diplomatic opportunities to make optimal
   decisions in complex multi-player scenarios.

   The agent supports different strategic approaches (aggressive expansion, defensive
   fortification, balanced gameplay) and maintains detailed analysis history for
   learning and adaptation. It integrates with the broader Haive framework for
   LLM-powered decision making and strategic evaluation.

   .. rubric:: Examples

   Creating a basic Risk agent::

       agent = RiskAgent(
           name="General_Patton",
           strategy="aggressive",
           risk_tolerance=0.8
       )

   Setting up an agent with game state::

       agent = RiskAgent(
           name="Strategic_AI",
           state=current_risk_state,
           strategy="balanced",
           risk_tolerance=0.6,
           diplomatic_stance="neutral"
       )

   Getting strategic analysis::

       analysis = agent.analyze_position()
       print(f"Territory control: {analysis.controlled_territories}")
       print(f"Recommended move: {analysis.recommended_move.move_type}")

   Making moves::

       move = agent.get_move()
       if move.move_type == MoveType.ATTACK:
           print(f"Attacking {move.to_territory} from {move.from_territory}")
       elif move.move_type == MoveType.PLACE_ARMIES:
           print(f"Placing {move.armies} armies in {move.to_territory}")

   .. note::

      The agent maintains detailed analysis history for learning and strategic
      adaptation. Full LLM integration enables sophisticated reasoning about
      territorial strategy, army management, and diplomatic considerations.


   .. autolink-examples:: games.risk.agent
      :collapse:


Classes
-------

.. autoapisummary::

   games.risk.agent.RiskAgent


Module Contents
---------------

.. py:class:: RiskAgent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Advanced AI agent for strategic Risk gameplay with sophisticated decision-making.

   This agent employs multi-layered strategic analysis to excel at the classic Risk
   board game, combining territorial evaluation, military logistics, continental
   strategy, and diplomatic considerations. It adapts its approach based on game
   state, opponent behavior, and strategic objectives.

   The agent supports various strategic personalities and maintains comprehensive
   analysis history for learning and adaptation. It integrates with LLM systems
   for complex reasoning about world domination strategy, resource allocation,
   and tactical decision-making.

   .. attribute:: name

      Unique identifier and display name for the agent.
      Used for game tracking and strategic identification.

      :type: str

   .. attribute:: state

      Current game state containing board position,
      army distributions, territorial control, and game phase information.

      :type: Optional[RiskState]

   .. attribute:: strategy

      Strategic approach determining decision-making priorities.
      Options: "aggressive" (expansion-focused), "defensive" (consolidation),
      "balanced" (opportunistic), "diplomatic" (alliance-building).

      :type: str

   .. attribute:: risk_tolerance

      Willingness to take risks in attacks and expansion.
      Range 0.0-1.0, where higher values favor bold moves over safe plays.

      :type: float

   .. attribute:: diplomatic_stance

      Approach to other players and alliance-building.
      Options: "aggressive" (hostile), "neutral" (independent), "cooperative".

      :type: str

   .. attribute:: analysis_history

      Complete history of strategic analyses.
      Used for learning, pattern recognition, and strategic adaptation.

      :type: List[RiskAnalysis]

   .. attribute:: preferred_continents

      Priority continents for expansion focus.
      Agent will prioritize gaining control of these continents for bonuses.

      :type: List[str]

   .. attribute:: minimum_armies_threshold

      Minimum armies to maintain in territories.
      Defensive parameter to avoid leaving territories vulnerable.

      :type: int

   .. rubric:: Examples

   Creating an aggressive expansion agent::

       agent = RiskAgent(
           name="Conqueror_Alpha",
           strategy="aggressive",
           risk_tolerance=0.9,
           diplomatic_stance="aggressive",
           preferred_continents=["Asia", "Europe"],
           minimum_armies_threshold=2
       )

   Creating a defensive consolidation agent::

       agent = RiskAgent(
           name="Fortress_Beta",
           strategy="defensive",
           risk_tolerance=0.3,
           diplomatic_stance="neutral",
           preferred_continents=["Australia", "South America"],
           minimum_armies_threshold=4
       )

   Setting up agent with game state::

       agent = RiskAgent(
           name="Strategic_Gamma",
           state=current_game_state,
           strategy="balanced"
       )

       # Agent immediately begins analyzing position
       analysis = agent.analyze_position()

   Managing strategic adaptation::

       # Agent learns from previous analyses
       for analysis in agent.analysis_history[-5:]:
           if analysis.position_evaluation == "losing":
               agent.strategy = "defensive"  # Adapt to defensive play
               agent.risk_tolerance = max(0.2, agent.risk_tolerance - 0.1)

   .. note::

      The agent maintains state independence, allowing multiple agents to operate
      on different game states simultaneously. Strategic parameters can be adjusted
      dynamically for adaptive gameplay and experimental strategies.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RiskAgent
      :collapse:

   .. py:method:: _generate_analysis_explanation(territory_count: int, total_armies: int, continent_bonuses: int, position_evaluation: str) -> str

      Generate detailed explanation of strategic analysis and reasoning.

      :param territory_count: Number of controlled territories.
      :type territory_count: int
      :param total_armies: Total armies under control.
      :type total_armies: int
      :param continent_bonuses: Number of controlled continents.
      :type continent_bonuses: int
      :param position_evaluation: Overall position assessment.
      :type position_evaluation: str

      :returns: Detailed strategic analysis explanation.
      :rtype: str


      .. autolink-examples:: _generate_analysis_explanation
         :collapse:


   .. py:method:: _generate_attack_move(controlled_territories: list[haive.games.risk.models.Territory]) -> haive.games.risk.models.RiskMove

      Generate aggressive attack move targeting expansion opportunities.

      :param controlled_territories: Agent's controlled territories.
      :type controlled_territories: List[Territory]

      :returns: Attack move targeting optimal expansion opportunity.
      :rtype: RiskMove


      .. autolink-examples:: _generate_attack_move
         :collapse:


   .. py:method:: _generate_balanced_move(controlled_territories: list[haive.games.risk.models.Territory], position_evaluation: str) -> haive.games.risk.models.RiskMove

      Generate balanced move considering both offensive and defensive needs.

      :param controlled_territories: Agent's controlled territories.
      :type controlled_territories: List[Territory]
      :param position_evaluation: Current position strength.
      :type position_evaluation: str

      :returns: Balanced move optimizing risk vs. reward.
      :rtype: RiskMove


      .. autolink-examples:: _generate_balanced_move
         :collapse:


   .. py:method:: _generate_defensive_move(controlled_territories: list[haive.games.risk.models.Territory]) -> haive.games.risk.models.RiskMove

      Generate defensive move focusing on consolidation and fortification.

      :param controlled_territories: Agent's controlled territories.
      :type controlled_territories: List[Territory]

      :returns: Defensive move prioritizing territorial security.
      :rtype: RiskMove


      .. autolink-examples:: _generate_defensive_move
         :collapse:


   .. py:method:: _generate_strategic_move(controlled_territories: list[haive.games.risk.models.Territory], position_evaluation: str) -> haive.games.risk.models.RiskMove

      Generate strategic move recommendation based on position analysis.

      :param controlled_territories: Territories under agent control.
      :type controlled_territories: List[Territory]
      :param position_evaluation: Current position strength assessment.
      :type position_evaluation: str

      :returns: Strategic move recommendation optimized for current situation.
      :rtype: RiskMove


      .. autolink-examples:: _generate_strategic_move
         :collapse:


   .. py:method:: _refine_move_with_strategy(base_move: haive.games.risk.models.RiskMove, analysis: haive.games.risk.models.RiskAnalysis) -> haive.games.risk.models.RiskMove

      Refine move recommendation based on agent strategy and risk tolerance.

      :param base_move: Initial move recommendation.
      :type base_move: RiskMove
      :param analysis: Position analysis context.
      :type analysis: RiskAnalysis

      :returns: Refined move incorporating strategic preferences.
      :rtype: RiskMove


      .. autolink-examples:: _refine_move_with_strategy
         :collapse:


   .. py:method:: analyze_position() -> haive.games.risk.models.RiskAnalysis

      Perform comprehensive strategic analysis of current game position.

      Conducts multi-layered analysis of the game state including territorial
      control evaluation, army distribution assessment, continental bonus analysis,
      threat identification, and opportunity recognition. Generates strategic
      recommendations based on agent's personality and current situation.

      :returns: Comprehensive analysis object containing:
                - Territory control metrics and army distribution
                - Continental bonus evaluation and expansion opportunities
                - Threat assessment and defensive priorities
                - Strategic recommendations with detailed reasoning
                - Position evaluation (winning/neutral/losing)
      :rtype: RiskAnalysis

      :raises ValueError: If agent doesn't have a game state assigned for analysis.

      .. rubric:: Examples

      Basic position analysis::

          agent.state = current_game_state
          analysis = agent.analyze_position()

          print(f"Controlled territories: {analysis.controlled_territories}")
          print(f"Total armies: {analysis.total_armies}")
          print(f"Position: {analysis.position_evaluation}")

      Strategic decision making::

          analysis = agent.analyze_position()

          if analysis.position_evaluation == "winning":
              # Aggressive expansion
              move = analysis.recommended_move
          elif analysis.position_evaluation == "losing":
              # Defensive consolidation
              agent.strategy = "defensive"

      Historical analysis tracking::

          analysis = agent.analyze_position()
          agent.analysis_history.append(analysis)

          # Analyze trend over last 3 turns
          recent_analyses = agent.analysis_history[-3:]
          position_trend = [a.position_evaluation for a in recent_analyses]

      .. note::

         Analysis complexity scales with game state complexity. Full LLM
         integration provides sophisticated reasoning about strategic priorities,
         diplomatic considerations, and tactical execution.


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: get_move() -> haive.games.risk.models.RiskMove

      Determine optimal next move through strategic analysis and decision- making.

      Performs comprehensive position analysis and selects the best move based on
      current game state, agent strategy, risk tolerance, and historical performance.
      Automatically stores analysis in history for learning and adaptation.

      :returns: Optimized move decision containing:
                - Move type (attack, place armies, fortify, end turn)
                - Source and target territories (if applicable)
                - Army quantities and strategic reasoning
                - Risk assessment and expected outcomes
      :rtype: RiskMove

      :raises ValueError: If agent doesn't have a game state assigned.

      .. rubric:: Examples

      Basic move generation::

          agent.state = current_game_state
          move = agent.get_move()

          if move.move_type == MoveType.ATTACK:
              print(f"Attacking {move.to_territory} from {move.from_territory}")
              print(f"Using {move.attack_dice} dice against {move.defend_dice}")
          elif move.move_type == MoveType.PLACE_ARMIES:
              print(f"Placing {move.armies} armies in {move.to_territory}")

      Strategic adaptation::

          move = agent.get_move()

          # Adapt strategy based on move success
          if move.move_type == MoveType.ATTACK and move.success_probability < 0.4:
              agent.risk_tolerance = max(0.1, agent.risk_tolerance - 0.1)

      Decision tracking::

          move = agent.get_move()

          # Analysis automatically stored in history
          latest_analysis = agent.analysis_history[-1]
          print(f"Decision reasoning: {latest_analysis.explanation}")

      .. note::

         Move selection considers multiple factors including territorial security,
         expansion opportunities, continental bonuses, threat mitigation, and
         long-term strategic positioning.


      .. autolink-examples:: get_move
         :collapse:


   .. py:method:: validate_diplomatic_stance(v: str) -> str
      :classmethod:


      Validate diplomatic stance is supported.

      :param v: Diplomatic stance to validate.
      :type v: str

      :returns: Validated diplomatic stance string.
      :rtype: str

      :raises ValueError: If diplomatic stance is not supported.


      .. autolink-examples:: validate_diplomatic_stance
         :collapse:


   .. py:method:: validate_strategy(v: str) -> str
      :classmethod:


      Validate strategic approach is supported.

      :param v: Strategy to validate.
      :type v: str

      :returns: Validated strategy string.
      :rtype: str

      :raises ValueError: If strategy is not supported.


      .. autolink-examples:: validate_strategy
         :collapse:


   .. py:attribute:: analysis_history
      :type:  list[haive.games.risk.models.RiskAnalysis]
      :value: None



   .. py:property:: analysis_summary
      :type: dict[str, int | float | str]


      Get summary statistics from analysis history.

      :returns: Summary containing:
                - total_analyses: Number of analyses performed
                - avg_territories: Average territories controlled
                - avg_armies: Average total armies
                - most_common_evaluation: Most frequent position evaluation
                - strategic_trend: Overall strategic effectiveness trend
      :rtype: Dict[str, Union[int, float, str]]

      .. autolink-examples:: analysis_summary
         :collapse:


   .. py:attribute:: diplomatic_stance
      :type:  str
      :value: None



   .. py:attribute:: minimum_armies_threshold
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: preferred_continents
      :type:  list[str]
      :value: None



   .. py:attribute:: risk_tolerance
      :type:  float
      :value: None



   .. py:attribute:: state
      :type:  haive.games.risk.state.RiskState | None
      :value: None



   .. py:property:: strategic_effectiveness
      :type: float


      Calculate strategic effectiveness based on analysis history.

      :returns: Effectiveness score from 0.0 to 1.0 based on position improvements.
      :rtype: float

      .. rubric:: Examples

      Tracking agent performance::

          effectiveness = agent.strategic_effectiveness
          if effectiveness > 0.7:
              print("Agent performing well")
          elif effectiveness < 0.3:
              print("Agent may need strategy adjustment")

      .. autolink-examples:: strategic_effectiveness
         :collapse:


   .. py:attribute:: strategy
      :type:  str
      :value: None



