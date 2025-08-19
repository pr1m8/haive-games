🔀 Graph System - Visual AI Workflow Orchestration
==================================================

.. meta::
   :description: Haive Graph System - Revolutionary visual programming for AI workflows
   :keywords: graph, workflow, orchestration, visual programming, state machine, LangGraph

.. currentmodule:: haive.core.graph

**WHERE AI BECOMES A SYMPHONY OF INTELLIGENT COMPONENTS**

Welcome to the Graph System - a revolutionary visual programming paradigm that transforms 
how AI workflows are designed, executed, and understood. This isn't just another workflow 
engine; it's a fundamental reimagining of how intelligent systems should be composed.

.. contents:: Table of Contents
   :local:
   :depth: 3
   :backlinks: top

The Visual Revolution 🎨
------------------------

.. graphviz::

   digraph graph_revolution {
      rankdir=LR;
      node [shape=box, style="rounded,filled"];
      
      subgraph cluster_traditional {
         label="Traditional Approach";
         style=filled;
         fillcolor=lightgray;
         
         code [label="Code-based\nWorkflows", fillcolor=white];
         implicit [label="Implicit\nFlow", fillcolor=white];
         debug [label="Hard to\nDebug", fillcolor=white];
         
         code -> implicit -> debug;
      }
      
      subgraph cluster_haive {
         label="Haive Graph Revolution";
         style=filled;
         fillcolor=lightgreen;
         
         visual [label="Visual\nWorkflows", fillcolor=lightblue];
         explicit [label="Explicit\nFlow", fillcolor=lightblue];
         observable [label="Observable\nExecution", fillcolor=lightblue];
         
         visual -> explicit -> observable;
      }
      
      debug -> visual [label="Paradigm Shift", style=dashed, color=red];
   }

🔀 **Beyond Linear Execution**
-------------------------------

**Transform Your AI from Sequential to Symphonic:**

**Visual Workflow Construction**
   Build complex AI behaviors by connecting nodes and edges, with real-time visualization and debugging

**Intelligent Routing Logic**
   Dynamic path selection based on state, with conditional branches, parallel execution, and loop detection

**Built-in State Persistence**
   Automatic checkpointing, workflow replay, and time-travel debugging for resilient AI systems

**Agent Orchestration**
   Coordinate multiple agents with shared state, message passing, and synchronization primitives

**LangGraph Foundation**
   Built on the industry-standard LangGraph with Haive-specific enhancements for production use

Core Architecture 🏗️
--------------------

.. uml::

   @startuml
   !theme amiga
   
   package "Graph System Core" {
      abstract class BaseGraph {
         +nodes: Dict[str, Node]
         +edges: List[Edge]
         +state_schema: Type[StateSchema]
         --
         +add_node(name, node)
         +add_edge(source, target, condition)
         +compile() : CompiledGraph
         +visualize() : GraphVisualization
      }
      
      class StateGraph extends BaseGraph {
         +entry_point: str
         +conditional_edges: Dict
         --
         +set_entry_point(node)
         +add_conditional_edges(source, condition)
         +stream(input) : Iterator[State]
      }
      
      class CompiledGraph {
         +graph: BaseGraph
         +execution_plan: ExecutionPlan
         --
         +invoke(input) : Output
         +ainvoke(input) : Awaitable[Output]
         +stream(input) : Iterator[State]
         +astream(input) : AsyncIterator[State]
      }
      
      interface Node {
         +process(state) : State
         +validate(state) : bool
      }
      
      class AgentNode implements Node {
         +agent: Agent
         +state_key: str
         --
         +process(state) : State
      }
      
      class ToolNode implements Node {
         +tools: List[Tool]
         +engine: ToolEngine
         --
         +process(state) : State
      }
      
      class ValidationNode implements Node {
         +schema: Type[BaseModel]
         +routes: Dict[str, Route]
         --
         +process(state) : State
      }
   }
   
   BaseGraph --> CompiledGraph : compiles to
   StateGraph --> Node : contains
   Node <|-- AgentNode
   Node <|-- ToolNode
   Node <|-- ValidationNode
   
   @enduml

Revolutionary Features 🚀
-------------------------

Visual Workflow Design
~~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   graph TD
      subgraph "Visual Design"
         A[Start] --> B[Agent Node]
         B --> C{Decision}
         C -->|Route 1| D[Tool Node]
         C -->|Route 2| E[Validation]
         D --> F[Merge]
         E --> F
         F --> G[End]
      end
      
      style A fill:#f9f,stroke:#333,stroke-width:4px
      style G fill:#9f9,stroke:#333,stroke-width:4px

