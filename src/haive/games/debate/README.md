# Debate

Structured debate and argumentation platform with LLM-powered participants and sophisticated scoring.

## Overview

The Debate module provides a comprehensive platform for structured discussions and formal debates, featuring AI participants that can engage in sophisticated argumentation, evidence presentation, and logical reasoning. Built on the Haive framework, it supports multiple debate formats and advanced judging mechanisms.

**Key Features:**

- **Multiple Debate Formats**: Parliamentary, Oxford-style, Lincoln-Douglas, and custom formats
- **AI Debaters**: LLM-powered participants with distinct arguing styles and expertise
- **Structured Phases**: Opening statements, rebuttals, cross-examination, and closing arguments
- **Intelligent Judging**: AI judges that evaluate arguments based on logic, evidence, and rhetoric
- **Topic Research**: Automated fact-checking and evidence gathering for debate topics
- **Real-time Scoring**: Dynamic evaluation of argument strength and debate performance
- **Rich Moderation**: AI moderators that enforce rules and guide discussion flow

**Debate Mechanics:**

- **Argument Structure**: Claims, evidence, warrants, and impact analysis
- **Rebuttal System**: Point-by-point refutation and counter-arguments
- **Time Management**: Configurable speaking times and turn enforcement
- **Evidence Validation**: Fact-checking and source verification
- **Flow Tracking**: Comprehensive argument mapping and progression

## Architecture

The debate system follows multi-participant game architecture:

```
DebateAgent
├── Configuration (DebateAgentConfig)
├── State Management (DebateStateManager)
├── Participants (debaters, judges, moderator)
├── Debate Flow (phases, timing, rules)
├── Scoring System (argument evaluation)
└── Workflow (LangGraph-based debate management)
```

### Core Components

- **DebateAgent**: Main debate controller managing flow and participants
- **DebateState**: Complete debate state with arguments, scores, and phase tracking
- **DebateStateManager**: Rule enforcement, timing, and argument validation
- **Participant**: Individual debater with role, style, and expertise
- **Statement**: Structured argument with type, content, and evidence
- **Topic**: Debate subject with research materials and context
- **Scoring Engine**: Argument evaluation and performance metrics

## Installation

This module is part of the `haive-games` package. Install it using:

```bash
pip install haive-games
```

## Usage Examples

### Basic Parliamentary Debate

```python
from haive.games.debate import DebateAgent, DebateAgentConfig
from haive.core.models.llm.configs import LLMConfig

# Configure LLM for debate participants
llm_config = LLMConfig(
    model="gpt-4",
    temperature=0.7,
    max_tokens=2000
)

# Create debate agent
config = DebateAgentConfig(
    aug_llm_configs={
        "proposition_1": llm_config,
        "proposition_2": llm_config,
        "opposition_1": llm_config,
        "opposition_2": llm_config,
        "judge": llm_config,
        "moderator": llm_config
    },
    debate_format="parliamentary",
    time_limit=480,  # 8 minutes per speaker
    max_statements=12,
    enable_scoring=True
)

# Run debate on AI ethics
topic = {
    "title": "AI Should Be Regulated by Government",
    "description": "Debate whether artificial intelligence development and deployment should be subject to government regulation."
}

agent = DebateAgent(config)
result = agent.run_debate(topic=topic)

print(f"Winning side: {result.get('winner')}")
print(f"Final scores: {result.get('scores')}")
print(f"Best argument: {result.get('best_argument')}")
```

### Oxford-Style Debate

```python
# Configure Oxford-style debate
config = DebateAgentConfig(
    aug_llm_configs=llm_configs,
    debate_format="oxford",
    participants=[
        "pro_speaker_1", "pro_speaker_2", "pro_speaker_3",
        "con_speaker_1", "con_speaker_2", "con_speaker_3"
    ],
    time_limit=360,  # 6 minutes per speaker
    allow_interruptions=False,
    enable_audience_voting=True
)

topic = {
    "title": "This House Believes That Social Media Does More Harm Than Good",
    "description": "Debate the overall impact of social media on society, considering both benefits and drawbacks."
}

agent = DebateAgent(config)
result = agent.run_debate(topic=topic)
```

### Lincoln-Douglas Style

```python
# One-on-one philosophical debate
config = DebateAgentConfig(
    aug_llm_configs={
        "affirmative": LLMConfig(
            model="gpt-4",
            temperature=0.6,
            system_prompt="You are a skilled debater arguing for the affirmative position with philosophical rigor."
        ),
        "negative": LLMConfig(
            model="gpt-4",
            temperature=0.6,
            system_prompt="You are a skilled debater arguing for the negative position with logical precision."
        ),
        "judge": llm_config
    },
    debate_format="lincoln_douglas",
    time_limit=240,  # 4 minutes constructive, 3 minutes rebuttal
    focus_on_values=True,
    philosophical_framework=True
)

topic = {
    "title": "Justice Ought to Take Precedence Over Security",
    "description": "A philosophical debate about the relative importance of justice versus security in governance."
}

agent = DebateAgent(config)
result = agent.run_debate(topic=topic)
```

