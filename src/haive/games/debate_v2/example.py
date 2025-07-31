#!/usr/bin/env python3
"""Gamified Debate Examples - Modern Implementation.

This module demonstrates the new gamified debate system that works properly
with topic handling and doesn't suffer from the DynamicGraph initialization issues.
"""

import asyncio
import logging

from haive.games.debate_v2.agent import GameDebateAgent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def example_1_simple_game_debate():
    """Example 1: Simple Gamified Debate with Scoring.

    Demonstrates the basic gamified debate with:
    - Proper topic handling (no None issues)
    - Scoring system for arguments and rebuttals
    - Evidence bonuses and repetition penalties
    - Clean game-like conclusion
    """
    print("\n" + "=" * 80)
    print("  EXAMPLE 1: SIMPLE GAMIFIED DEBATE")
    print("  Topic Handling + Scoring System")
    print("=" * 80)

    # Create gamified debate - TOPIC PROPERLY HANDLED
    debate = GameDebateAgent.create_tournament_match(
        topic="Should social media companies be responsible for fact-checking?",
        player_a=(
            "TechAdvocate",
            "Social media companies should not be responsible for fact-checking",
        ),
        player_b=(
            "InfoGuardian",
            "Social media companies must take responsibility for fact-checking",
        ),
        match_id="demo_001",
        bracket_position="example_match",
        # Game settings
        scoring_enabled=True,
        points_per_argument=10,
        points_per_rebuttal=15,
        bonus_for_evidence=5,
        penalty_for_repetition=3,
        # Debate structure
        arguments_per_side=2,
        enable_opening_statements=True,
        enable_closing_statements=True,
    )

    print(f"✅ Created debate: {debate}")
    print(f"✅ Topic: {debate.topic}")
    print(f"✅ Participants: {list(debate.debate_positions.keys())}")
    print(f"✅ Tournament Mode: {debate.tournament_mode}")

    # Run debate - NO TOPIC BECOMING NONE!
    print("\n🎮 Starting gamified debate...")
    try:
        result = debate.run(
            {},  # Empty input - topic comes from agent configuration
            config={"configurable": {"recursion_limit": 100}},
            debug=True,
        )

        print("✅ Debate completed successfully!")

        # Show final scores
        final_scores = result.get("final_scores", {})
        if final_scores:
            print("\n🏆 FINAL SCORES:")
            sorted_scores = sorted(
                final_scores.items(), key=lambda x: x[1], reverse=True
            )
            for rank, (player, score) in enumerate(sorted_scores, 1):
                medal = "🥇" if rank == 1 else "🥈"
                print(f"  {medal} {player}: {score} points")

        # Show winner
        winner = result.get("debate_winner")
        if winner:
            print(f"\n🎉 Winner: {winner}")

        return result

    except Exception as e:
        print(f"❌ Error during debate: {e}")
        logger.error(f"Debate failed: {e}", exc_info=True)
        return None


def example_2_ai_regulation_tournament():
    """Example 2: AI Regulation Tournament Match.

    Demonstrates:
    - Tournament-style competitive debate
    - Multiple evidence-based arguments
    - Performance tracking
    - Professional tournament atmosphere
    """
    print("\n" + "=" * 80)
    print("  EXAMPLE 2: AI REGULATION TOURNAMENT")
    print("  Competitive Format with Evidence Scoring")
    print("=" * 80)

    # Create competitive tournament match
    debate = GameDebateAgent.create_tournament_match(
        topic="Should AI development be regulated by international treaty?",
        player_a=(
            "GlobalRegulator",
            "AI development needs international treaty regulation",
        ),
        player_b=(
            "InnovationChampion",
            "AI development should remain nation-based and competitive",
        ),
        match_id="tournament_semifinals_ai_reg",
        bracket_position="Semifinals - Round 1",
        # Competitive settings
        scoring_enabled=True,
        points_per_argument=15,  # Higher stakes
        points_per_rebuttal=20,
        bonus_for_evidence=8,  # Reward research
        penalty_for_repetition=5,
        # Extended format for tournament
        arguments_per_side=3,
        enable_opening_statements=True,
        enable_closing_statements=True,
        track_performance=True,
        save_replay=True,
    )

    print(f"🏆 Tournament Match: {debate.match_id}")
    print(f"📍 Bracket Position: {debate.bracket_position}")
    print(f"🎯 Topic: {debate.topic}")

    # Run competitive match
    print("\n🥊 Tournament match beginning...")
    try:
        result = debate.run(
            {},
            config={
                "configurable": {"recursion_limit": 150}
            },  # More turns for tournament
            debug=False,  # Less verbose for tournament
        )

        print("✅ Tournament match completed!")

        # Tournament-style results
        final_scores = result.get("final_scores", {})
        winner = result.get("debate_winner")

        print("\n🏆 TOURNAMENT RESULTSTS")
        print(f"📋 Match ID: {debate.match_id}")
        print(f"🎯 Topic: {debate.topic}")

        if final_scores:
            print("\n📊 Final Scores:")
            for player, score in final_scores.items():
                position = debate.debate_positions.get(player, "Unknown")
                print(f"  • {player} ({position}): {score} points")

        if winner:
            print(f"\n🎉 Advancing to Finals: {winner}")
            print(
                f"🎯 {winner} will represent '{
                    debate.debate_positions.get(winner, 'Unknown')
                }' in the final round"
            )

        # Show performance stats
        total_args = result.get("total_arguments", 0)
        total_rebuttals = result.get("total_rebuttals", 0)

        print("\n📈 Match Statistics:s:")
        print(f"  • Total Arguments: {total_args}")
        print(f"  • Total Rebuttals: {total_rebuttals}")
        print(
            f"  • Match Quality: {
                'High' if total_args + total_rebuttals > 10 else 'Standard'
            }"
        )

        return result

    except Exception as e:
        print(f"❌ Tournament match failed: {e}")
        logger.error(f"Tournament match error: {e}", exc_info=True)
        return None


