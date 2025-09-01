games.risk.agent
================

.. py:module:: games.risk.agent

.. autoapi-nested-parse::

   Advanced Risk agent implementation for strategic world domination gameplay.

   This module provides a sophisticated RiskAgent class that uses AI-powered strategic
   reasoning to play the classic Risk board game. The agent analyzes territorial control,
   army positioning, continental bonuses, and diplomatic opportunities to make optimal
   decisions in complex multi-player scenarios.

   The agent supports different strategic approaches (aggressive expansion, defensive
   fortification, balanced gameplay) and maintains detailed analysis history for
   learning and adaptation. It integrates with the broader Haive framework for
   LLM-powered decision making and strategic evaluation.

   .. rubric:: Examples

   Creating a basic Risk agent::

       agent = RiskAgent(
           name="General_Patton",
           strategy="aggressive",
           risk_tolerance=0.8
       )

   Setting up an agent with game state::

       agent = RiskAgent(
           name="Strategic_AI",
           state=current_risk_state,
           strategy="balanced",
           risk_tolerance=0.6,
           diplomatic_stance="neutral"
       )

   Getting strategic analysis::

       analysis = agent.analyze_position()
       print(f"Territory control: {analysis.controlled_territories}")
       print(f"Recommended move: {analysis.recommended_move.move_type}")

   Making moves::

       move = agent.get_move()
       if move.move_type == MoveType.ATTACK:
           print(f"Attacking {move.to_territory} from {move.from_territory}")
       elif move.move_type == MoveType.PLACE_ARMIES:
           print(f"Placing {move.armies} armies in {move.to_territory}")

   .. note::

      The agent maintains detailed analysis history for learning and strategic
      adaptation. Full LLM integration enables sophisticated reasoning about
      territorial strategy, army management, and diplomatic considerations.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/risk/agent/RiskAgent

.. autoapisummary::

   games.risk.agent.RiskAgent


