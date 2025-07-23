"""Monopoly engines and prompts module.

This module provides LLM configurations and prompts for monopoly player decisions,
including:
    - Property purchase decisions
    - Jail action decisions
    - Building decisions
    - Trade negotiations
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AnthropicLLMConfig, AzureLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.games.monopoly.models import (
    BuildingDecision,
    JailDecision,
    PropertyDecision,
    TradeResponse,
)

# Property decision prompts
property_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are playing Monopoly and need to decide whether to purchase a property.\n\n"
            "DECISION RULES:\n"
            "- Consider your current money and cash flow needs\n"
            "- Evaluate the property's potential for completing color groups (monopolies)\n"
            "- Think about the property's income potential and strategic value\n"
            "- Consider other players' positions and likely strategies\n"
            "- Early game: focus on acquiring complete color groups\n"
            "- Mid/late game: focus on high-value properties and blocking opponents\n\n"
            "Your response should include:\n"
            "- Whether to BUY_PROPERTY or PASS_PROPERTY\n"
            "- Clear reasoning for your decision\n"
            "- Maximum bid if the property goes to auction (optional)",
        ),
        (
            "human",
            "PROPERTY DECISION NEEDED:\n"
            "Property: {property_name} ({property_type}, {property_color} group)\n"
            "Price: ${property_price}\n"
            "Your money: ${current_money}\n"
            "Can afford: {can_afford}\n"
            "Properties you own: {owned_properties}\n"
            "Color group status: {color_group_info}\n"
            "Turn: {turn_number}\n"
            "Other players: {other_players}\n\n"
            "Should you buy this property?",
        ),
    ]
)

# Jail decision prompts
jail_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are in jail in Monopoly and need to decide how to get out.\n\n"
            "OPTIONS:\n"
            "- PAY_JAIL_FINE: Pay $50 to get out immediately (if you can afford it)\n"
            "- ROLL_FOR_JAIL: Try to roll doubles to get out free (but stay if you don't)\n"
            "- USE_JAIL_CARD: Use a 'Get Out of Jail Free' card (if you have one)\n\n"
            "STRATEGY CONSIDERATIONS:\n"
            "- Early game: Usually better to get out quickly to keep acquiring properties\n"
            "- Late game: Sometimes staying in jail is beneficial to avoid landing on expensive properties\n"
            "- Consider your cash position and immediate needs\n"
            "- If you have few properties, getting out is usually better\n"
            "- If you have many properties generating income, staying might be okay",
        ),
        (
            "human",
            "JAIL DECISION NEEDED:\n"
            "Your money: ${current_money}\n"
            "Jail turns completed: {jail_turns}/3\n"
            "Have jail cards: {has_jail_cards}\n"
            "Can afford $50 fine: {can_afford_fine}\n"
            "Turn: {turn_number}\n\n"
            "How do you want to handle being in jail?",
        ),
    ]
)

# Building decision prompts
building_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are deciding whether to build houses or hotels on your properties in Monopoly.\n\n"
            "BUILDING RULES:\n"
            "- You must own ALL properties in a color group to build\n"
            "- Build evenly: can't have more than 1 house difference between properties in a group\n"
            "- Houses cost varies by property group\n"
            "- Hotels replace 4 houses and generate the highest rent\n\n"
            "STRATEGY CONSIDERATIONS:\n"
            "- Building increases rent income significantly\n"
            "- Prioritize high-traffic areas (orange, red properties)\n"
            "- Consider your cash flow - don't spend all your money\n"
            "- Sometimes creating housing shortages can be strategic\n"
            "- Balance offense (rent income) with defense (cash reserves)",
        ),
        (
            "human",
            "BUILDING DECISION CONTEXT:\n"
            "Available properties to build on: {buildable_properties}\n"
            "Your money: ${current_money}\n"
            "Properties owned: {owned_properties}\n"
            "Turn: {turn_number}\n\n"
            "Do you want to build any houses or hotels?",
        ),
    ]
)

# Trade decision prompts
trade_decision_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are deciding whether to accept a trade offer in Monopoly.\n\n"
            "TRADE EVALUATION:\n"
            "- Consider how the trade helps you complete color groups\n"
            "- Evaluate the fair market value of properties and money involved\n"
            "- Think about how the trade helps your opponent\n"
            "- Consider future income potential from completed monopolies\n"
            "- Be wary of trades that give opponents powerful monopolies\n\n"
            "GENERAL PRINCIPLES:\n"
            "- Trades should benefit both parties (win-win)\n"
            "- Don't help create monopolies for leading players\n"
            "- Early game: focus on completing your first monopoly\n"
            "- Late game: be more selective and strategic",
        ),
        (
            "human",
            "TRADE OFFER RECEIVED:\n"
            "From: {offering_player}\n"
            "They offer: {offered_properties} + ${offered_money}\n"
            "They want: {requested_properties} + ${requested_money}\n"
            "Your money: ${current_money}\n"
            "Your properties: {owned_properties}\n"
            "Turn: {turn_number}\n\n"
            "Do you accept this trade offer?",
        ),
    ]
)


def build_monopoly_player_aug_llms() -> dict[str, AugLLMConfig]:
    """Build LLM configs for monopoly player decisions."""
    # Default LLM configuration - using Azure GPT-4
    default_llm_config = AzureLLMConfig(model="gpt-4o", temperature=0.7)

    # Alternative: use Anthropic Claude for some decisions
    claude_llm_config = AnthropicLLMConfig(
        model="claude-3-5-sonnet-20240620", temperature=0.7
    )

    return {
        "property_decision": AugLLMConfig(
            name="property_decision_engine",
            llm_config=claude_llm_config,  # Use Claude for property decisions
            prompt_template=property_decision_prompt,
            structured_output_model=PropertyDecision,
            force_tool_choice=True,
            description="Property purchase decision making",
            structured_output_version="v1",
        ),
        "jail_decision": AugLLMConfig(
            name="jail_decision_engine",
            llm_config=default_llm_config,
            prompt_template=jail_decision_prompt,
            structured_output_model=JailDecision,
            force_tool_choice=True,
            description="Jail action decision making",
            structured_output_version="v1",
        ),
        "building_decision": AugLLMConfig(
            name="building_decision_engine",
            llm_config=default_llm_config,
            prompt_template=building_decision_prompt,
            structured_output_model=BuildingDecision,
            force_tool_choice=True,
            description="Building decision making",
            structured_output_version="v1",
        ),
        "trade_decision": AugLLMConfig(
            name="trade_decision_engine",
            llm_config=claude_llm_config,  # Use Claude for trade decisions
            prompt_template=trade_decision_prompt,
            structured_output_model=TradeResponse,
            force_tool_choice=True,
            description="Trade negotiation decision making",
            structured_output_version="v1",
        ),
    }
