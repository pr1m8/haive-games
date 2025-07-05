"""Test cases for Risk game agent.

This module tests the RiskAgent class and its decision-making capabilities
for playing the Risk game.
"""

import pytest

from haive.games.risk.agent import RiskAgent
from haive.games.risk.models import MoveType, RiskAnalysis, RiskMove
from haive.games.risk.state import RiskState


class TestRiskAgent:
    """Test cases for RiskAgent class."""

    def test_agent_creation_basic(self) -> None:
        """Test creating a basic RiskAgent."""
        agent = RiskAgent(name="TestAgent")

        assert agent.name == "TestAgent"
        assert agent.state is None
        assert agent.strategy == "balanced"
        assert agent.analysis_history == []

    def test_agent_creation_with_strategy(self) -> None:
        """Test creating a RiskAgent with specific strategy."""
        agent = RiskAgent(name="AggressiveAgent", strategy="aggressive")

        assert agent.name == "AggressiveAgent"
        assert agent.strategy == "aggressive"

    def test_agent_creation_with_state(self) -> None:
        """Test creating a RiskAgent with initial state."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)
        agent = RiskAgent(name="Alice", state=state)

        assert agent.name == "Alice"
        assert agent.state == state

    def test_analyze_position_no_state(self) -> None:
        """Test that analyze_position fails when agent has no state."""
        agent = RiskAgent(name="TestAgent")

        with pytest.raises(
            ValueError, match="Agent must have a state to analyze position"
        ):
            agent.analyze_position()

    def test_analyze_position_with_state(self) -> None:
        """Test analyze_position with valid state."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice some territories
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alaska"].armies = 5
        state.territories["Alberta"].owner = "Alice"
        state.territories["Alberta"].armies = 3

        agent = RiskAgent(name="Alice", state=state)
        analysis = agent.analyze_position()

        assert isinstance(analysis, RiskAnalysis)
        assert analysis.player == "Alice"
        assert analysis.controlled_territories == 2
        assert analysis.total_armies == 8  # 5 + 3
        assert analysis.position_evaluation == "neutral"
        assert isinstance(analysis.recommended_move, RiskMove)
        assert analysis.explanation is not None

    def test_analyze_position_with_continent_control(self) -> None:
        """Test analyze_position when agent controls continents."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice all of Australia
        australia_territories = [
            "Eastern Australia",
            "Western Australia",
            "New Guinea",
            "Indonesia",
        ]
        for territory_name in australia_territories:
            state.territories[territory_name].owner = "Alice"
            state.territories[territory_name].armies = 2

        agent = RiskAgent(name="Alice", state=state)
        analysis = agent.analyze_position()

        assert analysis.controlled_territories == 4
        assert analysis.total_armies == 8  # 4 territories * 2 armies each
        assert "Australia" in analysis.controlled_continents

    def test_get_move_no_state(self) -> None:
        """Test that get_move fails when agent has no state."""
        agent = RiskAgent(name="TestAgent")

        with pytest.raises(ValueError, match="Agent must have a state to get a move"):
            agent.get_move()

    def test_get_move_with_state(self) -> None:
        """Test get_move with valid state."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice some territories
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alaska"].armies = 5

        agent = RiskAgent(name="Alice", state=state)
        move = agent.get_move()

        assert isinstance(move, RiskMove)
        assert move.player == "Alice"
        assert move.move_type == MoveType.PLACE_ARMIES

        # Check that analysis was added to history
        assert len(agent.analysis_history) == 1
        assert agent.analysis_history[0].player == "Alice"

    def test_get_move_updates_analysis_history(self) -> None:
        """Test that get_move adds analysis to history."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice some territories
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alaska"].armies = 5

        agent = RiskAgent(name="Alice", state=state)

        # Get multiple moves
        move1 = agent.get_move()
        move2 = agent.get_move()

        assert len(agent.analysis_history) == 2
        assert all(analysis.player == "Alice" for analysis in agent.analysis_history)
        assert isinstance(move1, RiskMove)
        assert isinstance(move2, RiskMove)

    def test_analyze_position_no_territories(self) -> None:
        """Test analyze_position when agent controls no territories."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Don't give Alice any territories
        agent = RiskAgent(name="Alice", state=state)

        # This should not crash, even with no territories
        analysis = agent.analyze_position()

        assert analysis.controlled_territories == 0
        assert analysis.total_armies == 0
        assert analysis.controlled_continents == []

    def test_analyze_position_multiple_continents(self) -> None:
        """Test analyze_position with multiple continent control."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice all of Australia and South America
        australia_territories = [
            "Eastern Australia",
            "Western Australia",
            "New Guinea",
            "Indonesia",
        ]
        south_america_territories = ["Argentina", "Brazil", "Peru", "Venezuela"]

        total_territories = 0
        total_armies = 0

        for territory_name in australia_territories + south_america_territories:
            state.territories[territory_name].owner = "Alice"
            state.territories[territory_name].armies = 3
            total_territories += 1
            total_armies += 3

        agent = RiskAgent(name="Alice", state=state)
        analysis = agent.analyze_position()

        assert analysis.controlled_territories == total_territories
        assert analysis.total_armies == total_armies
        assert len(analysis.controlled_continents) == 2
        assert "Australia" in analysis.controlled_continents
        assert "South America" in analysis.controlled_continents

    def test_agent_with_different_strategies(self) -> None:
        """Test agents with different strategies."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Set up some territory ownership
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alaska"].armies = 5

        # Create agents with different strategies
        aggressive_agent = RiskAgent(name="Alice", state=state, strategy="aggressive")
        defensive_agent = RiskAgent(name="Alice", state=state, strategy="defensive")
        balanced_agent = RiskAgent(name="Alice", state=state, strategy="balanced")

        # All should be able to analyze and get moves
        aggressive_analysis = aggressive_agent.analyze_position()
        defensive_analysis = defensive_agent.analyze_position()
        balanced_analysis = balanced_agent.analyze_position()

        assert aggressive_analysis.player == "Alice"
        assert defensive_analysis.player == "Alice"
        assert balanced_analysis.player == "Alice"

        aggressive_move = aggressive_agent.get_move()
        defensive_move = defensive_agent.get_move()
        balanced_move = balanced_agent.get_move()

        assert all(
            isinstance(move, RiskMove)
            for move in [aggressive_move, defensive_move, balanced_move]
        )
        assert all(
            move.player == "Alice"
            for move in [aggressive_move, defensive_move, balanced_move]
        )

    def test_state_updates_affect_analysis(self) -> None:
        """Test that changing state affects subsequent analysis."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice one territory initially
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alaska"].armies = 2

        agent = RiskAgent(name="Alice", state=state)

        # First analysis
        analysis1 = agent.analyze_position()
        assert analysis1.controlled_territories == 1
        assert analysis1.total_armies == 2

        # Give Alice more territories
        state.territories["Alberta"].owner = "Alice"
        state.territories["Alberta"].armies = 3
        state.territories["Quebec"].owner = "Alice"
        state.territories["Quebec"].armies = 4

        # Second analysis should reflect the changes
        analysis2 = agent.analyze_position()
        assert analysis2.controlled_territories == 3
        assert analysis2.total_armies == 9  # 2 + 3 + 4

    def test_recommended_move_structure(self) -> None:
        """Test that recommended moves have proper structure."""
        player_names = ["Alice", "Bob", "Charlie"]
        state = RiskState.initialize(player_names)

        # Give Alice a territory
        state.territories["Alaska"].owner = "Alice"
        state.territories["Alaska"].armies = 5

        agent = RiskAgent(name="Alice", state=state)
        analysis = agent.analyze_position()

        recommended_move = analysis.recommended_move
        assert recommended_move.move_type == MoveType.PLACE_ARMIES
        assert recommended_move.player == "Alice"
        assert recommended_move.to_territory == "Alaska"
        assert recommended_move.armies == 1
        assert recommended_move.from_territory is None  # Not needed for PLACE_ARMIES
        assert recommended_move.cards is None  # Not needed for PLACE_ARMIES
        assert recommended_move.attack_dice is None  # Not needed for PLACE_ARMIES
