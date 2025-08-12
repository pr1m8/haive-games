
:py:mod:`games.debate.agent`
============================

.. py:module:: games.debate.agent

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DebateAgent {
        node [shape=record];
        "DebateAgent" [label="DebateAgent"];
        "haive.games.framework.multi_player.MultiPlayerGameAgent[haive.games.debate.config.DebateAgentConfig]" -> "DebateAgent";
      }

.. autoclass:: games.debate.agent.DebateAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.debate.agent
   :collapse:
   
.. autolink-skip:: next