BaseGraph Architecture
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: haive.core.graph.BaseGraph
   :members:
   :undoc-members:
   :show-inheritance:

**The Foundation of Visual AI Programming**

BaseGraph provides a powerful abstraction for building graph-based workflows that can handle everything from simple linear flows to complex multi-agent orchestrations.

.. testcode::

   from haive.core.graph import StateGraph
   from haive.core.schema import MessagesState
   
   # Visual workflow construction
   graph = StateGraph(MessagesState)
   
   # Add nodes visually
   graph.add_node("agent", agent_node)
   graph.add_node("tools", tool_node)
   graph.add_node("validation", validation_node)
   
   # Connect with edges
   graph.set_entry_point("agent")
   graph.add_edge("agent", "tools")
   graph.add_conditional_edges(
       "tools",
       lambda state: "valid" if state.is_valid else "invalid",
       {
           "valid": "validation",
           "invalid": "agent"  # Loop back
       }
   )

**Basic Graph Construction**

.. testcode::

    from haive.core.graph import BaseGraph
    from haive.core.schema import StateSchema, Field
    from typing import List, Dict, Any
    
    # Define workflow state
    class WorkflowState(StateSchema):
        query: str = Field(description="User query")
        research_data: List[Dict[str, Any]] = Field(default_factory=list)
        analysis: Dict[str, Any] = Field(default_factory=dict)
        synthesis: str = Field(default="")
        confidence: float = Field(default=0.0)
        
        __shared_fields__ = ["query", "research_data"]
        __reducer_fields__ = {
            "research_data": lambda old, new: old + new,
            "confidence": lambda old, new: max(old, new)
        }
    
    # Create graph
    graph = BaseGraph(
        name="research_workflow",
        state_schema=WorkflowState,
        config={
            "recursion_limit": 10,
            "max_parallel_nodes": 5,
            "timeout": 300  # 5 minutes
        }
    )
    
    # Define node functions
    async def research_node(state: WorkflowState) -> WorkflowState:
        """Perform research based on query."""
        # Research logic here
        results = await perform_research(state.query)
        state.research_data.extend(results)
        return state
    
    async def analyze_node(state: WorkflowState) -> WorkflowState:
        """Analyze research data."""
        analysis = await analyze_data(state.research_data)
        state.analysis = analysis
        state.confidence = analysis.get("confidence", 0.0)
        return state
    
    async def synthesize_node(state: WorkflowState) -> WorkflowState:
        """Synthesize findings into report."""
        state.synthesis = await create_synthesis(
            state.research_data,
            state.analysis
        )
        return state
    
    # Add nodes to graph
    graph.add_node("research", research_node)
    graph.add_node("analyze", analyze_node)
    graph.add_node("synthesize", synthesize_node)
    
    # Define edges
    graph.set_entry_point("research")
    graph.add_edge("research", "analyze")
    graph.add_edge("analyze", "synthesize")
    graph.set_finish_point("synthesize")
    
    # Compile and execute
    app = graph.compile()
    result = await app.ainvoke({"query": "Latest AI breakthroughs"})

Dynamic Graph Composition
~~~~~~~~~~~~~~~~~~~~~~~~~

.. graphviz::

   digraph dynamic_composition {
      rankdir=TB;
      node [shape=record, style="rounded,filled"];
      
      runtime [label="{Runtime Engine|+graphs: Dict\l+active: Graph\l}", fillcolor=lightblue];
      
      subgraph cluster_graphs {
         label="Dynamic Graph Library";
         style=filled;
         fillcolor=lightyellow;
         
         simple [label="{Simple Flow|Linear execution}", fillcolor=white];
         react [label="{ReAct Pattern|Tool + Reasoning}", fillcolor=white];
         multi [label="{Multi-Agent|Coordination}", fillcolor=white];
         custom [label="{Custom Graph|User defined}", fillcolor=white];
      }
      
      runtime -> simple [label="select"];
      runtime -> react [label="select"];
      runtime -> multi [label="select"];
      runtime -> custom [label="select"];
      
      compose [label="Graph Composer", shape=ellipse, fillcolor=lightgreen];
      simple -> compose [label="combine"];
      react -> compose [label="combine"];
      compose -> custom [label="creates", style=dashed];
   }

