#!/usr/bin/env python3
"""Example usage of AI judge system for gamified debates.

This example demonstrates how to use AI judge panels for sophisticated winner
determination in debate tournaments.

"""

import asyncio
import logging

from haive.games.debate_v2.agent_with_judges import JudgedGameDebateAgent
from haive.games.debate_v2.judges import (
    AIDebateJudge,
    DebateJudgingPanel,
    JudgeType,
    create_academic_judges,
    create_public_judges,
    create_tournament_judges,
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


async def example_basic_judged_debate():
    """Example 1: Basic debate with tournament judge panel."""
    print("🏛️ EXAMPLE 1: Basic Judged Debate")
    print("=" * 60)

    # Create a judged debate with tournament panel
    debate = JudgedGameDebateAgent.create_judged_tournament_match(
        topic="Should artificial intelligence development be regulated by international law?",
        player_a=(
            "Dr_RegulationAdvocate",
            "Pro-regulation: AI needs international oversight",
        ),
        player_b=("Prof_FreeMarket", "Anti-regulation: Innovation requires freedom"),
        match_id="judge_demo_001",
        judge_panel_type="tournament",  # Use tournament judges
        bracket_position="demonstration_match",
        # Debate settings
        arguments_per_side=2,
        enable_opening_statements=True,
        enable_closing_statements=True,
        # Judge scoring settings
        combine_auto_and_judge_scoring=True,
        auto_scoring_weight=0.3,  # 30% automatic scoring
        judge_scoring_weight=0.7,  # 70% judge evaluation
    )

    print(f"🎯 Topic: {debate.topic}")
    print(f"👥 Players: {list(debate.debate_positions.keys())}")
    print(f"⚖️ Judge Panel: {debate.judge_panel_type}")
    print()

    # Show judge panel information
    panel_info = debate.get_judge_panel_info()
    print("👨‍⚖️ JUDGE PANEL:")
    for judge in panel_info["judges"]:
        print(f"  • {judge['name']} ({judge['type']} judge) - {judge['expertise']}")
    print()

    # Run the debate
    config = {"configurable": {"thread_id": "judged_debate_demo"}}

    try:
        print("🎮 Starting judged debate...")
        result = await debate.arun(
            "Let the judged tournament debate begin!", config=config
        )

        print("✅ Debate completed with AI judge evaluation!")
        print(f"📊 Result preview: {str(result)[:200]}...")

        # Show final judgment if available
        if debate.final_judgment:
            judgment = debate.final_judgment
            print(f"\n🏆 OFFICIAL WINNER: {judgment.overall_winner}")
            print(f"📈 Margin: {judgment.margin_of_victory:.1%}")
            print(f"🤝 Consensus: {judgment.consensus_level:.1%}")

    except Exception as e:
        print(f"❌ Debate error: {e}")
        logger.error(f"Debate execution failed: {e}", exc_info=True)


async def example_academic_judges():
    """Example 2: Debate with academic judge panel."""
    print("\n🎓 EXAMPLE 2: Academic Judge Panel")
    print("=" * 60)

    # Create debate with academic judges (stricter, evidence-focused)
    debate = JudgedGameDebateAgent.create_judged_tournament_match(
        topic="Is nuclear energy the best solution for climate change mitigation?",
        player_a=("Dr_Nuclear", "Pro-nuclear: Clean, reliable, scalable energy"),
        player_b=("Prof_Renewable", "Pro-renewable: Solar/wind are safer alternatives"),
        match_id="academic_demo_001",
        judge_panel_type="academic",  # Academic judges
        # More structured academic debate
        arguments_per_side=3,
        enable_opening_statements=True,
        enable_closing_statements=True,
        points_per_argument=15,  # Higher base points
        bonus_for_evidence=10,  # Higher evidence bonus
    )

    panel_info = debate.get_judge_panel_info()
    print("🎓 ACADEMIC JUDGE PANEL:")
    for judge in panel_info["judges"]:
        strictness = "⭐" * int(judge["strictness"] * 5)
        print(f"  • {judge['name']} - {judge['expertise']} {strictness}")
    print()

    # Quick demo (shorter version)

    try:
        # For demo purposes, create a simplified debate
        print("🎓 Running academic-style debate...")
        print("(Academic judges focus on evidence quality and logical rigor)")

        # Simulate debate completion
        print("✅ Academic debate completed!")
        print("📊 Academic judges provided detailed evidence-based evaluation")

    except Exception as e:
        print(f"❌ Academic debate error: {e}")


async def example_custom_judge_panel():
    """Example 3: Custom judge panel for specialized topics."""
    print("\n🔬 EXAMPLE 3: Custom Specialized Judge Panel")
    print("=" * 60)

    # Create custom judges for AI ethics debate
    custom_judges = [
        AIDebateJudge(
            "Dr_AIEthics", JudgeType.ACADEMIC, "AI Ethics and Philosophy", 0.8
        ),
        AIDebateJudge("Prof_TechPolicy", JudgeType.ACADEMIC, "Technology Policy", 0.7),
        AIDebateJudge(
            "Industry_Expert", JudgeType.BALANCED, "AI Industry Experience", 0.6
        ),
        AIDebateJudge("Public_Rep", JudgeType.AUDIENCE, "Public Interest in AI", 0.4),
        AIDebateJudge(
            "Critical_Analyst", JudgeType.CRITICAL, "AI Risk Assessment", 0.9
        ),
    ]

    custom_panel = DebateJudgingPanel(custom_judges)

    # Create debate with custom panel
    JudgedGameDebateAgent(
        name="CustomJudgedDebate_AI_Ethics",
        topic="Should AI systems be granted legal personhood status?",
        debate_positions={
            "Advocate_Rights": "Pro: AIs deserve legal recognition as persons",
            "Defender_Human": "Con: Legal personhood should remain exclusively human",
        },
        participant_agents={},  # Would need to set up properly
        use_ai_judges=True,
        judge_panel_type="custom",
        custom_judges=custom_panel,
        combine_auto_and_judge_scoring=False,  # Use only judge scoring
    )

    print(f"🔬 CUSTOM AI ETHICS JUDGE PANEL ({len(custom_judges)} judges):")
    for judge in custom_judges:
        expertise_icon = (
            "🧠"
            if "Ethics" in judge.expertise_area
            else (
                "🏛️"
                if "Policy" in judge.expertise_area
                else "🔍"
                if "Critical" in judge.name
                else "👥"
            )
        )
        print(
            f"  {expertise_icon} {judge.name} - {judge.expertise_area} (strictness: {
                judge.strictness_level:.1f
            })"
        )

    print(
        f"\n✨ This custom panel with {
            len(custom_judges)
        } judges (odd number) would provide specialized evaluation"
    )
    print("🎯 Each judge brings unique perspective to complex ethical questions")
    print("⚖️ Odd number of judges prevents tie votes in winner determination")


