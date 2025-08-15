games.debate.factory
====================

.. py:module:: games.debate.factory


Classes
-------

.. autoapisummary::

   games.debate.factory.DebateFactory


Module Contents
---------------

.. py:class:: DebateFactory

   Factory for creating specialized debate formats.


   .. autolink-examples:: DebateFactory
      :collapse:

   .. py:method:: create_legal_trial(case_details: dict[str, Any], participants: dict[str, str]) -> haive.games.debate.agent.DebateAgent
      :staticmethod:


      Create a legal trial format.

      :param case_details: Details of the legal case
      :param participants: Dict mapping participant IDs to roles

      :returns: Configured trial debate agent
      :rtype: DebateAgent


      .. autolink-examples:: create_legal_trial
         :collapse:


   .. py:method:: create_panel_discussion(panel_topic: str, host_name: str, panelists: list[dict[str, Any]]) -> haive.games.debate.agent.DebateAgent
      :staticmethod:


      Create a panel discussion format.

      :param panel_topic: Topic of discussion
      :param host_name: Name of panel host/moderator
      :param panelists: List of panelist details

      :returns: Configured panel discussion agent
      :rtype: DebateAgent


      .. autolink-examples:: create_panel_discussion
         :collapse:


   .. py:method:: create_presidential_debate(candidates: list[dict[str, Any]], moderator_name: str, topic: str) -> haive.games.debate.agent.DebateAgent
      :staticmethod:


      Create a presidential debate format.

      :param candidates: List of candidate details
      :param moderator_name: Name of debate moderator
      :param topic: Debate topic

      :returns: Configured presidential debate agent
      :rtype: DebateAgent


      .. autolink-examples:: create_presidential_debate
         :collapse:


   .. py:method:: create_prisoner_dilemma(prisoners: list[dict[str, Any]], scenario: str) -> haive.games.debate.agent.DebateAgent
      :staticmethod:


      Create a prisoner's dilemma simulation.

      :param prisoners: List of prisoner details
      :param scenario: Description of the dilemma scenario

      :returns: Configured prisoner's dilemma agent
      :rtype: DebateAgent


      .. autolink-examples:: create_prisoner_dilemma
         :collapse:


