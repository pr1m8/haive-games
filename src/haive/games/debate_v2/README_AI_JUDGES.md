# AI Judge System for Gamified Debates

**Version**: 1.0  
**Purpose**: Comprehensive guide to using AI judges for sophisticated debate winner determination  
**Last Updated**: 2025-01-11

## 🏛️ Overview

The AI Judge System provides sophisticated evaluation of debate performances using multiple AI judges with different expertise and perspectives. This creates more nuanced and fair winner determination than simple automatic scoring.

## 🎯 How Winner Determination Works

### 1. Automatic Scoring (Basic)

The basic `GameDebateAgent` uses automatic scoring:

```python
# Basic automatic scoring
- Arguments: 10 points each
- Rebuttals: 15 points each
- Evidence bonus: +5 points
- Repetition penalty: -3 points
# Winner = highest total score
```

### 2. AI Judge Evaluation (Advanced)

The `JudgedGameDebateAgent` uses AI judge panels:

```python
# AI judges evaluate on multiple criteria:
- Logical Strength (1-10)
- Evidence Quality (1-10)
- Persuasiveness (1-10)
- Clarity (1-10)
- Consistency (1-10)
- Rebuttal Quality (1-10)
# Winner = judge consensus + average scores
```

### 3. Combined Scoring (Recommended)

Best approach combines both methods:

```python
# Weighted combination:
final_score = (auto_score * 0.3) + (judge_score * 0.7)
# Provides both objective metrics and subjective evaluation
```

## 🧑‍⚖️ Judge Panel Configuration

### Configurable Panel Size

**Default**: 3 judges (recommended to avoid tie votes)  
**Range**: 1-15 judges  
**Best Practice**: Always use odd numbers!

```python
# Quick comparison of panel sizes
panel_3 = create_tournament_judges(3)   # Fast decisions
panel_5 = create_tournament_judges(5)   # Balanced speed/accuracy
panel_7 = create_tournament_judges(7)   # Research-optimal
panel_9 = create_tournament_judges(9)   # Maximum accuracy
```

### Academic Judges

- **Focus**: Logic, evidence, research quality
- **Best for**: Scholarly debates, technical topics
- **Strictness**: High (7-9/10)
- **Recommended Size**: 7 judges (research-optimal)

```python
from haive.games.debate_v2.judges import create_academic_judges

panel = create_academic_judges(7)  # Optimal for academic rigor
# Higher strictness, evidence-focused evaluation
```

### Tournament Judges

- **Focus**: Balanced evaluation across all criteria
- **Best for**: Competitive debates, general topics
- **Strictness**: Medium (5-7/10)
- **Recommended Size**: 3-5 judges (efficient decisions)

```python
from haive.games.debate_v2.judges import create_tournament_judges

panel = create_tournament_judges(3)  # Fast tournament decisions
# Balanced perspectives for fair competition
```

### Public Judges

- **Focus**: Audience appeal, accessibility
- **Best for**: Policy debates, public interest topics
- **Strictness**: Low-Medium (4-6/10)
- **Recommended Size**: 3 judges (public consensus)

```python
from haive.games.debate_v2.judges import create_public_judges

panel = create_public_judges(3)  # Clear public verdict
# Accessible evaluation for general audiences
```

### Custom Judges

- **Focus**: Your specific expertise area
- **Best for**: Specialized topics
- **Strictness**: Configurable

```python
from haive.games.debate_v2.judges import AIDebateJudge, JudgeType, DebateJudgingPanel

# Create specialized judges
judges = [
    AIDebateJudge("Dr_Climate", JudgeType.ACADEMIC, "Climate Science", 0.8),
    AIDebateJudge("Policy_Expert", JudgeType.BALANCED, "Environmental Policy", 0.7),
    AIDebateJudge("Public_Rep", JudgeType.AUDIENCE, "Public Environment Concerns", 0.5)
]
panel = DebateJudgingPanel(judges)
```

## 🚀 Quick Start Examples

### Example 1: Tournament Debate with AI Judges