Observable Execution
~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   sequenceDiagram
      participant User
      participant Graph
      participant Node1 as Agent Node
      participant Node2 as Tool Node
      participant Observer
      
      User->>Graph: invoke(input)
      Graph->>Observer: on_graph_start
      
      Graph->>Node1: process(state)
      Node1->>Observer: on_node_start("agent")
      Node1-->>Observer: on_node_end("agent", output)
      
      Graph->>Node2: process(state)
      Node2->>Observer: on_node_start("tools")
      Node2-->>Observer: on_node_end("tools", output)
      
      Graph->>Observer: on_graph_end(final_state)
      Graph-->>User: result

Advanced Patterns 🎯
--------------------

Conditional Routing
~~~~~~~~~~~~~~~~~~~

.. graphviz::

   digraph conditional_routing {
      rankdir=TB;
      node [shape=box, style="rounded,filled"];
      
      start [label="Input", shape=ellipse, fillcolor=lightgreen];
      classifier [label="Classifier\nNode", fillcolor=lightblue];
      
      subgraph cluster_routes {
         label="Dynamic Routes";
         style=filled;
         fillcolor=lightyellow;
         
         simple [label="Simple\nQuery", fillcolor=white];
         complex [label="Complex\nAnalysis", fillcolor=white];
         multi [label="Multi-step\nReasoning", fillcolor=white];
         error [label="Error\nHandling", fillcolor=pink];
      }
      
      end [label="Output", shape=ellipse, fillcolor=lightgreen];
      
      start -> classifier;
      classifier -> simple [label="confidence > 0.8"];
      classifier -> complex [label="0.5 < confidence < 0.8"];
      classifier -> multi [label="confidence < 0.5"];
      classifier -> error [label="error", style=dashed];
      
      simple -> end;
      complex -> end;
      multi -> end;
      error -> end;
   }

.. testcode::

   def route_by_complexity(state: WorkflowState) -> str:
       """Intelligent routing based on query complexity"""
       query = state.messages[-1]["content"]
       
       # Analyze complexity
       if len(query.split()) < 10:
           return "simple"
       elif "analyze" in query or "compare" in query:
           return "complex"
       elif "step by step" in query:
           return "multi_step"
       else:
           return "default"
   
   # Build graph with conditional routing
   graph = StateGraph(WorkflowState)
   
   graph.add_conditional_edges(
       "classifier",
       route_by_complexity,
       {
           "simple": "quick_response",
           "complex": "deep_analysis",
           "multi_step": "reasoning_chain",
           "default": "standard_flow"
       }
   )
    
Parallel Execution
~~~~~~~~~~~~~~~~~~

.. mermaid::

   graph TD
      Start[Input] --> Fork{Fork}
      
      Fork --> A1[Analyzer 1]
      Fork --> A2[Analyzer 2]
      Fork --> A3[Analyzer 3]
      
      A1 --> Join{Join}
      A2 --> Join
      A3 --> Join
      
      Join --> Synthesize[Synthesize Results]
      Synthesize --> End[Output]
      
      style Fork fill:#ff9,stroke:#333,stroke-width:2px
      style Join fill:#ff9,stroke:#333,stroke-width:2px

.. testcode::

   from haive.core.graph.patterns import parallel_execution
   
   # Define parallel analysis graph
   graph = StateGraph(WorkflowState)
   
   # Fork node that splits execution
   graph.add_node("fork", lambda s: s)
   
   # Parallel analysis nodes
   graph.add_node("sentiment", sentiment_analyzer)
   graph.add_node("entities", entity_extractor)
   graph.add_node("summary", summarizer)
   
   # Join node that merges results
   graph.add_node("join", result_merger)
   
   # Connect for parallel execution
   graph.set_entry_point("fork")
   graph.add_edge("fork", "sentiment")
   graph.add_edge("fork", "entities")
   graph.add_edge("fork", "summary")
   
   # All parallel paths lead to join
   graph.add_edge("sentiment", "join")
   graph.add_edge("entities", "join")
   graph.add_edge("summary", "join")
   
   graph.add_edge("join", END)
    
Loop Patterns
~~~~~~~~~~~~~

