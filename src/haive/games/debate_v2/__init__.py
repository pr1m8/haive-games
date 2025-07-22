"""Module exports."""

from debate_v2.agent import (
    GameDebateAgent,
    conclude_conversation,
    create_tournament_match,
    process_response,
    setup_agent,
    validate_game_setup,
)
from debate_v2.agent_with_judges import (
    JudgedGameDebateAgent,
    create_judged_tournament_match,
    get_judge_panel_info,
    setup_agent,
)
from debate_v2.example import (
    example_1_simple_game_debate,
    example_2_ai_regulation_tournament,
    example_3_rapid_fire_debate,
    main,
)
from debate_v2.judges import (
    AIDebateJudge,
    DebateJudgingPanel,
    DebateJudgment,
    JudgeScore,
    JudgeType,
    JudgingCriteria,
    create_academic_judges,
    create_expert_panel,
    create_public_judges,
    create_standard_panel,
    create_tournament_judges,
)
from debate_v2.simple_test import (
    main,
    test_agent_creation,
    test_game_features,
    test_inheritance,
    test_topic_handling,
)
from debate_v2.test_judges import (
    test_judge_creation,
    test_judged_agent_creation,
    test_scoring_combination,
)

__all__ = [
    "AIDebateJudge",
    "DebateJudgingPanel",
    "DebateJudgment",
    "GameDebateAgent",
    "JudgeScore",
    "JudgeType",
    "JudgedGameDebateAgent",
    "JudgingCriteria",
    "conclude_conversation",
    "create_academic_judges",
    "create_expert_panel",
    "create_judged_tournament_match",
    "create_public_judges",
    "create_standard_panel",
    "create_tournament_judges",
    "create_tournament_match",
    "example_1_simple_game_debate",
    "example_2_ai_regulation_tournament",
    "example_3_rapid_fire_debate",
    "get_judge_panel_info",
    "main",
    "process_response",
    "setup_agent",
    "test_agent_creation",
    "test_game_features",
    "test_inheritance",
    "test_judge_creation",
    "test_judged_agent_creation",
    "test_scoring_combination",
    "test_topic_handling",
    "validate_game_setup",
]
