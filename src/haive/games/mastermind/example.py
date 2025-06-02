from haive.games.mastermind.agent import MastermindAgent
from haive.games.mastermind.config import MastermindConfig

a = MastermindAgent(config=MastermindConfig())
a.run_game(visualize=True)
