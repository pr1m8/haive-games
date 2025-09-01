games.debate.models
===================

.. py:module:: games.debate.models

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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/debate/models/DebateAnalysis
   /autoapi/games/debate/models/DebatePhase
   /autoapi/games/debate/models/Participant
   /autoapi/games/debate/models/Statement
   /autoapi/games/debate/models/Topic
   /autoapi/games/debate/models/Vote

.. autoapisummary::

   games.debate.models.DebateAnalysis
   games.debate.models.DebatePhase
   games.debate.models.Participant
   games.debate.models.Statement
   games.debate.models.Topic
   games.debate.models.Vote


