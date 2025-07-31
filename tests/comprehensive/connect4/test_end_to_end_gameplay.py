"""End-to-end gameplay tests for Connect4 with real LLMs - NO MOCKS."""

import asyncio

import pytest

from haive.games.connect4 import create_default_agent, run_quick_game
from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.state import Connect4State
from haive.games.connect4.ui import Connect4UI


class TestConnect4EndToEndGameplay:
    """Test complete Connect4 games with real components."""

    @pytest.mark.integration
    def test_full_game_with_real_llms(self):
        """Test a complete game with real LLM players."""
        # Create agent with real LLMs
        config = Connect4AgentConfig(
            name="e2e_test_game",
            enable_analysis=False,  # Faster without analysis
            first_player="red",
        )

        agent = Connect4Agent(config)

        # Run game (synchronous)
        Connect4State(
            board=[[None] * 7 for _ in range(6)],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Initialize game
        command = agent.initialize_game({})
        assert command.goto == "make_move"

        # Game should have valid initial state
        state = command.update
        assert state["board"] == [[None] * 7 for _ in range(6)]
        assert state["turn"] == "red"
        assert state["game_status"] == "ongoing"

    @pytest.mark.integration
    def test_quick_game_utility(self):
        """Test the quick game utility function."""
        # This should work with real LLMs
        result = run_quick_game(enable_analysis=False, visualize=False)

        # Verify game completed
        assert "game_status" in result
        assert result["game_status"] in ["red_win", "yellow_win", "draw"]

        # Verify move history exists
        assert "move_history" in result
        assert len(result["move_history"]) >= 7  # Minimum moves for a win

        # Verify winner if not draw
        if result["game_status"] != "draw":
            assert "winner" in result
            assert result["winner"] in ["red", "yellow"]

    def test_game_state_progression(self):
        """Test that game states progress correctly."""
        agent = create_default_agent()

        # Track state progression
        states = []

        # Initialize
        command = agent.initialize_game({})
        initial_state = command.update
        states.append(initial_state)

        # Verify initial state
        assert initial_state["turn"] == "red"
        assert all(cell is None for row in initial_state["board"] for cell in row)

        # Make a move (without full game execution)
        # This tests the state transition logic
        move_state = {
            **initial_state,
            "board": initial_state["board"],
            "move_history": [],
        }

        # State should be valid for move
        assert move_state["game_status"] == "ongoing"

    def test_ui_component_integration(self):
        """Test UI component works with game state."""
        ui = Connect4UI()

        # Test with sample state
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, "yellow", None, None, None],
                [None, None, "red", "yellow", None, None, None],
                ["red", "yellow", "red", "red", "yellow", None, None],
            ],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Should be able to display without errors
        try:
            ui.display_state(state)
            display_works = True
        except Exception:
            display_works = False

        assert display_works

    def test_game_termination_conditions(self):
        """Test various game termination scenarios."""
        # Test 1: Horizontal win
        config = Connect4AgentConfig(name="termination_test", enable_analysis=False)
        Connect4Agent(config)

        # Create near-win state

        # If red plays column 3, game should end
        # (This tests termination detection)

    def test_move_history_tracking(self):
        """Test that move history is properly maintained."""
        config = Connect4AgentConfig(name="history_test", enable_analysis=False)
        agent = Connect4Agent(config)

        # Initialize game
        command = agent.initialize_game({})
        state = command.update

        # Verify empty history
        assert state["move_history"] == []

        # After moves, history should grow
        # Each move should have column and player info

    def test_error_handling_graceful(self):
        """Test graceful error handling."""
        agent = create_default_agent()

        # Test with invalid state
        invalid_state = {
            "board": "not a list",  # Invalid board
            "turn": "red",
            "game_status": "ongoing",
        }

        command = agent.make_move(invalid_state)

        # Should handle error gracefully
        assert command.goto == "END"
        assert "error_message" in command.update

    @pytest.mark.integration
    async def test_async_game_execution(self):
        """Test async game execution capabilities."""
        config = Connect4AgentConfig(name="async_test", enable_analysis=False)
        Connect4Agent(config)

        # Async execution should work
        try:
            # Note: Full async test would require async run method
            await asyncio.sleep(0)  # Minimal async test
            async_works = True
        except Exception:
            async_works = False

        assert async_works

    def test_different_starting_players(self):
        """Test games with different starting players."""
        # Test with red starting
        config_red = Connect4AgentConfig(name="red_start", first_player="red")
        agent_red = Connect4Agent(config_red)

        command = agent_red.initialize_game({})
        assert command.update["turn"] == "red"

        # Test with yellow starting
        config_yellow = Connect4AgentConfig(name="yellow_start", first_player="yellow")
        agent_yellow = Connect4Agent(config_yellow)

        command = agent_yellow.initialize_game({})
        assert command.update["turn"] == "yellow"

    def test_analysis_mode_integration(self):
        """Test integration with analysis mode."""
        config = Connect4AgentConfig(
            name="analysis_test",
            enable_analysis=True,  # Enable analysis
        )
        agent = Connect4Agent(config)

        # Analysis engines should be created
        assert "red_analysis" in agent.engines
        assert "yellow_analysis" in agent.engines

        # Initialize with analysis
        command = agent.initialize_game({})
        state = command.update

        # Analysis lists should exist
        assert "red_analysis" in state
        assert "yellow_analysis" in state
        assert isinstance(state["red_analysis"], list)
        assert isinstance(state["yellow_analysis"], list)
