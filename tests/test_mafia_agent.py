"""Test suite for Mafia game agent."""

# Standard library imports
import asyncio
from typing import Any, Dict, List, Optional

# Third-party imports
import pytest
from langgraph.types import Command

# Local imports
from haive.games.mafia.agent import (
    MafiaAgent,
    MafiaAgentConfig,
    create_mafia_agents,
    mafia_router,
)
from haive.games.mafia.models import (
    MafiaAction,
    MafiaActionType,
    MafiaGameConfig,
    MafiaGameState,
    MafiaObservation,
    MafiaPlayer,
    MafiaRole,
    MafiaRoundPhase,
)
from haive.games.mafia.state_manager import MafiaStateManager


class TestMafiaAgentConfig:
    """Test the MafiaAgentConfig class."""

    def test_default_config(self):
        """Test default agent configuration."""
        config = MafiaAgentConfig()

        assert config.name == "MafiaAgent"
        assert config.player_name == "Player1"
        assert config.strategy == "balanced"
        assert config.aggression_level == 0.5
        assert config.deception_level == 0.5

    def test_custom_config(self):
        """Test custom agent configuration."""
        config = MafiaAgentConfig(
            name="CustomAgent",
            player_name="Alice",
            strategy="aggressive",
            aggression_level=0.8,
            deception_level=0.3,
        )

        assert config.name == "CustomAgent"
        assert config.player_name == "Alice"
        assert config.strategy == "aggressive"
        assert config.aggression_level == 0.8
        assert config.deception_level == 0.3

    def test_config_validation(self):
        """Test configuration validation."""
        # Invalid aggression level
        with pytest.raises(ValueError):
            MafiaAgentConfig(aggression_level=1.5)

        with pytest.raises(ValueError):
            MafiaAgentConfig(aggression_level=-0.1)

        # Invalid deception level
        with pytest.raises(ValueError):
            MafiaAgentConfig(deception_level=2.0)

        # Invalid strategy
        with pytest.raises(ValueError):
            MafiaAgentConfig(strategy="invalid_strategy")


