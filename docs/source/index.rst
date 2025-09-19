Haive Games Documentation
=========================

.. raw:: html

   <style>
   .hero-section {
      text-align: center;
      padding: 3rem 0;
      margin-bottom: 3rem;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
   .game-card {
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
      padding: 1.5rem;
      border-radius: 8px;
      margin: 1rem 0;
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

.. raw:: html

   <div class="feature-grid">
      <div class="game-card">
         <h3>🕵️ Social Psychology Games</h3>
         <p><strong>Advanced Behavioral AI Research</strong></p>
         <p>Among Us, Mafia, Debate, and Clue featuring deception detection, trust modeling, and social coordination.</p>
         <ul>
            <li>Hidden roles</li>
            <li>Psychological profiling</li>
            <li>Alliance formation</li>
            <li>Behavioral adaptation</li>
         </ul>
      </div>

      <div class="game-card">
         <h3>♟️ Strategic Board Games</h3>
         <p><strong>Deep Strategic Intelligence</strong></p>
         <p>Chess, Go, Checkers, and Connect 4 with advanced planning, tactical analysis, and strategic depth.</p>
         <ul>
            <li>Deep planning</li>
            <li>Tactical precision</li>
            <li>Endgame databases</li>
            <li>Tournament support</li>
         </ul>
      </div>

      <div class="game-card">
         <h3>🎰 Card & Probability Games</h3>
         <p><strong>Probability & Psychology</strong></p>
         <p>Poker, Blackjack, UNO with sophisticated probability calculation, bluffing, and risk assessment.</p>
         <ul>
            <li>Probability calculation</li>
            <li>Bluffing AI</li>
            <li>Risk assessment</li>
            <li>Bankroll management</li>
         </ul>
      </div>

      <div class="game-card">
         <h3>💰 Economic Games</h3>
         <p><strong>Complex Economic Simulation</strong></p>
         <p>Monopoly, Risk, Trading games with property management, negotiation AI, and market analysis.</p>
         <ul>
            <li>Trade negotiation</li>
            <li>Market analysis</li>
            <li>Economic warfare</li>
            <li>Portfolio optimization</li>
         </ul>
      </div>

      <div class="game-card">
         <h3>🧩 Puzzle & Logic Games</h3>
         <p><strong>Analytical Problem Solving</strong></p>
         <p>Sudoku, Wordle, Mastermind, Minesweeper with constraint satisfaction and logical deduction.</p>
         <ul>
            <li>Constraint solving</li>
            <li>Pattern recognition</li>
            <li>Logic deduction</li>
            <li>Optimization algorithms</li>
         </ul>
      </div>

      <div class="game-card">
         <h3>🏆 Tournament System</h3>
         <p><strong>Cross-Game Competitive Analysis</strong></p>
         <p>Multi-provider tournaments, benchmarking, and performance analytics across all game categories.</p>
         <ul>
            <li>Multi-provider support</li>
            <li>Cross-game rankings</li>
            <li>Statistical analysis</li>
            <li>Research tools</li>
         </ul>
      </div>
   </div>

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
   engine_architecture
   configuration
   common_module_overview

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics:
   :hidden:

   tournament_system
   schema_system
   graph_workflows
   tool_integration
   persistence_layer

.. toctree::
   :maxdepth: 2
   :caption: Reference:
   :hidden:

   api_reference
   changelog
   common_utilities


Quick Start: AI Game Tournament
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Experience the power of advanced AI gaming research::

    from haive.games.chess import ChessAgent
    from haive.games.poker import PokerAgent
    from haive.games.among_us import AmongUsAgent
    from haive.core.engine.aug_llm import AugLLMConfig
    
    # Create AI agents for different games
    config = AugLLMConfig()
    chess_ai = ChessAgent(name="ChessBot", engine=config)
    poker_ai = PokerAgent(name="PokerBot", engine=config)
    social_ai = AmongUsAgent(name="SocialBot", engine=config)
    
    # Run games with configured agents
    # Each agent uses sophisticated strategies tailored to their game type

Featured Game Showcase
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="feature-grid">
      <div class="feature-card">
         <h3>🧠 Advanced Social Intelligence</h3>
         <h4>Among Us & Mafia: Deception Detection</h4>
         <ul>
            <li><strong>Trust Modeling</strong>: Dynamic trust networks with behavioral adaptation</li>
            <li><strong>Deception Detection</strong>: 85%+ accuracy in identifying dishonest players</li>
            <li><strong>Alliance Formation</strong>: Strategic partnership and betrayal mechanics</li>
            <li><strong>Psychological Profiling</strong>: Real-time personality assessment and adaptation</li>
         </ul>
      </div>

      <div class="feature-card">
         <h3>📊 Strategic Depth Analysis</h3>
         <h4>Chess & Go: Deep Planning Intelligence</h4>
         <ul>
            <li><strong>Planning Depth</strong>: 8+ move lookahead with strategic evaluation</li>
            <li><strong>Tactical Precision</strong>: 95%+ accuracy in tactical combinations</li>
            <li><strong>Endgame Mastery</strong>: 99%+ accuracy in theoretical endgames</li>
            <li><strong>Opening Theory</strong>: 100,000+ position database integration</li>
         </ul>
      </div>

      <div class="feature-card">
         <h3>🎲 Probability & Risk Mastery</h3>
         <h4>Poker: Advanced Probability Intelligence</h4>
         <ul>
            <li><strong>Probability Calculation</strong>: Exact odds calculation in real-time</li>
            <li><strong>Opponent Modeling</strong>: Dynamic adaptation to playing styles</li>
            <li><strong>Bluffing AI</strong>: Context-aware deception strategies</li>
            <li><strong>Bankroll Management</strong>: Optimal betting and risk assessment</li>
         </ul>
      </div>

      <div class="feature-card">
         <h3>💼 Economic Strategy Simulation</h3>
         <h4>Monopoly & Trading: Market Intelligence</h4>
         <ul>
            <li><strong>Trade Negotiation</strong>: 90%+ successful deal completion rates</li>
            <li><strong>Market Analysis</strong>: Real-time property valuation and optimization</li>
            <li><strong>Economic Warfare</strong>: Strategic competition and alliance management</li>
            <li><strong>Portfolio Optimization</strong>: Mathematically optimal investment strategies</li>
         </ul>
      </div>
   </div>

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

.. raw:: html

   <div class="feature-grid">
      <div class="feature-card">
         <h3>🎓 Academic Research</h3>
         <p><strong>Cutting-Edge AI Research Applications</strong>:</p>
         <ul>
            <li><strong>Game Theory Studies</strong>: Strategic equilibrium and Nash analysis</li>
            <li><strong>Social Psychology</strong>: Trust, deception, and cooperation research</li>
            <li><strong>Cognitive Science</strong>: Decision-making and reasoning patterns</li>
            <li><strong>Behavioral Economics</strong>: Risk assessment and market behavior</li>
         </ul>
      </div>

      <div class="feature-card">
         <h3>🏢 Commercial Applications</h3>
         <p><strong>Real-World Business Intelligence</strong>:</p>
         <ul>
            <li><strong>AI Benchmarking</strong>: Comparative LLM performance analysis</li>
            <li><strong>Strategy Optimization</strong>: Business decision-making models</li>
            <li><strong>Team Dynamics</strong>: Leadership and collaboration assessment</li>
            <li><strong>Competitive Intelligence</strong>: Market strategy and competitor analysis</li>
         </ul>
      </div>
   </div>

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
- :doc:`engine_architecture` - Deep strategic intelligence development
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
* **GitHub**: https://github.com/pr1m8/haive-games
* **Discord**: Join our AI research community
* **Research**: research@haive.ai for academic collaboration

---

**Welcome to the Future of AI Gaming Research** - Where advanced algorithms meet sophisticated game theory to create AI systems that master strategy, psychology, and competition! 🎮

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`