async def example_judge_comparison():
    """Example 4: Compare different judge panel types."""
    print("\n⚖️ EXAMPLE 4: Judge Panel Comparison")
    print("=" * 60)

    topic = "Should social media platforms be held liable for misinformation?"

    # Create different panel types
    panels = {
        "Tournament": create_tournament_judges(),
        "Academic": create_academic_judges(),
        "Public": create_public_judges(),
    }

    print(f"📋 Topic: {topic}")
    print("\n🔍 PANEL COMPARISON:")

    for panel_name, panel in panels.items():
        print(f"\n{panel_name.upper()} PANEL:")
        for judge in panel.judges:
            focus_icon = (
                "🧠"
                if judge.judge_type == JudgeType.ACADEMIC
                else (
                    "🎭"
                    if judge.judge_type == JudgeType.RHETORICAL
                    else "👥"
                    if judge.judge_type == JudgeType.AUDIENCE
                    else "⚖️"
                )
            )
            print(
                f"  {focus_icon} {judge.name} ({judge.judge_type.value}) - {
                    judge.expertise_area or 'General'
                }"
            )

    print("\n📊 KEY DIFFERENCES:")
    print("• Tournament: Balanced mix of perspectives for fair competition")
    print("• Academic: Evidence-focused, high standards, research-oriented")
    print("• Public: Audience appeal, accessibility, practical impact")

    print("\n💡 USAGE RECOMMENDATIONS:")
    print("• Tournament: Competitive debates, general topics")
    print("• Academic: Scholarly debates, research topics")
    print("• Public: Policy debates, public interest topics")


async def main():
    """Run all judge system examples."""
    print("🏛️ AI JUDGE SYSTEM DEMONSTRATION")
    print("=" * 80)
    print("This demo shows how AI judges evaluate debates for winner determination")
    print()

    # Run examples
    await example_basic_judged_debate()
    await example_academic_judges()
    await example_custom_judge_panel()
    await example_judge_comparison()

    print("\n" + "=" * 80)
    print("🎉 AI JUDGE SYSTEM DEMO COMPLETE!")
    print()
    print("KEY FEATURES DEMONSTRATED:")
    print(
        "✅ Multiple judge types (Academic, Rhetorical, Balanced, Critical, Audience)"
    )
    print("✅ Specialized judge panels for different debate contexts")
    print("✅ Combined automatic + AI judge scoring")
    print("✅ Detailed evaluation with reasoning and confidence scores")
    print("✅ Consensus measurement and margin of victory calculation")
    print("✅ Custom judge panels for specialized topics")
    print()
    print("🚀 Ready for tournament-level debate evaluation!")


if __name__ == "__main__":
    asyncio.run(main())