### Advanced Debate with Research

```python
# Debate with automatic fact-checking and research
config = DebateAgentConfig(
    aug_llm_configs={
        **participant_configs,
        "researcher": llm_config,
        "fact_checker": llm_config
    },
    debate_format="research_intensive",
    enable_research_phase=True,
    fact_checking=True,
    evidence_validation=True,
    research_time=1800,  # 30 minutes for research
    citation_required=True
)

topic = {
    "title": "Climate Change Policies Should Prioritize Economic Growth",
    "description": "Debate the balance between environmental protection and economic considerations in climate policy.",
    "research_areas": ["climate science", "economic policy", "environmental law", "international agreements"]
}

agent = DebateAgent(config)
result = agent.run_debate(topic=topic, enable_research=True)
```

### Tournament Debate Series

```python
# Multiple debates with ranking system
topics = [
    {"title": "Universal Basic Income Should Be Implemented", "side_bias": "balanced"},
    {"title": "Space Exploration Is a Priority Over Earth Problems", "side_bias": "balanced"},
    {"title": "Privacy Rights Should Override National Security", "side_bias": "balanced"}
]

tournament_results = []
for topic in topics:
    agent = DebateAgent(config)
    result = agent.run_debate(topic=topic)
    tournament_results.append({
        "topic": topic["title"],
        "winner": result.get("winner"),
        "scores": result.get("scores"),
        "quality": result.get("argument_quality")
    })

print("Tournament Results:")
for i, result in enumerate(tournament_results, 1):
    print(f"Round {i}: {result['topic']} - Winner: {result['winner']}")
```

## Debate Formats

### Parliamentary Debate

**Structure:**

1. **Opening Statements** (8 minutes each)
   - Government Opening
   - Opposition Opening
2. **Member Speeches** (8 minutes each)
   - Government Member
   - Opposition Member
3. **Rebuttal Speeches** (4 minutes each)
   - Opposition Rebuttal
   - Government Rebuttal

**Rules:**

- Points of Information allowed
- Government defines the motion
- Opposition may accept or redefine

### Oxford-Style Debate

**Structure:**

1. **Opening Statements** (6 minutes each side)
2. **Main Arguments** (8 minutes per speaker)
3. **Rebuttals** (4 minutes each)
4. **Closing Statements** (3 minutes each)

**Features:**

- Formal proposition/opposition
- Audience voting before and after
- Emphasis on persuasion

### Lincoln-Douglas Debate

**Structure:**

1. **Affirmative Constructive** (6 minutes)
2. **Negative Cross-Examination** (3 minutes)
3. **Negative Constructive** (7 minutes)
4. **Affirmative Cross-Examination** (3 minutes)
5. **Affirmative Rebuttal** (4 minutes)
6. **Negative Rebuttal** (6 minutes)
7. **Affirmative Rebuttal** (3 minutes)

**Focus:**

- Philosophical and ethical frameworks
- Value-based argumentation
- Logical reasoning emphasis

## Configuration Options

### DebateAgentConfig

```python
class DebateAgentConfig:
    aug_llm_configs: Dict[str, LLMConfig]  # Participant engines
    debate_format: str = "parliamentary"   # Debate format type
    time_limit: int = 480                  # Seconds per speaker
    max_statements: int = 20               # Maximum statements per debate
    participants: List[str] = None         # Custom participant list
    enable_scoring: bool = True            # Enable argument scoring
    allow_interruptions: bool = True       # Allow points of information
    fact_checking: bool = False            # Enable fact validation
    evidence_validation: bool = False      # Validate evidence sources
    enable_research_phase: bool = False    # Pre-debate research
    research_time: int = 900               # Research phase duration
    citation_required: bool = False        # Require source citations
    judge_count: int = 1                   # Number of judges
    audience_voting: bool = False          # Enable audience participation
```

### Participant Configurations

- **debaters**: Main argument presenters
- **judges**: Argument evaluators and decision makers
- **moderator**: Debate flow controller and rule enforcer
- **researcher**: Fact-checker and evidence validator (optional)
- **audience**: Voting participants (optional)

## API Reference

### DebateAgent

```python
class DebateAgent(MultiPlayerGameAgent[DebateAgentConfig]):
    """Main debate facilitation agent."""

    def run_debate(self, topic: Dict[str, Any]) -> Dict[str, Any]:
        """Run a complete structured debate."""

    def add_participant(self, participant_id: str, role: str) -> None:
        """Add participant to debate."""

    def evaluate_argument(self, statement: str, context: Dict) -> Dict[str, Any]:
        """Evaluate argument quality and logic."""

    def get_debate_flow(self, state: DebateState) -> List[Dict]:
        """Get current debate flow and argument mapping."""
```

### DebateStateManager

```python
class DebateStateManager:
    """Manages debate state and rules."""

    def initialize(self, participants: List[str], topic: Topic) -> DebateState:
        """Initialize new debate."""

    def advance_phase(self, state: DebateState) -> DebateState:
        """Move to next debate phase."""

    def add_statement(self, state: DebateState, statement: Statement) -> DebateState:
        """Add statement to debate flow."""

    def calculate_scores(self, state: DebateState) -> Dict[str, float]:
        """Calculate current debate scores."""

    def validate_statement(self, statement: Statement) -> bool:
        """Validate statement format and content."""
```

