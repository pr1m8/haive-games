"""Agent core module.

This module provides agent functionality for the Haive framework.

Classes:
    WordConnectionsAgent: WordConnectionsAgent implementation.

Functions:
    setup_workflow: Setup Workflow functionality.
    play_turn: Play Turn functionality.
    should_continue: Should Continue functionality.
"""

from typing import Any

from haive.core.engine.agent.agent import register_agent
from langgraph.graph import END, START

from haive.games.framework.base import GameAgent
from haive.games.single_player.wordle.config import WordConnectionsAgentConfig
from haive.games.single_player.wordle.models import (
    WordConnectionsState,
)


@register_agent(WordConnectionsAgentConfig)
class WordConnectionsAgent(GameAgent[WordConnectionsAgentConfig]):
    """Agent for playing the Word Connections game."""

    def setup_workflow(self) -> None:
        """Set up the game workflow using the graph_builder."""
        # Add nodes to the existing graph_builder
        self.graph_builder.add_node("play_turn", self.play_turn)

        # Add edges
        self.graph_builder.add_edge(START, "play_turn")
        self.graph_builder.add_conditional_edges(
            "play_turn", self.should_continue, {True: "play_turn", False: END}
        )

        # Compile the graph (this sets self.graph internally)
        self.compile()

    def play_turn(self, state: dict[str, Any]) -> dict[str, Any]:
        """Play one turn of the game."""
        game_state = WordConnectionsState(**state)

        if game_state.game_status != "playing":
            return state

        # Display current state
        if self.config.visualize:
            print("\n" + "=" * 50)
            print(game_state.display_grid)
            print("=" * 50)

        # Format context for LLM
        context = {
            "display_grid": game_state.display_grid,
            "incorrect_guesses": (
                "\n".join(
                    [f"- {', '.join(guess)}" for guess in game_state.incorrect_guesses]
                )
                if game_state.incorrect_guesses
                else "None"
            ),
        }

        # Get guess from LLM
        response = self.config.game_engine.invoke(context)

        # Extract the guess from the response
        if hasattr(response, "words"):
            guess_words = response.words
            category = response.category
            reasoning = response.reasoning
        else:
            # Handle tool response format
            guess_words = response[0].words
            category = response[0].category
            reasoning = response[0].reasoning

        if self.config.visualize:
            print(f"\n🤔 Guess: {', '.join(guess_words)}")
            print(f"📝 Category: {category}")
            print(f"💭 Reasoning: {reasoning}")

        # Check if guess is correct
        guess_set = set(guess_words)
        correct_category = None

        for cat, words in game_state.categories.items():
            if set(words) == guess_set:
                correct_category = cat
                break

        if correct_category:
            # Correct!
            game_state.found_categories[correct_category] = guess_words
            if self.config.visualize:
                print("✅ CORRECT!")

            # Check if won
            if len(game_state.found_categories) == 4:
                game_state.game_status = "won"
                if self.config.visualize:
                    print("\n🎉 YOU WIN! All categories found!")
        else:
            # Incorrect
            game_state.incorrect_guesses.append(guess_words)
            game_state.mistakes_remaining -= 1

            if self.config.visualize:
                print(
                    f"❌ Incorrect! {game_state.mistakes_remaining} mistakes remaining"
                )

            # Check if lost
            if game_state.mistakes_remaining == 0:
                game_state.game_status = "lost"
                if self.config.visualize:
                    print("\n😔 GAME OVER!")
                    print("\nThe categories were:")
                    for cat, words in game_state.categories.items():
                        if cat not in game_state.found_categories:
                            difficulty = game_state.difficulty_map.get(cat, "")
                            emoji = {
                                "yellow": "🟨",
                                "green": "🟩",
                                "blue": "🟦",
                                "purple": "🟪",
                            }.get(difficulty, "")
                            print(f"{emoji} {cat}: {', '.join(words)}")

        return game_state.model_dump()

    def should_continue(self, state: dict[str, Any]) -> bool:
        """Check if game should continue."""
        return state["game_status"] == "playing"

    def initialize_game(self, puzzle_data: dict = None) -> WordConnectionsState:
        """Initialize a new game."""
        # Example puzzle
        if not puzzle_data:
            puzzle_data = {
                "categories": {
                    "Fine print": ["ASTERISK", "CATCH", "CONDITION", "STRINGS"],
                    "Characters with green skin": [
                        "ELPHABA",
                        "GRINCH",
                        "HULK",
                        "SHREK",
                    ],
                    "Features of the National Mall in D.C.": [
                        "CAPITOL",
                        "MALL",
                        "OBELISK",
                        "POOL",
                    ],
                    "Famous riddle-givers": [
                        "BRIDGE TROLL",
                        "MAD HATTER",
                        "RIDDLER",
                        "SPHINX",
                    ],
                },
                "difficulties": {
                    "Fine print": "yellow",
                    "Characters with green skin": "green",
                    "Features of the National Mall in D.C.": "blue",
                    "Famous riddle-givers": "purple",
                },
            }

        # Create grid (shuffle all words)
        import random

        all_words = []
        for words in puzzle_data["categories"].values():
            all_words.extend(words)
        random.shuffle(all_words)

        return WordConnectionsState(
            grid=all_words,
            categories=puzzle_data["categories"],
            difficulty_map=puzzle_data["difficulties"],
            found_categories={},
            incorrect_guesses=[],
            mistakes_remaining=4,
            game_status="playing",
        )

    def setup_routing(self) -> None:
        """Set up the routing for the game."""
        # Build routing map - CRITICAL FIX: ValidationNodeConfig returns Send objects, not strings
        console.print("\n[bold yellow]Building routing map...[/bold yellow]")

        # IMPORTANT: ValidationNodeConfig primarily returns Send objects for routing
        # The routing_map only handles edge cases where strings are returned
        routing_map = {
            "has_errors": "agent_node"  # Only for fallback error cases
            # Removed 'tool_node' and 'parse_output' - these are handled via Send objects
        }

        console.print(f"  [cyan]Routing map (for string returns): {routing_map}[/cyan]")
        console.print(
            "  [green]✓ Valid tools will be routed via Send objects (not routing map)[/green]"
        )

        # Show routing explanation
        from rich.table import Table

        routing_table = Table(
            title="ValidationNodeConfig Routing Behavior",
            show_header=True,
            header_style="bold magenta",
        )
        routing_table.add_column("Scenario", style="cyan")
        routing_table.add_column("Return Type", style="yellow")
        routing_table.add_column("Destination", style="green")
        routing_table.add_column("Description", style="dim")

        routing_table.add_row(
            "Valid LangChain tools",
            "Send objects",
            "tool_node",
            "Direct routing via Send",
        )
        routing_table.add_row(
            "Valid Pydantic tools",
            "Send objects",
            "parse_output",
            "Direct routing via Send",
        )
        routing_table.add_row(
            "All tools invalid", "Send objects", "agent_node", "Error routing via Send"
        )
        routing_table.add_row(
            "Mixed valid/invalid",
            "List[Send]",
            "Multiple nodes",
            "Multiple Send objects",
        )
        routing_table.add_row(
            "Fallback errors", "String 'has_errors'", "agent_node", "Uses routing_map"
        )

        console.print(routing_table)

        console.print(
            "\n[bold green]KEY INSIGHT: ValidationNodeConfig handles routing internally via Send objects![/bold green]"
        )
        console.print(
            "[yellow]The routing_map is only a fallback for edge cases[/yellow]"
        )

        # Create validation node config with proper tool routing information
        validation_config = ValidationNodeConfig(
            name="val_node",
            schemas=schemas,
            tools=self.engine.tools,  # Pass the tools for routing decisions
            tool_routes=getattr(
                self.engine, "tool_routes", {}
            ),  # Pass tool_routes for proper routing
            agent_node="agent_node",  # Where to send validation errors
            tool_node=(
                "tool_node" if self.has_tool_node else None
            ),  # Where to send LangChain tools
            parser_node=(
                "parse_output" if self.has_parser_node else None
            ),  # Where to send Pydantic tools
        )

        console.print(
            "\n[cyan]Created ValidationNodeConfig with proper routing:[/cyan]"
        )
        console.print(f"  schemas: {len(schemas)} items")
        console.print(f"  tools: {len(validation_config.tools)} items")
        console.print(f"  tool_routes: {validation_config.tool_routes}")
        console.print(f"  agent_node: {validation_config.agent_node}")
        console.print(f"  tool_node: {validation_config.tool_node}")
        console.print(f"  parser_node: {validation_config.parser_node}")
