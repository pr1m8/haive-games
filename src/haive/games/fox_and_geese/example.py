from haive.games.fox_and_geese.agent import FoxAndGeeseAgent
from haive.games.fox_and_geese.config import FoxAndGeeseConfig

# Initialize the agent with default config
agent = FoxAndGeeseAgent(FoxAndGeeseConfig())

# Set up the workflow and run the game
agent.setup_workflow()
agent.run_game(visualize=True)
