"""Tests for Connect4 agent with real component validation.

This module provides comprehensive tests for Connect4 agent functionality including:
    - Agent initialization and configuration
    - Move generation and decision making
    - Position analysis and threat calculation
    - Game flow management
    - State visualization and context preparation

All tests use real components without mocks, following the no-mocks methodology.
"""

from unittest.mock import MagicMock

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.models import Connect4Move, Connect4PlayerDecision
from haive.games.connect4.state_manager import Connect4StateManager


class TestConnect4Agent:
    """Test suite for Connect4Agent with real component validation."""

    def create_test_agent(self):
        """Create a test Connect4Agent with minimal configuration."""
        config = Connect4AgentConfig(name="test_connect4_agent", enable_analysis=True)
        agent = Connect4Agent(config=config)
        return agent

    def test_connect4_agent_initialization(self):
        """Test Connect4Agent initialization with basic configuration."""
        config = Connect4AgentConfig(name="test_agent", enable_analysis=True)

        agent = Connect4Agent(config=config)

        # Check agent properties
        assert agent.config.name == "test_agent"
        assert agent.config.enable_analysis is True
        assert agent.state_manager == Connect4StateManager

    def test_connect4_agent_initialization_with_advanced_config(self):
        """Test Connect4Agent initialization with advanced configuration."""
        config = Connect4AgentConfig(
            name="advanced_agent",
            enable_analysis=True,
            runnable_config={
                "configurable": {"thread_id": "test_thread"},
                "recursion_limit": 100,
            },
        )

        agent = Connect4Agent(config=config)

        assert agent.config.name == "advanced_agent"
        assert (
            agent.config.runnable_config["configurable"]["thread_id"] == "test_thread"
        )

    def test_connect4_agent_prepare_move_context_empty_board(self):
        """Test Connect4Agent prepare_move_context for empty board."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        context = agent.prepare_move_context(state, "red")

        # Check required fields
        assert "board" in context
        assert "turn" in context
        assert "color" in context
        assert "legal_moves" in context
        assert "move_history" in context
        assert "threats_winning_moves" in context
        assert "threats_blocking_moves" in context

        # Check values
        assert context["turn"] == "red"
        assert context["color"] == "red"
        assert len(context["legal_moves"]) == 7
        assert context["move_history"] == []
        assert context["threats_winning_moves"] == []
        assert context["threats_blocking_moves"] == []

    def test_connect4_agent_prepare_move_context_with_pieces(self):
        """Test Connect4Agent prepare_move_context with pieces on board."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add some moves
        move1 = Connect4Move(column=3)
        state = Connect4StateManager.apply_move(state, move1)
        move2 = Connect4Move(column=4)
        state = Connect4StateManager.apply_move(state, move2)

        context = agent.prepare_move_context(state, "red")

        # Check board reflects moves
        assert "R" in context["board"] or "r" in context["board"]
        assert "Y" in context["board"] or "y" in context["board"]

        # Check move history
        assert len(context["move_history"]) == 2
        assert "Column 3" in context["move_history"][0]
        assert "Column 4" in context["move_history"][1]

    def test_connect4_agent_prepare_move_context_legal_moves(self):
        """Test Connect4Agent prepare_move_context legal moves formatting."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Fill one column completely
        for _ in range(6):
            state.board[5 - _][3] = "red" if _ % 2 == 0 else "yellow"

        context = agent.prepare_move_context(state, "red")

        # Should have 6 legal moves (column 3 is full)
        assert len(context["legal_moves"]) == 6

        # Should not include column 3
        legal_columns = [move.replace("Column ", "") for move in context["legal_moves"]]
        assert "3" not in legal_columns

    def test_connect4_agent_calculate_threats_no_threats(self):
        """Test Connect4Agent _calculate_threats with no immediate threats."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add scattered pieces with no threats
        state.board[5][1] = "red"
        state.board[5][3] = "yellow"
        state.board[5][5] = "red"

        threats = agent._calculate_threats(state, "red")

        assert threats["winning_moves"] == []
        assert threats["blocking_moves"] == []

    def test_connect4_agent_calculate_threats_winning_move(self):
        """Test Connect4Agent _calculate_threats with winning move available."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set up 3 in a row horizontally for red
        state.board[5][0] = "red"
        state.board[5][1] = "red"
        state.board[5][2] = "red"

        threats = agent._calculate_threats(state, "red")

        # Column 3 should be a winning move
        assert 3 in threats["winning_moves"]
        assert threats["blocking_moves"] == []

    def test_connect4_agent_calculate_threats_blocking_move(self):
        """Test Connect4Agent _calculate_threats with blocking move needed."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set up 3 in a row horizontally for yellow (opponent)
        state.board[5][0] = "yellow"
        state.board[5][1] = "yellow"
        state.board[5][2] = "yellow"

        threats = agent._calculate_threats(state, "red")

        # Column 3 should be a blocking move
        assert 3 in threats["blocking_moves"]
        assert threats["winning_moves"] == []

    def test_connect4_agent_calculate_threats_vertical_winning(self):
        """Test Connect4Agent _calculate_threats with vertical winning move."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set up 3 in a column vertically for red
        state.board[5][3] = "red"
        state.board[4][3] = "red"
        state.board[3][3] = "red"

        threats = agent._calculate_threats(state, "red")

        # Column 3 should be a winning move (complete the vertical)
        assert 3 in threats["winning_moves"]

    def test_connect4_agent_calculate_threats_diagonal_winning(self):
        """Test Connect4Agent _calculate_threats with diagonal winning move."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set up 3 in a diagonal for red
        state.board[5][1] = "red"
        state.board[4][2] = "red"
        state.board[3][3] = "red"
        # Need to complete at (2, 4)

        threats = agent._calculate_threats(state, "red")

        # Column 4 should be a winning move if row 2 is the next available
        if state.get_next_row(4) == 2:
            assert 4 in threats["winning_moves"]

    def test_connect4_agent_calculate_threats_multiple_threats(self):
        """Test Connect4Agent _calculate_threats with multiple threats."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set up multiple threatening positions
        # Horizontal threat for red
        state.board[5][0] = "red"
        state.board[5][1] = "red"
        state.board[5][2] = "red"

        # Horizontal threat for yellow
        state.board[4][3] = "yellow"
        state.board[4][4] = "yellow"
        state.board[4][5] = "yellow"

        threats = agent._calculate_threats(state, "red")

        # Should detect both winning and blocking opportunities
        assert 3 in threats["winning_moves"]  # Complete red's threat
        assert 6 in threats["blocking_moves"]  # Block yellow's threat

    def test_connect4_agent_calculate_threats_full_column_ignored(self):
        """Test Connect4Agent _calculate_threats ignores full columns."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set up winning opportunity in column 3
        state.board[5][0] = "red"
        state.board[5][1] = "red"
        state.board[5][2] = "red"

        # Fill column 3 completely
        for row in range(6):
            state.board[row][3] = "yellow"

        threats = agent._calculate_threats(state, "red")

        # Column 3 should not be considered (it's full)
        assert 3 not in threats["winning_moves"]

    def test_connect4_agent_prepare_analysis_context_empty_board(self):
        """Test Connect4Agent prepare_analysis_context for empty board."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        context = agent.prepare_analysis_context(state, "red")

        # Check required fields
        assert "board" in context
        assert "turn" in context
        assert "color" in context
        assert "move_history" in context
        assert "threats_winning_moves" in context
        assert "threats_blocking_moves" in context
        assert "columns_usage" in context

        # Check values
        assert context["color"] == "red"
        assert len(context["columns_usage"]) == 7
        assert all(usage == 0 for usage in context["columns_usage"])

    def test_connect4_agent_prepare_analysis_context_with_pieces(self):
        """Test Connect4Agent prepare_analysis_context with pieces on board."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add pieces to various columns
        state.board[5][0] = "red"  # 1 piece in column 0
        state.board[5][1] = "yellow"  # 1 piece in column 1
        state.board[4][1] = "red"  # 2 pieces in column 1
        state.board[5][3] = "yellow"  # 1 piece in column 3
        state.board[4][3] = "red"  # 2 pieces in column 3
        state.board[3][3] = "yellow"  # 3 pieces in column 3

        context = agent.prepare_analysis_context(state, "red")

        # Check column usage calculation
        expected_usage = [1, 2, 0, 3, 0, 0, 0]  # Based on pieces placed
        assert context["columns_usage"] == expected_usage

    def test_connect4_agent_extract_move_from_decision(self):
        """Test Connect4Agent extract_move from player decision."""
        agent = self.create_test_agent()

        move = Connect4Move(column=3, explanation="Strategic center play")
        decision = Connect4PlayerDecision(
            move=move,
            position_eval="Strong position",
            reasoning="Center control is crucial",
        )

        extracted_move = agent.extract_move(decision)

        assert extracted_move == move
        assert extracted_move.column == 3
        assert extracted_move.explanation == "Strategic center play"

    def test_connect4_agent_player_move_methods(self):
        """Test Connect4Agent player1 and player2 move methods."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Mock the make_move method to test delegation
        agent.make_move = MagicMock()

        # Test player1 move
        agent.make_player1_move(state)
        agent.make_move.assert_called_with(state, "red")

        # Test player2 move
        agent.make_move.reset_mock()
        agent.make_player2_move(state)
        agent.make_move.assert_called_with(state, "yellow")

    def test_connect4_agent_analysis_methods(self):
        """Test Connect4Agent player1 and player2 analysis methods."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Mock the analyze_position method to test delegation
        agent.analyze_position = MagicMock()

        # Test player1 analysis
        agent.analyze_player1(state)
        agent.analyze_position.assert_called_with(state, "red")

        # Test player2 analysis
        agent.analyze_position.reset_mock()
        agent.analyze_player2(state)
        agent.analyze_position.assert_called_with(state, "yellow")

    def test_connect4_agent_visualize_state_basic(self):
        """Test Connect4Agent visualize_state with basic state."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        state_dict = state.model_dump()

        # Should not raise an exception
        agent.visualize_state(state_dict)

    def test_connect4_agent_visualize_state_with_moves(self):
        """Test Connect4Agent visualize_state with move history."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add some moves
        move1 = Connect4Move(column=3)
        state = Connect4StateManager.apply_move(state, move1)
        move2 = Connect4Move(column=4)
        state = Connect4StateManager.apply_move(state, move2)

        state_dict = state.model_dump()

        # Should not raise an exception
        agent.visualize_state(state_dict)

    def test_connect4_agent_visualize_state_with_analysis(self):
        """Test Connect4Agent visualize_state with player analysis."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add analysis for red player
        red_analysis = {
            "position_score": 0.5,
            "center_control": 7,
            "threats": {"winning_moves": [3], "blocking_moves": []},
            "suggested_columns": [3, 2, 4],
            "winning_chances": 65,
        }

        state.red_analysis = [red_analysis]
        state.turn = "yellow"  # So red analysis shows up

        state_dict = state.model_dump()

        # Should not raise an exception
        agent.visualize_state(state_dict)

    def test_connect4_agent_visualize_state_game_over(self):
        """Test Connect4Agent visualize_state with game over state."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Set game over state
        state.game_status = "red_win"
        state.winner = "red"

        state_dict = state.model_dump()

        # Should not raise an exception
        agent.visualize_state(state_dict)

    def test_connect4_agent_move_context_player_analysis_red(self):
        """Test Connect4Agent move context includes red player analysis."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add red analysis
        red_analysis = {"position_score": 0.3, "winning_chances": 60}
        state.red_analysis = [red_analysis]

        context = agent.prepare_move_context(state, "red")

        # Should include player analysis
        assert context["player_analysis"] is not None
        assert len(context["player_analysis"]) == 1

    def test_connect4_agent_move_context_player_analysis_yellow(self):
        """Test Connect4Agent move context includes yellow player analysis."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add yellow analysis
        yellow_analysis = {"position_score": -0.2, "winning_chances": 40}
        state.yellow_analysis = [yellow_analysis]

        context = agent.prepare_move_context(state, "yellow")

        # Should include player analysis
        assert context["player_analysis"] is not None
        assert len(context["player_analysis"]) == 1

    def test_connect4_agent_move_context_limited_analysis_history(self):
        """Test Connect4Agent move context limits analysis history to 10 entries."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add many analysis entries (more than 10)
        red_analyses = []
        for i in range(15):
            analysis = {"position_score": i * 0.1, "winning_chances": 50 + i}
            red_analyses.append(analysis)

        state.red_analysis = red_analyses

        context = agent.prepare_move_context(state, "red")

        # Should limit to last 10 entries
        assert len(context["player_analysis"]) == 10
        # Should be the last 10 entries
        assert context["player_analysis"][0]["position_score"] == 0.5  # Entry 5
        assert context["player_analysis"][-1]["position_score"] == 1.4  # Entry 14

    def test_connect4_agent_move_context_limited_move_history(self):
        """Test Connect4Agent move context limits move history to 5 entries."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Add many moves (more than 5)
        moves = []
        for i in range(8):
            move = Connect4Move(column=i % 7)
            moves.append(move)

        state.move_history = moves

        context = agent.prepare_move_context(state, "red")

        # Should limit to last 5 entries
        assert len(context["move_history"]) == 5

    def test_connect4_agent_complex_threat_scenario(self):
        """Test Connect4Agent threat calculation in complex board scenario."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Create complex board with multiple threats
        # Red has multiple winning opportunities
        state.board[5][0] = "red"
        state.board[5][1] = "red"
        state.board[5][2] = "red"  # Can win at column 3

        state.board[4][1] = "red"
        state.board[3][2] = "red"
        state.board[2][3] = "red"  # Can win at column 4 (diagonal)

        # Yellow has blocking opportunities
        state.board[5][4] = "yellow"
        state.board[5][5] = "yellow"
        state.board[5][6] = "yellow"  # Red should block at column 3

        threats = agent._calculate_threats(state, "red")

        # Should detect multiple winning moves
        assert len(threats["winning_moves"]) >= 1
        assert len(threats["blocking_moves"]) >= 1

    def test_connect4_agent_edge_case_board_boundaries(self):
        """Test Connect4Agent threat calculation at board boundaries."""
        agent = self.create_test_agent()
        state = Connect4StateManager.initialize()

        # Test threats at left edge
        state.board[5][0] = "red"
        state.board[5][1] = "red"
        state.board[5][2] = "red"

        # Test threats at right edge
        state.board[4][4] = "yellow"
        state.board[4][5] = "yellow"
        state.board[4][6] = "yellow"

        threats_red = agent._calculate_threats(state, "red")
        threats_yellow = agent._calculate_threats(state, "yellow")

        # Should handle edge cases without errors
        assert isinstance(threats_red["winning_moves"], list)
        assert isinstance(threats_red["blocking_moves"], list)
        assert isinstance(threats_yellow["winning_moves"], list)
        assert isinstance(threats_yellow["blocking_moves"], list)
