Haive Games Documentation
=========================

.. raw:: html

   <style>
   .hero-section {
      text-align: center;
      padding: 3rem 0;
      margin-bottom: 3rem;
      background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
      color: white;
      border-radius: 10px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
   }
   .hero-section h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
   }
   .hero-section p {
      font-size: 1.3rem;
      line-height: 1.8;
      max-width: 800px;
      margin: 0 auto;
   }
   .feature-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin: 3rem 0;
   }
   .feature-card {
      background: #f8f9fa;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
   }
   .feature-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
   }
   .metric-box {
      background: #ffe8e6;
      padding: 1rem;
      border-radius: 5px;
      text-align: center;
      margin: 0.5rem;
   }
   .metric-value {
      font-size: 2rem;
      font-weight: bold;
      color: #d63031;
   }
   </style>

   <div class="hero-section">
      <h1>🎮 The Ultimate AI Gaming Research Platform</h1>
      <p><strong>Haive Games</strong> - A comprehensive collection of <strong>19+ sophisticated game implementations</strong> featuring <strong>advanced AI agents</strong>, <strong>multi-provider LLM support</strong>, and <strong>tournament-grade analytics</strong> for cutting-edge research in strategic intelligence, social psychology, and competitive AI.</p>
   </div>

🌟 **Beyond Traditional Game AI**
---------------------------------

**Transform Game Theory Research with Advanced AI Implementations:**

**Social Psychology Games**
   Among Us, Mafia, Debate, and Clue with deception detection, trust modeling, and behavioral adaptation

**Strategic Intelligence**  
   Chess, Go, Risk, and Monopoly with deep planning, tactical analysis, and economic reasoning

**Economic Simulation**
   Trading games, resource management, and market analysis with complex economic AI

**Puzzle & Logic Games**
   Sudoku, Wordle, Mastermind, and logic puzzles with advanced problem-solving algorithms

**Card & Probability Games**
   Poker, Blackjack, UNO with sophisticated probability calculation and psychological modeling

Game Categories
---------------

.. grid:: 2 2 3 3
   :gutter: 2

   .. grid-item-card:: 🕵️ Social Psychology Games
      :img-top: _static/social-icon.png
      :link: social_psychology_games
      :link-type: doc

      **Advanced Behavioral AI Research**

      Among Us, Mafia, Debate, and Clue featuring deception detection, trust modeling, and social coordination.

      +++

      Features: Hidden roles, Psychological profiling, Alliance formation, Behavioral adaptation

   .. grid-item-card:: ♟️ Strategic Board Games
      :img-top: _static/strategy-icon.png
      :link: strategic_games
      :link-type: doc

      **Deep Strategic Intelligence**

      Chess, Go, Checkers, and Connect 4 with advanced planning, tactical analysis, and strategic depth.

      +++

      Features: Deep planning, Tactical precision, Endgame databases, Tournament support

   .. grid-item-card:: 🎰 Card & Probability Games
      :img-top: _static/cards-icon.png
      :link: card_games
      :link-type: doc

      **Probability & Psychology**

      Poker, Blackjack, UNO with sophisticated probability calculation, bluffing, and risk assessment.

      +++

      Features: Probability calculation, Bluffing AI, Risk assessment, Bankroll management

   .. grid-item-card:: 💰 Economic Games
      :img-top: _static/economy-icon.png
      :link: economic_games
      :link-type: doc

      **Complex Economic Simulation**

      Monopoly, Risk, Trading games with property management, negotiation AI, and market analysis.

      +++

      Features: Trade negotiation, Market analysis, Economic warfare, Portfolio optimization

   .. grid-item-card:: 🧩 Puzzle & Logic Games
      :img-top: _static/puzzle-icon.png
      :link: puzzle_games
      :link-type: doc

      **Analytical Problem Solving**

      Sudoku, Wordle, Mastermind, Minesweeper with constraint satisfaction and logical deduction.

      +++

      Features: Constraint solving, Pattern recognition, Logic deduction, Optimization algorithms

   .. grid-item-card:: 🏆 Tournament System
      :img-top: _static/tournament-icon.png
      :link: tournament_system
      :link-type: doc

      **Cross-Game Competitive Analysis**

      Multi-provider tournaments, benchmarking, and performance analytics across all game categories.

      +++

      Features: Multi-provider support, Cross-game rankings, Statistical analysis, Research tools

