games.among_us.config
=====================

.. py:module:: games.among_us.config


Classes
-------

.. autoapisummary::

   games.among_us.config.AmongUsAgentConfig


Module Contents
---------------

.. py:class:: AmongUsAgentConfig

   Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


   Configuration for Among Us game agent.


   .. autolink-examples:: AmongUsAgentConfig
      :collapse:

   .. py:method:: _create_default_engines(values)
      :classmethod:


      Create default engines configuration.


      .. autolink-examples:: _create_default_engines
         :collapse:


   .. py:method:: casual_game(player_count: int = 6) -> AmongUsAgentConfig
      :classmethod:


      Create configuration for casual gameplay.

      Features:
      - Balanced timing for relaxed discussion
      - Standard movement speed
      - Moderate kill cooldown
      - Visualization enabled

      :param player_count: Number of players (default: 6).

      :returns: Casual game configuration.
      :rtype: AmongUsAgentConfig


      .. autolink-examples:: casual_game
         :collapse:


   .. py:method:: educational_game(player_count: int = 5) -> AmongUsAgentConfig
      :classmethod:


      Create configuration for educational/demonstration purposes.

      Features:
      - Extended discussion for learning
      - Slower pace for observation
      - Higher movement speed for clarity
      - Always show task progress

      :param player_count: Number of players (default: 5).

      :returns: Educational configuration.
      :rtype: AmongUsAgentConfig


      .. autolink-examples:: educational_game
         :collapse:


   .. py:method:: set_defaults(values)

      Set default values based on provided values.


      .. autolink-examples:: set_defaults
         :collapse:


   .. py:method:: speed_game(player_count: int = 8) -> AmongUsAgentConfig
      :classmethod:


      Create configuration for fast-paced gameplay.

      Features:
      - Short discussion and voting times
      - Fast movement speed
      - Reduced kill cooldown
      - Quick decision making

      :param player_count: Number of players (default: 8).

      :returns: Speed game configuration.
      :rtype: AmongUsAgentConfig


      .. autolink-examples:: speed_game
         :collapse:


   .. py:method:: tournament_game(player_count: int = 10) -> AmongUsAgentConfig
      :classmethod:


      Create configuration for tournament play.

      Features:
      - Extended discussion time for strategy
      - Longer voting time for careful decisions
      - Reduced kill cooldown for action
      - Competitive balance

      :param player_count: Number of players (default: 10).

      :returns: Tournament configuration.
      :rtype: AmongUsAgentConfig


      .. autolink-examples:: tournament_game
         :collapse:


   .. py:attribute:: discussion_time
      :type:  int
      :value: None



   .. py:attribute:: emergency_meetings_per_player
      :type:  int
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]] | None
      :value: None



   .. py:property:: game_balance
      :type: dict[str, Any]


      Calculate game balance metrics and recommendations.

      :returns: Balance analysis including ratios and recommendations.
      :rtype: Dict[str, Any]

      .. autolink-examples:: game_balance
         :collapse:


   .. py:attribute:: kill_cooldown
      :type:  int
      :value: None



   .. py:attribute:: llm_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: map_locations
      :type:  list[str] | None
      :value: None



   .. py:attribute:: map_name
      :type:  str
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: num_impostors
      :type:  int
      :value: None



   .. py:attribute:: player_movement_speed
      :type:  float
      :value: None



   .. py:attribute:: player_names
      :type:  list[str]
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



   .. py:attribute:: task_bar_updates
      :type:  Literal['always', 'meetings', 'never']
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



   .. py:attribute:: voting_time
      :type:  int
      :value: None