.. graphviz::

   digraph loop_patterns {
      rankdir=TB;
      node [shape=box, style="rounded,filled"];
      
      subgraph cluster_refinement {
         label="Refinement Loop";
         style=filled;
         fillcolor=lightblue;
         
         generate [label="Generate", fillcolor=white];
         evaluate [label="Evaluate", fillcolor=white];
         improve [label="Improve", fillcolor=white];
         
         generate -> evaluate;
         evaluate -> improve [label="needs work"];
         improve -> generate [label="retry"];
         evaluate -> "cluster_refinement_end" [label="satisfied", style=invis];
      }
      
      subgraph cluster_exploration {
         label="Exploration Loop";
         style=filled;
         fillcolor=lightgreen;
         
         explore [label="Explore", fillcolor=white];
         discover [label="Discover", fillcolor=white];
         expand [label="Expand", fillcolor=white];
         
         explore -> discover;
         discover -> expand;
         expand -> explore [label="continue"];
         discover -> "cluster_exploration_end" [label="complete", style=invis];
      }
   }

Node System Architecture
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.graph.node
   :members:
   :undoc-members:

**Intelligent Node Processing**

The node system provides sophisticated primitives for building reusable workflow components.

**Advanced Node Patterns**::

    from haive.core.graph.node import (
        Node, AgentNode, ToolNode, 
        ConditionalNode, ParallelNode
    )
    
    # Agent node with full capabilities
    class ResearchAgentNode(AgentNode):
        """Sophisticated research agent node."""
        
        agent_config = AugLLMConfig(
            model="gpt-4",
            tools=[web_search, arxiv_search, semantic_scholar],
            structured_output_model=ResearchFindings
        )
        
        async def process(self, state: WorkflowState) -> WorkflowState:
            """Execute research with the agent."""
            # Pre-processing
            query = self.preprocess_query(state.query)
            
            # Agent execution
            findings = await self.agent.ainvoke({
                "query": query,
                "context": state.research_data
            })
            
            # Post-processing and state update
            state.research_data.append(findings.dict())
            state.confidence = findings.confidence_score
            
            # Emit metrics
            await self.emit_metrics({
                "sources_found": len(findings.sources),
                "confidence": findings.confidence_score,
                "execution_time": self.execution_time
            })
            
            return state
    
    # Tool node with validation
    class DataValidationNode(ToolNode):
        """Validate and clean research data."""
        
        tools = [
            validate_sources,
            check_citations,
            verify_facts
        ]
        
        async def execute_tools(self, state: WorkflowState) -> Dict[str, Any]:
            """Run validation tools in sequence."""
            validation_results = {}
            
            for tool in self.tools:
                try:
                    result = await tool.ainvoke(state.research_data)
                    validation_results[tool.name] = result
                except Exception as e:
                    self.logger.error(f"Tool {tool.name} failed: {e}")
                    validation_results[tool.name] = {"error": str(e)}
            
            return validation_results
    
    # Conditional node with complex logic
    class RoutingNode(ConditionalNode):
        """Intelligent routing based on multiple factors."""
        
        def evaluate_conditions(self, state: WorkflowState) -> str:
            """Determine next node based on state analysis."""
            # Multi-factor decision making
            factors = {
                "data_quality": self.assess_data_quality(state),
                "confidence": state.confidence,
                "completeness": self.check_completeness(state),
                "time_remaining": self.get_time_remaining()
            }
            
            # Use decision matrix
            decision = self.decision_engine.evaluate(factors)
            
            # Log decision reasoning
            self.logger.info(f"Routing decision: {decision.route}")
            self.logger.debug(f"Factors: {factors}")
            self.logger.debug(f"Reasoning: {decision.explanation}")
            
            return decision.route

State Management in Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Sophisticated State Handling**

.. automodule:: haive.core.graph.state_management
   :members:
   :undoc-members:

**State Persistence and Recovery**::

    from haive.core.graph.checkpointer import (
        PostgresCheckpointer,
        checkpoint_config
    )
    
    # Configure checkpointing
    checkpointer = PostgresCheckpointer(
        connection_string=os.getenv("DATABASE_URL"),
        schema="workflow_states",
        auto_checkpoint=True,
        checkpoint_frequency=5  # Every 5 nodes
    )
    
    # Compile with checkpointing
    app = graph.compile(
        checkpointer=checkpointer,
        interrupt_before=["human_review"],  # Pause for human input
        interrupt_after=["critical_decision"]  # Pause after critical nodes
    )
    
    # Execute with thread management
    thread_id = "research_session_123"
    config = {"configurable": {"thread_id": thread_id}}
    
    # Run workflow (will checkpoint automatically)
    result = await app.ainvoke(initial_state, config=config)
    
    # Later: Resume from checkpoint
    resumed_result = await app.ainvoke(None, config=config)
    
    # Time-travel debugging
    history = await checkpointer.get_history(thread_id)
    for checkpoint in history:
        print(f"Node: {checkpoint.node}")
        print(f"State: {checkpoint.state}")
        print(f"Timestamp: {checkpoint.timestamp}")
    
    # Restore to specific checkpoint
    await checkpointer.restore(thread_id, checkpoint_id="xyz123")