```python
from haive.games.debate_v2.agent_with_judges import JudgedGameDebateAgent

# Create judged tournament match with optimal judge count
debate = JudgedGameDebateAgent.create_judged_tournament_match(
    topic="Should AI development be regulated internationally?",
    player_a=("Dr_Regulation", "Pro: AI needs global oversight"),
    player_b=("Prof_Innovation", "Con: Regulation stifles progress"),
    match_id="tournament_001",
    judge_panel_type="tournament",  # Use tournament judges
    num_judges=3,  # Optimal for quick, clear decisions
    # Scoring configuration
    combine_auto_and_judge_scoring=True,
    auto_scoring_weight=0.3,  # 30% automatic
    judge_scoring_weight=0.7   # 70% AI judges
)

# Run the debate
config = {"configurable": {"thread_id": "judged_debate_001"}}
result = await debate.arun("Begin the judged tournament!", config=config)

# Get final judgment
if debate.final_judgment:
    judgment = debate.final_judgment
    print(f"Winner: {judgment.overall_winner}")
    print(f"Margin: {judgment.margin_of_victory:.1%}")
    print(f"Consensus: {judgment.consensus_level:.1%}")
```

### Example 2: Academic Debate with Research-Optimal Judges

```python
# Create academic debate with research-optimal judge count
debate = JudgedGameDebateAgent.create_judged_tournament_match(
    topic="Nuclear energy vs renewable energy for climate goals",
    player_a=("Dr_Nuclear", "Pro-nuclear position"),
    player_b=("Prof_Renewable", "Pro-renewable position"),
    match_id="academic_001",
    judge_panel_type="academic",  # Strict academic judges
    num_judges=7,  # Research-optimal for error minimization
    # Academic settings
    arguments_per_side=3,  # More arguments
    bonus_for_evidence=15,  # Higher evidence bonus
    penalty_for_repetition=10,  # Higher penalty
)

# Academic judges will focus heavily on:
# - Research quality and citations
# - Logical consistency
# - Technical accuracy
```

### Example 3: Custom Judge Panel for Specialized Topic

```python
from haive.games.debate_v2.judges import AIDebateJudge, JudgeType, DebateJudgingPanel

# Create AI ethics specialist panel
ethics_judges = [
    AIDebateJudge("Dr_AIEthics", JudgeType.ACADEMIC, "AI Ethics", 0.8),
    AIDebateJudge("Tech_Philosopher", JudgeType.ACADEMIC, "Philosophy of Technology", 0.7),
    AIDebateJudge("Industry_Insider", JudgeType.BALANCED, "AI Industry", 0.6),
    AIDebateJudge("Public_Advocate", JudgeType.AUDIENCE, "AI Public Policy", 0.5),
    AIDebateJudge("Critical_Analyst", JudgeType.CRITICAL, "AI Risk Assessment", 0.9)
]
ethics_panel = DebateJudgingPanel(ethics_judges)

# Create debate with custom panel
debate = JudgedGameDebateAgent(
    name="AIEthicsDebate",
    topic="Should AI systems be granted legal personhood?",
    participant_agents=participant_agents,  # Pre-created agents
    debate_positions={
        "Advocate": "Pro: AIs deserve legal recognition",
        "Defender": "Con: Personhood should remain human-only"
    },
    use_ai_judges=True,
    judge_panel_type="custom",
    custom_judges=ethics_panel,
    combine_auto_and_judge_scoring=False  # Use only judge scoring
)
```

## 📊 Understanding Judge Evaluations

### Judge Score Breakdown

Each judge provides:

```python
{
    "criteria_scores": {
        "logical_strength": 8,      # How sound are the arguments?
        "evidence_quality": 7,      # How well-researched?
        "persuasiveness": 9,        # How convincing?
        "clarity": 8,               # How clear and organized?
        "consistency": 7,           # How consistent throughout?
        "rebuttal_quality": 8       # How well did they counter?
    },
    "total_score": 47,              # Sum of criteria (max 60)
    "reasoning": "Detailed explanation...",
    "winner_vote": "Player_Name",   # Who this judge thinks won
    "confidence": 0.85              # Judge's confidence (0-1)
}
```