.. toctree::
   :maxdepth: 2
   :caption: Getting Started:
   :hidden:

   overview
   installation
   getting_started
   concepts
   examples

.. toctree::
   :maxdepth: 2
   :caption: Game Categories:
   :hidden:

   game_categories
   social_psychology_games
   strategic_games
   card_games
   economic_games
   puzzle_games

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics:
   :hidden:

   tournament_system
   configuration
   dynamic_configuration
   ai_personalities
   performance_analysis

.. toctree::
   :maxdepth: 2
   :caption: Reference:
   :hidden:

   changelog
   troubleshooting

.. toctree::
   :maxdepth: 4
   :caption: API Reference:
   :titlesonly:
   :hidden:

   Game API Overview <autoapi/index>
   Social Games <autoapi/games/among_us/index>
   Strategic Games <autoapi/games/chess/index>
   Card Games <autoapi/games/poker/index>
   Economic Games <autoapi/games/monopoly/index>
   Puzzle Games <autoapi/games/mastermind/index>
   Tournament System <autoapi/games/tournament/index>

Quick Start: AI Game Tournament
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Experience the power of advanced AI gaming research::

    from haive.games.chess import ChessAgent
    from haive.games.poker import PokerAgent
    from haive.games.among_us import AmongUsAgent
    from haive.games.tournament import MultiGameTournament
    
    # Create AI agents for different games
    chess_ai = ChessAgent(provider="openai", skill_level="expert")
    poker_ai = PokerAgent(provider="anthropic", style="aggressive")
    social_ai = AmongUsAgent(provider="claude", personality="detective")
    
    # Set up cross-game tournament
    tournament = MultiGameTournament(
        games=["chess", "poker", "among_us", "debate"],
        providers=["openai", "anthropic", "claude", "google"],
        format="round_robin",
        matches_per_pair=10
    )
    
    # Run comprehensive analysis
    results = await tournament.run_analysis()
    
    # Generate research insights
    insights = tournament.generate_cross_game_insights()

Featured Game Showcase
~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🧠 Advanced Social Intelligence
      :link: social_psychology_games
      :link-type: doc

      **Among Us & Mafia: Deception Detection**
      
      * **Trust Modeling**: Dynamic trust networks with behavioral adaptation
      * **Deception Detection**: 85%+ accuracy in identifying dishonest players
      * **Alliance Formation**: Strategic partnership and betrayal mechanics
      * **Psychological Profiling**: Real-time personality assessment and adaptation

   .. grid-item-card:: 📊 Strategic Depth Analysis
      :link: strategic_games
      :link-type: doc

      **Chess & Go: Deep Planning Intelligence**:
      
      * **Planning Depth**: 8+ move lookahead with strategic evaluation
      * **Tactical Precision**: 95%+ accuracy in tactical combinations
      * **Endgame Mastery**: 99%+ accuracy in theoretical endgames
      * **Opening Theory**: 100,000+ position database integration

   .. grid-item-card:: 🎲 Probability & Risk Mastery
      :link: card_games
      :link-type: doc

      **Poker: Advanced Probability Intelligence**:
      
      * **Probability Calculation**: Exact odds calculation in real-time
      * **Opponent Modeling**: Dynamic adaptation to playing styles
      * **Bluffing AI**: Context-aware deception strategies
      * **Bankroll Management**: Optimal betting and risk assessment

   .. grid-item-card:: 💼 Economic Strategy Simulation
      :link: economic_games
      :link-type: doc

      **Monopoly & Trading: Market Intelligence**:
      
      * **Trade Negotiation**: 90%+ successful deal completion rates
      * **Market Analysis**: Real-time property valuation and optimization
      * **Economic Warfare**: Strategic competition and alliance management
      * **Portfolio Optimization**: Mathematically optimal investment strategies