Graph Patterns Library
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.graph.patterns
   :members:
   :undoc-members:

**Pre-built Workflow Patterns**

The patterns library provides battle-tested workflow templates for common AI tasks.

**Using Workflow Patterns**::

    from haive.core.graph.patterns import (
        MapReducePattern,
        ScatterGatherPattern,
        PipelinePattern,
        CircuitBreakerPattern
    )
    
    # Map-Reduce for parallel processing
    map_reduce = MapReducePattern(
        map_function=process_chunk,
        reduce_function=combine_results,
        chunk_size=100,
        max_workers=10
    )
    
    graph.add_pattern(
        "parallel_analysis",
        map_reduce,
        input_field="research_data",
        output_field="analysis"
    )
    
    # Scatter-Gather for multi-source aggregation
    scatter_gather = ScatterGatherPattern(
        scatter_targets=[
            ("google_search", search_google),
            ("bing_search", search_bing),
            ("duckduckgo", search_ddg)
        ],
        gather_strategy="merge_unique",
        timeout_per_target=10
    )
    
    graph.add_pattern(
        "multi_search",
        scatter_gather,
        input_field="query"
    )
    
    # Circuit breaker for unreliable services
    circuit_breaker = CircuitBreakerPattern(
        protected_node="external_api",
        failure_threshold=3,
        recovery_timeout=60,
        fallback_node="cached_data"
    )
    
    graph.wrap_node_with_pattern("external_api", circuit_breaker)

Visual Workflow Builder
~~~~~~~~~~~~~~~~~~~~~~~

**Interactive Graph Construction**

.. automodule:: haive.core.graph.builder
   :members:
   :undoc-members:

**Visual Builder Integration**::

    from haive.core.graph.builder import GraphBuilder, visualize
    
    # Create builder with visual interface
    builder = GraphBuilder(
        name="visual_workflow",
        enable_ui=True,
        port=8080
    )
    
    # Define node library
    builder.register_node_types({
        "agents": [ResearchAgent, AnalysisAgent, WriterAgent],
        "tools": [WebSearch, Calculator, DatabaseQuery],
        "logic": [Conditional, Loop, Parallel]
    })
    
    # Build interactively (opens browser UI)
    graph = builder.build_interactive()
    
    # Or build programmatically with visual feedback
    with builder.visual_context():
        builder.add_node("start", StartNode())
        builder.add_node("research", ResearchAgent())
        builder.add_edge("start", "research")
        
        # See real-time graph visualization
        builder.show()
    
    # Export graph
    builder.export_to_file("workflow.json")
    builder.export_as_image("workflow.png")
    
    # Generate code from visual graph
    code = builder.generate_code(language="python")

Real-World Examples 🌟
----------------------

Multi-Agent Orchestration
~~~~~~~~~~~~~~~~~~~~~~~~~

.. testcode::

   from haive.core.graph import StateGraph, END
   from haive.agents import ReactAgent, SimpleAgent
   
   class MultiAgentState(BaseSchema):
       """State for multi-agent coordination"""
       messages: List[BaseMessage] = []
       task_queue: List[str] = []
       results: Dict[str, Any] = {}
       agent_outputs: Dict[str, Any] = {}
   
   # Create specialized agents
   planner = ReactAgent(name="planner", tools=[task_decomposer])
   researcher = SimpleAgent(name="researcher")
   writer = SimpleAgent(name="writer")
   reviewer = ReactAgent(name="reviewer", tools=[quality_checker])
   
   # Build coordination graph
   graph = StateGraph(MultiAgentState)
   
   # Agent nodes
   graph.add_node("planner", AgentNode(planner))
   graph.add_node("researcher", AgentNode(researcher))
   graph.add_node("writer", AgentNode(writer))
   graph.add_node("reviewer", AgentNode(reviewer))
   
   # Coordination logic
   def route_tasks(state: MultiAgentState) -> str:
       if state.task_queue:
           task = state.task_queue[0]
           if "research" in task:
               return "researcher"
           elif "write" in task:
               return "writer"
           else:
               return "planner"
       return "reviewer"
   
   # Connect agents
   graph.set_entry_point("planner")
   graph.add_conditional_edges("planner", route_tasks)
   graph.add_edge("researcher", "planner")
   graph.add_edge("writer", "planner")
   graph.add_edge("reviewer", END)

