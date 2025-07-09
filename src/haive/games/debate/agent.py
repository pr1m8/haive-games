"""Debate Agent implementation for structured debate facilitation.

This module provides a comprehensive debate agent that facilitates various types
of structured debates including parliamentary, Oxford-style, and Lincoln-Douglas
formats. The agent manages participant turns, phase transitions, moderation,
and evaluation throughout the debate process.

The DebateAgent uses a multi-phase workflow system with configurable timing,
participant roles, and debate formats. It supports AI-powered participants,
human participants, and hybrid debates with sophisticated state management.

Examples:
    Creating a basic debate agent::

        config = DebateAgentConfig(
            debate_format="parliamentary",
            max_statements=20,
            time_limit=1800,
            participant_roles={"player_1": "pro", "player_2": "con"},
            moderator_role=True
        )
        agent = DebateAgent(config)

    Running a debate::

        initial_state = {
            "topic": {
                "title": "AI Should Be Regulated by Government",
                "description": "Debate whether AI development requires regulation"
            },
            "participants": ["debater_1", "debater_2", "moderator"]
        }
        result = await agent.run(initial_state)

    Configuring for Oxford-style debate::

        config = DebateAgentConfig(
            debate_format="oxford",
            allow_interruptions=True,
            visualize=True,
            participant_roles={
                "pro_1": "pro", "pro_2": "pro",
                "con_1": "con", "con_2": "con",
                "moderator": "moderator"
            }
        )

Note:
    The agent requires properly configured engines for different participant
    roles (debater, moderator, judge) and uses the DebateStateManager for
    all state transitions and rule enforcement.
"""

import time
from typing import Any, Dict, List, Optional, Union

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.graph import END
from langgraph.types import Command

from haive.games.debate.config import DebateAgentConfig
from haive.games.debate.models import DebatePhase, Participant, Statement, Topic
from haive.games.debate.state import DebateState
from haive.games.debate.state_manager import DebateStateManager
from haive.games.framework.multi_player import MultiPlayerGameAgent