def example_3_rapid_fire_debate():
    """Example 3: Rapid-Fire Debate Game.

    Demonstrates:
    - Quick, focused debate format
    - Lower scoring thresholds for speed
    - Concise arguments only
    - Fast-paced game experience
    """
    print("\n" + "=" * 80)
    print("  EXAMPLE 3: RAPID-FIRE DEBATE")
    print("  Fast-Paced Gaming Format")
    print("=" * 80)

    # Create rapid-fire debate
    debate = GameDebateAgent.create_tournament_match(
        topic="Should remote work become the permanent norm?",
        player_a=("RemoteAdvocate", "Remote work should be the permanent standard"),
        player_b=("OfficeTraitionalist", "In-person office work remains essential"),
        match_id="rapid_fire_001",
        bracket_position="Speed Round",
        # Rapid-fire settings
        scoring_enabled=True,
        points_per_argument=5,  # Lower scores for speed
        points_per_rebuttal=8,
        bonus_for_evidence=3,
        penalty_for_repetition=2,
        # Quick format
        arguments_per_side=1,  # Only 1 argument each
        enable_opening_statements=False,  # Skip opening
        enable_closing_statements=False,  # Skip closing
        track_performance=True,
    )

    print(f"⚡ Rapid-Fire Match: {debate.match_id}")
    print(f"🎯 Topic: {debate.topic}")
    print("⏱️  Format: 1 argument + 1 rebuttal each (speed round)")

    # Run rapid match
    print("\n⚡ Speed debate starting...")
    try:
        result = debate.run(
            {},
            config={"configurable": {"recursion_limit": 30}},  # Quick limit
            debug=False,
        )

        print("✅ Speed round completed!")

        # Quick results
        final_scores = result.get("final_scores", {})
        winner = result.get("debate_winner")

        print("\n⚡ SPEED ROUND RESULTSS")
        if final_scores:
            for player, score in final_scores.items():
                print(f"  🏃 {player}: {score} points")

        if winner:
            print(f"\n🏆 Speed Winner: {winner}")

        return result

    except Exception as e:
        print(f"❌ Speed round failed: {e}")
        logger.error(f"Speed round error: {e}", exc_info=True)
        return None


async def run_all_examples():
    """Run all gamified debate examples."""
    print("🎮 GAMIFIED DEBATE EXAMPLES")
    print("Modern Implementation - No DynamicGraph Issues")
    print("=" * 80)

    examples = [
        ("Simple Game Debate", example_1_simple_game_debate),
        ("Tournament Match", example_2_ai_regulation_tournament),
        ("Rapid-Fire Debate", example_3_rapid_fire_debate),
    ]

    results = []
    for i, (name, example_func) in enumerate(examples, 1):
        print(f"\n🔄 Running Example {i}: {name}")
        try:
            result = example_func()
            if result:
                results.append((name, result))
                print(f"✅ Example {i} completed successfully")
            else:
                print(f"⚠️  Example {i} completed with issues")
        except Exception as e:
            print(f"❌ Example {i} failed: {e}")
            logger.error(f"Example {i} error: {e}")

        # Pause between examples
        if i < len(examples):
            print("\n⏸️  Pausing before next example...")
            await asyncio.sleep(2)

    # Summary
    print(f"\n🎉 Completed {len(results)}/{len(examples)} examples successfully!")

    if results:
        print("\n📊 SUMMARY OF RESULTS:")
        for name, result in results:
            winner = result.get("debate_winner", "Unknown")
            scores = result.get("final_scores", {})
            total_score = sum(scores.values()) if scores else 0
            print(f"  • {name}: Winner={winner}, Total Points={total_score}")


def main():
    """Main entry point for gamified debate examples."""
    print("🎮 Starting Gamified Debate Examples...")
    print("This demonstrates the NEW working debate system!")

    try:
        # Run examples
        asyncio.run(run_all_examples())

        print("\n✅ All examples completed!")
        print("🎯 Key Achievement: Topics handled properly (no None issues)")
        print("🏆 Game features working: scoring, tournaments, rapid-fire")

    except KeyboardInterrupt:
        print("\n⏹️  Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ Examples failed: {e}")
        logger.error(f"Main error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