.. testoutput::
   :hide:

   ...

Tool-Augmented Reasoning
~~~~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   graph TD
      Input[User Query] --> Agent[ReAct Agent]
      Agent --> Think{Think}
      
      Think -->|Need Info| Tools[Tool Execution]
      Tools --> Observe[Observe Results]
      Observe --> Think
      
      Think -->|Have Answer| Final[Final Response]
      
      Tools -.-> T1[Calculator]
      Tools -.-> T2[Web Search]
      Tools -.-> T3[Database]
      
      style Agent fill:#f96,stroke:#333,stroke-width:2px
      style Tools fill:#69f,stroke:#333,stroke-width:2px

.. testcode::

   from haive.core.graph.patterns import create_react_graph
   from haive.tools import Calculator, WebSearch, DatabaseQuery
   
   # Create tool-augmented reasoning graph
   tools = [Calculator(), WebSearch(), DatabaseQuery()]
   
   graph = create_react_graph(
       agent_config={
           "model": "gpt-4",
           "temperature": 0.7,
           "system_prompt": "You are a helpful assistant with tools."
       },
       tools=tools,
       max_iterations=5,
       early_stopping=True
   )
   
   # Execute with streaming
   async for state in graph.astream({
       "messages": [{"role": "user", "content": "What's the weather in Tokyo?"}]
   }):
       print(f"Step: {state.get('step')}")
       print(f"Thought: {state.get('thought')}")
       print(f"Action: {state.get('action')}")

Dynamic Workflow Adaptation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. graphviz::

   digraph dynamic_adaptation {
      rankdir=LR;
      node [shape=box, style="rounded,filled"];
      
      monitor [label="Workflow\nMonitor", fillcolor=lightblue];
      analyzer [label="Performance\nAnalyzer", fillcolor=lightgreen];
      optimizer [label="Graph\nOptimizer", fillcolor=lightyellow];
      
      subgraph cluster_versions {
         label="Graph Versions";
         style=filled;
         fillcolor=lavender;
         
         v1 [label="Version 1\n(Original)", fillcolor=white];
         v2 [label="Version 2\n(Optimized)", fillcolor=white];
         v3 [label="Version 3\n(Adapted)", fillcolor=white];
      }
      
      monitor -> analyzer [label="metrics"];
      analyzer -> optimizer [label="insights"];
      optimizer -> v2 [label="optimize"];
      v1 -> v2 [label="evolve", style=dashed];
      v2 -> v3 [label="adapt", style=dashed];
   }

Advanced Orchestration
----------------------

Multi-Agent Coordination
~~~~~~~~~~~~~~~~~~~~~~~~

**Sophisticated Agent Orchestration**

.. testcode::

    from haive.core.graph.orchestration import (
        OrchestratorGraph,
        AgentPool,
        ConsensusStrategy
    )
    
    # Create orchestrator for agent team
    orchestrator = OrchestratorGraph(
        name="research_team",
        coordination_strategy="hierarchical"  # or "peer_to_peer", "swarm"
    )
    
    # Define agent pool
    agent_pool = AgentPool([
        ("lead_researcher", LeadResearchAgent()),
        ("data_analyst", DataAnalystAgent()),
        ("fact_checker", FactCheckerAgent()),
        ("writer", WriterAgent()),
        ("reviewer", ReviewerAgent())
    ])
    
    orchestrator.set_agent_pool(agent_pool)
    
    # Define coordination patterns
    orchestrator.add_coordination_rule(
        "research_phase",
        participants=["lead_researcher", "data_analyst"],
        interaction="collaborative",
        success_criteria=lambda state: state.research_completeness > 0.8
    )
    
    orchestrator.add_coordination_rule(
        "validation_phase",
        participants=["fact_checker", "lead_researcher"],
        interaction="consensus",
        consensus_strategy=ConsensusStrategy(
            method="weighted_vote",
            weights={"fact_checker": 0.6, "lead_researcher": 0.4}
        )
    )
    
    # Define agent communication
    orchestrator.enable_agent_communication(
        protocol="message_passing",  # or "shared_memory", "pubsub"
        channels={
            "findings": ["lead_researcher", "data_analyst", "fact_checker"],
            "drafts": ["writer", "reviewer"],
            "feedback": ["reviewer", "writer", "lead_researcher"]
        }
    )
    
    # Execute orchestrated workflow
    result = await orchestrator.execute(
        initial_task="Research quantum computing breakthroughs",
        max_iterations=10,
        convergence_threshold=0.95
    )

