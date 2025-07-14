#!/usr/bin/env python3
"""
Haive Games Examples

This file demonstrates comprehensive usage of the Haive Games framework,
including quick starts, tournaments, custom games, and advanced patterns.
"""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

# Import various game implementations
from haive.games.chess import ChessAgent, ChessConfig
from haive.games.poker import PokerAgent, PokerConfig
from haive.games.tic_tac_toe import TicTacToeAgent, TicTacToeConfig
from haive.games.wordle import WordleAgent, WordleConfig


def example_quick_game():
    """Example 1: Quick game setup - Tic Tac Toe."""
    print("=== Example 1: Quick Tic Tac Toe Game ===\n")

    # Simple configuration
    config = TicTacToeConfig(
        player_names=["Alice", "Bob"],
        llm_config=AugLLMConfig(
            temperature=0.3,
            system_message="You are playing Tic Tac Toe. Think strategically!",
        ),
    )

    # Create and run game
    game = TicTacToeAgent(config)
    result = game.run()

    # Display results
    print(f"Winner: {result.winner}")
    print(f"Total moves: {len(result.moves)}")
    print(f"Final board:\n{result.final_board}")


def example_advanced_chess():
    """Example 2: Advanced game with custom engines - Chess."""
    print("\n\n=== Example 2: Advanced Chess Game ===\n")

    # Create different player personalities
    aggressive_engine = AugLLMConfig(
        name="aggressive_player",
        temperature=0.7,
        system_message="""You are an aggressive chess player. 
        Prioritize attacks, sacrifices for position, and king safety threats.
        Always look for tactical opportunities.""",
    )

    defensive_engine = AugLLMConfig(
        name="defensive_player",
        temperature=0.2,
        system_message="""You are a defensive chess player.
        Prioritize king safety, pawn structure, and positional advantages.
        Avoid risky moves unless forced.""",
    )

    # Configure game
    config = ChessConfig(
        white_engine=aggressive_engine,
        black_engine=defensive_engine,
        time_limit=300,  # 5 minutes per player
        enable_analysis=True,
    )

    # Run game
    game = ChessAgent(config)
    result = game.run()

    # Analyze game
    print(f"Winner: {result.winner}")
    print(f"Game length: {result.total_moves} moves")
    print(f"Opening: {result.opening_name}")
    print(f"Key moments: {result.critical_positions}")


async def example_poker_tournament():
    """Example 3: Multi-player tournament - Poker."""
    print("\n\n=== Example 3: Poker Tournament ===\n")

    # Create player configurations
    players = []
    for i, style in enumerate(["tight", "loose", "aggressive", "balanced"]):
        engine = AugLLMConfig(
            name=f"player_{i}",
            temperature=0.4,
            system_message=f"""You are a {style} poker player.
            {'Fold often, play premium hands' if style == 'tight' else
             'Play many hands, see flops' if style == 'loose' else
             'Bet and raise frequently' if style == 'aggressive' else
             'Adapt to opponents and situations'}""",
        )
        players.append(
            {
                "name": f"Player_{style.title()}",
                "engine": engine,
                "starting_chips": 10000,
            }
        )

    # Tournament configuration
    config = PokerConfig(
        players=players,
        small_blind=50,
        big_blind=100,
        blind_increase_interval=10,  # Hands
        enable_all_in=True,
        show_probabilities=True,
    )

    # Run tournament
    game = PokerAgent(config)
    result = await game.arun()

    # Display results
    print("\nTournament Results:")
    for i, player_result in enumerate(result.final_standings):
        print(f"{i+1}. {player_result.name}: ${player_result.chips}")

    print(f"\nTotal hands played: {result.total_hands}")
    print(f"Biggest pot: ${result.biggest_pot}")


