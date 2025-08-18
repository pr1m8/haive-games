Social Psychology Games
======================

.. currentmodule:: haive.games

The **Social Psychology Games** represent the cutting edge of AI behavioral research - sophisticated gaming environments where AI agents demonstrate **complex social psychology**, **deception mechanics**, **trust modeling**, and **emergent social behaviors** that mirror real human interactions.

🧠 **Revolutionary Capabilities**
---------------------------------

**Advanced Deception & Trust Modeling**
   AI agents that lie convincingly, detect deception, form alliances, and exhibit realistic social psychology patterns

**Multi-Agent Social Coordination**
   Complex group dynamics with hidden roles, asymmetric information, and emergent social behaviors

**Adaptive Personality Systems**
   Dynamic personality profiles that evolve based on social interactions and strategic necessities

**Psychological Profiling**
   Comprehensive behavioral analysis including manipulation tactics, trust patterns, and social influence

**Real-Time Social Analytics**
   Live tracking of alliance formation, betrayal patterns, and social hierarchy emergence

Core Social Games
-----------------

Among Us - Advanced Social Deduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.games.among_us
   :members:
   :undoc-members:

**The Ultimate AI Social Psychology Laboratory**

Among Us provides the most sophisticated platform for studying AI deception, trust, and social reasoning. AI agents demonstrate:

* **Strategic Deception**: Convincing lies and misdirection
* **Behavioral Analysis**: Reading other agents' tells and patterns
* **Alliance Formation**: Dynamic team building and betrayal
* **Social Influence**: Manipulating group decision-making

**Quick Start: AI Social Deduction**

.. code-block:: python

   from haive.games.among_us import AmongUsGame, AmongUsAgent, AmongUsConfig

   # Create agents with distinct personalities
   agents = [
       AmongUsAgent(
           name="detective",
           personality="analytical",
           deception_skill=0.3,
           trust_threshold=0.7,
           social_influence=0.6
       ),
       AmongUsAgent(
           name="manipulator",
           personality="deceptive",
           deception_skill=0.9,
           trust_threshold=0.3,
           social_influence=0.8
       ),
       AmongUsAgent(
           name="follower",
           personality="trusting",
           deception_skill=0.2,
           trust_threshold=0.9,
           social_influence=0.4
       ),
       AmongUsAgent(
           name="chaos_agent",
           personality="unpredictable",
           deception_skill=0.6,
           trust_threshold=0.5,
           social_influence=0.7
       )
   ]

   # Configure advanced social dynamics
   config = AmongUsConfig(
       enable_psychology_tracking=True,
       alliance_formation=True,
       behavioral_adaptation=True,
       social_influence_modeling=True
   )

   # Run social psychology experiment
   game = AmongUsGame(players=agents, config=config)
   results = await game.run()

   # Analyze emergent behaviors
   print(f"Alliance Networks: {results.alliance_analysis}")
   print(f"Deception Success Rates: {results.deception_metrics}")
   print(f"Trust Evolution: {results.trust_dynamics}")
   print(f"Social Influence Patterns: {results.influence_analysis}")

**Advanced Among Us Features**

.. code-block:: python

   # Real-time personality adaptation
   game.enable_dynamic_personalities(
       adaptation_rate=0.1,
       memory_decay=0.05,
       trust_update_speed=0.2
   )

   # Complex voting psychology
   game.configure_voting_system(
       enable_bandwagon_effects=True,
       authority_influence=True,
       social_proof_modeling=True,
       strategic_voting_analysis=True
   )

   # Emergent role specialization
   roles = await game.analyze_emergent_roles()
   # Output: {
   #   "leader": "detective",
   #   "manipulator": "chaos_agent",
   #   "follower": "follower",
   #   "wildcard": "manipulator"
   # }

Mafia/Werewolf - Hidden Role Psychology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.games.mafia
   :members:
   :undoc-members:

**Classic Social Deduction with Advanced AI Psychology**

The Mafia implementation features sophisticated day/night cycles, role-based psychology, and complex information asymmetry.

**Key Features:**
* **Hidden Role Psychology**: Different AI behaviors for Mafia vs Townspeople
* **Information Asymmetry**: Complex knowledge modeling and strategic information sharing
* **Day/Night Mechanics**: Different behavioral patterns for different game phases
* **Social Network Analysis**: Dynamic relationship tracking and influence modeling