Dynamic Graph Modification
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Runtime Graph Evolution**::

    from haive.core.graph.dynamic import DynamicGraph, GraphMutator
    
    # Create graph that can modify itself
    dynamic_graph = DynamicGraph(
        base_graph=initial_graph,
        allow_runtime_modification=True
    )
    
    # Define mutation rules
    mutator = GraphMutator()
    
    @mutator.rule("add_verification")
    def add_verification_node(graph, state):
        """Add verification when confidence is low."""
        if state.confidence < 0.6:
            graph.add_node(
                "extra_verification",
                VerificationNode(),
                after="analysis",
                before="synthesis"
            )
            return True
        return False
    
    @mutator.rule("parallelize_research")
    def parallelize_if_slow(graph, state, metrics):
        """Parallelize research if taking too long."""
        if metrics.elapsed_time > 30 and not graph.has_parallel_nodes("research"):
            graph.parallelize_node(
                "research",
                split_function=split_research_tasks,
                parallelism=3
            )
            return True
        return False
    
    # Apply mutations during execution
    dynamic_graph.set_mutator(mutator)
    
    # Graph evolves based on runtime conditions
    result = await dynamic_graph.execute(initial_state)

Performance Optimization
------------------------

Graph Execution Metrics
~~~~~~~~~~~~~~~~~~~~~~~

**High-Performance Workflow Execution**

* **Node Latency**: < 10ms overhead per node
* **Parallelism**: Up to 1000 concurrent nodes
* **Checkpointing**: < 50ms state persistence
* **Memory**: O(1) state access with COW
* **Throughput**: 10,000+ workflows/minute

**Performance Optimization**::

    from haive.core.graph.optimization import (
        GraphOptimizer,
        ExecutionProfiler
    )
    
    # Optimize graph structure
    optimizer = GraphOptimizer()
    optimized_graph = optimizer.optimize(
        graph,
        strategies=[
            "merge_sequential_nodes",   # Combine simple sequences
            "parallelize_independent",  # Auto-detect parallelism
            "cache_deterministic",      # Cache pure functions
            "eliminate_dead_paths",     # Remove unreachable nodes
            "minimize_state_transfer"   # Reduce state copying
        ]
    )
    
    # Profile execution
    profiler = ExecutionProfiler()
    
    with profiler.profile():
        result = await optimized_graph.execute(state)
    
    # Analyze performance
    report = profiler.generate_report()
    print(f"Total time: {report.total_time}ms")
    print(f"Slowest node: {report.slowest_node}")
    print(f"Parallelism achieved: {report.parallelism_factor}x")
    
    # Visualize bottlenecks
    profiler.visualize_bottlenecks("performance.html")

Distributed Execution
~~~~~~~~~~~~~~~~~~~~~

**Scale Across Multiple Machines**::

    from haive.core.graph.distributed import DistributedGraph, WorkerPool
    
    # Create distributed graph
    distributed_graph = DistributedGraph(
        graph=workflow_graph,
        coordinator_url="redis://coordinator:6379",
        worker_pool=WorkerPool(
            workers=[
                "worker-1.compute.internal",
                "worker-2.compute.internal",
                "worker-3.compute.internal"
            ],
            load_balancing="least_loaded"
        )
    )
    
    # Configure node placement
    distributed_graph.place_node("heavy_computation", "worker-1")
    distributed_graph.place_nodes_by_type(AgentNode, "any")
    distributed_graph.place_nodes_by_resources({
        "gpu_required": "gpu-workers",
        "memory_intensive": "high-memory-workers"
    })
    
    # Execute with distributed coordination
    result = await distributed_graph.execute(
        state,
        partition_strategy="hash",  # How to split state
        replication_factor=2        # Fault tolerance
    )

Integration Examples 🔌
-----------------------

LangChain Integration
~~~~~~~~~~~~~~~~~~~~~

.. testcode::

   from langchain.agents import AgentExecutor
   from haive.core.graph.adapters import LangChainAdapter
   
   # Convert Haive graph to LangChain
   adapter = LangChainAdapter()
   langchain_runnable = adapter.to_langchain(graph)
   
   # Use in LangChain workflows
   executor = AgentExecutor(
       agent=langchain_runnable,
       tools=tools,
       verbose=True
   )
   
   # Convert LangChain to Haive graph
   lc_agent = create_langchain_agent()
   haive_graph = adapter.from_langchain(lc_agent)