### Panel Consensus Calculation

```python
# Winner determination process:
1. Count winner votes from all judges
2. If clear majority (>50%), declare winner
3. If tie, use average scores as tiebreaker
4. Calculate margin of victory (score difference)
5. Calculate consensus level (agreement percentage)
```

### Example Final Judgment

```python
{
    "overall_winner": "Dr_Regulation",
    "margin_of_victory": 0.23,      # 23% victory margin
    "consensus_level": 0.80,        # 80% of judges agreed
    "judgment_summary": "Detailed panel evaluation...",
    "judge_scores": {
        "Dr_Regulation": [judge1_score, judge2_score, ...],
        "Prof_Innovation": [judge1_score, judge2_score, ...]
    }
}
```

## ⚖️ Choosing the Right Judge Panel

### Decision Matrix

| Debate Type            | Panel Type | Judge Count | Why                       |
| ---------------------- | ---------- | ----------- | ------------------------- |
| **Quick Tournaments**  | Tournament | 3 judges    | Fast, clear decisions     |
| **Major Competitions** | Tournament | 5 judges    | Balanced speed/accuracy   |
| **Academic Research**  | Academic   | 7 judges    | Research-optimal accuracy |
| **High-Stakes Events** | Any Type   | 9 judges    | Maximum reliability       |
| **Policy Debates**     | Public     | 3 judges    | Clear public consensus    |
| **Technical Topics**   | Custom     | 5-7 judges  | Specialized expertise     |

### Panel Size Guidelines

**Research-Based Recommendations:**

- **3 judges**: Standard for appeals courts, fast decisions
- **5 judges**: Good balance of perspectives and efficiency
- **7 judges**: Optimal for error minimization (research-backed)
- **9 judges**: Supreme Court standard, maximum accuracy

```python
# Size comparison examples
quick_tournament = create_tournament_judges(3)   # Fast decisions
balanced_comp = create_tournament_judges(5)      # Speed + accuracy
research_optimal = create_academic_judges(7)     # Minimum errors
maximum_accuracy = create_tournament_judges(9)   # Highest reliability

# ALWAYS use odd numbers to prevent ties!
even_panel = create_tournament_judges(4)  # ⚠️ Warning: can cause ties
```

## 🎛️ Configuration Options

### Scoring Weights

```python
# Automatic scoring only
combine_auto_and_judge_scoring=False

# Judge scoring only
combine_auto_and_judge_scoring=False
use_ai_judges=True

# Combined scoring (recommended)
combine_auto_and_judge_scoring=True
auto_scoring_weight=0.3      # 30% automatic
judge_scoring_weight=0.7     # 70% judges

# Equal weighting
auto_scoring_weight=0.5      # 50% automatic
judge_scoring_weight=0.5     # 50% judges
```

### Judge Panel Selection

```python
# Built-in panels with configurable sizes
judge_panel_type="tournament", num_judges=3  # Fast competition
judge_panel_type="tournament", num_judges=5  # Balanced competition
judge_panel_type="academic", num_judges=7    # Research-optimal
judge_panel_type="public", num_judges=3      # Public consensus

# Custom panel
judge_panel_type="custom"
custom_judges=your_panel       # Your specialized judges
num_judges=len(your_panel.judges)  # Match your panel size
```

### Debate Settings

```python
# Academic style
arguments_per_side=3
enable_opening_statements=True
enable_closing_statements=True
bonus_for_evidence=15          # High evidence bonus

# Tournament style
arguments_per_side=2
enable_opening_statements=True
enable_closing_statements=True
bonus_for_evidence=5           # Moderate bonus

# Quick style
arguments_per_side=1
enable_opening_statements=False
enable_closing_statements=False
```

## 🔧 Advanced Features

### Get Judge Panel Information

```python
panel_info = debate.get_judge_panel_info()
print(f"Panel type: {panel_info['panel_type']}")
print(f"Judge count: {panel_info['judge_count']}")

for judge in panel_info['judges']:
    print(f"• {judge['name']} ({judge['type']}) - {judge['expertise']}")
```

