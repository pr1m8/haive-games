Haive Games Documentation
========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   getting_started
   game_categories
   advanced_ai_games
   tournament_system
   social_psychology_games
   strategic_games
   dynamic_configuration
   multi_agent_coordination
   benchmark_framework
   examples
   api_reference
   quickstart
   troubleshooting
   changelog

Welcome to Haive Games
----------------------

**The most advanced AI gaming research platform on Earth** - Haive Games provides **revolutionary multi-agent gaming environments** where AI systems demonstrate complex social psychology, strategic reasoning, economic modeling, and competitive intelligence across **19+ sophisticated game implementations**.

🎮 **The Game Changer**: This isn't just a collection of games - it's a **living laboratory** for AI behavioral research, featuring **dynamic multi-provider tournaments**, **social deception mechanics**, **economic simulation**, and **adaptive AI personalities** that evolve during gameplay!

Revolutionary AI Gaming Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Beyond Traditional Gaming - Enter the Future of AI Research:**

* **🧠 Social AI Psychology** - Advanced deception, trust modeling, and emergent social behaviors
* **🏆 Cross-Provider Tournaments** - Claude vs OpenAI vs Anthropic across 19+ games with comprehensive benchmarking
* **💰 Economic AI Simulation** - Complex property management, trade negotiations, and market strategies
* **🎭 Multi-Agent Orchestration** - Specialized role agents with dynamic interaction patterns
* **🔄 Real-Time Configuration** - Hot-swap AI providers, strategies, and personalities mid-game
* **📊 Comprehensive Benchmarking** - Performance analysis, optimization guidance, and statistical insights
* **🗣️ Argumentative AI** - Structured debate systems with real-time fact-checking and evidence validation

**Revolutionary Example**: Deploy a Monopoly tournament where **Claude agents negotiate property trades** while **OpenAI agents optimize portfolios** and **Anthropic agents analyze market psychology** - all while the system **dynamically adjusts strategies**, **profiles performance**, and **generates comprehensive behavioral analysis**!

Core Gaming Categories
~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2 2 3 3
   :gutter: 2

   .. grid-item-card:: 🧠 Social Psychology Games
      :img-top: _static/social-games-icon.png
      :link: social_psychology_games
      :link-type: doc

      **Advanced Behavioral AI**

      Among Us, Mafia, Debate - games featuring deception, trust, argumentation, and complex social dynamics.

      +++

      Features: Hidden roles, Psychology modeling, Social reasoning

   .. grid-item-card:: ♟️ Strategic Board Games
      :img-top: _static/board-games-icon.png
      :link: strategic_games
      :link-type: doc

      **Deep Strategic Reasoning**

      Chess, Go, Checkers, Reversi - classic strategy games with advanced AI engines and tournament support.

      +++

      Features: Multiple difficulty levels, Engine variations, Tournament brackets

   .. grid-item-card:: 🃏 Advanced Card Games
      :img-top: _static/card-games-icon.png
      :link: game_categories
      :link-type: doc

      **Probability & Psychology**

      Poker, Hold'em, Blackjack, UNO - games combining statistical analysis with psychological warfare.

      +++

      Features: Bluffing mechanics, Risk assessment, Bankroll management

   .. grid-item-card:: 💰 Economic Simulation
      :img-top: _static/economy-games-icon.png
      :link: strategic_games
      :link-type: doc

      **Complex Economic AI**

      Monopoly, Risk - full economic ecosystems with property management, negotiations, and strategic investments.

      +++

      Features: Trade negotiations, Resource management, Market analysis

   .. grid-item-card:: 🧩 Puzzle & Logic Games
      :img-top: _static/puzzle-games-icon.png
      :link: game_categories
      :link-type: doc

      **Analytical Problem Solving**

      Sudoku, Wordle, Crosswords, Mastermind - pure logic and pattern recognition challenges.

      +++

      Features: Difficulty scaling, Hint systems, Performance analytics

   .. grid-item-card:: 🏆 Tournament Framework
      :img-top: _static/tournament-icon.png
      :link: tournament_system
      :link-type: doc

      **Cross-Provider Competition**

      Comprehensive tournament system with multi-provider support and statistical analysis.

      +++

      Features: Automated brackets, Performance profiling, Cross-game analytics

