Getting Started
===============

Welcome to haive-games! This guide will help you get up and running with the Haive AI Gaming Research Platform.

Installation
------------

Install haive-games using pip:

.. code-block:: bash

   pip install haive-games

Or with Poetry:

.. code-block:: bash

   poetry add haive-games

Quick Start Example
-------------------

Here's a simple example to get you started with haive-games:

.. code-block:: python

   from haive.games.chess import ChessAgent
   from haive.games.poker import PokerAgent
   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Configure the AI engine
   config = AugLLMConfig(
       model="gpt-4",
       temperature=0.7,
       system_message="You are a strategic game player."
   )
   
   # Create game agents
   chess_ai = ChessAgent(
       name="ChessBot",
       engine=config,
       difficulty="intermediate"
   )
   
   poker_ai = PokerAgent(
       name="PokerBot",
       engine=config,
       style="aggressive"
   )
   
   print("Ready to play games with haive-games!")

Core Concepts
-------------

Game State Management
~~~~~~~~~~~~~~~~~~~~~

haive-games uses state schemas to manage game states and AI agent data:

.. code-block:: python

   from haive.games.common import GameState
   from pydantic import Field
   from typing import List, Dict, Any
   
   class ChessGameState(GameState):
       """Chess game state tracking."""
       board: List[List[str]] = Field(default_factory=list)
       moves_history: List[str] = Field(default_factory=list)
       current_player: str = Field(default="white")
       
   # Create and use game state
   game = ChessGameState()
   game.moves_history.append("e2-e4")

AI Agent Configuration
~~~~~~~~~~~~~~~~~~~~~~

Configure AI agents for different playing styles and strategies:

.. code-block:: python

   from haive.games.chess import ChessAgent
   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Basic chess agent
   chess_ai = ChessAgent(
       name="BasicBot",
       engine=AugLLMConfig(model="gpt-4"),
       difficulty="beginner"
   )
   
   # Advanced strategic agent
   strategic_ai = ChessAgent(
       name="StrategicBot",
       engine=AugLLMConfig(
           model="gpt-4",
           temperature=0.3,
           system_message="You are a chess grandmaster."
       ),
       difficulty="expert",
       opening_book=True,
       endgame_database=True
   )

Tournament System
~~~~~~~~~~~~~~~~~

Run tournaments between different AI agents:

.. code-block:: python

   from haive.games.tournament import Tournament
   from haive.games.chess import ChessAgent
   from haive.games.go import GoAgent
   
   # Create tournament
   tournament = Tournament(name="AI Championship")
   
   # Add participants
   tournament.add_agent(ChessAgent(name="Bot1"))
   tournament.add_agent(ChessAgent(name="Bot2"))
   tournament.add_agent(GoAgent(name="Bot3"))
   
   # Run tournament
   results = tournament.run(
       games_per_match=10,
       time_control="5+0"
   )
   
   # Get rankings
   rankings = tournament.get_rankings()

Next Steps
----------

1. **Explore Game Categories**: Check out all :doc:`game_categories`
2. **Social Psychology Games**: Learn about :doc:`social_psychology_games`
3. **Tournament System**: Master the :doc:`tournament_system`
4. **Join the Community**: Visit our `GitHub repository <https://github.com/haive-ai/haive>`_

Common Patterns
---------------

Playing a Chess Game
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.games.chess import ChessGame, ChessAgent
   
   # Create game and agents
   game = ChessGame()
   white_ai = ChessAgent(name="White", color="white")
   black_ai = ChessAgent(name="Black", color="black")
   
   # Play game
   while not game.is_over():
       if game.current_player == "white":
           move = white_ai.get_move(game.board)
       else:
           move = black_ai.get_move(game.board)
       
       game.make_move(move)
   
   print(f"Winner: {game.get_winner()}")

Social Deduction Game
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.games.among_us import AmongUsGame, AmongUsAgent
   
   # Create social deduction game
   game = AmongUsGame(num_players=10, num_impostors=2)
   
   # Create AI agents with personalities
   agents = [
       AmongUsAgent(name=f"Player{i}", personality="suspicious")
       for i in range(10)
   ]
   
   # Run game with discussion phases
   game.start()
   while not game.is_over():
       # Task phase
       game.run_task_phase()
       
       # Discussion phase
       accusations = game.run_discussion(agents)
       
       # Voting phase
       ejected = game.run_voting(accusations)
   
   print(f"Winners: {game.get_winners()}")

Research Analytics
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.games.analytics import GameAnalyzer
   from haive.games.poker import PokerGame
   
   # Analyze game behavior
   analyzer = GameAnalyzer()
   
   # Run multiple games
   for i in range(100):
       game = PokerGame(num_players=6)
       game.play_full_game()
       analyzer.add_game(game)
   
   # Get insights
   metrics = analyzer.get_metrics()
   print(f"Bluff success rate: {metrics['bluff_success_rate']}")
   print(f"Average pot size: {metrics['avg_pot_size']}")

Best Practices
--------------

1. **Choose appropriate difficulty** - Match AI difficulty to research needs
2. **Configure personality traits** - Use personality profiles for social games
3. **Collect metrics** - Track performance data for analysis
4. **Test different strategies** - Compare AI behaviors across games
5. **Use tournament system** - Benchmark different AI implementations

Game Categories
---------------

**Board Games**
   Chess, Go, Checkers, Reversi, Connect 4, Tic-Tac-Toe

**Card Games**
   Poker, Blackjack, UNO, Hold'em

**Social Psychology**
   Among Us, Mafia, Clue, Debate

**Strategy Games**
   Risk, Monopoly, Battleship

**Puzzle Games**
   Sudoku, Wordle, Mastermind, Nim

Getting Help
------------

- **Documentation**: Explore our comprehensive guides
- **GitHub Issues**: Report bugs or request new games
- **Examples**: Check the examples/ directory
- **API Reference**: See the complete :doc:`API documentation <autoapi/haive/index>`