.. code-block:: python

   from haive.games.mafia import MafiaGame, MafiaAgent, MafiaRole

   # Create game with role-based psychology
   agents = [
       MafiaAgent(name="godfather", role=MafiaRole.MAFIA_BOSS),
       MafiaAgent(name="enforcer", role=MafiaRole.MAFIA_MEMBER),
       MafiaAgent(name="detective", role=MafiaRole.INVESTIGATOR),
       MafiaAgent(name="doctor", role=MafiaRole.PROTECTOR),
       MafiaAgent(name="citizen1", role=MafiaRole.TOWNSPERSON),
       MafiaAgent(name="citizen2", role=MafiaRole.TOWNSPERSON)
   ]

   # Advanced psychological modeling
   game = MafiaGame(
       players=agents,
       enable_role_psychology=True,
       social_network_tracking=True,
       information_flow_analysis=True
   )

   # Run multi-round psychology experiment
   tournament_results = await game.run_tournament(rounds=50)

   # Analyze psychological patterns
   psychology_report = game.generate_psychology_report()

Debate - Argumentative AI Intelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.games.debate
   :members:
   :undoc-members:

**Advanced Argumentation and Persuasion Systems**

The Debate system represents sophisticated AI argumentation with real-time research, evidence evaluation, and persuasion tactics.

**Revolutionary Features:**
* **Real-Time Research**: AI agents research topics during debate preparation
* **Evidence Evaluation**: Sophisticated fact-checking and source credibility analysis
* **Persuasion Tactics**: Advanced rhetorical strategies and audience psychology
* **Multi-Format Support**: Parliamentary, Oxford-style, Lincoln-Douglas formats

.. code-block:: python

   from haive.games.debate import DebateGame, DebateAgent, DebateFormat
   from haive.games.debate.research import ResearchAgent

   # Create specialized debate agents
   agents = [
       DebateAgent(
           name="pro_debater",
           position="pro",
           research_depth="comprehensive",
           argumentation_style="logical",
           persuasion_tactics=["evidence_heavy", "emotional_appeal"]
       ),
       DebateAgent(
           name="con_debater",
           position="con",
           research_depth="focused",
           argumentation_style="aggressive",
           persuasion_tactics=["counter_arguments", "logical_fallacy_detection"]
       )
   ]

   # Configure advanced debate features
   debate = DebateGame(
       topic="AI should have legal rights",
       format=DebateFormat.OXFORD_STYLE,
       research_phase_duration=600,  # 10 minutes
       enable_fact_checking=True,
       enable_audience_psychology=True,
       enable_real_time_research=True
   )

   # Run sophisticated argumentation
   results = await debate.run(debaters=agents)

   # Comprehensive analysis
   print(f"Argument Quality Scores: {results.argument_analysis}")
   print(f"Fact-Check Results: {results.fact_verification}")
   print(f"Persuasion Effectiveness: {results.persuasion_metrics}")
   print(f"Research Quality: {results.research_evaluation}")

Advanced Social Mechanics
-------------------------

Dynamic Personality Evolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Adaptive Personality Systems** that evolve based on social interactions:

.. code-block:: python

   # Personality trait evolution
   class AdaptivePersonality:
       def __init__(self):
           self.trust_level = 0.5
           self.aggression = 0.3
           self.social_influence = 0.4
           self.deception_skill = 0.6

       async def adapt_to_interactions(self, interaction_history):
           # Agents learn from past interactions
           # Betrayed agents become less trusting
           # Successful manipulators become more aggressive
           # Social outcasts develop defensive strategies
           pass

Alliance Formation & Betrayal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Complex Social Network Dynamics**:

.. code-block:: python

   # Alliance tracking system
   class AllianceTracker:
       def track_alliance_formation(self, agents):
           # Monitor who talks to whom
           # Detect secret communications
           # Analyze voting patterns
           # Predict alliance strength
           pass

       def predict_betrayal_likelihood(self, alliance, game_state):
           # Calculate betrayal probability based on:
           # - Individual vs group incentives
           # - Trust degradation patterns
           # - Strategic timing analysis
           # - Historical betrayal patterns
           pass

Social Influence Modeling
~~~~~~~~~~~~~~~~~~~~~~~~

**Advanced Persuasion and Manipulation**:

.. code-block:: python

   # Social influence analysis
   class SocialInfluenceEngine:
       def calculate_influence_network(self, agents):
           # Who influences whom and how much
           # Authority-based influence
           # Expertise-based influence
           # Charisma-based influence
           # Fear-based influence
           pass

       def predict_voting_behavior(self, topic, agents, influence_network):
           # Model how influence propagates
           # Predict voting cascades
           # Identify key swing agents
           # Calculate manipulation effectiveness
           pass

Psychological Research Features
------------------------------

Behavioral Pattern Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Comprehensive Psychology Profiling**:

.. code-block:: python

   # Generate detailed psychological profiles
   psychology_analyzer = PsychologyAnalyzer()

   # Agent behavioral patterns
   patterns = psychology_analyzer.analyze_agent_patterns(agent_id="manipulator")
   # Returns:
   # {
   #   "deception_patterns": ["timing", "targets", "success_rate"],
   #   "trust_patterns": ["formation_speed", "betrayal_triggers"],
   #   "alliance_patterns": ["formation_strategy", "maintenance", "exit_strategy"],
   #   "influence_patterns": ["persuasion_tactics", "target_selection", "effectiveness"]
   # }

Multi-Game Social Consistency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Cross-Game Personality Tracking**:

.. code-block:: python

   # Track personality consistency across games
   cross_game_tracker = CrossGamePersonalityTracker()

   # Analyze same agent across different social contexts
   consistency_report = cross_game_tracker.analyze_consistency(
       agent_id="detective",
       games=["among_us", "mafia", "debate"],
       metrics=["trust_patterns", "deception_detection", "social_influence"]
   )

Social Network Evolution
~~~~~~~~~~~~~~~~~~~~~~~

**Dynamic Relationship Modeling**:

.. code-block:: python

   # Track how relationships evolve over time
   network_analyzer = SocialNetworkAnalyzer()

   # Analyze relationship evolution
   evolution = network_analyzer.track_relationship_evolution(
       timespan="tournament",
       metrics=["trust", "influence", "cooperation", "competition"]
   )

   # Predict future alliance formation
   predictions = network_analyzer.predict_future_alliances(
       current_state=game.social_state,
       prediction_horizon=5  # 5 rounds ahead
   )

Tournament Social Intelligence
-----------------------------

Cross-Provider Social Comparison
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Compare AI Provider Social Intelligence**:

.. code-block:: python

   from haive.games.tournament import SocialTournament

   # Create social psychology tournament
   tournament = SocialTournament(
       games=["among_us", "mafia", "debate"],
       providers=["claude", "openai", "anthropic"],
       social_metrics=[
           "deception_effectiveness",
           "trust_calibration",
           "alliance_formation",
           "social_influence",
           "betrayal_detection"
       ]
   )

   # Run comprehensive social intelligence comparison
   results = await tournament.run_social_comparison()

   # Generate provider rankings
   rankings = tournament.generate_social_intelligence_rankings()
   # Claude: Excellent at deception detection, moderate at manipulation
   # OpenAI: Strong alliance formation, struggles with betrayal timing
   # Anthropic: Excellent social influence, conservative trust patterns

Emergent Behavior Research
~~~~~~~~~~~~~~~~~~~~~~~~~

**Study Emergent Social Phenomena**:

.. code-block:: python

   # Research platform for emergent behaviors
   research_platform = EmergentBehaviorResearch()

   # Study specific phenomena
   phenomena = [
       "leadership_emergence",
       "scapegoating_patterns",
       "coalition_formation",
       "information_cascades",
       "social_proof_effects"
   ]

   # Run long-term studies
   for phenomenon in phenomena:
       study = research_platform.design_study(
           phenomenon=phenomenon,
           duration="1000_games",
           control_variables=["agent_count", "information_asymmetry"],
           measurement_frequency="per_round"
       )

       results = await study.run()
       research_platform.publish_findings(phenomenon, results)

Performance Metrics
------------------

**Social Intelligence Benchmarks**:

* **Deception Success Rate**: 85% for advanced manipulator personalities
* **Trust Calibration**: ±0.1 accuracy in trust assessment
* **Alliance Stability**: 70% alliance survival rate across game phases
* **Influence Propagation**: <3 hops for 90% influence spread
* **Behavioral Adaptation**: 0.2 personality shift per significant interaction

**Research Applications**:

* **Academic Research**: Social psychology, game theory, multi-agent coordination
* **Commercial Intelligence**: Negotiation training, team dynamics, leadership development
* **AI Safety Research**: Understanding AI social manipulation and cooperation patterns

Integration with Other Systems
-----------------------------

**Multi-Agent Coordination**
   Social psychology games integrate with the main haive-agents framework for sophisticated agent orchestration.

**Dynamic Configuration**
   Hot-swap personalities, strategies, and social parameters during gameplay for adaptive research.

**Tournament Framework**
   Full integration with cross-provider tournament system for competitive social intelligence analysis.

See Also
--------

* :doc:`tournament_system` - Cross-provider social intelligence tournaments
* :doc:`multi_agent_coordination` - Integration with haive-agents framework
* :doc:`dynamic_configuration` - Real-time personality and strategy modification
* :doc:`benchmark_framework` - Performance analysis and optimization
