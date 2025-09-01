Haive Games Overview
====================

.. module:: haive.games

Welcome to **haive-games**, the comprehensive AI gaming research platform! 🎮

.. note::
   
   Looking for other Haive packages? The complete framework documentation will be available at the `Haive root documentation <https://github.com/pr1m8/haive>`_.

.. grid:: 2
   :gutter: 3
   :margin: 0
   :padding: 0

   .. grid-item-card:: 🎯 **Strategy Games**
      :link: game_categories
      :link-type: doc
      :class-card: sd-border-2

      Chess, Go, Checkers, and more with advanced AI strategies and planning algorithms.

      .. button-ref:: game_categories
         :color: primary
         :outline:
         :expand:

         Explore Games →

   .. grid-item-card:: 🧠 **Social Psychology**
      :link: social_psychology_games
      :link-type: doc
      :class-card: sd-border-2

      Among Us, Mafia, and Clue with deception detection and social reasoning.

      .. button-ref:: social_psychology_games
         :color: primary
         :outline:
         :expand:

         View Social Games →

   .. grid-item-card:: 🎰 **Card & Probability**
      :link: game_categories
      :link-type: doc
      :class-card: sd-border-2

      Poker, Blackjack, and UNO with sophisticated probability calculations.

      .. button-ref:: game_categories
         :color: primary
         :outline:
         :expand:

         Card Games →

   .. grid-item-card:: 🏆 **Tournament System**
      :link: tournament_system
      :link-type: doc
      :class-card: sd-border-2

      Multi-provider tournaments with cross-game performance analytics.

      .. button-ref:: tournament_system
         :color: primary
         :outline:
         :expand:

         Tournament Docs →

Quick Start 🏃‍♂️
--------------

.. tab-set::

   .. tab-item:: Installation

      .. code-block:: bash

         # Install haive-games
         pip install haive-games

         # Or with Poetry (recommended)
         poetry add haive-games

   .. tab-item:: Basic Usage

      .. code-block:: python

         from haive.games.chess import ChessAgent
         from haive.core.engine import AugLLMConfig

         # Configure your AI
         config = AugLLMConfig(
             model="gpt-4",
             temperature=0.7
         )

         # Create game agent
         chess_ai = ChessAgent(
             name="ChessBot",
             engine=config
         )

   .. tab-item:: Advanced

      .. code-block:: python

         from haive.games.tournament import Tournament
         from haive.games.among_us import AmongUsAgent
         from haive.games.poker import PokerAgent

         # Create tournament
         tournament = Tournament()
         tournament.add_agent(AmongUsAgent(name="SocialBot"))
         tournament.add_agent(PokerAgent(name="BluffMaster"))
         tournament.run()

Game Categories 🎮
-----------------

.. grid:: 3
   :gutter: 2

   .. grid-item::

      .. card:: **Board Games** ♟️
         :class-card: sd-bg-light

         - :class:`~haive.games.chess.ChessAgent`
         - :class:`~haive.games.go.GoAgent`
         - :class:`~haive.games.checkers.CheckersAgent`
         - :class:`~haive.games.reversi.ReversiAgent`

   .. grid-item::

      .. card:: **Social Games** 🕵️
         :class-card: sd-bg-light

         - :class:`~haive.games.among_us.AmongUsAgent`
         - :class:`~haive.games.mafia.MafiaAgent`
         - :class:`~haive.games.clue.ClueAgent`
         - :class:`~haive.games.debate.DebateAgent`

   .. grid-item::

      .. card:: **Card Games** 🃏
         :class-card: sd-bg-light

         - :class:`~haive.games.poker.PokerAgent`
         - :class:`~haive.games.blackjack.BlackjackAgent`
         - :class:`~haive.games.uno.UNOAgent`
         - :class:`~haive.games.holdem.HoldEmAgent`

Architecture Overview 🏗️
----------------------