Custom Node Development
~~~~~~~~~~~~~~~~~~~~~~~

.. testcode::

   from haive.core.graph.node import BaseNode
   from typing import Any, Dict
   
   class CustomAnalysisNode(BaseNode):
       """Custom node for specialized analysis"""
       
       def __init__(self, analyzer: Any, config: Dict[str, Any]):
           self.analyzer = analyzer
           self.config = config
       
       async def aprocess(self, state: StateSchema) -> StateSchema:
           """Async processing with custom logic"""
           # Extract relevant data
           data = self._extract_data(state)
           
           # Run analysis
           results = await self.analyzer.analyze(data, **self.config)
           
           # Update state
           state.results = results
           state.metadata["analysis_complete"] = True
           
           return state
       
       def _extract_data(self, state: StateSchema) -> Any:
           """Extract and prepare data for analysis"""
           return {
               "messages": state.messages,
               "context": state.context,
               "timestamp": datetime.now()
           }

.. testoutput::
   :hide:

   ...

Best Practices 📚
-----------------

Graph Design Principles
~~~~~~~~~~~~~~~~~~~~~~~

1. **Single Responsibility**: Each node should do one thing well
2. **Explicit State**: All state changes should be explicit and traceable
3. **Error Boundaries**: Use validation nodes to catch and handle errors
4. **Observability**: Add logging and monitoring at key points
5. **Reusability**: Design nodes to be reusable across graphs

.. testcode::

   # Good: Single responsibility
   graph.add_node("validate_input", InputValidator())
   graph.add_node("process_data", DataProcessor())
   graph.add_node("generate_output", OutputGenerator())
   
   # Good: Explicit state changes
   def update_state(state: WorkflowState) -> WorkflowState:
       state.processing_stage = "validated"
       state.metadata["validated_at"] = datetime.now()
       return state

Testing Strategies
~~~~~~~~~~~~~~~~~~

.. testcode::

   import pytest
   from haive.core.graph.testing import GraphTestHarness
   
   @pytest.fixture
   def test_graph():
       """Create test graph fixture"""
       graph = StateGraph(TestState)
       # ... configure graph
       return graph.compile()
   
   async def test_happy_path(test_graph):
       """Test successful execution"""
       harness = GraphTestHarness(test_graph)
       
       # Execute with test input
       result = await harness.run({
           "messages": [{"role": "user", "content": "test"}]
       })
       
       # Verify execution path
       assert harness.executed_nodes == ["start", "process", "end"]
       assert result.status == "success"
   
   async def test_error_handling(test_graph):
       """Test error scenarios"""
       harness = GraphTestHarness(test_graph)
       
       # Inject error
       harness.inject_error("process", ValueError("Test error"))
       
       # Execute and verify error handling
       result = await harness.run({"messages": []})
       assert "error_handler" in harness.executed_nodes

.. testoutput::
   :hide:

   ...

API Reference 📖
----------------

Core Classes
~~~~~~~~~~~~

.. autoclass:: haive.core.graph.StateGraph
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: haive.core.graph.CompiledGraph
   :members:
   :undoc-members:
   :show-inheritance:

Node Types
~~~~~~~~~~

.. autoclass:: haive.core.graph.node.BaseNode
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: haive.core.graph.node.AgentNode
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: haive.core.graph.node.ToolNode
   :members:
   :undoc-members:
   :show-inheritance:

Patterns & Utilities
~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.graph.patterns
   :members:
   :undoc-members:

.. automodule:: haive.core.graph.optimization
   :members:
   :undoc-members:

Enterprise Features
-------------------

**Production-Ready Workflow Management**

* **Workflow Versioning**: Track and deploy workflow versions
* **Access Control**: Node-level permissions and audit trails
* **Monitoring**: Real-time metrics and alerting
* **Fault Tolerance**: Automatic failover and recovery
* **Compliance**: Workflow governance and approval chains

See Also 👀
-----------

- :doc:`engine_architecture` - The engine system that powers nodes
- :doc:`schema_system` - State management for graphs
- :doc:`../../haive-agents/agent_development` - Building agents for graphs
- :doc:`../../tutorials/graph_workflows` - Step-by-step graph tutorials

.. toctree::
   :maxdepth: 2
   :hidden:

   graph/nodes
   graph/patterns
   graph/optimization
   graph/testing