class TestMafiaAgent:
    """Test the MafiaAgent class."""

    def test_init_agent(self):
        """Test initializing the agent."""
        config = MafiaAgentConfig(player_name="TestPlayer")
        agent = MafiaAgent(config)

        assert agent.config == config
        assert agent.config.player_name == "TestPlayer"
        assert isinstance(agent.state_manager, MafiaStateManager)

    def test_agent_with_game_state(self):
        """Test agent with existing game state."""
        # Create game state
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="TestPlayer", role=MafiaRole.MAFIA),
                MafiaPlayer(name="Other", role=MafiaRole.CITIZEN),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        config = MafiaAgentConfig(player_name="TestPlayer")
        agent = MafiaAgent(config, game_state=game_state)

        assert len(agent.state_manager.state.players) == 2
        assert agent.state_manager.state.phase == MafiaRoundPhase.NIGHT

    def test_perceive_environment(self):
        """Test environment perception."""
        # Setup game state
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="TestPlayer", role=MafiaRole.DETECTIVE, is_alive=True),
                MafiaPlayer(name="Suspect", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Dead", role=MafiaRole.CITIZEN, is_alive=False),
            ],
            phase=MafiaRoundPhase.NIGHT,
            eliminated_players=["Dead"],
        )

        config = MafiaAgentConfig(player_name="TestPlayer")
        agent = MafiaAgent(config, game_state=game_state)

        # Perceive environment
        observation = agent._perceive_environment()

        assert isinstance(observation, MafiaObservation)
        assert observation.player_name == "TestPlayer"
        assert observation.role == MafiaRole.DETECTIVE
        assert observation.is_alive is True
        assert observation.phase == MafiaRoundPhase.NIGHT
        assert len(observation.alive_players) == 2
        assert observation.dead_players == ["Dead"]

    def test_decide_action_mafia_night(self):
        """Test mafia decision making at night."""
        # Setup as mafia at night
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="MafiaPlayer", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Victim1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Victim2", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        config = MafiaAgentConfig(
            player_name="MafiaPlayer", strategy="aggressive", aggression_level=0.9
        )
        agent = MafiaAgent(config, game_state=game_state)

        # Get observation and decide action
        observation = agent._perceive_environment()
        action = agent._decide_action(observation)

        assert isinstance(action, MafiaAction)
        assert action.player_name == "MafiaPlayer"
        assert action.action_type == MafiaActionType.KILL
        assert action.target in ["Victim1", "Victim2"]

    def test_decide_action_detective_night(self):
        """Test detective decision making at night."""
        # Setup as detective at night
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Detective", role=MafiaRole.DETECTIVE, is_alive=True),
                MafiaPlayer(name="Suspect1", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Suspect2", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        config = MafiaAgentConfig(player_name="Detective")
        agent = MafiaAgent(config, game_state=game_state)

        # Get observation and decide action
        observation = agent._perceive_environment()
        action = agent._decide_action(observation)

        assert isinstance(action, MafiaAction)
        assert action.player_name == "Detective"
        assert action.action_type in [MafiaActionType.INVESTIGATE, MafiaActionType.PASS]
        if action.action_type == MafiaActionType.INVESTIGATE:
            assert action.target in ["Suspect1", "Suspect2"]

    def test_decide_action_citizen_day_voting(self):
        """Test citizen voting decision."""
        # Setup voting phase
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Citizen", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Suspect", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Other", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
        )

        config = MafiaAgentConfig(player_name="Citizen")
        agent = MafiaAgent(config, game_state=game_state)

        # Get observation and decide action
        observation = agent._perceive_environment()
        action = agent._decide_action(observation)

        assert isinstance(action, MafiaAction)
        assert action.player_name == "Citizen"
        assert action.action_type == MafiaActionType.VOTE
        assert action.target in ["Suspect", "Other"]

    def test_decide_action_dead_player(self):
        """Test dead player cannot act."""
        # Setup with dead player
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="DeadPlayer", role=MafiaRole.CITIZEN, is_alive=False),
                MafiaPlayer(name="Alive", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
        )

        config = MafiaAgentConfig(player_name="DeadPlayer")
        agent = MafiaAgent(config, game_state=game_state)

        # Get observation and decide action
        observation = agent._perceive_environment()
        action = agent._decide_action(observation)

        assert action is None  # Dead players can't act

    def test_strategy_affects_decisions(self):
        """Test that strategy affects decision making."""
        # Same game state, different strategies
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Player", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Target1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Target2", role=MafiaRole.DETECTIVE, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        # Aggressive strategy - more likely to target special roles
        aggressive_config = MafiaAgentConfig(
            player_name="Player", strategy="aggressive", aggression_level=0.9
        )
        aggressive_agent = MafiaAgent(aggressive_config, game_state=game_state)

        # Defensive strategy - more conservative
        defensive_config = MafiaAgentConfig(
            player_name="Player", strategy="defensive", aggression_level=0.2
        )
        defensive_agent = MafiaAgent(defensive_config, game_state=game_state)

        # Both should decide to kill, but may have different target preferences
        obs = aggressive_agent._perceive_environment()
        aggressive_action = aggressive_agent._decide_action(obs)
        defensive_action = defensive_agent._decide_action(obs)

        assert aggressive_action.action_type == MafiaActionType.KILL
        assert defensive_action.action_type == MafiaActionType.KILL
        # Strategies may lead to different targets

    async def test_ainvoke(self):
        """Test async invoke method."""
        # Setup game state
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="TestPlayer", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Other", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
        )

        config = MafiaAgentConfig(player_name="TestPlayer")
        agent = MafiaAgent(config, game_state=game_state)

        # Mock state
        state = {"game_state": game_state.model_dump()}

        # Invoke agent
        result = await agent.ainvoke(state)

        assert isinstance(result, Command)
        assert result.update is not None
        assert "game_state" in result.update
        assert result.goto is not None

    def test_invoke_sync(self):
        """Test sync invoke method."""
        # Setup game state
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="TestPlayer", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Target", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        config = MafiaAgentConfig(player_name="TestPlayer")
        agent = MafiaAgent(config, game_state=game_state)

        # Mock state
        state = {"game_state": game_state.model_dump()}

        # Invoke agent
        result = agent.invoke(state)

        assert isinstance(result, Command)
        assert result.update is not None
        assert "game_state" in result.update
        # Should have taken an action
        updated_state = MafiaGameState(**result.update["game_state"])
        assert len(updated_state.actions) > 0

    def test_memory_persistence(self):
        """Test agent memory persistence."""
        config = MafiaAgentConfig(player_name="TestPlayer")
        agent = MafiaAgent(config)

        # Add some memory
        agent.memory["suspect_list"] = ["Player1", "Player2"]
        agent.memory["investigation_results"] = {"Player1": False}

        # Memory should persist across invocations
        assert agent.memory["suspect_list"] == ["Player1", "Player2"]
        assert agent.memory["investigation_results"]["Player1"] is False

    def test_game_over_handling(self):
        """Test handling game over state."""
        # Setup game over state
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Winner", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Loser", role=MafiaRole.CITIZEN, is_alive=False),
            ],
            phase=MafiaRoundPhase.GAME_OVER,
            game_over=True,
            winner="mafia",
        )

        config = MafiaAgentConfig(player_name="Winner")
        agent = MafiaAgent(config, game_state=game_state)

        # Should not take any action
        observation = agent._perceive_environment()
        action = agent._decide_action(observation)

        assert action is None  # No actions in game over state