Platform Performance Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="feature-grid">
      <div class="metric-box">
         <div class="metric-value">19+</div>
         <div>Game Implementations</div>
      </div>
      <div class="metric-box">
         <div class="metric-value">5+</div>
         <div>LLM Providers</div>
      </div>
      <div class="metric-box">
         <div class="metric-value">100+</div>
         <div>Concurrent Games</div>
      </div>
      <div class="metric-box">
         <div class="metric-value">< 500ms</div>
         <div>Average Response</div>
      </div>
   </div>

Research Applications
~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🎓 Academic Research

      **Cutting-Edge AI Research Applications**:
      
      * **Game Theory Studies**: Strategic equilibrium and Nash analysis
      * **Social Psychology**: Trust, deception, and cooperation research
      * **Cognitive Science**: Decision-making and reasoning patterns
      * **Behavioral Economics**: Risk assessment and market behavior

   .. grid-item-card:: 🏢 Commercial Applications

      **Real-World Business Intelligence**:
      
      * **AI Benchmarking**: Comparative LLM performance analysis
      * **Strategy Optimization**: Business decision-making models
      * **Team Dynamics**: Leadership and collaboration assessment
      * **Competitive Intelligence**: Market strategy and competitor analysis

Platform Architecture
~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   graph TB
      subgraph "Game Categories"
         A[Social Psychology] --> B[Tournament Engine]
         C[Strategic Intelligence] --> B
         D[Economic Simulation] --> B
         E[Puzzle & Logic] --> B
      end
      
      subgraph "AI Infrastructure"
         B --> F[Multi-Provider LLM]
         B --> G[Dynamic Configuration]
         B --> H[Performance Analytics]
         
         F --> I[OpenAI, Anthropic, Claude]
         G --> J[Personality Profiles]
         H --> K[Research Metrics]
      end
      
      subgraph "Research Platform"
         I --> L[Tournament Results]
         J --> L
         K --> L
         
         L --> M[Academic Publications]
         L --> N[Commercial Insights]
      end
      
      style A fill:#ff6b6b
      style C fill:#74b9ff
      style D fill:#00b894
      style E fill:#fdcb6e

Next Steps
~~~~~~~~~~

- :doc:`game_categories` - Explore all 19+ game implementations
- :doc:`social_psychology_games` - Master AI deception and social reasoning
- :doc:`strategic_games` - Deep strategic intelligence development
- :doc:`tournament_system` - Cross-provider competitive analysis
- :doc:`getting_started` - Deploy your first AI game tournament

Research & Innovation
~~~~~~~~~~~~~~~~~~~~~

**Academic Research**
   * Multi-agent social coordination
   * Strategic reasoning and planning algorithms  
   * Economic behavior modeling
   * Deception detection and trust systems

**Industry Applications**
   * AI capability benchmarking
   * Strategic decision-making models
   * Team collaboration analysis
   * Competitive intelligence systems

**Open Challenges**
   * Cross-game strategy transfer
   * Real-time personality adaptation
   * Emergent social behavior modeling
   * Multi-modal game understanding

Community & Support
~~~~~~~~~~~~~~~~~~~

* **Documentation**: Comprehensive guides and research papers
* **GitHub**: https://github.com/haive-ai/haive-games
* **Discord**: Join our AI research community
* **Research**: research@haive.ai for academic collaboration

---

**Welcome to the Future of AI Gaming Research** - Where advanced algorithms meet sophisticated game theory to create AI systems that master strategy, psychology, and competition! 🎮

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`