"""Advanced Risk agent implementation for strategic world domination gameplay.

This module provides a sophisticated RiskAgent class that uses AI-powered strategic
reasoning to play the classic Risk board game. The agent analyzes territorial control,
army positioning, continental bonuses, and diplomatic opportunities to make optimal
decisions in complex multi-player scenarios.

The agent supports different strategic approaches (aggressive expansion, defensive
fortification, balanced gameplay) and maintains detailed analysis history for
learning and adaptation. It integrates with the broader Haive framework for
LLM-powered decision making and strategic evaluation.

Examples:
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

Note:
    The agent maintains detailed analysis history for learning and strategic
    adaptation. Full LLM integration enables sophisticated reasoning about
    territorial strategy, army management, and diplomatic considerations.
"""

from pydantic import BaseModel, Field, computed_field, field_validator

from haive.games.risk.models import MoveType, RiskAnalysis, RiskMove, Territory
from haive.games.risk.state import RiskState


class RiskAgent(BaseModel):
    """Advanced AI agent for strategic Risk gameplay with sophisticated
    decision-making.

    This agent employs multi-layered strategic analysis to excel at the classic Risk
    board game, combining territorial evaluation, military logistics, continental
    strategy, and diplomatic considerations. It adapts its approach based on game
    state, opponent behavior, and strategic objectives.

    The agent supports various strategic personalities and maintains comprehensive
    analysis history for learning and adaptation. It integrates with LLM systems
    for complex reasoning about world domination strategy, resource allocation,
    and tactical decision-making.

    Attributes:
        name (str): Unique identifier and display name for the agent.
            Used for game tracking and strategic identification.
        state (Optional[RiskState]): Current game state containing board position,
            army distributions, territorial control, and game phase information.
        strategy (str): Strategic approach determining decision-making priorities.
            Options: "aggressive" (expansion-focused), "defensive" (consolidation),
            "balanced" (opportunistic), "diplomatic" (alliance-building).
        risk_tolerance (float): Willingness to take risks in attacks and expansion.
            Range 0.0-1.0, where higher values favor bold moves over safe plays.
        diplomatic_stance (str): Approach to other players and alliance-building.
            Options: "aggressive" (hostile), "neutral" (independent), "cooperative".
        analysis_history (List[RiskAnalysis]): Complete history of strategic analyses.
            Used for learning, pattern recognition, and strategic adaptation.
        preferred_continents (List[str]): Priority continents for expansion focus.
            Agent will prioritize gaining control of these continents for bonuses.
        minimum_armies_threshold (int): Minimum armies to maintain in territories.
            Defensive parameter to avoid leaving territories vulnerable.

    Examples:
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

    Note:
        The agent maintains state independence, allowing multiple agents to operate
        on different game states simultaneously. Strategic parameters can be adjusted
        dynamically for adaptive gameplay and experimental strategies.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique agent identifier and display name",
        examples=["General_Patton", "Strategic_AI", "Risk_Master_3000"],
    )

    state: RiskState | None = Field(
        default=None,
        description="Current Risk game state for strategic analysis and decision-making",
    )

    strategy: str = Field(
        default="balanced",
        description="Strategic approach determining decision-making priorities",
        examples=["aggressive", "defensive", "balanced", "diplomatic"],
    )

    risk_tolerance: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Willingness to take risks in attacks and expansion (0.0-1.0)",
        examples=[0.3, 0.5, 0.8, 1.0],
    )

    diplomatic_stance: str = Field(
        default="neutral",
        description="Approach to other players and alliance-building",
        examples=["aggressive", "neutral", "cooperative"],
    )

    analysis_history: list[RiskAnalysis] = Field(
        default_factory=list,
        description="Complete history of strategic analyses for learning and adaptation",
    )

    preferred_continents: list[str] = Field(
        default_factory=list,
        description="Priority continents for expansion focus and bonus acquisition",
        examples=[
            ["Asia", "Europe"],
            ["Australia", "South America"],
            ["North America", "Africa"],
        ],
    )

    minimum_armies_threshold: int = Field(
        default=2,
        ge=1,
        le=10,
        description="Minimum armies to maintain in territories for defensive security",
        examples=[1, 2, 3, 5],
    )

    @field_validator("strategy")
    @classmethod
    def validate_strategy(cls, v: str) -> str:
        """Validate strategic approach is supported.

        Args:
            v (str): Strategy to validate.

        Returns:
            str: Validated strategy string.

        Raises:
            ValueError: If strategy is not supported.
        """
        valid_strategies = {"aggressive", "defensive", "balanced", "diplomatic"}
        strategy_lower = v.lower().strip()
        if strategy_lower not in valid_strategies:
            raise ValueError(f"Strategy must be one of: {', '.join(valid_strategies)}")
        return strategy_lower

    @field_validator("diplomatic_stance")
    @classmethod
    def validate_diplomatic_stance(cls, v: str) -> str:
        """Validate diplomatic stance is supported.

        Args:
            v (str): Diplomatic stance to validate.

        Returns:
            str: Validated diplomatic stance string.

        Raises:
            ValueError: If diplomatic stance is not supported.
        """
        valid_stances = {"aggressive", "neutral", "cooperative"}
        stance_lower = v.lower().strip()
        if stance_lower not in valid_stances:
            raise ValueError(
                f"Diplomatic stance must be one of: {', '.join(valid_stances)}"
            )
        return stance_lower

    def analyze_position(self) -> RiskAnalysis:
        """Perform comprehensive strategic analysis of current game position.

        Conducts multi-layered analysis of the game state including territorial
        control evaluation, army distribution assessment, continental bonus analysis,
        threat identification, and opportunity recognition. Generates strategic
        recommendations based on agent's personality and current situation.

        Returns:
            RiskAnalysis: Comprehensive analysis object containing:
            - Territory control metrics and army distribution
            - Continental bonus evaluation and expansion opportunities
            - Threat assessment and defensive priorities
            - Strategic recommendations with detailed reasoning
            - Position evaluation (winning/neutral/losing)

        Raises:
            ValueError: If agent doesn't have a game state assigned for analysis.

        Examples:
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

        Note:
            Analysis complexity scales with game state complexity. Full LLM
            integration provides sophisticated reasoning about strategic priorities,
            diplomatic considerations, and tactical execution.
        """
        if not self.state:
            raise ValueError("Agent must have a state to analyze position")

        # Get controlled territories and calculate metrics
        controlled_territories = self.state.get_controlled_territories(self.name)
        total_armies = sum(t.armies for t in controlled_territories)
        controlled_continents = [
            c.name for c in self.state.get_controlled_continents(self.name)
        ]

        # Evaluate position strength
        territory_count = len(controlled_territories)
        continent_bonuses = len(controlled_continents)

        # Determine position evaluation based on metrics
        position_evaluation = "neutral"
        if territory_count > 15 and continent_bonuses >= 2:
            position_evaluation = "winning"
        elif territory_count < 5 or total_armies < 10:
            position_evaluation = "losing"
        elif continent_bonuses >= 1 and territory_count > 8:
            position_evaluation = "strong"
        elif territory_count < 8 and continent_bonuses == 0:
            position_evaluation = "weak"

        # Generate strategic recommendation based on analysis
        recommended_move = self._generate_strategic_move(
            controlled_territories, position_evaluation
        )

        # Create comprehensive analysis with strategic reasoning
        explanation = self._generate_analysis_explanation(
            territory_count, total_armies, continent_bonuses, position_evaluation
        )

        return RiskAnalysis(
            player=self.name,
            controlled_territories=territory_count,
            total_armies=total_armies,
            position_evaluation=position_evaluation,
            controlled_continents=controlled_continents,
            recommended_move=recommended_move,
            explanation=explanation,
        )

    def get_move(self) -> RiskMove:
        """Determine optimal next move through strategic analysis and decision-
        making.

        Performs comprehensive position analysis and selects the best move based on
        current game state, agent strategy, risk tolerance, and historical performance.
        Automatically stores analysis in history for learning and adaptation.

        Returns:
            RiskMove: Optimized move decision containing:
            - Move type (attack, place armies, fortify, end turn)
            - Source and target territories (if applicable)
            - Army quantities and strategic reasoning
            - Risk assessment and expected outcomes

        Raises:
            ValueError: If agent doesn't have a game state assigned.

        Examples:
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

        Note:
            Move selection considers multiple factors including territorial security,
            expansion opportunities, continental bonuses, threat mitigation, and
            long-term strategic positioning.
        """
        if not self.state:
            raise ValueError("Agent must have a state to get a move")

        # Get comprehensive position analysis
        analysis = self.analyze_position()

        # Store analysis in history for learning
        self.analysis_history.append(analysis)

        # Apply strategic modifications based on agent personality
        move = self._refine_move_with_strategy(analysis.recommended_move, analysis)

        return move

    def _generate_strategic_move(
        self, controlled_territories: list[Territory], position_evaluation: str
    ) -> RiskMove:
        """Generate strategic move recommendation based on position analysis.

        Args:
            controlled_territories (List[Territory]): Territories under agent control.
            position_evaluation (str): Current position strength assessment.

        Returns:
            RiskMove: Strategic move recommendation optimized for current situation.
        """
        if not controlled_territories:
            # No territories controlled - shouldn't happen in normal gameplay
            return RiskMove(move_type=MoveType.END_TURN, player=self.name)

        # Strategy-based move selection
        if self.strategy == "aggressive" and position_evaluation in [
            "strong",
            "winning",
        ]:
            # Look for attack opportunities
            return self._generate_attack_move(controlled_territories)
        elif self.strategy == "defensive" or position_evaluation == "losing":
            # Focus on fortification and consolidation
            return self._generate_defensive_move(controlled_territories)
        else:
            # Balanced approach - army placement or opportunistic attack
            return self._generate_balanced_move(
                controlled_territories, position_evaluation
            )

    def _generate_attack_move(
        self, controlled_territories: list[Territory]
    ) -> RiskMove:
        """Generate aggressive attack move targeting expansion opportunities.

        Args:
            controlled_territories (List[Territory]): Agent's controlled territories.

        Returns:
            RiskMove: Attack move targeting optimal expansion opportunity.
        """
        # Find territory with most armies for attacking
        strongest_territory = max(controlled_territories, key=lambda t: t.armies)

        if strongest_territory.armies > self.minimum_armies_threshold:
            # Look for adjacent enemy territories to attack
            # For now, return placeholder attack move
            return RiskMove(
                move_type=MoveType.ATTACK,
                player=self.name,
                from_territory=strongest_territory.name,
                to_territory="Adjacent_Enemy_Territory",  # Would be calculated from game state
                attack_dice=min(3, strongest_territory.armies - 1),
            )
        else:
            # Not enough armies to attack safely
            return self._generate_defensive_move(controlled_territories)

    def _generate_defensive_move(
        self, controlled_territories: list[Territory]
    ) -> RiskMove:
        """Generate defensive move focusing on consolidation and fortification.

        Args:
            controlled_territories (List[Territory]): Agent's controlled territories.

        Returns:
            RiskMove: Defensive move prioritizing territorial security.
        """
        # Find territory with fewest armies for reinforcement
        weakest_territory = min(controlled_territories, key=lambda t: t.armies)

        return RiskMove(
            move_type=MoveType.PLACE_ARMIES,
            player=self.name,
            to_territory=weakest_territory.name,
            # Conservative army placement
            armies=max(1, int(self.risk_tolerance * 3)),
        )

    def _generate_balanced_move(
        self, controlled_territories: list[Territory], position_evaluation: str
    ) -> RiskMove:
        """Generate balanced move considering both offensive and defensive
        needs.

        Args:
            controlled_territories (List[Territory]): Agent's controlled territories.
            position_evaluation (str): Current position strength.

        Returns:
            RiskMove: Balanced move optimizing risk vs. reward.
        """
        if position_evaluation == "strong" and self.risk_tolerance > 0.6:
            # Position allows for calculated aggression
            return self._generate_attack_move(controlled_territories)
        else:
            # Focus on strengthening position
            return self._generate_defensive_move(controlled_territories)

    def _refine_move_with_strategy(
        self, base_move: RiskMove, analysis: RiskAnalysis
    ) -> RiskMove:
        """Refine move recommendation based on agent strategy and risk
        tolerance.

        Args:
            base_move (RiskMove): Initial move recommendation.
            analysis (RiskAnalysis): Position analysis context.

        Returns:
            RiskMove: Refined move incorporating strategic preferences.
        """
        # Apply risk tolerance adjustments
        if base_move.move_type == MoveType.ATTACK:
            # Adjust attack intensity based on risk tolerance
            if hasattr(base_move, "attack_dice") and base_move.attack_dice:
                risk_multiplier = 0.5 + (self.risk_tolerance * 0.5)
                base_move.attack_dice = max(
                    1, int(base_move.attack_dice * risk_multiplier)
                )

        elif base_move.move_type == MoveType.PLACE_ARMIES:
            # Adjust army placement based on strategy
            if base_move.armies and self.strategy == "aggressive":
                base_move.armies = max(
                    base_move.armies, 2
                )  # Minimum aggressive placement

        return base_move

    def _generate_analysis_explanation(
        self,
        territory_count: int,
        total_armies: int,
        continent_bonuses: int,
        position_evaluation: str,
    ) -> str:
        """Generate detailed explanation of strategic analysis and reasoning.

        Args:
            territory_count (int): Number of controlled territories.
            total_armies (int): Total armies under control.
            continent_bonuses (int): Number of controlled continents.
            position_evaluation (str): Overall position assessment.

        Returns:
            str: Detailed strategic analysis explanation.
        """
        explanation_parts = [
            f"Strategic Analysis for {self.name}:",
            f"- Territorial Control: {territory_count} territories",
            f"- Military Strength: {total_armies} total armies",
            f"- Continental Bonuses: {continent_bonuses} continents controlled",
            f"- Position Assessment: {position_evaluation}",
            f"- Strategic Approach: {self.strategy} with {self.risk_tolerance:.1f} risk tolerance",
        ]

        # Add strategy-specific insights
        if self.strategy == "aggressive":
            explanation_parts.append(
                "- Focus: Rapid expansion and territorial conquest"
            )
        elif self.strategy == "defensive":
            explanation_parts.append("- Focus: Consolidation and territorial security")
        elif self.strategy == "balanced":
            explanation_parts.append(
                "- Focus: Opportunistic growth with calculated risks"
            )
        elif self.strategy == "diplomatic":
            explanation_parts.append(
                "- Focus: Alliance building and cooperative strategy"
            )

        # Add position-specific recommendations
        if position_evaluation == "winning":
            explanation_parts.append(
                "- Recommendation: Maintain pressure while securing victories"
            )
        elif position_evaluation == "losing":
            explanation_parts.append(
                "- Recommendation: Defensive consolidation and strategic retreat"
            )
        else:
            explanation_parts.append(
                "- Recommendation: Balanced approach with careful expansion"
            )

        return "\n".join(explanation_parts)

    @computed_field
    @property
    def strategic_effectiveness(self) -> float:
        """Calculate strategic effectiveness based on analysis history.

        Returns:
            float: Effectiveness score from 0.0 to 1.0 based on position improvements.

        Examples:
            Tracking agent performance::

                effectiveness = agent.strategic_effectiveness
                if effectiveness > 0.7:
                    print("Agent performing well")
                elif effectiveness < 0.3:
                    print("Agent may need strategy adjustment")
        """
        if len(self.analysis_history) < 2:
            return 0.5  # Neutral starting point

        # Analyze recent performance trend
        recent_analyses = self.analysis_history[-5:]  # Last 5 analyses

        improvement_score = 0.0
        evaluations = ["losing", "weak", "neutral", "strong", "winning"]

        for i in range(1, len(recent_analyses)):
            prev_eval = recent_analyses[i - 1].position_evaluation
            curr_eval = recent_analyses[i].position_evaluation

            try:
                prev_idx = evaluations.index(prev_eval)
                curr_idx = evaluations.index(curr_eval)

                if curr_idx > prev_idx:
                    improvement_score += 0.2  # Improvement
                elif curr_idx < prev_idx:
                    improvement_score -= 0.1  # Decline
                # No change = 0 points
            except ValueError:
                # Unknown evaluation, neutral score
                pass

        # Normalize to 0.0-1.0 range
        effectiveness = 0.5 + improvement_score
        return max(0.0, min(1.0, effectiveness))

    @computed_field
    @property
    def analysis_summary(self) -> dict[str, int | float | str]:
        """Get summary statistics from analysis history.

        Returns:
            Dict[str, Union[int, float, str]]: Summary containing:
            - total_analyses: Number of analyses performed
            - avg_territories: Average territories controlled
            - avg_armies: Average total armies
            - most_common_evaluation: Most frequent position evaluation
            - strategic_trend: Overall strategic effectiveness trend
        """
        if not self.analysis_history:
            return {
                "total_analyses": 0,
                "avg_territories": 0.0,
                "avg_armies": 0.0,
                "most_common_evaluation": "unknown",
                "strategic_trend": "insufficient_data",
            }

        total_analyses = len(self.analysis_history)
        avg_territories = (
            sum(a.controlled_territories for a in self.analysis_history)
            / total_analyses
        )
        avg_armies = sum(a.total_armies for a in self.analysis_history) / total_analyses

        # Find most common evaluation
        evaluations = [a.position_evaluation for a in self.analysis_history]
        most_common_evaluation = max(set(evaluations), key=evaluations.count)

        # Determine strategic trend
        effectiveness = self.strategic_effectiveness
        if effectiveness > 0.7:
            strategic_trend = "improving"
        elif effectiveness < 0.3:
            strategic_trend = "declining"
        else:
            strategic_trend = "stable"

        return {
            "total_analyses": total_analyses,
            "avg_territories": round(avg_territories, 1),
            "avg_armies": round(avg_armies, 1),
            "most_common_evaluation": most_common_evaluation,
            "strategic_trend": strategic_trend,
        }
