
:py:mod:`games.debate.models`
=============================

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


.. autolink-examples:: games.debate.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.debate.models.DebateAnalysis
   games.debate.models.DebatePhase
   games.debate.models.Participant
   games.debate.models.Statement
   games.debate.models.Topic
   games.debate.models.Vote


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_DebateAnalysis {
        node [shape=record];
        "DebateAnalysis" [label="DebateAnalysis"];
        "pydantic.BaseModel" -> "DebateAnalysis";
      }

.. autopydantic_model:: games.debate.models.DebateAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebatePhase:

   .. graphviz::
      :align: center

      digraph inheritance_DebatePhase {
        node [shape=record];
        "DebatePhase" [label="DebatePhase"];
        "str" -> "DebatePhase";
        "enum.Enum" -> "DebatePhase";
      }

.. autoclass:: games.debate.models.DebatePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **DebatePhase** is an Enum defined in ``games.debate.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Participant:

   .. graphviz::
      :align: center

      digraph inheritance_Participant {
        node [shape=record];
        "Participant" [label="Participant"];
        "pydantic.BaseModel" -> "Participant";
      }

.. autopydantic_model:: games.debate.models.Participant
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Statement:

   .. graphviz::
      :align: center

      digraph inheritance_Statement {
        node [shape=record];
        "Statement" [label="Statement"];
        "pydantic.BaseModel" -> "Statement";
      }

.. autopydantic_model:: games.debate.models.Statement
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Topic:

   .. graphviz::
      :align: center

      digraph inheritance_Topic {
        node [shape=record];
        "Topic" [label="Topic"];
        "pydantic.BaseModel" -> "Topic";
      }

.. autopydantic_model:: games.debate.models.Topic
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Vote:

   .. graphviz::
      :align: center

      digraph inheritance_Vote {
        node [shape=record];
        "Vote" [label="Vote"];
        "pydantic.BaseModel" -> "Vote";
      }

.. autopydantic_model:: games.debate.models.Vote
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: games.debate.models
   :collapse:
   
.. autolink-skip:: next
