games.debate.models
===================

.. py:module:: games.debate.models

Pydantic models for debate game components.

This module defines the core data models used in the debate game implementation,
including statements, participants, topics, votes, and debate phases. All models
use Pydantic for validation and serialization with comprehensive field documentation.

The models support various debate formats including parliamentary, Oxford-style,
and Lincoln-Douglas debates with proper type safety and validation.

.. rubric:: Examples

Creating a debate statement::

    statement = Statement(
        content="I believe AI regulation is essential for safety",
        speaker_id="participant_1",
        statement_type="opening",
        timestamp="2024-01-08T15:30:00Z"
    )

Setting up a debate topic::

    topic = Topic(
        title="AI Should Be Regulated by Government",
        description="Debate whether artificial intelligence development should be subject to government oversight",
        keywords=["artificial intelligence", "regulation", "government oversight"]
    )

Creating a participant::

    participant = Participant(
        id="debater_1",
        name="Dr. Smith",
        role="debater",
        position="pro",
        expertise=["AI ethics", "technology policy"]
    )



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">6 classes</span>   </div>

.. autoapi-nested-parse::

   Pydantic models for debate game components.

   This module defines the core data models used in the debate game implementation,
   including statements, participants, topics, votes, and debate phases. All models
   use Pydantic for validation and serialization with comprehensive field documentation.

   The models support various debate formats including parliamentary, Oxford-style,
   and Lincoln-Douglas debates with proper type safety and validation.

   .. rubric:: Examples

   Creating a debate statement::

       statement = Statement(
           content="I believe AI regulation is essential for safety",
           speaker_id="participant_1",
           statement_type="opening",
           timestamp="2024-01-08T15:30:00Z"
       )

   Setting up a debate topic::

       topic = Topic(
           title="AI Should Be Regulated by Government",
           description="Debate whether artificial intelligence development should be subject to government oversight",
           keywords=["artificial intelligence", "regulation", "government oversight"]
       )

   Creating a participant::

       participant = Participant(
           id="debater_1",
           name="Dr. Smith",
           role="debater",
           position="pro",
           expertise=["AI ethics", "technology policy"]
       )



      
            
            

.. admonition:: Classes (6)
   :class: note

   .. autoapisummary::

      games.debate.models.DebateAnalysis
      games.debate.models.DebatePhase
      games.debate.models.Participant
      games.debate.models.Statement
      games.debate.models.Topic
      games.debate.models.Vote

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebateAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Comprehensive analysis of debate performance and quality.

            This model provides structured evaluation of debate participants,
            arguments, and overall debate quality. It supports both automated
            AI analysis and human judge evaluations with detailed scoring
            and qualitative feedback.

            .. attribute:: participant_scores

               Individual performance scores.

               :type: Dict[str, float]

            .. attribute:: argument_quality

               Overall argument quality assessment.

               :type: float

            .. attribute:: engagement_level

               Participant engagement and interaction.

               :type: float

            .. attribute:: factual_accuracy

               Accuracy of claims and evidence.

               :type: float

            .. attribute:: rhetorical_effectiveness

               Persuasive power and delivery.

               :type: float

            .. attribute:: winner

               Determined winner if applicable.

               :type: Optional[str]

            .. attribute:: key_arguments

               Most significant arguments presented.

               :type: List[str]

            .. attribute:: strengths

               Notable strengths in the debate.

               :type: List[str]

            .. attribute:: weaknesses

               Areas needing improvement.

               :type: List[str]

            .. attribute:: recommendations

               Suggestions for future debates.

               :type: List[str]

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: argument_quality
               :type:  float
               :value: None



            .. py:attribute:: engagement_level
               :type:  float
               :value: None



            .. py:attribute:: factual_accuracy
               :type:  float
               :value: None



            .. py:attribute:: key_arguments
               :type:  list[str]
               :value: None



            .. py:attribute:: participant_scores
               :type:  dict[str, float]
               :value: None



            .. py:attribute:: recommendations
               :type:  list[str]
               :value: None



            .. py:attribute:: rhetorical_effectiveness
               :type:  float
               :value: None



            .. py:attribute:: strengths
               :type:  list[str]
               :value: None



            .. py:attribute:: weaknesses
               :type:  list[str]
               :value: None



            .. py:attribute:: winner
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DebatePhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Enumeration of debate phases for structured discussion flow.

            These phases represent the standard progression of formal debates,
            providing structure and ensuring all participants have appropriate
            opportunities to present arguments, respond to opponents, and reach
            conclusions. Different debate formats may use subsets of these phases.

            The phases are designed to support various debate formats including
            parliamentary, Oxford-style, Lincoln-Douglas, and custom formats
            while maintaining logical flow and fairness.

            .. attribute:: SETUP

               Initial preparation and rule establishment.

            .. attribute:: OPENING_STATEMENTS

               Initial position presentations.

            .. attribute:: DISCUSSION

               Open floor discussion and argument development.

            .. attribute:: REBUTTAL

               Direct responses to opposing arguments.

            .. attribute:: QUESTIONS

               Cross-examination and clarification phase.

            .. attribute:: CLOSING_STATEMENTS

               Final position summaries.

            .. attribute:: VOTING

               Decision-making and evaluation phase.

            .. attribute:: JUDGMENT

               Official results and analysis.

            .. attribute:: CONCLUSION

               Final wrap-up and documentation.

            .. rubric:: Examples

            Parliamentary debate flow::

                phases = [
                    DebatePhase.SETUP,
                    DebatePhase.OPENING_STATEMENTS,
                    DebatePhase.REBUTTAL,
                    DebatePhase.CLOSING_STATEMENTS,
                    DebatePhase.JUDGMENT
                ]

            Oxford-style debate::

                phases = [
                    DebatePhase.SETUP,
                    DebatePhase.OPENING_STATEMENTS,
                    DebatePhase.DISCUSSION,
                    DebatePhase.QUESTIONS,
                    DebatePhase.CLOSING_STATEMENTS,
                    DebatePhase.VOTING,
                    DebatePhase.CONCLUSION
                ]

            Lincoln-Douglas format::

                phases = [
                    DebatePhase.SETUP,
                    DebatePhase.OPENING_STATEMENTS,
                    DebatePhase.QUESTIONS,  # Cross-examination
                    DebatePhase.REBUTTAL,
                    DebatePhase.CLOSING_STATEMENTS,
                    DebatePhase.JUDGMENT
                ]

            .. note::

               Phase transitions should be managed by the debate agent to ensure
               proper timing and participant readiness. Some phases may be repeated
               (e.g., multiple rebuttal rounds) or skipped based on debate format.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:method:: get_lincoln_douglas_flow() -> list[DebatePhase]
               :classmethod:


               Get standard Lincoln-Douglas debate phase sequence.

               :returns: Ordered phases for Lincoln-Douglas format.
               :rtype: List[DebatePhase]



            .. py:method:: get_oxford_flow() -> list[DebatePhase]
               :classmethod:


               Get standard Oxford-style debate phase sequence.

               :returns: Ordered phases for Oxford format.
               :rtype: List[DebatePhase]



            .. py:method:: get_parliamentary_flow() -> list[DebatePhase]
               :classmethod:


               Get standard parliamentary debate phase sequence.

               :returns: Ordered phases for parliamentary format.
               :rtype: List[DebatePhase]



            .. py:attribute:: CLOSING_STATEMENTS
               :value: 'closing_statements'



            .. py:attribute:: CONCLUSION
               :value: 'conclusion'



            .. py:attribute:: DISCUSSION
               :value: 'discussion'



            .. py:attribute:: JUDGMENT
               :value: 'judgment'



            .. py:attribute:: OPENING_STATEMENTS
               :value: 'opening_statements'



            .. py:attribute:: QUESTIONS
               :value: 'questions'



            .. py:attribute:: REBUTTAL
               :value: 'rebuttal'



            .. py:attribute:: SETUP
               :value: 'setup'



            .. py:attribute:: VOTING
               :value: 'voting'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Participant(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a participant in the debate.

            A participant can be a debater, judge, moderator, or audience member with
            specific roles, expertise, and characteristics that influence their
            contribution to the debate. This model supports AI-powered participants
            with configurable personalities and human participants with tracked metadata.

            Participants can have positions (pro/con/neutral), expertise areas that
            inform their arguments, and personality traits that influence their
            debating style and decision-making patterns.

            .. attribute:: id

               Unique identifier for the participant.

               :type: str

            .. attribute:: name

               Display name shown in the debate interface.

               :type: str

            .. attribute:: role

               Function in the debate (debater, judge, moderator, audience).

               :type: str

            .. attribute:: position

               Stance on the topic (pro, con, neutral).

               :type: Optional[str]

            .. attribute:: persona

               Personality traits and characteristics.

               :type: Optional[Dict[str, str]]

            .. attribute:: expertise

               Subject matter expertise areas.

               :type: List[str]

            .. attribute:: bias

               Inherent bias level for realistic modeling.

               :type: Optional[float]

            .. rubric:: Examples

            Creating a pro debater::

                debater = Participant(
                    id="pro_debater_1",
                    name="Dr. Sarah Chen",
                    role="debater",
                    position="pro",
                    persona={
                        "style": "analytical",
                        "approach": "evidence-based",
                        "temperament": "calm"
                    },
                    expertise=["artificial intelligence", "technology policy", "ethics"],
                    bias=0.2
                )

            Creating a neutral moderator::

                moderator = Participant(
                    id="moderator_1",
                    name="Judge Williams",
                    role="moderator",
                    position="neutral",
                    persona={
                        "style": "formal",
                        "approach": "procedural",
                        "fairness": "strict"
                    },
                    expertise=["debate procedures", "parliamentary law"]
                )

            Creating a specialized judge::

                judge = Participant(
                    id="judge_1",
                    name="Prof. Martinez",
                    role="judge",
                    position="neutral",
                    expertise=["economics", "public policy", "data analysis"],
                    bias=-0.1
                )

            .. note::

               Bias values range from -1.0 (strongly biased toward con position)
               to +1.0 (strongly biased toward pro position), with 0.0 being
               perfectly neutral. Small bias values (±0.1 to ±0.3) create
               realistic human-like tendencies without compromising debate quality.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_position(v: str | None) -> str | None
               :classmethod:


               Validate debate position if provided.

               :param v: Position to validate.
               :type v: Optional[str]

               :returns: Validated position or None.
               :rtype: Optional[str]

               :raises ValueError: If position is not valid.



            .. py:method:: validate_role(v: str) -> str
               :classmethod:


               Validate participant role is recognized.

               :param v: Role to validate.
               :type v: str

               :returns: Validated role string.
               :rtype: str

               :raises ValueError: If role is not supported.



            .. py:attribute:: bias
               :type:  float | None
               :value: None



            .. py:attribute:: expertise
               :type:  list[str]
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: persona
               :type:  dict[str, str] | None
               :value: None



            .. py:attribute:: position
               :type:  str | None
               :value: None



            .. py:attribute:: role
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Statement(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a single statement in a debate or discussion.

            A statement is the fundamental unit of discourse in a debate, containing
            the speaker's argument, position, or response. Each statement includes
            metadata for tracking, analysis, and proper debate flow management.

            This model supports various statement types including opening statements,
            rebuttals, questions, and closing arguments. It also tracks references,
            sentiment analysis, and targeting for structured debate formats.

            .. attribute:: content

               The actual text content of the statement.

               :type: str

            .. attribute:: speaker_id

               Unique identifier of the participant making the statement.

               :type: str

            .. attribute:: target_id

               ID of targeted participant for directed statements.

               :type: Optional[str]

            .. attribute:: statement_type

               Category of statement for debate flow management.

               :type: str

            .. attribute:: references

               Citations, sources, or evidence supporting the statement.

               :type: List[str]

            .. attribute:: sentiment

               Sentiment analysis score if available.

               :type: Optional[float]

            .. attribute:: timestamp

               ISO format timestamp when the statement was made.

               :type: str

            .. rubric:: Examples

            Creating an opening statement::

                opening = Statement(
                    content="Government regulation of AI is necessary to prevent harmful outcomes",
                    speaker_id="pro_debater_1",
                    statement_type="opening",
                    references=["AI Safety Research Paper 2024"],
                    timestamp="2024-01-08T15:30:00Z"
                )

            Creating a rebuttal with targeting::

                rebuttal = Statement(
                    content="The previous speaker's concerns about innovation are unfounded",
                    speaker_id="con_debater_1",
                    target_id="pro_debater_1",
                    statement_type="rebuttal",
                    timestamp="2024-01-08T15:35:00Z"
                )

            Creating a question::

                question = Statement(
                    content="Can you provide specific examples of AI harm that regulation would prevent?",
                    speaker_id="moderator",
                    target_id="pro_debater_1",
                    statement_type="question",
                    timestamp="2024-01-08T15:40:00Z"
                )

            .. note::

               Statement types should follow debate format conventions. Common types
               include: "opening", "rebuttal", "question", "answer", "closing",
               "point_of_information", "point_of_order".

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_content(v: str) -> str
               :classmethod:


               Validate statement content is not empty and properly formatted.

               :param v: Content to validate.
               :type v: str

               :returns: Cleaned and validated content.
               :rtype: str

               :raises ValueError: If content is empty or contains only whitespace.



            .. py:method:: validate_timestamp(v: str) -> str
               :classmethod:


               Validate timestamp is in proper ISO format.

               :param v: Timestamp string to validate.
               :type v: str

               :returns: Validated timestamp string.
               :rtype: str

               :raises ValueError: If timestamp format is invalid.



            .. py:attribute:: content
               :type:  str
               :value: None



            .. py:attribute:: references
               :type:  list[str]
               :value: None



            .. py:attribute:: sentiment
               :type:  float | None
               :value: None



            .. py:attribute:: speaker_id
               :type:  str
               :value: None



            .. py:attribute:: statement_type
               :type:  str
               :value: None



            .. py:attribute:: target_id
               :type:  str | None
               :value: None



            .. py:attribute:: timestamp
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Topic(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a debate topic or resolution.

            A topic defines the subject matter for a debate, including the resolution
            to be argued, background context, and any constraints or guidelines for
            the discussion. Topics can range from simple yes/no propositions to
            complex policy discussions.

            This model supports various debate formats by allowing flexible topic
            definition with keywords for research and constraints for format-specific
            rules or limitations.

            .. attribute:: title

               The main resolution or question being debated.

               :type: str

            .. attribute:: description

               Detailed background and context for the topic.

               :type: str

            .. attribute:: keywords

               Key terms for research and fact-checking.

               :type: List[str]

            .. attribute:: constraints

               Format-specific rules or limitations.

               :type: Optional[Dict[str, str]]

            .. rubric:: Examples

            Simple policy topic::

                topic = Topic(
                    title="This House Believes That Social Media Does More Harm Than Good",
                    description="Debate the overall impact of social media platforms on society, considering both benefits and drawbacks",
                    keywords=["social media", "mental health", "democracy", "privacy"],
                    constraints={"time_limit": "8 minutes per speaker", "format": "Oxford"}
                )

            Technical topic with research areas::

                topic = Topic(
                    title="AI Development Should Prioritize Safety Over Speed",
                    description="Consider whether artificial intelligence research should emphasize safety measures even if it slows development",
                    keywords=["AI safety", "research ethics", "technological progress", "risk assessment"],
                    constraints={
                        "evidence_required": "true",
                        "fact_checking": "enabled",
                        "research_time": "30 minutes"
                    }
                )

            Philosophical topic::

                topic = Topic(
                    title="Justice Ought to Take Precedence Over Security",
                    description="A philosophical examination of the tension between individual rights and collective safety",
                    keywords=["justice", "security", "individual rights", "social contract"],
                    constraints={"format": "Lincoln-Douglas", "framework_required": "true"}
                )

            .. note::

               Topic titles should be clear, debatable propositions. For formal debates,
               use standard resolution formats like "This House Believes..." or
               "Resolved: ..." depending on the debate format.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_keywords(v: list[str]) -> list[str]
               :classmethod:


               Validate and clean keyword list.

               :param v: Keywords to validate.
               :type v: List[str]

               :returns: Cleaned list of non-empty keywords.
               :rtype: List[str]



            .. py:method:: validate_title(v: str) -> str
               :classmethod:


               Validate topic title is properly formatted.

               :param v: Title to validate.
               :type v: str

               :returns: Cleaned and validated title.
               :rtype: str

               :raises ValueError: If title is too short or improperly formatted.



            .. py:attribute:: constraints
               :type:  dict[str, str] | None
               :value: None



            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: keywords
               :type:  list[str]
               :value: None



            .. py:attribute:: title
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Vote(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a vote or evaluation from a participant.

            Votes are used for various purposes in debates including final judgments,
            audience polling, quality ratings, and procedural decisions. The flexible
            vote_value field supports different voting systems (binary, numeric, ranked).

            Votes can target specific participants (for best speaker awards), statements
            (for argument quality), or the overall debate topic (for winner determination).
            The reasoning field provides transparency and educational value.

            .. attribute:: voter_id

               Unique identifier of the participant casting the vote.

               :type: str

            .. attribute:: vote_value

               The actual vote (yes/no, 1-10, ranking).

               :type: Union[str, int, float]

            .. attribute:: target_id

               What/who is being voted on (participant, statement, topic).

               :type: Optional[str]

            .. attribute:: reason

               Explanation or justification for the vote.

               :type: Optional[str]

            .. rubric:: Examples

            Binary topic vote::

                topic_vote = Vote(
                    voter_id="judge_1",
                    vote_value="pro",
                    target_id="main_topic",
                    reason="The pro side provided more compelling evidence and stronger logical arguments"
                )

            Numeric quality rating::

                quality_vote = Vote(
                    voter_id="audience_member_3",
                    vote_value=8.5,
                    target_id="statement_15",
                    reason="Excellent use of data and clear reasoning, but could have addressed counterarguments"
                )

            Best speaker vote::

                speaker_vote = Vote(
                    voter_id="judge_2",
                    vote_value="winner",
                    target_id="pro_debater_1",
                    reason="Outstanding rhetorical skills and effective rebuttal strategy"
                )

            Procedural vote::

                procedural_vote = Vote(
                    voter_id="moderator",
                    vote_value="approve",
                    target_id="time_extension_request",
                    reason="Complex topic warrants additional time for thorough discussion"
                )

            .. note::

               Vote values should be consistent within each voting context. Use
               strings for categorical votes ("pro", "con", "abstain"), numbers
               for ratings (1-10 scales), and structured data for ranked choices.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_vote_value(v: str | int | float) -> str | int | float
               :classmethod:


               Validate vote value is reasonable.

               :param v: Vote value to validate.
               :type v: Union[str, int, float]

               :returns: Validated vote value.
               :rtype: Union[str, int, float]

               :raises ValueError: If vote value is invalid.



            .. py:attribute:: reason
               :type:  str | None
               :value: None



            .. py:attribute:: target_id
               :type:  str | None
               :value: None



            .. py:attribute:: vote_value
               :type:  str | int | float
               :value: None



            .. py:attribute:: voter_id
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

