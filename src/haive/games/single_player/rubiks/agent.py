"""Rubik's Cube agent implementation."""

import logging

from haive.core.engine.agent.agent import Agent, register_agent
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END
from langgraph.types import Command

from haive.games.single_player.rubiks.config import RubiksCubeConfig
from haive.games.single_player.rubiks.cube_ops import CubeOperations
from haive.games.single_player.rubiks.engines import build_rubiks_engines
from haive.games.single_player.rubiks.state import RubiksCubeState

logger = logging.getLogger(__name__)


@register_agent(RubiksCubeConfig)
class RubiksCubeAgent(Agent[RubiksCubeConfig]):
    """Rubik's Cube game agent."""

    def __init__(self, config: RubiksCubeConfig):
        """Initialize the chess agent."""
        super().__init__(config)
        self.engines = {}

        # Build engines
        engine_configs = build_rubiks_engines()

        # Create engines
        for key, engine_config in engine_configs.items():
            self.engines[key] = engine_config.create_runnable()
            if self.engines[key] is None:
                raise ValueError(f"Failed to create engine for {key}")

    def setup_workflow(self):
        """Set up the workflow graph."""
        # Add nodes
        self.graph.add_node("scramble", self.scramble_cube)
        self.graph.add_node("player_turn", self.handle_player_turn)
        self.graph.add_node("process_move", self.process_move)
        self.graph.add_node("check_solved", self.check_solved)
        self.graph.add_node("game_over", self.game_over)

        # Set entry point
        self.graph.set_entry_point("scramble")

        # Add edges
        self.graph.add_edge("scramble", "player_turn")

        # Player turn routing
        self.graph.add_conditional_edges(
            "player_turn",
            self.route_player_action,
            {
                "move": "process_move",
                "reset": "scramble",
                "quit": "game_over",
                "wait": "player_turn",
            },
        )

        # After move processing
        self.graph.add_edge("process_move", "check_solved")

        # Check if solved
        self.graph.add_conditional_edges(
            "check_solved",
            self.route_game_status,
            {"continue": "player_turn", "solved": "game_over"},
        )

        self.graph.add_edge("game_over", END)

    def scramble_cube(self, state: RubiksCubeState) -> Command:
        """Scramble the cube based on difficulty."""
        print(f"\n🎲 Scrambling cube ({self.config.difficulty} difficulty)...")

        # Get number of moves for difficulty
        num_moves = self.config.scramble_moves_count[self.config.difficulty]

        # Scramble the cube
        scrambled_state, scramble_moves = CubeOperations.scramble_cube(num_moves)

        # Create welcome message
        temp_state = RubiksCubeState(cube_state=scrambled_state)
        welcome_msg = AIMessage(
            content=f"""🧊 Welcome to Rubik's Cube!

I've scrambled the cube with {num_moves} moves ({self.config.difficulty} difficulty).

Your goal is to make all faces show a single color each.

Available moves:
- F, B, U, D, L, R (clockwise)
- F', B', U', D', L', R' (counter-clockwise)
- F2, B2, U2, D2, L2, R2 (180 degrees)

Commands:
- Type any move (e.g., "F", "R'", "U2")
- "reset" for a new game
- "quit" to exit

Current state:
{temp_state.get_cube_net()}

What's your first move?"""
        )

        return Command(
            update={
                "cube_state": scrambled_state,
                "scramble_moves": scramble_moves,
                "game_status": "playing",
                "move_count": 0,
                "move_history": [],
                "messages": [welcome_msg],
            }
        )

    def handle_player_turn(self, state: RubiksCubeState) -> Command:
        """Handle player input."""
        # Check if we have a player message
        if not state.messages:
            return Command(update={"last_action": "wait"})

        # Find the last human message
        player_message = None
        for msg in reversed(state.messages):
            if isinstance(msg, HumanMessage):
                player_message = msg.content
                break

        if not player_message:
            return Command(update={"last_action": "wait"})

        # Prepare context for player engine
        recent_moves = state.move_history[-5:] if state.move_history else []
        context = {
            "cube_net": state.get_cube_net(),
            "solve_percentage": state.solve_percentage,
            "faces_solved": state.faces_solved,
            "move_count": state.move_count,
            "recent_moves": ", ".join(recent_moves) if recent_moves else "None",
            "message": player_message,
        }

        try:
            # Get player action
            action = self.engines["playef"].invoke(context)

            # Store action for routing
            return Command(
                update={
                    "last_action": action.action_type,
                    "last_move": action.move,
                    "error_message": None,
                }
            )

        except Exception as e:
            error_msg = "I didn't understand that. Try a move like 'F' or 'R2', or type 'reset' for a new game."
            return Command(
                update={
                    "messages": [AIMessage(content=error_msg)],
                    "error_message": str(e),
                    "last_action": "wait",
                }
            )

    def process_move(self, state: RubiksCubeState) -> Command:
        """Process a cube move."""
        move = state.last_move
        if not move:
            return Command(update={"error_message": "No move specified"})

        try:
            # Apply the move
            new_cube_state = CubeOperations.apply_move(state.cube_state, move)

            # Create new state to check progress
            temp_state = RubiksCubeState(cube_state=new_cube_state)

            # Create response
            response = AIMessage(
                content=f"""✅ Applied move: {move}

Current state:
{temp_state.get_cube_net()}

Progress: {temp_state.solve_percentage:.1f}% complete ({temp_state.faces_solved}/6 faces solved)
Moves: {state.move_count + 1}"""
            )

            return Command(
                update={
                    "cube_state": new_cube_state,
                    "move_history": [move],  # Will be appended via reducer
                    "move_count": state.move_count + 1,
                    "messages": [response],
                }
            )

        except Exception as e:
            error_response = AIMessage(content=f"❌ Error applying move {move}: {e!s}")
            return Command(
                update={"messages": [error_response], "error_message": str(e)}
            )

    def check_solved(self, state: RubiksCubeState) -> Command:
        """Check if the cube is solved."""
        if self.config.auto_detect_solve and state.is_solved:
            return Command(
                update={
                    "game_status": "solved",
                    "messages": [
                        AIMessage(
                            content=f"""
🎉 CONGRATULATIONS! 🎉

You solved the Rubik's Cube in {state.move_count} moves!

Difficulty: {self.config.difficulty}
Move sequence: {' '.join(state.move_history)}

Type 'reset' for a new game or 'quit' to exit."""
                        )
                    ],
                }
            )

        return Command(update={})

    def game_over(self, state: RubiksCubeState) -> Command:
        """Handle game over."""
        if state.game_status == "solved":
            final_msg = "Thanks for playing! You solved the cube! 🏆"
        else:
            final_msg = "Thanks for playing! See you next time! 👋"

        return Command(update={"messages": [AIMessage(content=final_msg)]})

    def route_player_action(self, state: RubiksCubeState) -> str:
        """Route based on player action."""
        action = state.last_action
        if action in ["move", "reset", "quit"]:
            return action
        return "wait"

    def route_game_status(self, state: RubiksCubeState) -> str:
        """Route based on game status."""
        if state.game_status == "solved":
            return "solved"
        return "continue"
