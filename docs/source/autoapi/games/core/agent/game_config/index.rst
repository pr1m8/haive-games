games.core.agent.game_config
============================

.. py:module:: games.core.agent.game_config


Attributes
----------

.. autoapisummary::

   games.core.agent.game_config.Player


Classes
-------

.. autoapisummary::

   games.core.agent.game_config.GameAgentConfig
   games.core.agent.game_config.GamePlayerType
   games.core.agent.game_config.PlayerType


Module Contents
---------------

.. py:class:: GameAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`, :py:obj:`abc.ABC`


   Base class for game agent configurations.


   .. autolink-examples:: GameAgentConfig
      :collapse:

   .. py:method:: validate_players(v) -> Any
      :classmethod:


      Validate the players in the game.


      .. autolink-examples:: validate_players
         :collapse:


   .. py:property:: num_players
      :type: int


      Get the number of players in the game.

      .. autolink-examples:: num_players
         :collapse:


   .. py:attribute:: players
      :type:  list[Player]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.base.models.GameState]
      :value: None



.. py:class:: GamePlayerType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access:

     >>> Color.RED
     <Color.RED: 1>

   - value lookup:

     >>> Color(1)
     <Color.RED: 1>

   - name lookup:

     >>> Color['RED']
     <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. autolink-examples:: GamePlayerType
      :collapse:

   .. py:attribute:: MultiPlayer
      :value: 'multi_player'



   .. py:attribute:: SinglePlayer
      :value: 'single_player'



   .. py:attribute:: Team
      :value: 'team'



.. py:class:: PlayerType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerType
      :collapse:

.. py:data:: Player

