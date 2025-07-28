"""Simple demonstration of the Mafia game module.

This script provides a simplified demonstration of the Mafia game
functionality without relying on the full LangGraph integration. It
shows the basic game flow and state transitions.
"""

import random
import time

from haive.games.mafia.models import ActionType, GamePhase, MafiaAction, PlayerRole
from haive.games.mafia.state import MafiaGameState
from haive.games.mafia.state_manager import MafiaStateManager


def run_simple_demo():
    """Run a simplified demonstration of the Mafia game."""
    print("\n🎭 MAFIA GAME DEMO")
    print("=" * 60)

    # Create player names
    player_count = 5
    player_names = [f"Player_{i+1}" for i in range(player_count - 1)]
    player_names.append("Narrator")
    print(f"Players: {', '.join(player_names[:-1])} + Narrator")

    # Initialize the game state
    print("\n🎲 Initializing game state...")
    state = MafiaStateManager.initialize(player_names)

    # Display initial roles
    print("\n🔍 Role Assignment:")
    for player_id, role in state.roles.items():
        print(f"  {player_id}: {role.value}")

    # Visualize the initial state
    print("\n📊 Initial Game State:")
    visualize_state(state)

    # Progress through a few phases to demonstrate state transitions
    print("\n⏩ Advancing to Night Phase...")
    state = MafiaStateManager.advance_phase(state)
    visualize_state(state)

    # Find a mafia player and a target
    mafia_player = None
    for player_id, role in state.roles.items():
        if role == PlayerRole.MAFIA:
            mafia_player = player_id
            break

    if mafia_player:
        targets = [
            pid
            for pid, role in state.roles.items()
            if role != PlayerRole.MAFIA and pid != "Narrator"
        ]
        target = random.choice(targets)

        # Mafia night action
        print(f"\n🔪 {mafia_player} chooses to kill {target}...")
        kill_action = MafiaAction(
            player_id=mafia_player,
            action_type=ActionType.KILL,
            target_id=target,
            phase=GamePhase.NIGHT,
            round_number=state.round_number,
        )
        state = MafiaStateManager.apply_move(state, mafia_player, kill_action)

        # Resolve night actions
        state = MafiaStateManager.resolve_night_actions(state)

    # Advance to day discussion
    print("\n☀️ Morning comes...")
    state = MafiaStateManager.advance_phase(state)
    visualize_state(state)

    # Simulate a day discussion
    for player_id in state.players:
        if player_id != "Narrator" and state.player_states[player_id].is_alive:
            messages = [
                "I think we should be careful today.",
                "Did anyone notice anything suspicious last night?",
                "I'm not sure who to trust...",
                "Let's work together to find the mafia!",
            ]
            message = random.choice(messages)
            print(f"\n💬 {player_id}: {message}")

            speak_action = MafiaAction(
                player_id=player_id,
                action_type=ActionType.SPEAK,
                message=message,
                phase=GamePhase.DAY_DISCUSSION,
                round_number=state.round_number,
            )
            state = MafiaStateManager.apply_move(state, player_id, speak_action)
            time.sleep(0.5)

    # Advance to voting phase
    print("\n🗳️ Time to vote...")
    state = MafiaStateManager.advance_phase(state)
    visualize_state(state)

    # Simulate voting
    alive_players = [
        pid
        for pid, p_state in state.player_states.items()
        if p_state.is_alive and pid != "Narrator"
    ]

    for voter in alive_players:
        # Choose someone to vote for (not self)
        votees = [pid for pid in alive_players if pid != voter]
        votee = random.choice(votees)

        print(f"🗳️ {voter} votes for {votee}")
        vote_action = MafiaAction(
            player_id=voter,
            action_type=ActionType.VOTE,
            target_id=votee,
            phase=GamePhase.DAY_VOTING,
            round_number=state.round_number,
        )
        state = MafiaStateManager.apply_move(state, voter, vote_action)
        time.sleep(0.5)

    # Resolve votes and go to next night
    print("\n🌙 Night falls again...")
    state = MafiaStateManager.advance_phase(state)
    visualize_state(state)

    print("\n✅ Demo Complete!")


def visualize_state(state: MafiaGameState):
    """Simple visualization of the game state."""
    print("\n" + "=" * 60)
    day_number = state.day_number
    game_phase = state.game_phase.value.replace("_", " ").title()
    print(f"🎮 MAFIA GAME - Day {day_number}, {game_phase}")
    print(f"📌 Game Status: {state.game_status}")
    print("=" * 60)

    # Show players
    print("\n👥 Players:")
    for player_id, player_state in state.player_states.items():
        status = "🟢 ALIVE" if player_state.is_alive else "🔴 DEAD"
        print(f"  {player_id}: {status}")

    # Show announcements
    if state.public_announcements:
        print("\n📢 Recent Announcements:")
        for announcement in state.public_announcements[-3:]:
            print(f"  {announcement}")

    # Show votes in voting phase
    if state.game_phase == GamePhase.DAY_VOTING and state.votes:
        print("\n🗳️ Current Votes:")
        for voter, votee in state.votes.items():
            print(f"  {voter} voted for {votee}")

    # Show game statistics
    print("\n📊 Game Statistics:")
    print(f"  Alive Villagers: {state.alive_village_count}")
    print(f"  Alive Mafia: {state.alive_mafia_count}")

    # Show winner if game is over
    if state.game_status != "ongoing" and state.winner:
        print("\n🏆 Winner: " + state.winner.upper())
        if state.winner == "mafia":
            print("  The mafia has taken over the village!")
        else:
            print("  The village has eliminated all mafia members!")


if __name__ == "__main__":
    run_simple_demo()
