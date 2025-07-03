from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm.config import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph


class BasePlayerAgent(AgentConfig):
    engines: dict[str, AugLLMConfig]
    graph: BaseGraph | None = None

    # input_schema:
    # output_schema:
    #
    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self.engines = config.engines
        self.graph = config.graph

    def setup_workflow(self):
        if self.graph is None:
            raise ValueError("Graph is not set")