### Statement & Argument Models

```python
class Statement:
    """Individual debate statement."""
    speaker_id: str
    content: str
    statement_type: str  # "opening", "rebuttal", "point_of_info", "closing"
    timestamp: datetime
    evidence: List[str] = []
    citations: List[str] = []
    target_argument: Optional[str] = None

class Participant:
    """Debate participant."""
    id: str
    name: str
    role: str  # "debater", "judge", "moderator"
    side: Optional[str] = None  # "proposition", "opposition"
    expertise: List[str] = []
    speaking_style: str = "balanced"
```

## Argument Evaluation

### Scoring Criteria

1. **Logic and Reasoning** (25%)
   - Logical consistency
   - Valid inferences
   - Absence of fallacies

2. **Evidence and Support** (25%)
   - Quality of evidence
   - Source credibility
   - Relevance to claims

3. **Rhetoric and Delivery** (20%)
   - Persuasive language
   - Clear communication
   - Engaging presentation

4. **Rebuttal Quality** (20%)
   - Effective counter-arguments
   - Addressing opponent points
   - Defensive strategies

5. **Overall Impact** (10%)
   - Debate influence
   - Memorable arguments
   - Strategic positioning

### Automatic Fact-Checking

```python
# Enable fact validation
config = DebateAgentConfig(
    fact_checking=True,
    evidence_validation=True,
    citation_required=True,
    aug_llm_configs={
        **participant_configs,
        "fact_checker": LLMConfig(
            model="gpt-4",
            temperature=0.2,  # Conservative for fact-checking
            system_prompt="You are a rigorous fact-checker who validates claims and evidence."
        )
    }
)
```

## Performance & Optimization

### Recommended Settings

```python
# Quick debates
config = DebateAgentConfig(
    time_limit=180,  # 3 minutes per speaker
    max_statements=8,
    enable_scoring=False,
    fact_checking=False
)

# Comprehensive debates
config = DebateAgentConfig(
    time_limit=600,  # 10 minutes per speaker
    max_statements=24,
    enable_scoring=True,
    fact_checking=True,
    evidence_validation=True
)

# Tournament settings
config = DebateAgentConfig(
    time_limit=480,  # 8 minutes standard
    enable_scoring=True,
    judge_count=3,  # Multiple judges
    audience_voting=True
)
```

### Memory Usage

- **Short Debate**: ~15KB per debate state
- **Full Parliamentary**: ~50KB per complete debate
- **Research Phase**: ~100KB with evidence and citations
- **Tournament Series**: ~500KB for 10-debate tournament

## Testing

Run debate-specific tests:

```bash
# Run all debate tests
poetry run pytest packages/haive-games/tests/test_debate/ -v

# Test specific functionality
poetry run pytest packages/haive-games/tests/test_debate/test_scoring.py -v
poetry run pytest packages/haive-games/tests/test_debate/test_formats.py -v
```

## Troubleshooting

### Common Issues

1. **Time Limit Exceeded**

   ```python
   # Increase time limits or enable flexible timing
   config.time_limit = 600
   config.flexible_timing = True
   ```

2. **Argument Quality Issues**

   ```python
   # Enable more detailed prompting
   config.detailed_prompting = True
   config.argument_templates = True
   ```

3. **Fact-Checking Failures**

   ```python
   # Use more conservative fact-checking
   config.fact_checking_strictness = "moderate"
   ```

4. **Scoring Inconsistencies**
   ```python
   # Use multiple judges for consensus
   config.judge_count = 3
   config.consensus_scoring = True
   ```

## Advanced Features

### Custom Debate Formats

```python
# Define custom format
custom_format = {
    "name": "scientific_symposium",
    "phases": [
        {"name": "hypothesis", "time": 300, "speakers": "all"},
        {"name": "evidence", "time": 600, "speakers": "rotating"},
        {"name": "peer_review", "time": 400, "speakers": "cross_examination"},
        {"name": "conclusion", "time": 200, "speakers": "all"}
    ],
    "rules": {
        "evidence_required": True,
        "peer_review_mandatory": True,
        "consensus_building": True
    }
}

config.custom_format = custom_format
```

### Integration with External Tools

```python
# Research database integration
config.research_databases = [
    "academic_papers", "news_sources", "government_data"
]

# Real-time fact-checking APIs
config.fact_check_apis = [
    "factcheck_org", "snopes", "politifact"
]
```

## See Also

- [Mafia](../mafia/): Social deduction game with similar multi-participant dynamics
- [Among Us](../among_us/): Discussion and voting mechanics
- [Clue](../clue/): Logical deduction and reasoning challenges
- [Argument Mining Research](https://argmining.org/): Academic resources on computational argumentation
- [Debate Tournament Formats](https://www.speechanddebate.org/): Standard competitive debate formats
