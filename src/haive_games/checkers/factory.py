from haive_games.checkers.state import CheckersState

print(CheckersState.initialize().model_dump())

from haive_games.checkers.agent import CheckersAgent, CheckersAgentConfig

a = CheckersAgent(CheckersAgentConfig())
a.run()