Advanced AI Gaming Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🎭 Multi-Agent Social Coordination
      :link: multi_agent_coordination
      :link-type: doc

      **Revolutionary social gaming** where AI agents demonstrate complex personalities, form alliances, engage in deception, and exhibit emergent social behaviors.

   .. grid-item-card:: 🔄 Dynamic Configuration Systems
      :link: dynamic_configuration
      :link-type: doc

      **Hot-swap AI providers** (OpenAI ↔ Claude ↔ Anthropic), modify strategies mid-game, and adapt personalities based on opponent analysis.

   .. grid-item-card:: 🏆 Tournament Intelligence
      :link: tournament_system
      :link-type: doc

      **Cross-provider competitive analysis** with comprehensive benchmarking, performance profiling, and statistical insights across 19+ game types.

   .. grid-item-card:: 📊 Behavioral Analytics
      :link: benchmark_framework
      :link-type: doc

      **Deep AI behavioral analysis** with strategy profiling, decision-making patterns, and performance optimization guidance.

Quick Start: Social Deduction Mastery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Experience AI social psychology in action::

    from haive.games.among_us import AmongUsGame, AmongUsAgent
    from haive.games.mafia import MafiaAgent, MafiaState

    # Create Among Us game with AI psychology
    agents = [
        AmongUsAgent(name="detective", personality="analytical"),
        AmongUsAgent(name="manipulator", personality="deceptive"),
        AmongUsAgent(name="follower", personality="trusting"),
        AmongUsAgent(name="chaos", personality="unpredictable")
    ]

    game = AmongUsGame(players=agents)

    # Watch AI agents exhibit complex social behaviors:
    # - Form alliances and betray each other
    # - Engage in sophisticated deception
    # - Analyze voting patterns and behavior
    # - Adapt strategies based on opponent psychology

    results = await game.run()
    print(f"Behavioral Analysis: {results.psychology_profile}")

Advanced Economic AI Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploy sophisticated economic reasoning::

    from haive.games.monopoly import MonopolyGame, MonopolyAgent
    from haive.games.risk import RiskAgent, RiskState

    # Create economic simulation with different AI strategies
    economic_agents = [
        MonopolyAgent(name="investor", strategy="aggressive_property"),
        MonopolyAgent(name="trader", strategy="negotiation_focus"),
        MonopolyAgent(name="conservative", strategy="cash_preservation"),
        MonopolyAgent(name="speculator", strategy="high_risk_reward")
    ]

    # Advanced economic simulation
    monopoly = MonopolyGame(
        players=economic_agents,
        enable_trade_negotiations=True,
        market_analysis=True,
        behavioral_profiling=True
    )

    # AI agents will:
    # - Negotiate complex property trades
    # - Analyze market conditions
    # - Develop counter-strategies against opponents
    # - Optimize portfolio management
    # - Engage in economic warfare

    results = await monopoly.run_tournament()

Cross-Provider Tournament Excellence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pit AI providers against each other::

    from haive.games.tournament import TournamentFramework
    from haive.games.benchmark import GameBenchmark

    # Create cross-provider tournament
    tournament = TournamentFramework([
        "among_us", "chess", "poker", "debate", "monopoly"
    ])

    # Configure AI providers for competition
    providers = {
        "claude": {"model": "claude-3-sonnet", "temperature": 0.7},
        "openai": {"model": "gpt-4", "temperature": 0.7},
        "anthropic": {"model": "claude-3-haiku", "temperature": 0.7}
    }

    # Run comprehensive tournament
    results = await tournament.run_cross_provider_competition(
        providers=providers,
        games_per_match=10,
        include_psychology_analysis=True,
        generate_strategy_reports=True
    )

    # Get detailed competitive intelligence:
    # - Win/loss ratios per provider per game
    # - Strategic pattern analysis
    # - Behavioral adaptation tracking
    # - Performance optimization recommendations