def example_custom_game():
    """Example 4: Creating a custom game - Number Guessing."""
    print("\n\n=== Example 4: Custom Number Guessing Game ===\n")

    from haive.games.framework import GameAgent, GameConfig, GameState, GameStateManager

    # Define custom game state
    class NumberGameState(GameState):
        target_number: int = Field(default=0)
        guesses: List[int] = Field(default_factory=list)
        hints: List[str] = Field(default_factory=list)
        found: bool = Field(default=False)

    # Define configuration
    class NumberGameConfig(GameConfig):
        min_number: int = Field(default=1)
        max_number: int = Field(default=100)
        max_guesses: int = Field(default=7)

    # Create state manager
    class NumberGameStateManager(GameStateManager):
        def __init__(self, config: NumberGameConfig):
            super().__init__(config)
            import random

            self.target = random.randint(config.min_number, config.max_number)

        def initialize_state(self) -> NumberGameState:
            return NumberGameState(target_number=self.target)

        def is_game_over(self, state: NumberGameState) -> bool:
            return state.found or len(state.guesses) >= self.config.max_guesses

        def process_guess(self, state: NumberGameState, guess: int) -> NumberGameState:
            state.guesses.append(guess)

            if guess == self.target:
                state.found = True
                state.hints.append("Correct! You found the number!")
            elif guess < self.target:
                state.hints.append(f"{guess} is too low")
            else:
                state.hints.append(f"{guess} is too high")

            return state

        def get_valid_moves(self, state: NumberGameState) -> List[int]:
            return list(range(self.config.min_number, self.config.max_number + 1))

    # Create game agent
    class NumberGameAgent(GameAgent):
        def __init__(self, config: NumberGameConfig):
            super().__init__(config)
            self.state_manager = NumberGameStateManager(config)
            self.engine = AugLLMConfig(
                temperature=0.3,
                system_message="""You are playing a number guessing game.
                Use the hints to narrow down the target number.
                Be strategic about your guesses.""",
            )

        def run(self):
            state = self.state_manager.initialize_state()

            while not self.state_manager.is_game_over(state):
                # Get hint for agent
                hint = state.hints[-1] if state.hints else "No hints yet"

                # Get agent's guess (simplified - real implementation would parse response)
                import random

                if not state.guesses:
                    guess = random.randint(
                        self.config.min_number, self.config.max_number
                    )
                else:
                    # Binary search logic
                    last_guess = state.guesses[-1]
                    if "too low" in hint:
                        guess = random.randint(last_guess + 1, self.config.max_number)
                    else:
                        guess = random.randint(self.config.min_number, last_guess - 1)

                state = self.state_manager.process_guess(state, guess)
                print(f"Guess {len(state.guesses)}: {guess} - {state.hints[-1]}")

            return state

    # Play the game
    config = NumberGameConfig(max_number=50, max_guesses=6)
    game = NumberGameAgent(config)
    result = game.run()

    if result.found:
        print(
            f"\nFound the number {result.target_number} in {len(result.guesses)} guesses!"
        )
    else:
        print(f"\nFailed to find {result.target_number}. Guesses: {result.guesses}")


def example_game_evaluation():
    """Example 5: Evaluating and comparing agents."""
    print("\n\n=== Example 5: Agent Evaluation ===\n")

    # Define different agent strategies
    strategies = {
        "random": AugLLMConfig(
            temperature=1.0, system_message="Make random but valid moves."
        ),
        "minimax": AugLLMConfig(
            temperature=0.1,
            system_message="Think several moves ahead. Use minimax-like reasoning.",
        ),
        "heuristic": AugLLMConfig(
            temperature=0.3,
            system_message="Use position evaluation heuristics. Control the center.",
        ),
    }

    # Evaluate on Tic Tac Toe (quick games)
    results = {}
    for name, engine in strategies.items():
        config = TicTacToeConfig(
            player_names=["TestAgent", "Opponent"],
            player1_engine=engine,
            player2_engine=strategies["random"],  # Baseline
        )

        wins = 0
        games = 10

        for _ in range(games):
            game = TicTacToeAgent(config)
            result = game.run()
            if result.winner == "TestAgent":
                wins += 1

        results[name] = wins / games

    print("Win rates against random player:")
    for strategy, win_rate in results.items():
        print(f"  {strategy}: {win_rate:.1%}")


def example_game_visualization():
    """Example 6: Visualizing game states."""
    print("\n\n=== Example 6: Game Visualization ===\n")

    # Simple ASCII chess board visualization
    def visualize_chess_position(fen: str) -> str:
        """Convert FEN to ASCII board."""
        pieces = {
            "K": "♔",
            "Q": "♕",
            "R": "♖",
            "B": "♗",
            "N": "♘",
            "P": "♙",
            "k": "♚",
            "q": "♛",
            "r": "♜",
            "b": "♝",
            "n": "♞",
            "p": "♟",
            ".": "·",
        }

        rows = fen.split(" ")[0].split("/")
        board = []

        for row in rows:
            line = ""
            for char in row:
                if char.isdigit():
                    line += "·" * int(char)
                else:
                    line += pieces.get(char, char)
            board.append(line)

        # Add coordinates
        result = "  a b c d e f g h\n"
        for i, row in enumerate(board):
            result += f"{8-i} {' '.join(row)} {8-i}\n"
        result += "  a b c d e f g h"

        return result

    # Example position
    starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    print("Starting Chess Position:")
    print(visualize_chess_position(starting_fen))


def example_wordle_with_strategy():
    """Example 7: Single player game with strategy - Wordle."""
    print("\n\n=== Example 7: Strategic Wordle ===\n")

    # Configure with strategy hints
    config = WordleConfig(
        word_length=5,
        max_guesses=6,
        llm_config=AugLLMConfig(
            temperature=0.2,
            system_message="""You are playing Wordle. 
            Start with words containing common vowels and consonants.
            Use the feedback to eliminate possibilities.
            Green = correct position, Yellow = wrong position, Gray = not in word.""",
        ),
        starting_words_hint=["ADIEU", "ROAST", "LYNCH"],  # Strategic starting words
    )

    game = WordleAgent(config)
    result = game.run()

    print(f"Target word: {result.target_word}")
    print(f"Found in {len(result.guesses)} guesses: {result.found}")
    print("Guess progression:")
    for i, (guess, feedback) in enumerate(zip(result.guesses, result.feedback)):
        print(f"  {i+1}. {guess} -> {feedback}")


