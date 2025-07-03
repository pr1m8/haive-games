"""Tic Tac Toe Agent class for coordinating gameplay using LLM-driven decision-making.

This module defines the agent responsible for initializing the game,
coordinating turns, running inference engines, and maintaining the gameplay loop.
"""

import time
from typing import Any

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.graph import END
from langgraph.types import Command

from haive.games.framework.base.agent import GameAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.state import TicTacToeState
from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager


@register_agent(TicTacToeConfig)
class TicTacToeAgent(GameAgent[TicTacToeConfig]):
    """Agent for playing Tic Tac Toe using structured game flow and LLM inference."""

    def __init__(self, config: TicTacToeConfig = TicTacToeConfig()):
        """Initialize the Tic Tac Toe agent."""
        self.state_manager = TicTacToeStateManager
        super().__init__(config)

    def initialize_game(self, state: dict[str, Any]) -> Command:
        """Initialize a new Tic Tac Toe game."""
        print("[DEBUG] initialize_game called")

        game_state = self.state_manager.initialize(
            first_player=self.config.first_player,
            player_X=self.config.player_X,
            player_O=self.config.player_O,
        )

        print("[DEBUG] Game state initialized:")
        print(f"[DEBUG] Turn: {game_state.turn}")
        print(f"[DEBUG] Status: {game_state.game_status}")
        print(f"[DEBUG] Board: {game_state.board}")

        # Return only the essential fields for initialization
        return Command(
            update={
                "board": game_state.board,
                "turn": game_state.turn,
                "game_status": game_state.game_status,
                "player_X": game_state.player_X,
                "player_O": game_state.player_O,
                "winner": game_state.winner,
                "error_message": game_state.error_message,
                # Don't include lists that might cause issues
            },
            goto="make_move",
        )

    def prepare_move_context(self, state: TicTacToeState) -> dict[str, Any]:
        """Prepare structured context for generating a move."""
        legal_moves = self.state_manager.get_legal_moves(state)
        formatted_legal_moves = ", ".join(
            [f"({move.row}, {move.col})" for move in legal_moves]
        )

        current_player = (
            "player1"
            if (state.turn == "X" and state.player_X == "player1")
            or (state.turn == "O" and state.player_O == "player1")
            else "player2"
        )

        player_analysis = "No previous analysis available."
        if current_player == "player1" and state.player1_analysis:
            player_analysis = state.player1_analysis[-1]
        elif current_player == "player2" and state.player2_analysis:
            player_analysis = state.player2_analysis[-1]

        return {
            "board_string": state.board_string,
            "current_player": state.turn,
            "legal_moves": formatted_legal_moves,
            "player_analysis": player_analysis,
        }

    def prepare_analysis_context(
        self, state: TicTacToeState, symbol: str
    ) -> dict[str, Any]:
        """Prepare structured context for analyzing the game board."""
        return {
            "board_string": state.board_string,
            "player_symbol": symbol,
            "opponent_symbol": "O" if symbol == "X" else "X",
        }

    def make_move(self, state) -> Command:
        """Make a move for the current player."""
        print(f"[DEBUG] make_move called with state type: {type(state)}")

        # Convert dict to TicTacToeState if needed
        if isinstance(state, dict):
            try:
                game_state = TicTacToeState(**state)
                print("[DEBUG] Converted dict to TicTacToeState successfully")
                print(
                    f"[DEBUG] Turn: {game_state.turn}, Status: {game_state.game_status}"
                )
                print(f"[DEBUG] Board: {game_state.board}")
            except Exception as e:
                print(f"[DEBUG] State conversion failed: {e}")
                return Command(
                    update={"error_message": f"State conversion failed: {e!s}"},
                    goto=END,
                )
        else:
            game_state = state
            print("[DEBUG] Using state directly")

        if game_state.game_status != "ongoing":
            print(f"[DEBUG] Game not ongoing, status: {game_state.game_status}")
            return Command(update={}, goto=END)

        # Determine which engine to use based on current player
        if game_state.turn == "X":
            engine = self.engines["X_player"]
            engine_name = "X_player"
        else:
            engine = self.engines["O_player"]
            engine_name = "O_player"

        print(f"[DEBUG] Using engine: {engine_name} for turn: {game_state.turn}")

        try:
            context = self.prepare_move_context(game_state)
            print(f"[DEBUG] Prepared context keys: {list(context.keys())}")

            print("[DEBUG] Invoking engine...")
            move = engine.invoke(context)
            print(f"[DEBUG] Engine returned move: {move}")
            print(f"[DEBUG] Move type: {type(move)}")

            print("[DEBUG] Applying move...")
            new_state = self.state_manager.apply_move(game_state, move)
            print("[DEBUG] Move applied successfully")
            print(f"[DEBUG] New board: {new_state.board}")
            print(f"[DEBUG] New turn: {new_state.turn}")
            print(f"[DEBUG] New status: {new_state.game_status}")

            # Determine next node
            if new_state.game_status != "ongoing":
                next_node = END
            elif self.config.enable_analysis:
                next_node = "analyze"
            else:
                next_node = "make_move"

            print(f"[DEBUG] Next node: {next_node}")

            # Create targeted updates that work with our reducers
            update = {
                "board": new_state.board,  # Replace board
                "turn": new_state.turn,  # Replace turn
                "game_status": new_state.game_status,  # Replace status
                "winner": new_state.winner,  # Replace winner
                "move_history": [move],  # Add to move history
            }

            print(f"[DEBUG] Update dict: {update}")

            return Command(update=update, goto=next_node)

        except Exception as e:
            print(f"[DEBUG] Error in make_move: {e}")
            import traceback

            traceback.print_exc()
            return Command(update={"error_message": f"Move failed: {e!s}"}, goto=END)

    def analyze_position(self, state) -> Command:
        """Analyze the current position for the player who just moved."""
        print("[DEBUG] analyze_position called")

        # Convert dict to TicTacToeState if needed
        if isinstance(state, dict):
            try:
                game_state = TicTacToeState(**state)
            except Exception as e:
                return Command(
                    update={"error_message": f"State conversion failed: {e!s}"},
                    goto=END,
                )
        else:
            game_state = state

        if not self.config.enable_analysis or game_state.game_status != "ongoing":
            return Command(
                update={},
                goto="make_move" if game_state.game_status == "ongoing" else END,
            )

        # Analyze for the player who just moved (opposite of current turn)
        last_player = "O" if game_state.turn == "X" else "X"

        try:
            if last_player == "X":
                engine = self.engines["X_analyzer"]
                player_name = game_state.player_X
            else:
                engine = self.engines["O_analyzer"]
                player_name = game_state.player_O

            context = self.prepare_analysis_context(game_state, last_player)
            analysis = engine.invoke(context)

            print(f"[DEBUG] Analysis completed for {player_name}")

            # Determine next step
            next_node = "make_move" if game_state.game_status == "ongoing" else END

            # Add analysis to appropriate player using the accumulating reducer
            update = {}
            if player_name == "player1":
                update["player1_analysis"] = [analysis]
            else:
                update["player2_analysis"] = [analysis]

            return Command(update=update, goto=next_node)

        except Exception as e:
            print(f"[DEBUG] Error in analyze_position: {e}")
            return Command(
                update={"error_message": f"Analysis failed: {e!s}"},
                goto="make_move" if game_state.game_status == "ongoing" else END,
            )

    def visualize_state(self, state: TicTacToeState) -> None:
        """Visualize the current game state (for fallback use)."""
        if not self.config.visualize:
            return

        try:
            game_state = TicTacToeState(**state)
            print("\n" + "=" * 50)
            print(f"🎮 Game Status: {game_state.game_status}")
            if game_state.game_status == "ongoing":
                current_player = (
                    game_state.player_X
                    if game_state.turn == "X"
                    else game_state.player_O
                )
                print(f"Current Turn: {game_state.turn} ({current_player})")
            print("=" * 50)
            print(game_state.board_string)

            if game_state.move_history:
                last_move = game_state.move_history[-1]
                print(f"\n📝 Last Move: {last_move}")

            if game_state.error_message:
                print(f"\n⚠️ Error: {game_state.error_message}")

            time.sleep(0.5)

        except Exception as e:
            print(f"Error in visualize_state: {e}")

    def setup_workflow(self):
        """Set up the game workflow graph."""
        builder = DynamicGraph(state_schema=self.state_schema)

        # Add nodes
        builder.add_node("initialize", self.initialize_game)
        builder.add_node("make_move", self.make_move)
        builder.add_node("analyze", self.analyze_position)

        # Set entry point
        builder.set_entry_point("initialize")

        # Add explicit edges
        builder.add_edge("initialize", "make_move")
        builder.add_edge("make_move", "make_move")  # Self-loop for continuous play
        builder.add_edge("make_move", "analyze")  # For when analysis is enabled
        builder.add_edge("analyze", "make_move")  # Back to move after analysis

        self.graph = builder.build()

    def run_game(self, visualize: bool = True, debug: bool = False):
        """Run the full Tic Tac Toe game loop."""
        initial_state = TicTacToeStateManager.initialize(
            first_player=self.config.first_player,
            player_X=self.config.player_X,
            player_O=self.config.player_O,
        )

        # Run the game
        if visualize:
            for step in self.app.stream(
                initial_state,
                stream_mode="values",
                debug=debug,
                config=self.runnable_config,
            ):
                self.visualize_state(step)
                time.sleep(1)
            return step  # Final state

        return super().run(initial_state, debug=debug)
