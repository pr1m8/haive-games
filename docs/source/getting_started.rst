Getting Started
===============

Welcome to haive-core! This guide will help you get up and running with the Haive AI Agent Framework.

Installation
------------

Install haive-core using pip:

.. code-block:: bash

   pip install haive-core

Or with Poetry:

.. code-block:: bash

   poetry add haive-core

Quick Start Example
-------------------

Here's a simple example to get you started with haive-core:

.. code-block:: python

   from haive.core.engine.aug_llm import AugLLMConfig
   from haive.core.schema.prebuilt.messages_state import MessagesState
   
   # Configure the LLM engine
   config = AugLLMConfig(
       model="gpt-4",
       temperature=0.7,
       system_message="You are a helpful assistant."
   )
   
   # Create a simple state
   state = MessagesState()
   
   # Add a user message
   state.messages.append({
       "role": "user", 
       "content": "Hello! Can you help me understand haive-core?"
   })
   
   print("Ready to use haive-core!")

Core Concepts
-------------

State Management
~~~~~~~~~~~~~~~~

haive-core uses state schemas to manage agent conversations and data:

.. code-block:: python

   from haive.core.schema.state_schema import StateSchema
   from pydantic import Field
   from typing import List, Dict, Any
   
   class MyCustomState(StateSchema):
       """Custom state for your agent."""
       messages: List[Dict[str, Any]] = Field(default_factory=list)
       context: Dict[str, Any] = Field(default_factory=dict)
       
   # Create and use your state
   state = MyCustomState()
   state.context["user_name"] = "Alice"

Engine Configuration
~~~~~~~~~~~~~~~~~~~~

The AugLLMConfig provides flexible configuration for LLM engines:

.. code-block:: python

   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Basic configuration
   config = AugLLMConfig(
       model="gpt-4",
       temperature=0.7
   )
   
   # Advanced configuration with tools
   config = AugLLMConfig(
       model="gpt-4",
       temperature=0.3,
       tools=["calculator", "web_search"],
       structured_output_model=MyOutputModel
   )

Graph-Based Workflows
~~~~~~~~~~~~~~~~~~~~~

Build complex workflows using the graph system:

.. code-block:: python

   from haive.core.graph import StateGraph
   from haive.core.graph.node import create_node
   
   # Create a graph
   graph = StateGraph(state_schema=MessagesState)
   
   # Add nodes
   graph.add_node("process", process_function)
   graph.add_node("respond", respond_function)
   
   # Add edges
   graph.add_edge("process", "respond")
   graph.set_entry_point("process")
   
   # Compile and run
   app = graph.compile()
   result = app.invoke({"messages": []})

Next Steps
----------

1. **Explore the API Reference**: Check out the complete :doc:`API documentation <autoapi/haive/index>`
2. **Learn about Agents**: See how to build agents with haive-agents
3. **Add Tools**: Integrate tools from haive-tools
4. **Join the Community**: Visit our `GitHub repository <https://github.com/haive-ai/haive>`_

Common Patterns
---------------

Using Vector Stores
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.core.engine.vectorstore import VectorStoreConfig
   
   # Configure a vector store
   vector_config = VectorStoreConfig(
       provider="chroma",
       collection_name="my_documents"
   )

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from haive.core.errors import HaiveError
   
   try:
       # Your haive-core code
       result = engine.run(state)
   except HaiveError as e:
       print(f"Haive error: {e}")
       # Handle gracefully

Best Practices
--------------

1. **Always use type hints** - haive-core is built with type safety in mind
2. **Handle errors gracefully** - Use try/except blocks for production code  
3. **Configure appropriately** - Set temperature and other parameters based on your use case
4. **Use state schemas** - Define clear state structures for your workflows
5. **Test with real LLMs** - Avoid mocks when testing agent behavior

Getting Help
------------

- **Documentation**: You're already here!
- **GitHub Issues**: Report bugs or request features
- **Examples**: Check the examples/ directory in the repository
- **API Reference**: See the complete :doc:`API documentation <autoapi/haive/index>`