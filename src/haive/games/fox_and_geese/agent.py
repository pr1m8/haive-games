"""Fox and Geese game agent.

This module defines the Fox and Geese game agent, which uses language models
to generate moves and analyze positions in the game.
"""

import time
from typing import Any

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.constants import START

from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.fox_and_geese.state import FoxAndGeeseState
from haive.games.fox_and_geese.state_manager import FoxAndGeeseStateManager
from haive.games.framework.base.agent import GameAgent


@register_agent(FoxAndGeeseConfig)
class FoxAndGeeseAgent(GameAgent[FoxAndGeeseConfig]):
    """Agent for playing Fox and Geese.

    This class implements the Fox and Geese game agent, which uses language models
    to generate moves and analyze positions in the game.
    """

    def __init__(self, config: FoxAndGeeseConfig = FoxAndGeeseConfig()):
        """Initialize the Fox and Geese agent.

        Args:
            config (FoxAndGeeseConfig): The configuration for the Fox and Geese game.
        """
        super().__init__(config)
        self.state_manager = FoxAndGeeseStateManager
        self.engines = config.engines

    def initialize_game(self, state: dict[str, Any]) -> FoxAndGeeseState:
        """Initialize a new Fox and Geese game.

        Args:
            state (Dict[str, Any]): Initial state dictionary (unused here but required for interface).

        Returns:
            FoxAndGeeseState: Initialization command containing the new game state.
        """
        game_state = self.state_manager.initialize()
        return game_state

    def prepare_move_context(
        self, state: FoxAndGeeseState, player: str
    ) -> dict[str, Any]:
        """Prepare context for move generation.

        Args:
            state (FoxAndGeeseState): Current game state.
            player (str): The player making the move ('fox' or 'geese').

        Returns:
            Dict[str, Any]: Context dictionary for move generation.
        """
        # Format legal moves for display
        formatted_legal_moves = "\n".join(
            [str(move) for move in self.state_manager.get_legal_moves(state)]
        )

        # Get recent move history
        recent_moves = []
        for move in state.move_history[-5:]:
            recent_moves.append(str(move))

        # Prepare the context
        return {
            "board_string": state.board_string,
            "legal_moves": formatted_legal_moves,
            "move_history": "\n".join(recent_moves),
            "num_geese": state.num_geese,
        }

    def extract_move(self, response: Any, piece_type: str = "fox") -> FoxAndGeeseMove:
        """Extract move from engine response.

        Args:
            response (Any): Response from the engine.
            piece_type (str): Type of piece making the move ('fox' or 'goose').

        Returns:
            FoxAndGeeseMove: Parsed move object.
        """
        # Handle different response types
        if isinstance(response, FoxAndGeeseMove):
            # Already the right type
            return response
        elif hasattr(response, "content"):
            # AIMessage with content
            if isinstance(response.content, FoxAndGeeseMove):
                # Content is already the structured object
                return response.content
            elif isinstance(response.content, dict):
                # Content is a dict, convert to FoxAndGeeseMove
                return FoxAndGeeseMove(**response.content)
            elif isinstance(response.content, str):
                # String content - this shouldn't happen with structured output
                print(
                    f"⚠️ Warning: Received string content (structured output might not be working): {response.content[:100]}..."
                )
                # Try to parse JSON from the string
                import json

                try:
                    parsed = json.loads(response.content)
                    if isinstance(parsed, dict):
                        return FoxAndGeeseMove(**parsed)
                except:
                    pass
                # Return a dummy move for debugging - use correct piece type
                print(f"🔧 Creating dummy {piece_type} move for debugging")
                return self._create_dummy_move(piece_type)
            else:
                # Content is already a structured object
                return response.content
        elif isinstance(response, dict):
            # Response is a dict, convert to FoxAndGeeseMove
            return FoxAndGeeseMove(**response)
        else:
            # Fallback - create a dummy move
            print(f"❌ Warning: Unexpected response type: {type(response)}")
            return self._create_dummy_move(piece_type)

    def _create_dummy_move(self, piece_type: str) -> FoxAndGeeseMove:
        """Create a dummy move for debugging purposes.

        Args:
            piece_type (str): Type of piece ('fox' or 'goose').

        Returns:
            FoxAndGeeseMove: A dummy move.
        """
        if piece_type == "fox":
            # Simple fox move
            return FoxAndGeeseMove(
                from_pos=FoxAndGeesePosition(row=3, col=3),
                to_pos=FoxAndGeesePosition(row=2, col=2),
                piece_type="fox",
            )
        else:
            # Simple goose move
            return FoxAndGeeseMove(
                from_pos=FoxAndGeesePosition(row=1, col=0),
                to_pos=FoxAndGeesePosition(row=2, col=1),
                piece_type="goose",
            )

    def _get_legal_move_fallback(
        self, game_state: FoxAndGeeseState, piece_type: str
    ) -> FoxAndGeeseMove:
        """Get a legal move as a fallback when LLM fails.

        Args:
            game_state (FoxAndGeeseState): Current game state.
            piece_type (str): Type of piece ('fox' or 'goose').

        Returns:
            FoxAndGeeseMove: A legal move, or dummy if no legal moves.
        """
        try:
            legal_moves = self.state_manager.get_legal_moves(game_state)
            if legal_moves:
                # Return the first legal move
                return legal_moves[0]
            else:
                # No legal moves - game should be over
                print(f"⚠️ No legal moves available for {piece_type}")
                return self._create_dummy_move(piece_type)
        except Exception as e:
            print(f"❌ Error getting legal moves: {e}")
            return self._create_dummy_move(piece_type)

    def make_fox_move(self, state: dict[str, Any]) -> FoxAndGeeseState:
        """Make a move for the fox.

        Args:
            state (dict[str, Any]): Current game state.

        Returns:
            FoxAndGeeseState: Updated game state after the move.
        """
        try:
            # Convert dict to FoxAndGeeseState
            game_state = FoxAndGeeseState(**state)

            print(f"🦊 Fox move - Current turn: {game_state.turn}")

            # Ensure it's the fox's turn
            if game_state.turn != "fox":
                print(
                    f"⚠️ Not fox's turn (current: {game_state.turn}), skipping fox move"
                )
                return game_state

            # Check if fox has legal moves
            legal_moves = self.state_manager.get_legal_moves(game_state)
            if not legal_moves:
                print("🏁 Fox has no legal moves - game over!")
                game_state.game_status = "geese_win"
                game_state.winner = "geese"
                return game_state

            # Prepare context for the fox player
            context = self.prepare_move_context(game_state, "fox")

            try:
                # Call the fox player engine
                fox_player = self.engines["fox_player"].create_runnable()
                response = fox_player.invoke(context)

                # Extract the move
                move = self.extract_move(response, "fox")

                # Validate move is legal
                if move not in legal_moves:
                    print(f"⚠️ LLM move {move} not in legal moves, using fallback")
                    move = self._get_legal_move_fallback(game_state, "fox")

            except Exception as e:
                print(f"❌ Error calling fox engine: {e}")
                print("🔄 Using fallback legal move")
                move = self._get_legal_move_fallback(game_state, "fox")

            # Apply the move
            print(f"🦊 Applying fox move: {move}")
            new_state = self.state_manager.apply_move(game_state, move)

            # Return the updated state
            return new_state

        except Exception as e:
            print(f"❌ Critical error in fox move: {e}")
            # Return original state to prevent crashes
            game_state = FoxAndGeeseState(**state)
            return game_state

    def make_geese_move(self, state: dict[str, Any]) -> FoxAndGeeseState:
        """Make a move for the geese.

        Args:
            state (dict[str, Any]): Current game state.

        Returns:
            FoxAndGeeseState: Updated game state after the move.
        """
        try:
            # Convert dict to FoxAndGeeseState
            game_state = FoxAndGeeseState(**state)

            print(f"🐺 Geese move - Current turn: {game_state.turn}")

            # Ensure it's the geese's turn
            if game_state.turn != "geese":
                print(
                    f"⚠️ Not geese's turn (current: {game_state.turn}), skipping geese move"
                )
                return game_state

            # Check if geese have legal moves
            legal_moves = self.state_manager.get_legal_moves(game_state)
            if not legal_moves:
                print("🏁 Geese have no legal moves - game over!")
                game_state.game_status = "fox_win"
                game_state.winner = "fox"
                return game_state

            # Prepare context for the geese player
            context = self.prepare_move_context(game_state, "geese")

            try:
                # Call the geese player engine
                geese_player = self.engines["geese_player"].create_runnable()
                response = geese_player.invoke(context)

                # Extract the move
                move = self.extract_move(response, "goose")

                # Validate move is legal
                if move not in legal_moves:
                    print(f"⚠️ LLM move {move} not in legal moves, using fallback")
                    move = self._get_legal_move_fallback(game_state, "goose")

            except Exception as e:
                print(f"❌ Error calling geese engine: {e}")
                print("🔄 Using fallback legal move")
                move = self._get_legal_move_fallback(game_state, "goose")

            # Apply the move
            print(f"🐺 Applying geese move: {move}")
            new_state = self.state_manager.apply_move(game_state, move)

            # Return the updated state
            return new_state

        except Exception as e:
            print(f"❌ Critical error in geese move: {e}")
            # Return original state to prevent crashes
            return game_state

    def analyze_fox_position(self, state: dict[str, Any]) -> FoxAndGeeseState:
        """Analyze the current position from the Fox's perspective.

        Args:
            state (dict[str, Any]): Current game state.

        Returns:
            FoxAndGeeseState: Updated game state after the analysis.
        """
        # Convert dict to FoxAndGeeseState
        game_state = FoxAndGeeseState(**state)

        context = {
            "board_string": game_state.board_string,
            "turn": game_state.turn,
            "num_geese": game_state.num_geese,
            "move_history": "\n".join(
                [str(move) for move in game_state.move_history[-5:]]
            ),
        }

        fox_analyzer = self.engines["fox_analysis"].create_runnable()
        analysis = fox_analyzer.invoke(context)

        # Handle different analysis response types
        if hasattr(analysis, "content"):
            # AIMessage with content
            if isinstance(analysis.content, str):
                analysis_text = analysis.content
            else:
                analysis_text = str(analysis.content)
        else:
            analysis_text = str(analysis)

        new_state = (
            game_state.model_copy()
            if hasattr(game_state, "model_copy")
            else game_state.copy()
        )
        new_state.fox_analysis.append(analysis_text)

        return new_state

    def analyze_geese_position(self, state: dict[str, Any]) -> FoxAndGeeseState:
        """Analyze the current position from the Geese's perspective.

        Args:
            state (dict[str, Any]): Current game state.

        Returns:
            FoxAndGeeseState: Updated game state after the analysis.
        """
        # Convert dict to FoxAndGeeseState
        game_state = FoxAndGeeseState(**state)

        context = {
            "board_string": game_state.board_string,
            "turn": game_state.turn,
            "num_geese": game_state.num_geese,
            "move_history": "\n".join(
                [str(move) for move in game_state.move_history[-5:]]
            ),
        }

        geese_analyzer = self.engines["geese_analysis"].create_runnable()
        analysis = geese_analyzer.invoke(context)

        # Handle different analysis response types
        if hasattr(analysis, "content"):
            # AIMessage with content
            if isinstance(analysis.content, str):
                analysis_text = analysis.content
            else:
                analysis_text = str(analysis.content)
        else:
            analysis_text = str(analysis)

        new_state = (
            game_state.model_copy()
            if hasattr(game_state, "model_copy")
            else game_state.copy()
        )
        new_state.geese_analysis.append(analysis_text)

        return new_state

    def analyze_position(self, state: dict[str, Any]) -> FoxAndGeeseState:
        """Analyze the current position based on the current turn.

        Args:
            state (dict[str, Any]): Current game state.

        Returns:
            FoxAndGeeseState: Updated game state after the analysis.
        """
        # Convert dict to FoxAndGeeseState
        game_state = FoxAndGeeseState(**state)

        # Call the appropriate analyzer based on whose turn it is
        if game_state.turn == "fox":
            return self.analyze_fox_position(state)
        else:
            return self.analyze_geese_position(state)

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Visualize the current game state.

        Args:
            state (Dict[str, Any]): Current game state.
        """
        if not self.config.visualize:
            return

        # Extract the actual game state from the nested structure
        # The state might be nested under a node key (like 'initialize', 'fox_move', etc.)
        game_state_dict = None

        # Check if this is a nested state from the workflow
        for key, value in state.items():
            if isinstance(value, dict) and "turn" in value:
                game_state_dict = value
                break

        # If no nested state found, assume the state is at the top level
        if game_state_dict is None:
            game_state_dict = state

        # Create a FoxAndGeeseState from the dict
        game_state = FoxAndGeeseState(**game_state_dict)

        print("\n" + "=" * 50)
        print(f"🎮 Current Player: {game_state.turn}")
        print(f"📌 Game Status: {game_state.game_status}")
        print(f"🦊 Fox position: {game_state.fox_position}")
        print(f"🐺 Geese remaining: {game_state.num_geese}")
        print("=" * 50)

        # Print the board
        print("\n" + game_state.board_string)

        # Print last move if available
        if game_state.move_history:
            last_move = game_state.move_history[-1]
            print(f"\n📝 Last Move: {last_move!s}")

        # Print analysis if available
        if hasattr(game_state, "fox_analysis") and game_state.fox_analysis:
            print("\n🦊 Latest Fox Analysis:")
            print(game_state.fox_analysis[-1])

        if hasattr(game_state, "geese_analysis") and game_state.geese_analysis:
            print("\n🐺 Latest Geese Analysis:")
            print(game_state.geese_analysis[-1])

        # Add a short delay for readability
        time.sleep(0.5)

    def setup_workflow(self) -> None:
        """Set up the game workflow.

        Creates a dynamic graph with nodes for game initialization, move making,
        and analysis. Uses conditional branching to ensure only one player moves at a time.
        """
        # Create a graph builder
        builder = DynamicGraph(
            state_schema=self.state_schema,
            input_schema=self.input_schema,
            output_schema=self.output_schema,
            name=self.config.name,
        )

        # Add nodes for the main game flow
        builder.add_node("initialize", self.initialize_game)
        builder.add_node("fox_move", self.make_fox_move)
        builder.add_node("geese_move", self.make_geese_move)
        builder.add_node("analyze_fox", self.analyze_fox_position)
        builder.add_node("analyze_geese", self.analyze_geese_position)

        def game_over_node(state: dict[str, Any]) -> FoxAndGeeseState:
            """Final node for game over state."""
            return FoxAndGeeseState(**state)

        # Helper function to check if game is over
        def should_continue(state: dict) -> str:
            game_state = FoxAndGeeseState(**state)

            # Check if game is over by status
            if game_state.game_status != "ongoing":
                print(
                    f"🏁 Game over: {game_state.game_status} - Winner: {game_state.winner}"
                )
                return "game_over"

            # Check for too many moves (prevent infinite loops)
            if len(game_state.move_history) >= 100:  # Max 100 moves
                print("🏁 Game ended: Too many moves (100+ moves)")
                return "game_over"

            return "continue"

        # Set up linear flow to prevent concurrent updates
        builder.add_edge(START, "initialize")
        builder.add_edge("initialize", "fox_move")  # Start with fox

        # Add conditional edges for game termination
        builder.add_conditional_edges(
            "fox_move",
            should_continue,
            {"continue": "analyze_fox", "game_over": "game_over"},
        )
        builder.add_edge("analyze_fox", "geese_move")

        builder.add_conditional_edges(
            "geese_move",
            should_continue,
            {"continue": "analyze_geese", "game_over": "game_over"},
        )
        builder.add_edge("analyze_geese", "fox_move")  # Back to fox for next turn

        # Build the graph
        self.graph = builder.build()

    def run_game(self, visualize: bool = True) -> dict[str, Any]:
        """Run the full Fox and Geese game, optionally visualizing each step.

        Args:
            visualize (bool): Whether to visualize the game state.

        Returns:
            Dict[str, Any]: Final game state after completion.
        """
        # Initialize game state
        initial_state = self.state_manager.initialize()

        # Run the game
        game_state = self.stream(initial_state, stream_mode="values")

        # Visualize the game if requested
        if visualize:
            for state in game_state:
                self.visualize_state(state)
            return state  # Final state
        return super().run(initial_state)
