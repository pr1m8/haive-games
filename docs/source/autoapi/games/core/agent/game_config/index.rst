games.core.agent.game_config
============================

.. py:module:: games.core.agent.game_config

Module documentation for games.core.agent.game_config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.core.agent.game_config.Player

            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.core.agent.game_config.GameAgentConfig
      games.core.agent.game_config.GamePlayerType
      games.core.agent.game_config.PlayerType

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`, :py:obj:`abc.ABC`


            Base class for game agent configurations.


            .. py:method:: validate_players(v) -> Any
               :classmethod:


               Validate the players in the game.



            .. py:property:: num_players
               :type: int


               Get the number of players in the game.


            .. py:attribute:: players
               :type:  list[Player]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.base.models.GameState]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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


            .. py:attribute:: MultiPlayer
               :value: 'multi_player'



            .. py:attribute:: SinglePlayer
               :value: 'single_player'



            .. py:attribute:: Team
               :value: 'team'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: Player




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.agent.game_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