def example_game_with_observers():
    """Example 8: Games with observer pattern."""
    print("\n\n=== Example 8: Game with Observers ===\n")

    from haive.games.utils.observers import GameObserver, MoveLogger

    class CommentaryObserver(GameObserver):
        """Provide live commentary on the game."""

        def on_move(self, state, move, player):
            print(f"[Commentary] {player} plays {move}")

        def on_game_end(self, state, winner):
            print(f"[Commentary] Game over! {winner} wins!")

    class StatisticsObserver(GameObserver):
        """Track game statistics."""

        def __init__(self):
            self.move_count = 0
            self.player_moves = {}

        def on_move(self, state, move, player):
            self.move_count += 1
            self.player_moves[player] = self.player_moves.get(player, 0) + 1

        def on_game_end(self, state, winner):
            print(f"\n[Stats] Total moves: {self.move_count}")
            for player, count in self.player_moves.items():
                print(f"[Stats] {player}: {count} moves")

    # Create game with observers
    config = TicTacToeConfig(player_names=["Alice", "Bob"])
    game = TicTacToeAgent(config)

    # Add observers
    game.add_observer(CommentaryObserver())
    game.add_observer(StatisticsObserver())
    game.add_observer(MoveLogger(filename="game_log.txt"))

    # Run game
    game.run()


def example_parallel_games():
    """Example 9: Running games in parallel."""
    print("\n\n=== Example 9: Parallel Game Execution ===\n")

    async def run_game_async(game_id: int, config: TicTacToeConfig):
        """Run a single game asynchronously."""
        game = TicTacToeAgent(config)
        result = await game.arun()
        return game_id, result.winner

    async def run_parallel_tournament():
        """Run multiple games in parallel."""
        configs = []
        for i in range(10):
            config = TicTacToeConfig(
                player_names=[f"Agent_{i}_A", f"Agent_{i}_B"],
                llm_config=AugLLMConfig(temperature=0.3 + i * 0.05),
            )
            configs.append((i, config))

        # Run all games in parallel
        tasks = [run_game_async(game_id, config) for game_id, config in configs]
        results = await asyncio.gather(*tasks)

        # Summarize results
        print("Parallel Tournament Results:")
        for game_id, winner in results:
            print(f"  Game {game_id}: {winner} wins")

    # Run the tournament
    asyncio.run(run_parallel_tournament())


def example_save_and_load():
    """Example 10: Saving and loading game states."""
    print("\n\n=== Example 10: Save/Load Game States ===\n")

    import json
    from pathlib import Path

    # Start a game
    config = ChessConfig(player_names=["White", "Black"])
    game = ChessAgent(config)

    # Make a few moves
    state = game.state_manager.initialize_state()
    moves = [
        {"from": "e2", "to": "e4"},
        {"from": "e7", "to": "e5"},
        {"from": "g1", "to": "f3"},
    ]

    for move in moves:
        state = game.state_manager.process_move(state, move)

    # Save state
    save_data = {"state": state.dict(), "config": config.dict(), "move_history": moves}

    save_path = Path("chess_save.json")
    with open(save_path, "w") as f:
        json.dump(save_data, f, indent=2)

    print(f"Game saved to {save_path}")

    # Load state
    with open(save_path, "r") as f:
        loaded_data = json.load(f)

    # Restore game
    loaded_config = ChessConfig(**loaded_data["config"])
    loaded_game = ChessAgent(loaded_config)
    loaded_state = loaded_game.state_manager.state_class(**loaded_data["state"])

    print(f"Game loaded. Current turn: {loaded_state.current_player}")
    print(f"Moves played: {len(loaded_data['move_history'])}")

    # Clean up
    save_path.unlink()


def main():
    """Run all examples."""
    examples = [
        example_quick_game,
        example_advanced_chess,
        example_poker_tournament,
        example_custom_game,
        example_game_evaluation,
        example_game_visualization,
        example_wordle_with_strategy,
        example_game_with_observers,
        example_parallel_games,
        example_save_and_load,
    ]

    for example in examples:
        if asyncio.iscoroutinefunction(example):
            asyncio.run(example())
        else:
            example()
        input("\nPress Enter to continue to next example...")


if __name__ == "__main__":
    # Run specific example or all
    import sys

    if len(sys.argv) > 1:
        example_num = int(sys.argv[1]) - 1
        examples = [
            example_quick_game,
            example_advanced_chess,
            example_poker_tournament,
            example_custom_game,
            example_game_evaluation,
            example_game_visualization,
            example_wordle_with_strategy,
            example_game_with_observers,
            example_parallel_games,
            example_save_and_load,
        ]

        if 0 <= example_num < len(examples):
            example = examples[example_num]
            if asyncio.iscoroutinefunction(example):
                asyncio.run(example())
            else:
                example()
        else:
            print(f"Invalid example number. Choose 1-{len(examples)}")
    else:
        main()
