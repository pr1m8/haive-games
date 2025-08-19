Core Concepts
=============

Understanding the fundamental concepts of haive-core will help you build powerful AI agent systems.

Architecture Overview
---------------------

haive-core provides the foundation for building AI agents with:

- **Modular Design**: Composable components that work together
- **Type Safety**: Full type hints and Pydantic models throughout
- **Extensibility**: Plugin architecture for custom components
- **Scalability**: From simple chatbots to complex multi-agent systems

Key Components
--------------

Engines
~~~~~~~

The engine is the heart of any agent, managing LLM interactions:

.. code-block:: python

   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Basic engine configuration
   engine = AugLLMConfig(
       model="gpt-4",
       temperature=0.7,
       max_tokens=1000
   )
   
   # Advanced configuration
   engine = AugLLMConfig(
       model="claude-3-opus",
       temperature=0.3,
       system_message="You are a helpful assistant",
       tools=["calculator", "web_search"],
       structured_output_model=MyOutputModel
   )

State Management
~~~~~~~~~~~~~~~~

States hold conversation history and agent data:

.. code-block:: python

   from haive.core.schema.state_schema import StateSchema
   from haive.core.schema.prebuilt.messages_state import MessagesState
   from pydantic import Field
   
   # Use prebuilt state
   state = MessagesState()
   
   # Or create custom state
   class CustomState(StateSchema):
       messages: list = Field(default_factory=list)
       context: dict = Field(default_factory=dict)
       user_preferences: dict = Field(default_factory=dict)

Graph-Based Workflows
~~~~~~~~~~~~~~~~~~~~~

Build complex workflows using directed graphs:

.. code-block:: python

   from haive.core.graph import StateGraph
   
   # Create workflow graph
   workflow = StateGraph(state_schema=CustomState)
   
   # Add nodes (functions that process state)
   workflow.add_node("analyze", analyze_input)
   workflow.add_node("generate", generate_response)
   workflow.add_node("validate", validate_output)
   
   # Connect nodes
   workflow.add_edge("analyze", "generate")
   workflow.add_edge("generate", "validate")
   
   # Compile and run
   app = workflow.compile()
   result = app.invoke(initial_state)

Tools and Functions
~~~~~~~~~~~~~~~~~~~

Extend agent capabilities with tools:

.. code-block:: python

   from langchain_core.tools import tool
   
   @tool
   def calculator(expression: str) -> str:
       """Evaluate mathematical expressions."""
       return str(eval(expression))
   
   @tool
   def web_search(query: str) -> str:
       """Search the web for information."""
       # Implementation here
       return search_results
   
   # Add tools to engine
   engine = AugLLMConfig(tools=[calculator, web_search])

Vector Stores
~~~~~~~~~~~~~

Enable semantic search and retrieval:

.. code-block:: python

   from haive.core.engine.vectorstore import VectorStoreConfig
   
   # Configure vector store
   vector_config = VectorStoreConfig(
       provider="chroma",
       collection_name="knowledge_base",
       embedding_model="text-embedding-ada-002"
   )

Design Patterns
---------------

Agent Pattern
~~~~~~~~~~~~~

The basic agent pattern combines an engine with a workflow:

.. code-block:: python

   class SimpleAgent:
       def __init__(self, engine: AugLLMConfig):
           self.engine = engine
           self.workflow = self._build_workflow()
       
       def _build_workflow(self):
           graph = StateGraph(MessagesState)
           graph.add_node("process", self.process_message)
           graph.set_entry_point("process")
           graph.set_finish_point("process")
           return graph.compile()
       
       def process_message(self, state):
           # Agent logic here
           response = self.engine.invoke(state.messages)
           state.messages.append(response)
           return state

Multi-Agent Pattern
~~~~~~~~~~~~~~~~~~~

Coordinate multiple agents for complex tasks:

.. code-block:: python

   class MultiAgentSystem:
       def __init__(self):
           self.planner = PlannerAgent()
           self.researcher = ResearchAgent()
           self.writer = WriterAgent()
           self.reviewer = ReviewerAgent()
       
       def process_request(self, request):
           # Planner creates strategy
           plan = self.planner.create_plan(request)
           
           # Researcher gathers information
           research = self.researcher.gather_info(plan)
           
           # Writer creates content
           draft = self.writer.write_content(research)
           
           # Reviewer provides feedback
           final = self.reviewer.review_and_edit(draft)
           
           return final

Tool Integration Pattern
~~~~~~~~~~~~~~~~~~~~~~~~

Create reusable tool sets:

.. code-block:: python

   class ToolKit:
       @staticmethod
       def math_tools():
           return [calculator, equation_solver, statistics]
       
       @staticmethod
       def research_tools():
           return [web_search, arxiv_search, wikipedia]
       
       @staticmethod
       def code_tools():
           return [python_repl, code_analyzer, debugger]
   
   # Use in agent
   engine = AugLLMConfig(
       tools=ToolKit.math_tools() + ToolKit.research_tools()
   )

Best Practices
--------------

1. State Design
~~~~~~~~~~~~~~~

- Keep state schemas focused and minimal
- Use Pydantic for validation
- Document all fields clearly
- Version your schemas

2. Error Handling
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.core.errors import HaiveError
   
   try:
       result = agent.process(input_data)
   except HaiveError as e:
       logger.error(f"Agent error: {e}")
       # Graceful fallback
       result = default_response()

3. Testing
~~~~~~~~~~

- Test with real LLMs (avoid mocks)
- Use consistent temperature for tests
- Test edge cases and error paths
- Monitor token usage

4. Performance
~~~~~~~~~~~~~~

- Cache frequently used embeddings
- Batch similar requests
- Use appropriate chunk sizes
- Monitor and optimize prompts

5. Security
~~~~~~~~~~~

- Never expose API keys in code
- Validate all user inputs
- Limit tool permissions
- Audit agent outputs

Advanced Topics
---------------

Dynamic Graph Modification
~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify workflows at runtime:

.. code-block:: python

   # Add nodes dynamically
   if user_needs_translation:
       workflow.add_node("translate", translation_node)
       workflow.add_edge("generate", "translate")
       workflow.add_edge("translate", "validate")

Custom Engines
~~~~~~~~~~~~~~

Create specialized engines:

.. code-block:: python

   class CustomEngine(AugLLMConfig):
       def __init__(self, **kwargs):
           super().__init__(**kwargs)
           self.add_custom_handlers()
       
       def add_custom_handlers(self):
           # Add preprocessing
           self.add_preprocessor(self.clean_input)
           # Add postprocessing
           self.add_postprocessor(self.format_output)

Plugin Architecture
~~~~~~~~~~~~~~~~~~~

Extend haive-core with plugins:

.. code-block:: python

   from haive.core.registry import register_component
   
   @register_component("custom_tool")
   class CustomTool:
       def __call__(self, input_data):
           # Tool implementation
           return processed_data

Next Steps
----------

- Explore :doc:`installation` options
- Follow the :doc:`getting_started` tutorial
- Review :doc:`API Reference <autoapi/haive/index>`
- Check out examples in the repository