class TestCreateMafiaAgents:
    """Test the create_mafia_agents function."""

    def test_create_multiple_agents(self):
        """Test creating multiple agents."""
        player_names = ["Alice", "Bob", "Charlie"]
        agents = create_mafia_agents(player_names)

        assert len(agents) == 3
        assert all(isinstance(agent, MafiaAgent) for agent in agents)
        assert agents[0].config.player_name == "Alice"
        assert agents[1].config.player_name == "Bob"
        assert agents[2].config.player_name == "Charlie"

    def test_create_agents_with_strategies(self):
        """Test creating agents with specific strategies."""
        player_names = ["Aggressive", "Defensive"]
        strategies = ["aggressive", "defensive"]

        agents = create_mafia_agents(player_names, strategies=strategies)

        assert agents[0].config.strategy == "aggressive"
        assert agents[0].config.aggression_level > 0.5
        assert agents[1].config.strategy == "defensive"
        assert agents[1].config.aggression_level < 0.5

    def test_create_agents_with_game_state(self):
        """Test creating agents with shared game state."""
        player_names = ["Player1", "Player2"]
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Player1", role=MafiaRole.MAFIA),
                MafiaPlayer(name="Player2", role=MafiaRole.CITIZEN),
            ]
        )

        agents = create_mafia_agents(player_names, game_state=game_state)

        # All agents should share the same game state
        assert all(len(agent.state_manager.state.players) == 2 for agent in agents)


class TestMafiaRouter:
    """Test the mafia_router function."""

    def test_router_continue_game(self):
        """Test router during ongoing game."""
        state = {
            "game_state": {
                "phase": "night",
                "game_over": False,
                "players": [{"name": "Player1", "role": "citizen", "is_alive": True}],
            }
        }

        result = mafia_router(state)
        assert result == "continue"

    def test_router_game_over(self):
        """Test router when game is over."""
        state = {
            "game_state": {
                "phase": "game_over",
                "game_over": True,
                "winner": "mafia",
                "players": [],
            }
        }

        result = mafia_router(state)
        assert result == "end"

    def test_router_invalid_state(self):
        """Test router with invalid state."""
        # Missing game_state
        state = {}
        result = mafia_router(state)
        assert result == "end"

        # Missing required fields
        state = {"game_state": {}}
        result = mafia_router(state)
        assert result == "end"
