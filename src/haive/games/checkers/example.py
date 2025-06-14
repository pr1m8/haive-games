from haive.games.checkers.agent import CheckersAgent, CheckersAgentConfig
from haive.games.checkers.state import CheckersState

# print(CheckersState.initialize().model_dump())


a = CheckersAgent(CheckersAgentConfig())
a.run_game()
