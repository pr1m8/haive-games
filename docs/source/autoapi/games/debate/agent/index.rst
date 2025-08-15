games.debate.agent
==================

.. py:module:: games.debate.agent

.. autoapi-nested-parse::

   Debate Agent implementation for structured debate facilitation.

   This module provides a comprehensive debate agent that facilitates various types
   of structured debates including parliamentary, Oxford-style, and Lincoln-Douglas
   formats. The agent manages participant turns, phase transitions, moderation,
   and evaluation throughout the debate process.

   The DebateAgent uses a multi-phase workflow system with configurable timing,
   participant roles, and debate formats. It supports AI-powered participants,
   human participants, and hybrid debates with sophisticated state management.

   .. rubric:: Examples

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

   .. note::

      The agent requires properly configured engines for different participant
      roles (debater, moderator, judge) and uses the DebateStateManager for
      all state transitions and rule enforcement.


   .. autolink-examples:: games.debate.agent
      :collapse:


Classes
-------

.. autoapisummary::

   games.debate.agent.DebateAgent


Module Contents
---------------

.. py:class:: DebateAgent(config: haive.games.debate.config.DebateAgentConfig)

   Bases: :py:obj:`haive.games.framework.multi_player.MultiPlayerGameAgent`\ [\ :py:obj:`haive.games.debate.config.DebateAgentConfig`\ ]


   Intelligent agent for facilitating structured debates and discussions.

   The DebateAgent orchestrates multi-participant debates with sophisticated
   phase management, role-based interaction, and configurable formats. It handles
   participant turn management, moderator functions, voting systems, and
   comprehensive state tracking throughout the debate lifecycle.

   This agent supports various debate formats including parliamentary,
   Oxford-style, Lincoln-Douglas, and trial simulations. It can manage
   AI participants, human participants, or hybrid groups with appropriate
   context preparation and response extraction for each role.

   .. attribute:: state_manager

      Manages all debate state transitions
      and rule enforcement throughout the debate process.

      :type: DebateStateManager

   .. attribute:: config

      Configuration object containing debate format,
      timing, participant roles, and other behavioral settings.

      :type: DebateAgentConfig

   .. rubric:: Examples

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

   .. note::

      The agent requires appropriate engines to be configured for different
      participant roles. Each role (debater, moderator, judge, etc.) should
      have corresponding engine configurations in the agent setup.

   Initialize the debate agent with configuration.

   :param config: Configuration object containing debate
                  format, timing rules, participant roles, and behavioral settings.
   :type config: DebateAgentConfig

   .. note::

      The state_manager is set as a class reference and will be used
      to create instances for state management operations.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DebateAgent
      :collapse:

   .. py:method:: _extract_key_arguments(state: haive.games.debate.state.DebateState) -> str

      Extract and format key arguments from debate statements.

      Analyzes all debate statements to identify and summarize the most recent
      and significant arguments from both pro and con positions. This provides
      judges and moderators with a concise overview of the debate's core issues.

      :param state: Current debate state containing all statements
                    and participant position information.
      :type state: DebateState

      :returns: Formatted summary of key arguments with separate sections for
                pro and con positions. Shows last 3 arguments from each side,
                truncated to 100 characters for readability.
      :rtype: str

      .. rubric:: Examples

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

      .. note::

         Only includes arguments from participants with defined positions.
         Neutral participants and moderators are excluded from argument extraction.


      .. autolink-examples:: _extract_key_arguments
         :collapse:


   .. py:method:: _format_witness_statements(state: haive.games.debate.state.DebateState) -> str

      Format witness statements specifically for trial format debates.

      Extracts and formats all statements made by participants with the
      'witness' role, providing a chronological record of witness testimony
      for use in trial-style debates where evidence and testimony are critical.

      :param state: Current debate state containing all statements
                    and participant role information.
      :type state: DebateState

      :returns: Formatted list of witness statements with speaker names,
                or indication if no witness testimony has been given yet.
      :rtype: str

      .. rubric:: Examples

      Formatted witness testimony::

          testimony = agent._format_witness_statements(state)
          # Returns:
          # "Dr. Smith: I observed the AI system make several errors...
          # Expert Johnson: In my professional opinion, the system...
          # Witness Brown: I was present when the incident occurred..."

      No testimony case::

          testimony = agent._format_witness_statements(state)
          # Returns: "No witness testimony yet."

      .. note::

         Only includes statements from participants explicitly assigned
         the 'witness' role. Other participant types are filtered out.


      .. autolink-examples:: _format_witness_statements
         :collapse:


   .. py:method:: debate_setup(state: dict[str, Any]) -> langgraph.types.Command

      Handle the initial debate setup and configuration phase.

      Configures participant roles, assigns moderator if specified, and
      advances the debate to the first active phase. This method applies
      configuration-based role assignments and sets up special roles like
      moderators before beginning the actual debate proceedings.

      :param state: Current state dictionary or DebateState object
                    containing initialized participants and topic information.
      :type state: Dict[str, Any]

      :returns: LangGraph command to transition to participant turn handling
                with updated state including role assignments and phase advancement.
      :rtype: Command

      .. rubric:: Examples

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

      .. note::

         Role assignment from config takes precedence over default assignments.
         If moderator_role is enabled, the first player becomes moderator.
         Always advances to opening statements phase after setup.


      .. autolink-examples:: debate_setup
         :collapse:


   .. py:method:: determine_next_step(state: haive.games.debate.state.DebateState) -> str

      Determine the next step in the debate workflow.

      Analyzes the current debate state to decide whether to continue with
      participant turns, transition to the next phase, or end the debate.
      Uses phase-specific completion criteria to ensure proper debate flow
      and timing.

      :param state: Current debate state including phase information,
                    participant data, statements, and votes.
      :type state: DebateState

      :returns: Next workflow step identifier:
                - END: Debate has concluded or game status is not ongoing
                - "handle_phase_transition": Current phase is complete, advance
                - "handle_participant_turn": Continue with next participant
      :rtype: str

      .. rubric:: Examples

      Checking phase completion::

          next_step = agent.determine_next_step(state)
          if next_step == "handle_phase_transition":
              # All participants have given opening statements
          elif next_step == "handle_participant_turn":
              # Continue with next speaker
          elif next_step == END:
              # Debate has concluded

      .. note::

         Phase completion criteria:
         - Opening/Closing: All participants have made statements
         - Voting: All participants have cast votes
         - Other phases: Use turn-based progression


      .. autolink-examples:: determine_next_step
         :collapse:


   .. py:method:: extract_move(response: Any, role: str) -> dict[str, Any]

      Extract and structure move data from engine response.

      Processes responses from AI engines or other participants, converting
      them into standardized move dictionaries that can be applied to the
      debate state. Handles different response types based on participant role
      and response format.

      :param response: Raw response from the participant's engine. Can be
                       a Statement object, dictionary with structured data, or raw text.
      :type response: Any
      :param role: Role of the participant (affects response interpretation).
                   Roles like "moderator" have special handling for actions.
      :type role: str

      :returns: Structured move dictionary with standardized format.

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
      :rtype: Dict[str, Any]

      .. rubric:: Examples

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

      .. note::

         Fallback behavior treats any unrecognized response as a general
         statement to ensure debate flow continues even with unexpected responses.


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: get_player_role(state: haive.games.debate.state.DebateState, player_id: str) -> str

      Get the role of a specific player in the debate.

      Retrieves the assigned role for a participant from the debate state.
      Roles determine how participants interact with the debate, what context
      they receive, and how their responses are processed.

      :param state: Current debate state containing participant data.
      :type state: DebateState
      :param player_id: Unique identifier of the participant.
      :type player_id: str

      :returns: The participant's role (e.g., "debater", "moderator", "judge",
                "prosecutor", "defense", "witness"). Returns "debater" if participant
                not found or no role assigned.
      :rtype: str

      .. rubric:: Examples

      Getting participant roles::

          role = agent.get_player_role(state, "participant_1")
          if role == "moderator":
              # Handle moderator-specific logic
          elif role == "judge":
              # Handle judge-specific logic

      .. note::

         Default role is "debater" for unknown participants to ensure
         graceful handling of edge cases during debate flow.


      .. autolink-examples:: get_player_role
         :collapse:


   .. py:method:: handle_moderator_turn(state: haive.games.debate.state.DebateState) -> haive.games.debate.state.DebateState

      Handle special processing for moderator participant turns.

      Processes moderator-specific actions including debate guidance,
      phase advancement, time management, and procedural interventions.
      Moderators have special privileges and different context preparation
      compared to regular debaters.

      :param state: Current debate state with moderator information
                    and designated moderator ID.
      :type state: DebateState

      :returns: Updated state after moderator action, with potential
                phase changes, turn order adjustments, or procedural updates.
      :rtype: DebateState

      .. rubric:: Examples

      Moderator managing debate flow::

          # Moderator might receive context about phase completion
          # and decide to advance to next phase
          updated_state = agent.handle_moderator_turn(state)

      Moderator providing guidance::

          # Moderator might add guidance statement and continue
          # current phase with normal turn progression
          updated_state = agent.handle_moderator_turn(state)

      .. note::

         If no moderator is designated or no moderator engine is available,
         the turn is skipped and normal turn progression continues.
         Moderator "advance_phase" actions trigger immediate phase transitions.


      .. autolink-examples:: handle_moderator_turn
         :collapse:


   .. py:method:: handle_participant_turn(state: dict[str, Any]) -> langgraph.types.Command

      Handle individual participant turns within the debate.

      Manages the core debate loop by processing each participant's turn,
      including context preparation, engine invocation, move extraction,
      and state updates. Handles special cases for different participant
      roles and manages error recovery to maintain debate flow.

      :param state: Current debate state containing participant
                    information, statements, phase data, and turn order.
      :type state: Dict[str, Any]

      :returns: LangGraph command for next step in debate flow. Can be:
                - END: If debate has concluded or game status is not ongoing
                - handle_participant_turn: Continue with next participant
                - handle_phase_transition: Advance to next debate phase
      :rtype: Command

      .. rubric:: Examples

      Normal participant turn flow::

          command = agent.handle_participant_turn(state)
          # Processes current speaker's turn, updates state,
          # returns command for next participant or phase transition

      Handling moderator turn::

          # If current speaker is moderator, special handling applies
          command = agent.handle_participant_turn(state)
          # Moderator actions may advance phases or manage debate flow

      .. note::

         Automatically handles error recovery by skipping problematic turns.
         Engine selection is based on participant role and position.
         State visualization occurs if configured in agent settings.


      .. autolink-examples:: handle_participant_turn
         :collapse:


   .. py:method:: handle_phase_transition(state: dict[str, Any]) -> langgraph.types.Command

      Handle transition between debate phases.


      .. autolink-examples:: handle_phase_transition
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize the debate with topic, participants, and configuration.

      Sets up the initial debate state including topic validation, participant
      registration, role assignment, and format-specific configuration. This
      method handles both structured topic objects and simple string topics,
      creating a fully configured debate state ready for the setup phase.

      :param state: Initial state containing debate setup data.
                    Expected keys:
                    - topic (Union[str, Dict]): Debate topic as string or structured data
                    - participants (Union[List[str], Dict]): List of participant IDs
      :type state: Dict[str, Any]

      :returns: LangGraph command to transition to debate_setup phase with
                initialized state data.
      :rtype: Command

      .. rubric:: Examples

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

      .. note::

         If no topic is provided, defaults to "AI Ethics in Society".
         If no participants are provided, creates 4 default participants.
         Participant roles are assigned during the setup phase based on config.


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.debate.state.DebateState, player_id: str) -> dict[str, Any]

      Prepare contextual information for a participant's move.

      Generates role-specific context that provides participants with relevant
      information for making their next move. Context varies significantly based
      on participant role (debater, moderator, judge, etc.) and current debate
      phase, ensuring each participant receives appropriate information.

      :param state: Current debate state with all participants,
                    statements, votes, and phase information.
      :type state: DebateState
      :param player_id: Unique identifier of the participant whose turn it is.
      :type player_id: str

      :returns: Role-specific context dictionary containing relevant
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
      :rtype: Dict[str, Any]

      .. rubric:: Examples

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

      .. note::

         Returns empty dict if participant not found in state.
         Context is optimized for AI engines but human-readable for hybrid debates.


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: setup_workflow() -> None

      Setup the debate workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current debate state.


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: state_manager


