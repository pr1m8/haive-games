Haive Core Overview
===================

.. module:: haive.core

Welcome to **haive-core**, the foundation of the Haive AI Agent Framework! 🚀

.. note::
   
   Looking for other Haive packages? The complete framework documentation will be available at the `Haive root documentation <https://github.com/pr1m8/haive>`_.

.. grid:: 2
   :gutter: 3
   :margin: 0
   :padding: 0

   .. grid-item-card:: 🧠 **Core Engine**
      :link: autoapi/core/engine/index
      :link-type: doc
      :class-card: sd-border-2

      The brain of Haive - manages agent execution, LLM integration, and state management.

      .. button-ref:: autoapi/core/engine/index
         :color: primary
         :outline:
         :expand:

         Explore Engine →

   .. grid-item-card:: 📊 **Graph System**
      :link: autoapi/core/graph/index
      :link-type: doc
      :class-card: sd-border-2

      Powerful graph-based workflow orchestration with LangGraph integration.

      .. button-ref:: autoapi/core/graph/index
         :color: primary
         :outline:
         :expand:

         View Graphs →

   .. grid-item-card:: 🗃️ **State & Schema**
      :link: autoapi/core/schema/index
      :link-type: doc
      :class-card: sd-border-2

      Type-safe state management with Pydantic schemas and state persistence.

      .. button-ref:: autoapi/core/schema/index
         :color: primary
         :outline:
         :expand:

         Schema Docs →

   .. grid-item-card:: 🛠️ **Tools & Extensions**
      :link: autoapi/core/tools/index
      :link-type: doc
      :class-card: sd-border-2

      Rich tool ecosystem for agent capabilities - calculators, web search, and more.

      .. button-ref:: autoapi/core/tools/index
         :color: primary
         :outline:
         :expand:

         Browse Tools →

Quick Start 🏃‍♂️
--------------

.. tab-set::

   .. tab-item:: Installation

      .. code-block:: bash

         # Install haive-core
         pip install haive-core

         # Or with Poetry (recommended)
         poetry add haive-core

   .. tab-item:: Basic Usage

      .. code-block:: python

         from haive.core.engine import AugLLMConfig
         from haive.core.schema import StateSchema

         # Configure your LLM
         config = AugLLMConfig(
             model="gpt-4",
             temperature=0.7
         )

         # Define your state
         class MyState(StateSchema):
             messages: list[str]
             context: dict

   .. tab-item:: Advanced

      .. code-block:: python

         from haive.core.graph import DynamicGraph
         from haive.core.tools import CalculatorTool

         # Build complex workflows
         graph = DynamicGraph()
         graph.add_node("process", process_node)
         graph.add_tool(CalculatorTool())

Core Components 🎯
-----------------

.. grid:: 3
   :gutter: 2

   .. grid-item::

      .. card:: **Engine Module** 🔧
         :class-card: sd-bg-light

         - :class:`~haive.core.engine.AugLLMConfig`
         - :class:`~haive.core.engine.BaseAgent`
         - :class:`~haive.core.engine.ToolEngine`
         - :class:`~haive.core.engine.ValidationEngine`

   .. grid-item::

      .. card:: **Graph Module** 📈
         :class-card: sd-bg-light

         - :class:`~haive.core.graph.DynamicGraph`
         - :class:`~haive.core.graph.StateGraph`
         - :class:`~haive.core.graph.GraphNode`
         - :class:`~haive.core.graph.ValidationNode`

   .. grid-item::

      .. card:: **Schema Module** 📋
         :class-card: sd-bg-light

         - :class:`~haive.core.schema.StateSchema`
         - :class:`~haive.core.schema.MetaStateSchema`
         - :class:`~haive.core.schema.MessagesState`
         - :class:`~haive.core.schema.ToolMessage`

Architecture Overview 🏗️
----------------------

.. mermaid::

   graph TB
      A[Application Layer] --> B[haive-core]
      B --> C[Engine]
      B --> D[Graph]
      B --> E[Schema]
      B --> F[Tools]
      
      C --> G[LLM Integration]
      C --> H[Tool Management]
      
      D --> I[Workflow Orchestration]
      D --> J[State Management]
      
      E --> K[Type Safety]
      E --> L[Persistence]
      
      F --> M[Built-in Tools]
      F --> N[Custom Tools]

      style B fill:#2563eb,stroke:#1d4ed8,color:#fff
      style C fill:#60a5fa,stroke:#3b82f6
      style D fill:#60a5fa,stroke:#3b82f6
      style E fill:#60a5fa,stroke:#3b82f6
      style F fill:#60a5fa,stroke:#3b82f6

Key Features ✨
--------------

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **🔄 Auto-Persistence**
      :class-card: sd-border-1

      Automatic state saving and recovery with multiple backend support (PostgreSQL, Redis, File).

   .. grid-item-card:: **🌐 Multi-Provider Support**
      :class-card: sd-border-1

      Works with OpenAI, Anthropic, Google, AWS Bedrock, and more LLM providers.

   .. grid-item-card:: **📊 Graph-Based Workflows**
      :class-card: sd-border-1

      Build complex agent workflows with visual graph representation and debugging.

   .. grid-item-card:: **🛡️ Type Safety**
      :class-card: sd-border-1

      Full Pydantic integration for type-safe state management and validation.

   .. grid-item-card:: **🧩 Modular Design**
      :class-card: sd-border-1

      Clean separation of concerns with pluggable components and extensions.

   .. grid-item-card:: **⚡ High Performance**
      :class-card: sd-border-1

      Optimized for production use with async support and efficient state handling.

Integration Examples 🔗
--------------------

.. tab-set::

   .. tab-item:: With haive-agents

      .. code-block:: python

         from haive.core.engine import AugLLMConfig
         from haive.agents import ReactAgent

         # Core provides the foundation
         config = AugLLMConfig(temperature=0.7)
         
         # Agents build on top
         agent = ReactAgent(
             name="assistant",
             engine=config
         )

   .. tab-item:: With haive-tools

      .. code-block:: python

         from haive.core.tools import BaseTool
         from haive.tools import WebSearchTool

         # Core defines the interface
         class MyTool(BaseTool):
             def __call__(self, query: str) -> str:
                 return f"Processed: {query}"

   .. tab-item:: With haive-dataflow

      .. code-block:: python

         from haive.core.schema import StateSchema
         from haive.dataflow import StreamProcessor

         # Core schemas work with dataflow
         class StreamState(StateSchema):
             buffer: list[str]
             processed: int

Resources 📚
-----------

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 📖 **API Reference**
      :link: autoapi/index
      :link-type: doc

      Complete API documentation with examples

   .. grid-item-card:: 🎓 **Tutorials**
      :link: tutorials/index
      :link-type: doc

      Step-by-step guides and examples

   .. grid-item-card:: 💬 **Community**
      :link: https://github.com/haive-ai/haive/discussions
      :link-type: url

      Join discussions and get help

Need Help? 🤝
------------

- 📝 Check our :doc:`tutorials/index` for step-by-step guides
- 🐛 Found a bug? `Report it on GitHub <https://github.com/haive-ai/haive/issues>`_
- 💡 Have a feature request? `Start a discussion <https://github.com/haive-ai/haive/discussions>`_
- 📧 Contact us at support@haive.ai

.. toctree::
   :hidden:
   :maxdepth: 2

   installation
   quickstart
   tutorials/index
   api/index
   changelog