.. mermaid::

   graph TB
      A[Application Layer] --> B[haive-games]
      B --> C[Game Engines]
      B --> D[AI Agents]
      B --> E[Tournament System]
      B --> F[Analytics]
      
      C --> G[Board Games]
      C --> H[Card Games]
      C --> I[Social Games]
      
      D --> J[Strategy AI]
      D --> K[Probability AI]
      D --> L[Social AI]
      
      E --> M[Multi-Provider]
      E --> N[Cross-Game]
      
      F --> O[Performance Metrics]
      F --> P[Research Data]

      style B fill:#2563eb,stroke:#1d4ed8,color:#fff
      style C fill:#60a5fa,stroke:#3b82f6
      style D fill:#60a5fa,stroke:#3b82f6
      style E fill:#60a5fa,stroke:#3b82f6
      style F fill:#60a5fa,stroke:#3b82f6

Key Features ✨
--------------

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **🎮 19+ Game Implementations**
      :class-card: sd-border-1

      Comprehensive collection of board games, card games, social deduction games, and puzzles.

   .. grid-item-card:: **🤖 Advanced AI Strategies**
      :class-card: sd-border-1

      Sophisticated AI agents with game-specific strategies and learning capabilities.

   .. grid-item-card:: **🏆 Tournament System**
      :class-card: sd-border-1

      Multi-provider tournaments with cross-game rankings and performance analytics.

   .. grid-item-card:: **📊 Research Analytics**
      :class-card: sd-border-1

      Detailed performance metrics, behavioral analysis, and research-grade data collection.

   .. grid-item-card:: **🧠 Social Psychology**
      :class-card: sd-border-1

      Deception detection, trust modeling, and social reasoning in multiplayer games.

   .. grid-item-card:: **⚡ High Performance**
      :class-card: sd-border-1

      Optimized for real-time gameplay with async support and efficient state management.

Integration Examples 🔗
--------------------

.. tab-set::

   .. tab-item:: With haive-agents

      .. code-block:: python

         from haive.games.chess import ChessAgent
         from haive.agents import ReactAgent

         # Combine game AI with reasoning
         chess_ai = ChessAgent(name="ChessBot")
         reasoning_agent = ReactAgent(
             name="strategist",
             tools=[chess_ai]
         )

   .. tab-item:: Multi-Game Tournament

      .. code-block:: python

         from haive.games.tournament import Tournament
         from haive.games import ChessAgent, PokerAgent, GoAgent

         # Run cross-game tournament
         tournament = Tournament(
             agents=[
                 ChessAgent(name="Bot1"),
                 PokerAgent(name="Bot1"),
                 GoAgent(name="Bot1")
             ]
         )
         results = tournament.run_all()

   .. tab-item:: Research Analytics

      .. code-block:: python

         from haive.games.analytics import GameAnalyzer
         from haive.games.among_us import AmongUsGame

         # Analyze social dynamics
         game = AmongUsGame(players=10)
         analyzer = GameAnalyzer(game)
         
         # Get behavioral metrics
         trust_network = analyzer.get_trust_network()
         deception_rates = analyzer.get_deception_metrics()

Resources 📚
-----------

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 📖 **Game Documentation**
      :link: game_categories
      :link-type: doc

      Complete guide to all game implementations

   .. grid-item-card:: 🎓 **Tutorials**
      :link: getting_started
      :link-type: doc

      Step-by-step guides and examples

   .. grid-item-card:: 💬 **Community**
      :link: https://github.com/haive-ai/haive/discussions
      :link-type: url

      Join discussions and share strategies

Need Help? 🤝
------------

- 📝 Check our :doc:`getting_started` for quick tutorials
- 🐛 Found a bug? `Report it on GitHub <https://github.com/haive-ai/haive/issues>`_
- 💡 Have a feature request? `Start a discussion <https://github.com/haive-ai/haive/discussions>`_
- 📧 Contact us at games@haive.ai

.. toctree::
   :hidden:
   :maxdepth: 2

   installation
   getting_started
   game_categories
   social_psychology_games
   tournament_system
   changelog