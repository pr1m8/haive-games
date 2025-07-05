"""Risk agent implementation.

This module defines the RiskAgent class that can play the Risk game
using LLM-based decision making.
"""

from pydantic import BaseModel, Field

from haive.games.risk.models import MoveType, RiskAnalysis, RiskMove
from haive.games.risk.state import RiskState


class RiskAgent(BaseModel):
    """Agent for playing the Risk game.

    This agent uses LLM-based reasoning to make strategic decisions
    in the Risk game, including territory selection, army placement,
    attack planning, and fortification.

    Attributes:
        name: The name of the agent.
        state: The current game state.
        strategy: The agent's strategic approach (aggressive, defensive, balanced).
        analysis_history: History of position analyses made by this agent.
    """

    name: str
    state: RiskState | None = None
    strategy: str = "balanced"  # aggressive, defensive, balanced
    analysis_history: list[RiskAnalysis] = Field(default_factory=list)

    def analyze_position(self) -> RiskAnalysis:
        """Analyze the current game position from this agent's perspective.

        Uses strategic reasoning to evaluate the game state and suggest optimal moves.

        Returns:
            A RiskAnalysis object containing position evaluation and recommended moves.

        Raises:
            ValueError: If the agent doesn't have a state assigned.
        """
        if not self.state:
            raise ValueError("Agent must have a state to analyze position")

        # This would be implemented with LLM calls in a complete version
        # For now, just return a placeholder analysis
        return RiskAnalysis(
            player=self.name,
            controlled_territories=len(
                self.state.get_controlled_territories(self.name)
            ),
            total_armies=sum(
                t.armies for t in self.state.get_controlled_territories(self.name)
            ),
            position_evaluation="neutral",
            controlled_continents=[
                c.name for c in self.state.get_controlled_continents(self.name)
            ],
            recommended_move=RiskMove(
                move_type=MoveType.PLACE_ARMIES,
                player=self.name,
                to_territory=(
                    self.state.get_controlled_territories(self.name)[0].name
                    if self.state.get_controlled_territories(self.name)
                    else None
                ),
                armies=1,
            ),
            explanation="Placeholder analysis. Full implementation would use LLM reasoning.",
        )

    def get_move(self) -> RiskMove:
        """Determine the next move for this agent.

        Analyzes the current position and selects the optimal move based on
        the agent's strategy and game state.

        Returns:
            A RiskMove object representing the agent's chosen action.

        Raises:
            ValueError: If the agent doesn't have a state assigned.
        """
        if not self.state:
            raise ValueError("Agent must have a state to get a move")

        # Get position analysis
        analysis = self.analyze_position()

        # Store analysis in history
        self.analysis_history.append(analysis)

        # Return the recommended move from the analysis
        return analysis.recommended_move
