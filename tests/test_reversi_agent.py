"""Test cases for Reversi game agent.

This module tests the ReversiAgent class and its game management capabilities
for playing Reversi/Othello.
"""

# Standard library imports

# Third-party imports
from langgraph.types import Command

# Local imports
from haive.games.reversi.agent import ReversiAgent
from haive.games.reversi.config import ReversiConfig
from haive.games.reversi.models import (
    Position,
    ReversiAnalysis,
    ReversiMove,
)
from haive.games.reversi.state import ReversiState
from haive.games.reversi.state_manager import ReversiStateManager


class TestReversiAgent:
    """Test cases for ReversiAgent class."""

    def test_agent_initialization_default(self) -> None:
        """Test creating ReversiAgent with default config."""
        agent = ReversiAgent()

        assert agent.state_manager == ReversiStateManager
        assert isinstance(agent.config, ReversiConfig)
        assert agent.config.first_player == "B"
        assert agent.config.player_B == "player1"
        assert agent.config.player_W == "player2"

    def test_agent_initialization_custom_config(self) -> None:
        """Test creating ReversiAgent with custom config."""
        config = ReversiConfig(
            first_player="W",
            player_B="Alice",
            player_W="Bob",
            visualize=True,
            enable_analysis=False,
            board_size=10,
        )
        agent = ReversiAgent(config)

        assert agent.config == config
        assert agent.config.first_player == "W"
        assert agent.config.player_B == "Alice"
        assert agent.config.player_W == "Bob"
        assert agent.config.visualize is True
        assert agent.config.enable_analysis is False
        assert agent.config.board_size == 10

    def test_initialize_game(self) -> None:
        """Test game initialization."""
        agent = ReversiAgent()

        command = agent.initialize_game({})
        assert isinstance(command, Command)

        update_data = command.update
        assert update_data is not None

        # Should create a valid initial state
        state = ReversiState(**update_data)
        assert state.current_player == "B"
        assert len(state.board) == 8
        assert len(state.board[0]) == 8
        assert state.scores["B"] == 2
        assert state.scores["W"] == 2
        assert not state.game_over
        assert state.winner is None

        # Check initial board setup
        assert state.board[3][3] == "W"
        assert state.board[3][4] == "B"
        assert state.board[4][3] == "B"
        assert state.board[4][4] == "W"

    def test_initialize_game_with_white_first(self) -> None:
        """Test game initialization with white player first."""
        config = ReversiConfig(first_player="W")
        agent = ReversiAgent(config)

        command = agent.initialize_game({})
        state = ReversiState(**command.update)

        assert state.current_player == "W"

    def test_get_legal_moves(self) -> None:
        """Test getting legal moves for current player."""
        agent = ReversiAgent()

        # Initialize game
        init_command = agent.initialize_game({})
        state_dict = init_command.update

        # Get legal moves
        command = agent.get_legal_moves(state_dict)
        state = ReversiState(**command.update)

        # Black should have 4 legal moves at start
        assert len(state.legal_moves) == 4
        expected_moves = [(2, 3), (3, 2), (4, 5), (5, 4)]
        for move in expected_moves:
            assert move in state.legal_moves

    def test_validate_move_valid(self) -> None:
        """Test validating a legal move."""
        agent = ReversiAgent()

        # Initialize game
        init_command = agent.initialize_game({})
        state_dict = init_command.update

        # Get legal moves first
        moves_command = agent.get_legal_moves(state_dict)
        state_dict = moves_command.update

        # Validate a legal move
        move = ReversiMove(position=Position(row=2, col=3), player="B")
        state_dict["pending_move"] = move.model_dump()

        command = agent.validate_move(state_dict)
        state = ReversiState(**command.update)

        assert state.error is None
        assert state.pending_move is not None

    def test_validate_move_invalid(self) -> None:
        """Test validating an illegal move."""
        agent = ReversiAgent()

        # Initialize game
        init_command = agent.initialize_game({})
        state_dict = init_command.update

        # Try invalid move (corner position)
        move = ReversiMove(position=Position(row=0, col=0), player="B")
        state_dict["pending_move"] = move.model_dump()

        command = agent.validate_move(state_dict)
        state = ReversiState(**command.update)

        assert state.error is not None
        assert "Invalid move" in state.error
        assert state.pending_move is None

    def test_make_move(self) -> None:
        """Test making a valid move."""
        agent = ReversiAgent()

        # Initialize and prepare move
        init_command = agent.initialize_game({})
        state_dict = init_command.update

        # Get legal moves
        moves_command = agent.get_legal_moves(state_dict)
        state_dict = moves_command.update

        # Make move at (2, 3)
        move = ReversiMove(position=Position(row=2, col=3), player="B")
        state_dict["pending_move"] = move.model_dump()
        state_dict["error"] = None  # Clear any error

        command = agent.make_move(state_dict)
        state = ReversiState(**command.update)

        # Check move was made
        assert state.board[2][3] == "B"
        assert state.board[3][3] == "B"  # Flipped piece
        assert state.current_player == "W"  # Turn switched
        assert state.scores["B"] == 4  # Updated score
        assert state.scores["W"] == 1
        assert len(state.move_history) == 1
        assert state.pending_move is None

    def test_skip_turn_when_no_moves(self) -> None:
        """Test skipping turn when player has no legal moves."""
        agent = ReversiAgent()

        # Create a board state where one player has no moves
        # This is a simplified scenario
        state_dict = {
            "board": [["." for _ in range(8)] for _ in range(8)],
            "current_player": "B",
            "scores": {"B": 1, "W": 1},
            "move_history": [],
            "game_over": False,
            "winner": None,
            "legal_moves": [],  # No legal moves
            "pending_move": None,
            "error": None,
            "analysis": None,
        }

        # Only two pieces on board in corners
        state_dict["board"][0][0] = "B"
        state_dict["board"][7][7] = "W"

        command = agent.skip_turn(state_dict)
        state = ReversiState(**command.update)

        assert state.current_player == "W"  # Turn switched
        assert len(state.move_history) == 1
        assert state.move_history[0]["position"] == "pass"

    def test_check_game_end_with_winner(self) -> None:
        """Test checking game end condition with a winner."""
        agent = ReversiAgent()

        # Create end game state - board full with more black pieces
        board = [["B" for _ in range(8)] for _ in range(8)]
        board[7][7] = "W"  # One white piece

        state_dict = {
            "board": board,
            "current_player": "B",
            "scores": {"B": 63, "W": 1},
            "move_history": [],
            "game_over": False,
            "winner": None,
            "legal_moves": [],
            "pending_move": None,
            "error": None,
            "analysis": None,
        }

        command = agent.check_game_end(state_dict)
        state = ReversiState(**command.update)

        assert state.game_over is True
        assert state.winner == "B"

    def test_check_game_end_with_tie(self) -> None:
        """Test checking game end with a tie."""
        agent = ReversiAgent()

        # Create tie game state
        board = [["." for _ in range(8)] for _ in range(8)]
        # Fill board with equal pieces
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    board[i][j] = "B"
                else:
                    board[i][j] = "W"

        state_dict = {
            "board": board,
            "current_player": "B",
            "scores": {"B": 32, "W": 32},
            "move_history": [],
            "game_over": False,
            "winner": None,
            "legal_moves": [],
            "pending_move": None,
            "error": None,
            "analysis": None,
        }

        command = agent.check_game_end(state_dict)
        state = ReversiState(**command.update)

        assert state.game_over is True
        assert state.winner == "tie"

    def test_analyze_position(self) -> None:
        """Test position analysis functionality."""
        config = ReversiConfig(enable_analysis=True)
        agent = ReversiAgent(config)

        # Initialize game
        init_command = agent.initialize_game({})
        state_dict = init_command.update

        command = agent.analyze_position(state_dict)
        state = ReversiState(**command.update)

        assert state.analysis is not None
        analysis = ReversiAnalysis(**state.analysis)

        # Check analysis components
        assert analysis.position_score is not None
        assert len(analysis.best_moves) > 0
        assert analysis.game_phase in ["opening", "midgame", "endgame"]
        assert "mobility" in analysis.evaluation_factors
        assert "corners" in analysis.evaluation_factors
        assert "stability" in analysis.evaluation_factors

    def test_computer_move_generation(self) -> None:
        """Test computer move generation."""
        config = ReversiConfig(computer_player="W")
        agent = ReversiAgent(config)

        # Initialize game
        init_command = agent.initialize_game({})
        state_dict = init_command.update

        # Make a move as black
        move = ReversiMove(position=Position(row=2, col=3), player="B")
        state_dict["pending_move"] = move.model_dump()
        make_move_command = agent.make_move(state_dict)
        state_dict = make_move_command.update

        # Generate computer move
        command = agent.generate_computer_move(state_dict)
        state = ReversiState(**command.update)

        # Computer should have selected a move
        assert state.pending_move is not None
        pending = ReversiMove(**state.pending_move)
        assert pending.player == "W"
        assert (pending.position.row, pending.position.col) in state.legal_moves

    def test_router_continue_condition(self) -> None:
        """Test router returns continue when game is ongoing."""
        agent = ReversiAgent()
        state_dict = {"game_over": False}

        result = agent.router(state_dict)
        assert result == "continue"

    def test_router_end_condition(self) -> None:
        """Test router returns end when game is over."""
        agent = ReversiAgent()
        state_dict = {"game_over": True}

        result = agent.router(state_dict)
        assert result == "end"

    def test_edge_case_pass_moves(self) -> None:
        """Test handling consecutive pass moves ending the game."""
        agent = ReversiAgent()

        # Create state where both players must pass
        state_dict = {
            "board": [["." for _ in range(8)] for _ in range(8)],
            "current_player": "B",
            "scores": {"B": 2, "W": 2},
            "move_history": [{"player": "W", "position": "pass", "flipped": 0}],
            "game_over": False,
            "winner": None,
            "legal_moves": [],
            "pending_move": None,
            "error": None,
            "analysis": None,
        }

        # Setup isolated pieces
        state_dict["board"][0][0] = "B"
        state_dict["board"][0][1] = "B"
        state_dict["board"][7][6] = "W"
        state_dict["board"][7][7] = "W"

        # Black passes
        command = agent.skip_turn(state_dict)
        state_dict = command.update

        # Check if game ends after two consecutive passes
        command = agent.check_game_end(state_dict)
        state = ReversiState(**command.update)

        assert state.game_over is True
        assert state.winner == "tie"  # Equal pieces

    def test_corner_control_strategy(self) -> None:
        """Test that computer prioritizes corner moves."""
        config = ReversiConfig(computer_player="B", difficulty="hard")
        agent = ReversiAgent(config)

        # Create state where corner is available
        state_dict = {
            "board": [["." for _ in range(8)] for _ in range(8)],
            "current_player": "B",
            "scores": {"B": 10, "W": 10},
            "move_history": [],
            "game_over": False,
            "winner": None,
            "legal_moves": [(0, 0), (2, 3), (4, 5)],  # Corner available
            "pending_move": None,
            "error": None,
            "analysis": None,
        }

        # Setup board to make corner legal
        for i in range(1, 4):
            state_dict["board"][i][0] = "W"
        state_dict["board"][4][0] = "B"

        command = agent.generate_computer_move(state_dict)
        state = ReversiState(**command.update)

        # Should choose corner move
        move = ReversiMove(**state.pending_move)
        assert (move.position.row, move.position.col) == (0, 0)

    async def test_async_invoke(self) -> None:
        """Test async invocation of agent."""
        agent = ReversiAgent()
        state_dict = {}

        result = await agent.ainvoke(state_dict)

        assert isinstance(result, Command)
        assert result.update is not None

        # Should initialize game
        state = ReversiState(**result.update)
        assert state.current_player in ["B", "W"]
        assert state.scores["B"] == 2
        assert state.scores["W"] == 2

    def test_invoke_sync(self) -> None:
        """Test synchronous invocation of agent."""
        agent = ReversiAgent()
        state_dict = {}

        result = agent.invoke(state_dict)

        assert isinstance(result, Command)
        assert result.update is not None

        # Should initialize game
        state = ReversiState(**result.update)
        assert state.current_player in ["B", "W"]
        assert not state.game_over