### Access Final Judgment

```python
if debate.final_judgment:
    judgment = debate.final_judgment

    # Overall results
    print(f"Winner: {judgment.overall_winner}")
    print(f"Margin: {judgment.margin_of_victory:.1%}")
    print(f"Consensus: {judgment.consensus_level:.1%}")

    # Individual judge reasoning
    for player, scores in judgment.judge_scores.items():
        print(f"\n{player}:")
        for score in scores:
            print(f"  {score.judge_name}: {score.total_score}/60")
            print(f"    Reasoning: {score.reasoning[:100]}...")
```

### Custom Judge Creation

```python
# Create your own specialized judge
my_judge = AIDebateJudge(
    name="Expert_Climate",
    judge_type=JudgeType.ACADEMIC,
    expertise_area="Climate Science and Policy",
    strictness_level=0.8  # Very strict (0.0-1.0)
)

# Add to custom panel
custom_panel = DebateJudgingPanel([my_judge, other_judges...])
```

## 🎯 Best Practices

### 1. Choose Optimal Judge Count

```python
# Quick decisions → 3 judges
num_judges=3  # Appeals court standard, fast consensus

# Balanced evaluation → 5 judges
num_judges=5  # Good speed/accuracy tradeoff

# Maximum accuracy → 7 judges
num_judges=7  # Research-optimal for error minimization

# Critical decisions → 9 judges
num_judges=9  # Supreme Court standard, highest reliability
```

### 2. Always Use Odd Numbers

```python
# ✅ GOOD: Prevents tie votes
num_judges=3  # Clear winner
num_judges=5  # Clear winner
num_judges=7  # Clear winner

# ❌ AVOID: Can cause ties
num_judges=4  # ⚠️ Warning logged
num_judges=6  # ⚠️ Warning logged
```

### 3. Match Panel Type to Purpose

```python
# Quick tournaments → Tournament panel, 3 judges
# Academic research → Academic panel, 7 judges
# Public policy → Public panel, 3 judges
# Specialized topics → Custom panel, 5-7 judges
```

### 4. Use Combined Scoring

```python
# Recommended: 30% auto + 70% judges
combine_auto_and_judge_scoring=True
auto_scoring_weight=0.3
judge_scoring_weight=0.7
```

### 4. Review Judge Reasoning

```python
# Always check judge reasoning for insights
for score in judgment.judge_scores[player]:
    if score.confidence > 0.8:  # High confidence scores
        print(f"Key insight: {score.reasoning}")
```

## 🚀 Ready to Judge!

The AI Judge System provides sophisticated, fair, and transparent winner determination with **configurable panel sizes** based on judicial research. Choose your optimal judge count, configure your weights, and let the AI judges provide detailed evaluation!

**Quick Start:**

- **Fast tournaments**: 3 judges
- **Balanced evaluation**: 5 judges
- **Research-optimal**: 7 judges
- **Maximum accuracy**: 9 judges

**Next Steps:**

1. Try the examples in `example_with_judges.py`
2. Run tests with `test_judges.py`
3. Experiment with different panel sizes
4. Create your own custom judge panels
5. Host judged tournament brackets with optimal judge counts!

**Remember**: Always use odd numbers of judges to prevent tie votes! 🎯

---

## 📊 Research-Based Judge Panel Sizing

**Based on judicial and decision-making research:**

- **3 judges**: Standard for appellate courts, prevents ties
- **7 judges**: Optimal point for minimizing decision errors
- **9 judges**: U.S. Supreme Court standard, maximum deliberation

**Performance vs. Speed Tradeoff:**

- Fewer judges = Faster decisions
- More judges = Higher accuracy, but slower consensus
- Odd numbers = Essential for tie prevention

---

**Files in this implementation:**

- `judges.py` - AI judge system core with configurable panel sizes
- `agent_with_judges.py` - Judged debate agent with num_judges parameter
- `example_with_judges.py` - Usage examples with different panel sizes
- `test_judges.py` - Verification tests for configurable judges
- `README_AI_JUDGES.md` - This comprehensive guide