Dynamic AI Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Real-time AI personality and strategy modification::

    from haive.games.chess import ChessAgent
    from haive.games.chess.dynamic_config import *

    # Start with budget configuration
    agent = ChessAgent(config=budget_chess())

    # Mid-game strategy analysis reveals need for stronger play
    if game.critical_position_detected():
        # Hot-swap to competitive configuration
        await agent.reconfigure(competitive_chess())

    # Opponent playing unexpectedly? Switch to experimental
    if opponent.unusual_patterns_detected():
        await agent.reconfigure(experimental_chess())

    # Dynamic personality adjustment based on game state
    await agent.modify_personality({
        "aggression": 0.8,  # More aggressive in winning position
        "risk_tolerance": 0.6,  # Moderate risk for complex positions
        "time_management": "blitz"  # Fast play in time pressure
    })

Social Psychology Research Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 🕵️ Deception & Trust
      :text-align: center

      **Among Us & Mafia**: AI agents that lie, detect lies, form alliances, and exhibit realistic social psychology patterns.

   .. grid-item-card:: 🗣️ Argumentation Intelligence
      :text-align: center

      **Debate System**: AI that researches topics, constructs arguments, engages in real-time rebuttals, and adapts to opponent strategies.

   .. grid-item-card:: 🤝 Negotiation Mastery
      :text-align: center

      **Economic Games**: Complex trade negotiations, coalition building, and strategic economic warfare between AI agents.

Game Architecture Innovation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Revolutionary Framework Design:**

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🏗️ Universal Game Engine
      :link: api_reference
      :link-type: doc

      **Generic type system** supporting any game type - Position, GamePiece, Space, Container, Move, Player with event-driven architecture.

   .. grid-item-card:: ⚡ Real-Time & Turn-Based Hybrid
      :link: advanced_ai_games
      :link-type: doc

      **Sophisticated state management** supporting both real-time action games and complex turn-based strategy with cooldown systems.

Performance & Research Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Tournament Scale**: 19+ game types with cross-provider competition
* **Social Complexity**: 8+ agent personalities with psychological modeling
* **Economic Depth**: Full property management with trade negotiation systems
* **Response Time**: <500ms for strategic decisions, <2s for complex social analysis
* **Scalability**: 100+ concurrent games, 1000+ agent interactions per tournament

Game Categories Deep Dive
~~~~~~~~~~~~~~~~~~~~~~~~~

**🧠 Social Psychology & Deception Games**
   Advanced AI behavioral research through social deduction, hidden roles, and complex multi-agent psychology.

**♟️ Strategic Intelligence Games**
   Deep reasoning challenges featuring advanced AI engines with tournament-grade competitive analysis.

**💰 Economic & Negotiation Games**
   Sophisticated economic modeling with property management, trade systems, and market analysis.

**🎯 Analytical & Puzzle Games**
   Pure logic and pattern recognition with adaptive difficulty and performance optimization.

**🎭 Hybrid Social-Strategy Games**
   Complex games combining social dynamics with strategic depth for advanced AI research.

Next Steps
~~~~~~~~~~

- :doc:`getting_started` - Understand the gaming platform architecture
- :doc:`quickstart` - Deploy your first AI tournament
- :doc:`game_categories` - Explore all 19+ game implementations
- :doc:`social_psychology_games` - Master AI deception and social reasoning
- :doc:`tournament_system` - Run cross-provider competitive analysis
- :doc:`dynamic_configuration` - Hot-swap AI strategies and personalities
- :doc:`examples` - See advanced multi-agent gaming scenarios

Research Applications
~~~~~~~~~~~~~~~~~~~~~

**Academic Research**
   * AI behavioral psychology studies
   * Multi-agent coordination research
   * Game theory and strategic reasoning
   * Social dynamics and trust modeling

**Commercial Applications**
   * AI training and benchmarking
   * Strategy optimization research
   * Competitive intelligence analysis
   * Human-AI interaction studies

**Entertainment & Education**
   * Advanced AI gaming experiences
   * Educational game development
   * Interactive AI demonstrations
   * Gaming tournament platforms

Getting Help
~~~~~~~~~~~~

* **Documentation**: Comprehensive guides and API references
* **GitHub Issues**: https://github.com/haive-ai/haive-games/issues
* **Research Community**: Join our AI gaming research discussions
* **Tournament Leaderboards**: Competitive AI provider rankings

---

**The Future of AI Gaming Research Starts Here** - Deploy sophisticated AI agents across 19+ game environments and discover emergent behaviors, strategic intelligence, and social psychology patterns that advance the frontiers of artificial intelligence! 🚀

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