@register_agent(DebateAgentConfig)
class DebateAgent(MultiPlayerGameAgent[DebateAgentConfig]):
    """Intelligent agent for facilitating structured debates and discussions.

    The DebateAgent orchestrates multi-participant debates with sophisticated
    phase management, role-based interaction, and configurable formats. It handles
    participant turn management, moderator functions, voting systems, and
    comprehensive state tracking throughout the debate lifecycle.

    This agent supports various debate formats including parliamentary,
    Oxford-style, Lincoln-Douglas, and trial simulations. It can manage
    AI participants, human participants, or hybrid groups with appropriate
    context preparation and response extraction for each role.

    Attributes:
        state_manager (DebateStateManager): Manages all debate state transitions
            and rule enforcement throughout the debate process.
        config (DebateAgentConfig): Configuration object containing debate format,
            timing, participant roles, and other behavioral settings.

    Examples:
        Creating and configuring a debate agent::

            config = DebateAgentConfig(
                debate_format="parliamentary",
                max_statements=15,
                time_limit=1200,
                allow_interruptions=False,
                moderator_role=True,
                participant_roles={
                    "debater_1": "pro",
                    "debater_2": "con",
                    "moderator": "moderator"
                }
            )
            agent = DebateAgent(config)

        Running a debate with custom topic::

            debate_state = {
                "topic": {
                    "title": "This House Believes Climate Action Should Prioritize Economy",
                    "description": "Debate the balance between environmental protection and economic growth",
                    "keywords": ["climate change", "economy", "environmental policy"]
                },
                "participants": ["pro_debater", "con_debater", "judge"]
            }
            result = await agent.arun(debate_state)

        Handling trial format::

            config = DebateAgentConfig(
                debate_format="trial",
                participant_roles={
                    "prosecutor": "prosecutor",
                    "defense": "defense",
                    "judge": "judge",
                    "witness_1": "witness"
                }
            )
            trial_agent = DebateAgent(config)

    Note:
        The agent requires appropriate engines to be configured for different
        participant roles. Each role (debater, moderator, judge, etc.) should
        have corresponding engine configurations in the agent setup.
    """

    def __init__(self, config: DebateAgentConfig) -> None:
        """Initialize the debate agent with configuration.

        Args:
            config (DebateAgentConfig): Configuration object containing debate
                format, timing rules, participant roles, and behavioral settings.

        Note:
            The state_manager is set as a class reference and will be used
            to create instances for state management operations.
        """
        self.state_manager = DebateStateManager
        super().__init__(config)

    def initialize_game(self, state: Dict[str, Any]) -> Command:
        """Initialize the debate with topic, participants, and configuration.

        Sets up the initial debate state including topic validation, participant
        registration, role assignment, and format-specific configuration. This
        method handles both structured topic objects and simple string topics,
        creating a fully configured debate state ready for the setup phase.

        Args:
            state (Dict[str, Any]): Initial state containing debate setup data.
                Expected keys:
                - topic (Union[str, Dict]): Debate topic as string or structured data
                - participants (Union[List[str], Dict]): List of participant IDs

        Returns:
            Command: LangGraph command to transition to debate_setup phase with
            initialized state data.

        Examples:
            Basic initialization with string topic::

                state = {
                    "topic": "Should AI be regulated?",
                    "participants": ["debater_1", "debater_2"]
                }
                command = agent.initialize_game(state)

            Initialization with structured topic::

                state = {
                    "topic": {
                        "title": "This House Believes AI Needs Regulation",
                        "description": "Comprehensive debate on AI governance",
                        "keywords": ["artificial intelligence", "regulation", "policy"]
                    },
                    "participants": ["pro_debater", "con_debater", "moderator"]
                }
                command = agent.initialize_game(state)

        Note:
            If no topic is provided, defaults to "AI Ethics in Society".
            If no participants are provided, creates 4 default participants.
            Participant roles are assigned during the setup phase based on config.
        """
        # Extract debate topic if provided, otherwise use default
        topic_data = state.get(
            "topic",
            {
                "title": "AI Ethics in Society",
                "description": "Discuss the ethical implications of AI in modern society",
            },
        )

        if isinstance(topic_data, str):
            topic_data = {"title": topic_data, "description": topic_data}

        topic = Topic(**topic_data)

        # Extract participants or use default
        player_list = state.get("participants", [f"participant_{i}" for i in range(4)])
        if isinstance(player_list, dict):
            player_list = list(player_list.keys())

        # Initialize with format from config
        debate_state = self.state_manager.initialize(
            player_list,
            topic,
            format_type=self.config.debate_format,
            time_limit=self.config.time_limit,
            max_statements=self.config.max_statements,
            allow_interruptions=self.config.allow_interruptions,
        )

        # Convert to dict for graph
        if hasattr(debate_state, "model_dump"):
            state_dict = debate_state.model_dump()
        else:
            state_dict = debate_state.dict()

        return Command(update=state_dict, goto="debate_setup")

    def get_player_role(self, state: DebateState, player_id: str) -> str:
        """Get the role of a specific player in the debate.

        Retrieves the assigned role for a participant from the debate state.
        Roles determine how participants interact with the debate, what context
        they receive, and how their responses are processed.

        Args:
            state (DebateState): Current debate state containing participant data.
            player_id (str): Unique identifier of the participant.

        Returns:
            str: The participant's role (e.g., "debater", "moderator", "judge",
            "prosecutor", "defense", "witness"). Returns "debater" if participant
            not found or no role assigned.

        Examples:
            Getting participant roles::

                role = agent.get_player_role(state, "participant_1")
                if role == "moderator":
                    # Handle moderator-specific logic
                elif role == "judge":
                    # Handle judge-specific logic

        Note:
            Default role is "debater" for unknown participants to ensure
            graceful handling of edge cases during debate flow.
        """
        if player_id in state.participants:
            return state.participants[player_id].role
        return "debater"  # Default role

    def prepare_move_context(
        self, state: DebateState, player_id: str
    ) -> Dict[str, Any]:
        """Prepare contextual information for a participant's move.

        Generates role-specific context that provides participants with relevant
        information for making their next move. Context varies significantly based
        on participant role (debater, moderator, judge, etc.) and current debate
        phase, ensuring each participant receives appropriate information.

        Args:
            state (DebateState): Current debate state with all participants,
                statements, votes, and phase information.
            player_id (str): Unique identifier of the participant whose turn it is.

        Returns:
            Dict[str, Any]: Role-specific context dictionary containing relevant
            information for the participant's decision-making. Contents vary by role:

            For debaters:
                - topic: Debate topic and description
                - debate_phase: Current phase of debate
                - position: Participant's stance (pro/con/neutral)
                - recent_statements: Last 5 statements from all participants
                - your_statements: Participant's previous statements
                - statement_type: Expected type for current phase

            For moderators:
                - topic: Debate topic and description
                - debate_phase: Current phase of debate
                - participants: List of all participants with roles
                - recent_statements: Recent debate activity
                - current_speaker: Who is currently speaking
                - action_prompt: Suggested moderator action

            For judges:
                - topic: Debate topic and description
                - debate_phase: Current phase of debate
                - all_statements: Complete statement history
                - key_arguments: Extracted pro/con arguments
                - action_prompt: Evaluation guidance

        Examples:
            Preparing context for debater::

                context = agent.prepare_move_context(state, "debater_1")
                # Returns: {
                #     "topic": "AI Regulation Topic",
                #     "position": "pro",
                #     "recent_statements": "...",
                #     "statement_type": "opening statement"
                # }

            Preparing context for moderator::

                context = agent.prepare_move_context(state, "moderator")
                # Returns: {
                #     "topic": "AI Regulation Topic",
                #     "participants": "...",
                #     "action_prompt": "provide guidance..."
                # }

        Note:
            Returns empty dict if participant not found in state.
            Context is optimized for AI engines but human-readable for hybrid debates.
        """
        participant = state.participants.get(player_id)
        if not participant:
            return {}

        # Get recent statements (last 5)
        recent_statements = state.statements[-5:] if state.statements else []
        formatted_recent = []

        for stmt in recent_statements:
            speaker_name = state.participants.get(
                stmt.speaker_id,
                Participant(id=stmt.speaker_id, name=stmt.speaker_id, role="unknown"),
            ).name
            formatted_recent.append(f"{speaker_name}: {stmt.content}")

        # Get this player's previous statements
        player_statements = [s for s in state.statements if s.speaker_id == player_id]
        formatted_player = [
            f"{s.statement_type.capitalize()}: {s.content}" for s in player_statements
        ]

        # Determine statement type based on phase
        statement_type = "statement"
        if state.debate_phase == DebatePhase.OPENING_STATEMENTS:
            statement_type = "opening statement"
        elif state.debate_phase == DebatePhase.REBUTTAL:
            statement_type = "rebuttal"
        elif state.debate_phase == DebatePhase.QUESTIONS:
            statement_type = "response to question"
        elif state.debate_phase == DebatePhase.CLOSING_STATEMENTS:
            statement_type = "closing statement"

        # Format based on role
        if participant.role == "moderator":
            action_prompt = (
                "provide guidance or ask a question to move the debate forward"
            )
            if state.debate_phase in [DebatePhase.SETUP, DebatePhase.JUDGMENT]:
                action_prompt = "summarize the current state and suggest next steps"

            return {
                "topic": state.topic.title,
                "topic_description": state.topic.description,
                "debate_phase": state.debate_phase,
                "participants": "\n".join(
                    [f"{p.name} ({p.role})" for p in state.participants.values()]
                ),
                "recent_statements": "\n".join(formatted_recent),
                "current_speaker": state.participants.get(
                    state.current_speaker,
                    Participant(id="unknown", name="Unknown", role="unknown"),
                ).name,
                "action_prompt": action_prompt,
            }

        if participant.role == "judge":
            # For trial format
            all_statements = [
                f"{state.participants.get(s.speaker_id, Participant(id=s.speaker_id, name=s.speaker_id, role='unknown')).name}: {s.content}"
                for s in state.statements
            ]

            action_prompt = "provide your analysis of the arguments presented so far"
            if state.debate_phase == DebatePhase.JUDGMENT:
                action_prompt = "render your final decision with explanation"

            return {
                "topic": state.topic.title,
                "topic_description": state.topic.description,
                "debate_phase": state.debate_phase,
                "all_statements": "\n".join(all_statements),
                "key_arguments": self._extract_key_arguments(state),
                "action_prompt": action_prompt,
            }

        if participant.role in ["prosecutor", "defense"]:
            # For trial format
            opponent_role = (
                "defense" if participant.role == "prosecutor" else "prosecutor"
            )
            opponent_claims = [
                s.content
                for s in state.statements
                if state.participants.get(
                    s.speaker_id, Participant(id="", name="", role="")
                ).role
                == opponent_role
            ]

            evidence = (
                "Evidence is still being collected"  # Would be populated from state
            )

            return {
                "topic": state.topic.title,
                "debate_phase": state.debate_phase,
                "evidence": evidence,
                "witness_statements": self._format_witness_statements(state),
                "recent_statements": "\n".join(formatted_recent),
                "statement_type": statement_type,
                "prosecution_claims": (
                    "\n".join(opponent_claims) if participant.role == "defense" else ""
                ),
                "client_info": (
                    "Defendant information" if participant.role == "defense" else ""
                ),
            }

        # Standard debater
        return {
            "topic": state.topic.title,
            "topic_description": state.topic.description,
            "debate_phase": state.debate_phase,
            "position": participant.position or "neutral",
            "recent_statements": "\n".join(formatted_recent),
            "your_statements": "\n".join(formatted_player),
            "statement_type": statement_type,
        }

    def _extract_key_arguments(self, state: DebateState) -> str:
        """Extract and format key arguments from debate statements.

        Analyzes all debate statements to identify and summarize the most recent
        and significant arguments from both pro and con positions. This provides
        judges and moderators with a concise overview of the debate's core issues.

        Args:
            state (DebateState): Current debate state containing all statements
                and participant position information.

        Returns:
            str: Formatted summary of key arguments with separate sections for
            pro and con positions. Shows last 3 arguments from each side,
            truncated to 100 characters for readability.

        Examples:
            Extracted argument summary::

                args = agent._extract_key_arguments(state)
                # Returns:
                # "PRO Arguments:
                # - AI regulation ensures safety and prevents misuse...
                # - Government oversight provides necessary accountability...
                #
                # CON Arguments:
                # - Regulation stifles innovation and economic growth...
                # - Market forces can self-regulate more effectively..."

        Note:
            Only includes arguments from participants with defined positions.
            Neutral participants and moderators are excluded from argument extraction.
        """
        pro_args = []
        con_args = []

        for stmt in state.statements:
            participant = state.participants.get(stmt.speaker_id)
            if not participant:
                continue

            if participant.position == "pro":
                pro_args.append(
                    f"- {stmt.content[:100]}..."
                    if len(stmt.content) > 100
                    else f"- {stmt.content}"
                )
            elif participant.position == "con":
                con_args.append(
                    f"- {stmt.content[:100]}..."
                    if len(stmt.content) > 100
                    else f"- {stmt.content}"
                )

        result = "PRO Arguments:\n" + "\n".join(pro_args[-3:])  # Last 3 arguments
        result += "\n\nCON Arguments:\n" + "\n".join(con_args[-3:])

        return result

    def _format_witness_statements(self, state: DebateState) -> str:
        """Format witness statements specifically for trial format debates.

        Extracts and formats all statements made by participants with the
        'witness' role, providing a chronological record of witness testimony
        for use in trial-style debates where evidence and testimony are critical.

        Args:
            state (DebateState): Current debate state containing all statements
                and participant role information.

        Returns:
            str: Formatted list of witness statements with speaker names,
            or indication if no witness testimony has been given yet.

        Examples:
            Formatted witness testimony::

                testimony = agent._format_witness_statements(state)
                # Returns:
                # "Dr. Smith: I observed the AI system make several errors...
                # Expert Johnson: In my professional opinion, the system...
                # Witness Brown: I was present when the incident occurred..."

            No testimony case::

                testimony = agent._format_witness_statements(state)
                # Returns: "No witness testimony yet."

        Note:
            Only includes statements from participants explicitly assigned
            the 'witness' role. Other participant types are filtered out.
        """
        witness_stmts = []

        for stmt in state.statements:
            participant = state.participants.get(stmt.speaker_id)
            if participant and participant.role == "witness":
                witness_stmts.append(f"{participant.name}: {stmt.content}")

        if not witness_stmts:
            return "No witness testimony yet."

        return "\n".join(witness_stmts)

    def extract_move(self, response: Any, role: str) -> Dict[str, Any]:
        """Extract and structure move data from engine response.

        Processes responses from AI engines or other participants, converting
        them into standardized move dictionaries that can be applied to the
        debate state. Handles different response types based on participant role
        and response format.

        Args:
            response (Any): Raw response from the participant's engine. Can be
                a Statement object, dictionary with structured data, or raw text.
            role (str): Role of the participant (affects response interpretation).
                Roles like "moderator" have special handling for actions.

        Returns:
            Dict[str, Any]: Structured move dictionary with standardized format.

            For statements:
                - type: "statement"
                - content: Text content of the statement
                - statement_type: Category (opening, rebuttal, etc.)
                - target_id: Optional target participant
                - references: Supporting evidence or citations

            For votes:
                - type: "vote"
                - vote_value: The vote decision
                - target_id: What/who is being voted on
                - reason: Explanation for the vote

            For moderation:
                - type: "moderation"
                - action: Moderator action to take
                - note: Additional context or explanation

        Examples:
            Extracting statement from structured response::

                statement = Statement(
                    content="I believe regulation is necessary",
                    statement_type="opening",
                    speaker_id="debater_1"
                )
                move = agent.extract_move(statement, "debater")
                # Returns: {
                #     "type": "statement",
                #     "content": "I believe regulation is necessary",
                #     "statement_type": "opening"
                # }

            Extracting vote from dictionary::

                response = {
                    "vote_value": "pro",
                    "target_id": "main_topic",
                    "reason": "Stronger arguments"
                }
                move = agent.extract_move(response, "judge")
                # Returns: {
                #     "type": "vote",
                #     "vote_value": "pro",
                #     "target_id": "main_topic",
                #     "reason": "Stronger arguments"
                # }

        Note:
            Fallback behavior treats any unrecognized response as a general
            statement to ensure debate flow continues even with unexpected responses.
        """
        if isinstance(response, Statement):
            # If response is already a structured Statement
            return {
                "type": "statement",
                "content": response.content,
                "statement_type": response.statement_type,
                "target_id": response.target_id,
                "references": response.references,
            }

        # Handle other response types based on role
        if isinstance(response, dict):
            if "vote_value" in response:
                return {
                    "type": "vote",
                    "vote_value": response.get("vote_value"),
                    "target_id": response.get("target_id"),
                    "reason": response.get("reason", ""),
                }
            if "action" in response and role == "moderator":
                return {
                    "type": "moderation",
                    "action": response.get("action"),
                    "note": response.get("note", ""),
                }

        # Fallback: treat as general statement
        content = str(response)
        if hasattr(response, "content"):
            content = response.content

        return {"type": "statement", "content": content, "statement_type": "general"}

    def debate_setup(self, state: Dict[str, Any]) -> Command:
        """Handle the initial debate setup and configuration phase.

        Configures participant roles, assigns moderator if specified, and
        advances the debate to the first active phase. This method applies
        configuration-based role assignments and sets up special roles like
        moderators before beginning the actual debate proceedings.

        Args:
            state (Dict[str, Any]): Current state dictionary or DebateState object
                containing initialized participants and topic information.

        Returns:
            Command: LangGraph command to transition to participant turn handling
            with updated state including role assignments and phase advancement.

        Examples:
            Setting up debate with configured roles::

                # With config.participant_roles = {
                #     "player_1": "pro", "player_2": "con", "player_3": "moderator"
                # }
                command = agent.debate_setup(state)
                # Results in participants assigned their configured roles

            Setting up with automatic moderator::

                # With config.moderator_role = True
                command = agent.debate_setup(state)
                # First player becomes moderator automatically

        Note:
            Role assignment from config takes precedence over default assignments.
            If moderator_role is enabled, the first player becomes moderator.
            Always advances to opening statements phase after setup.
        """
        state_obj = DebateState(**state) if isinstance(state, dict) else state

        # Initialize participant personas if needed
        if self.config.participant_roles:
            for player_id, role in self.config.participant_roles.items():
                if player_id in state_obj.participants:
                    state_obj.participants[player_id].role = role

        # Set moderator if configured
        if self.config.moderator_role and state_obj.players:
            moderator_id = state_obj.players[0]  # Default first player as moderator
            if moderator_id in state_obj.participants:
                state_obj.participants[moderator_id].role = "moderator"
                state_obj.moderator_id = moderator_id

        # Advance to opening phase
        updated_state = self.state_manager.advance_phase(state_obj)

        if hasattr(updated_state, "model_dump"):
            return Command(
                update=updated_state.model_dump(), goto="handle_participant_turn"
            )
        return Command(update=updated_state.dict(), goto="handle_participant_turn")

    def handle_participant_turn(self, state: Dict[str, Any]) -> Command:
        """Handle individual participant turns within the debate.

        Manages the core debate loop by processing each participant's turn,
        including context preparation, engine invocation, move extraction,
        and state updates. Handles special cases for different participant
        roles and manages error recovery to maintain debate flow.

        Args:
            state (Dict[str, Any]): Current debate state containing participant
                information, statements, phase data, and turn order.

        Returns:
            Command: LangGraph command for next step in debate flow. Can be:
            - END: If debate has concluded or game status is not ongoing
            - handle_participant_turn: Continue with next participant
            - handle_phase_transition: Advance to next debate phase

        Examples:
            Normal participant turn flow::

                command = agent.handle_participant_turn(state)
                # Processes current speaker's turn, updates state,
                # returns command for next participant or phase transition

            Handling moderator turn::

                # If current speaker is moderator, special handling applies
                command = agent.handle_participant_turn(state)
                # Moderator actions may advance phases or manage debate flow

        Note:
            Automatically handles error recovery by skipping problematic turns.
            Engine selection is based on participant role and position.
            State visualization occurs if configured in agent settings.
        """
        state_obj = DebateState(**state) if isinstance(state, dict) else state

        # Check for game end
        if (
            state_obj.game_status != "ongoing"
            or state_obj.debate_phase == DebatePhase.CONCLUSION
        ):
            if hasattr(state_obj, "model_dump"):
                return Command(update=state_obj.model_dump(), goto=END)
            return Command(update=state_obj.dict(), goto=END)

        # Get current speaker
        current_speaker = state_obj.current_speaker
        if not current_speaker:
            # No current speaker, advance phase
            updated_state = self.state_manager.advance_phase(state_obj)
            if hasattr(updated_state, "model_dump"):
                return Command(
                    update=updated_state.model_dump(), goto="handle_phase_transition"
                )
            return Command(update=updated_state.dict(), goto="handle_phase_transition")

        # Check if special handling needed for moderator
        if (
            state_obj.participants.get(
                current_speaker, Participant(id="", name="", role="")
            ).role
            == "moderator"
        ):
            updated_state = self.handle_moderator_turn(state_obj)
            next_step = self.determine_next_step(updated_state)
            if hasattr(updated_state, "model_dump"):
                return Command(update=updated_state.model_dump(), goto=next_step)
            return Command(update=updated_state.dict(), goto=next_step)

        # Process regular participant turn
        participant = state_obj.participants.get(current_speaker)
        if not participant:
            # Invalid participant, skip turn
            state_obj.current_speaker_idx = (state_obj.current_speaker_idx + 1) % len(
                state_obj.turn_order
            )
            if hasattr(state_obj, "model_dump"):
                return Command(
                    update=state_obj.model_dump(), goto="handle_participant_turn"
                )
            return Command(update=state_obj.dict(), goto="handle_participant_turn")

        # Get the appropriate engine for this role
        role = participant.role
        position = participant.position

        # Select engine based on role and position
        if role == "debater" and position in ["pro", "con"]:
            engine_key = position
        else:
            engine_key = "statement"

        engine = self.get_engine_for_player(role, engine_key)
        if not engine:
            # Fallback to default debater engine
            engine = self.get_engine_for_player("debater", "statement")

        if not engine:
            # Still no engine, skip turn
            state_obj.current_speaker_idx = (state_obj.current_speaker_idx + 1) % len(
                state_obj.turn_order
            )
            if hasattr(state_obj, "model_dump"):
                return Command(
                    update=state_obj.model_dump(), goto="handle_participant_turn"
                )
            return Command(update=state_obj.dict(), goto="handle_participant_turn")

        # Generate move
        try:
            context = self.prepare_move_context(state_obj, current_speaker)
            response = engine.invoke(context)
            move = self.extract_move(response, role)

            # Apply move
            updated_state = self.state_manager.apply_move(
                state_obj, current_speaker, move
            )

            # Check game status
            updated_state = self.state_manager.check_game_status(updated_state)

            # Determine next step
            next_step = self.determine_next_step(updated_state)

            if hasattr(updated_state, "model_dump"):
                return Command(update=updated_state.model_dump(), goto=next_step)
            return Command(update=updated_state.dict(), goto=next_step)

        except Exception as e:
            print(f"Error in participant turn: {e}")
            # Skip turn on error
            state_obj.current_speaker_idx = (state_obj.current_speaker_idx + 1) % len(
                state_obj.turn_order
            )
            if hasattr(state_obj, "model_dump"):
                return Command(
                    update=state_obj.model_dump(), goto="handle_participant_turn"
                )
            return Command(update=state_obj.dict(), goto="handle_participant_turn")

    def handle_moderator_turn(self, state: DebateState) -> DebateState:
        """Handle special processing for moderator participant turns.

        Processes moderator-specific actions including debate guidance,
        phase advancement, time management, and procedural interventions.
        Moderators have special privileges and different context preparation
        compared to regular debaters.

        Args:
            state (DebateState): Current debate state with moderator information
                and designated moderator ID.

        Returns:
            DebateState: Updated state after moderator action, with potential
            phase changes, turn order adjustments, or procedural updates.

        Examples:
            Moderator managing debate flow::

                # Moderator might receive context about phase completion
                # and decide to advance to next phase
                updated_state = agent.handle_moderator_turn(state)

            Moderator providing guidance::

                # Moderator might add guidance statement and continue
                # current phase with normal turn progression
                updated_state = agent.handle_moderator_turn(state)

        Note:
            If no moderator is designated or no moderator engine is available,
            the turn is skipped and normal turn progression continues.
            Moderator "advance_phase" actions trigger immediate phase transitions.
        """
        moderator_id = state.moderator_id
        if not moderator_id:
            # No designated moderator, skip
            state.current_speaker_idx = (state.current_speaker_idx + 1) % len(
                state.turn_order
            )
            return state

        engine = self.get_engine_for_player("moderator", "moderate")
        if not engine:
            # No moderator engine, skip
            state.current_speaker_idx = (state.current_speaker_idx + 1) % len(
                state.turn_order
            )
            return state

        try:
            context = self.prepare_move_context(state, moderator_id)
            response = engine.invoke(context)
            move = self.extract_move(response, "moderator")

            # Apply move
            updated_state = self.state_manager.apply_move(state, moderator_id, move)

            # Special handling for moderator actions
            if (
                move.get("type") == "moderation"
                and move.get("action") == "advance_phase"
            ):
                updated_state = self.state_manager.advance_phase(updated_state)

            return updated_state

        except Exception as e:
            print(f"Error in moderator turn: {e}")
            # Skip turn on error
            state.current_speaker_idx = (state.current_speaker_idx + 1) % len(
                state.turn_order
            )
            return state

    def determine_next_step(self, state: DebateState) -> str:
        """Determine the next step in the debate workflow.

        Analyzes the current debate state to decide whether to continue with
        participant turns, transition to the next phase, or end the debate.
        Uses phase-specific completion criteria to ensure proper debate flow
        and timing.

        Args:
            state (DebateState): Current debate state including phase information,
                participant data, statements, and votes.

        Returns:
            str: Next workflow step identifier:
            - END: Debate has concluded or game status is not ongoing
            - "handle_phase_transition": Current phase is complete, advance
            - "handle_participant_turn": Continue with next participant

        Examples:
            Checking phase completion::

                next_step = agent.determine_next_step(state)
                if next_step == "handle_phase_transition":
                    # All participants have given opening statements
                elif next_step == "handle_participant_turn":
                    # Continue with next speaker
                elif next_step == END:
                    # Debate has concluded

        Note:
            Phase completion criteria:
            - Opening/Closing: All participants have made statements
            - Voting: All participants have cast votes
            - Other phases: Use turn-based progression
        """
        # End if game over
        if (
            state.game_status != "ongoing"
            or state.debate_phase == DebatePhase.CONCLUSION
        ):
            return END

        # Check phase completion
        if state.debate_phase in [
            DebatePhase.OPENING_STATEMENTS,
            DebatePhase.CLOSING_STATEMENTS,
        ]:
            # Count statements in current phase
            phase_statements = [
                s
                for s in state.statements
                if getattr(s, "timestamp", "").startswith(state.debate_phase)
            ]

            participant_count = len(state.participants)
            if len(phase_statements) >= participant_count:
                return "handle_phase_transition"

        # Check if everyone has voted in voting phase
        if state.debate_phase == DebatePhase.VOTING:
            if len(state.votes) >= len(state.participants):
                return "handle_phase_transition"

        # Continue with participant turns
        return "handle_participant_turn"

    def handle_phase_transition(self, state: dict[str, Any]) -> Command:
        """Handle transition between debate phases."""
        state_obj = DebateState(**state) if isinstance(state, dict) else state

        try:
            # Advance to the next phase
            updated_state = self.state_manager.advance_phase(state_obj)

            # Reset speaker index for new phase
            updated_state.current_speaker_idx = 0

            # Check if game has ended
            if (
                updated_state.game_status != "ongoing"
                or updated_state.debate_phase == DebatePhase.CONCLUSION
            ):
                if hasattr(updated_state, "model_dump"):
                    return Command(update=updated_state.model_dump(), goto=END)
                return Command(update=updated_state.dict(), goto=END)

            # Continue with participant turns in new phase
            if hasattr(updated_state, "model_dump"):
                return Command(
                    update=updated_state.model_dump(), goto="handle_participant_turn"
                )
            return Command(update=updated_state.dict(), goto="handle_participant_turn")

        except Exception as e:
            print(f"Error in phase transition: {e}")
            # On error, end the debate
            state_obj.game_status = "ended"
            if hasattr(state_obj, "model_dump"):
                return Command(update=state_obj.model_dump(), goto=END)
            return Command(update=state_obj.dict(), goto=END)

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Visualize the current debate state."""
        if not self.config.visualize:
            return

        state_obj = state if isinstance(state, DebateState) else DebateState(**state)

        print("\n" + "=" * 60)
        print(f"🎭 DEBATE: {state_obj.topic.title}")
        print(f"📊 Phase: {state_obj.debate_phase}")
        print(f"👤 Current Speaker: {state_obj.current_speaker}")
        print("=" * 60)

        # Show recent statements
        if state_obj.statements:
            print("\n📝 Recent Statements:")
            for i, stmt in enumerate(state_obj.statements[-5:]):
                participant = state_obj.participants.get(
                    stmt.speaker_id,
                    Participant(
                        id=stmt.speaker_id,
                        name=f"Unknown-{stmt.speaker_id}",
                        role="unknown",
                    ),
                )
                print(
                    f"{i+1}. [{participant.role.upper()}] {participant.name}: {stmt.content[:100]}..."
                    if len(stmt.content) > 100
                    else f"{i+1}. [{participant.role.upper()}] {participant.name}: {stmt.content}"
                )

        # Show votes in voting phase
        if state_obj.debate_phase == DebatePhase.VOTING and state_obj.votes:
            print("\n🗳️ Current Votes:")
            for voter_id, vote_list in state_obj.votes.items():
                if not vote_list:
                    continue
                voter = state_obj.participants.get(
                    voter_id,
                    Participant(
                        id=voter_id, name=f"Unknown-{voter_id}", role="unknown"
                    ),
                )
                latest_vote = vote_list[-1]
                target = (
                    state_obj.participants.get(
                        latest_vote.target_id,
                        Participant(
                            id=latest_vote.target_id,
                            name=f"Unknown-{latest_vote.target_id}",
                            role="unknown",
                        ),
                    )
                    if latest_vote.target_id
                    else None
                )
                if target:
                    print(
                        f"- {voter.name} voted for {target.name}: {latest_vote.vote_value}"
                    )
                else:
                    print(f"- {voter.name} voted: {latest_vote.vote_value}")

        time.sleep(0.5)  # Brief pause for readability

    def setup_workflow(self) -> None:
        """Setup the debate workflow."""
        gb = DynamicGraph(
            components=[self.config], state_schema=self.config.state_schema
        )

        # Add the nodes
        gb.add_node("initialize", self.initialize_game)
        gb.add_node("debate_setup", self.debate_setup)
        gb.add_node("handle_participant_turn", self.handle_participant_turn)
        gb.add_node("handle_phase_transition", self.handle_phase_transition)

        # Add the edges
        gb.add_edge("initialize", "debate_setup")
        gb.add_edge("debate_setup", "handle_participant_turn")
        gb.add_edge("handle_participant_turn", "handle_participant_turn")
        gb.add_edge("handle_participant_turn", "handle_phase_transition")
        gb.add_edge("handle_phase_transition", "handle_participant_turn")
        gb.add_edge("handle_phase_transition", END)

        self.graph = gb.build()
