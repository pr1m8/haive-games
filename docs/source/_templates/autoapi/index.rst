{# Enhanced AutoAPI index with sphinx-design and emojis #}
haive-core API Reference
========================

.. grid:: 1
   :gutter: 3
   :margin: 0
   :padding: 0

   .. grid-item-card:: 🚀 **Welcome to haive-core API Documentation**
      :class-card: sd-border-2 sd-shadow-sm

      Complete API reference for the haive-core package with interactive navigation and detailed documentation for every module, class, and function.

      .. button-link:: ../overview.html
         :color: primary
         :expand:

         ← Back to Overview

Quick Jump 🎯
------------

.. grid:: 4
   :gutter: 2
   :class: sd-text-center

   .. grid-item::
      
      .. button-ref:: #engine-system
         :color: info
         :outline:

         🧠 Engine

   .. grid-item::
      
      .. button-ref:: #schema-system
         :color: info
         :outline:

         📋 Schema

   .. grid-item::
      
      .. button-ref:: #graph-system
         :color: info
         :outline:

         📊 Graph

   .. grid-item::
      
      .. button-ref:: #tools-system
         :color: info
         :outline:

         🛠️ Tools

Core Systems 💎
--------------

.. _engine-system:

Engine System 🧠
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **AugLLMConfig** ⚡
      :link: core/engine/aug_llm/index
      :link-type: doc
      :class-card: sd-border-1

      Enhanced LLM configuration with multi-provider support
      
      .. code-block:: python

         from haive.core.engine import AugLLMConfig
         
         config = AugLLMConfig(
             model="gpt-4",
             temperature=0.7,
             tools=[calculator]
         )

   .. grid-item-card:: **BaseAgent** 🤖
      :link: core/engine/agent/index
      :link-type: doc
      :class-card: sd-border-1

      Foundation class for all Haive agents
      
      .. code-block:: python

         from haive.core.engine import BaseAgent
         
         class MyAgent(BaseAgent):
             def run(self, input):
                 # Agent logic here
                 pass

.. admonition:: Engine Modules
   :class: dropdown

   .. autosummary::
      :toctree: 
      :template: custom-module-template.rst
      :recursive:
      
      haive.core.engine.aug_llm
      haive.core.engine.agent
      haive.core.engine.tool
      haive.core.engine.retriever
      haive.core.engine.vectorstore
      haive.core.engine.providers

.. _schema-system:

Schema System 📋
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **StateSchema** 📝
      :link: core/schema/state_schema/index
      :link-type: doc
      :class-card: sd-border-1

      Type-safe state management with Pydantic
      
      .. code-block:: python

         from haive.core.schema import StateSchema
         
         class AgentState(StateSchema):
             messages: list[str]
             context: dict[str, Any]

   .. grid-item-card:: **MetaStateSchema** 🎭
      :link: core/schema/prebuilt/meta_state/index
      :link-type: doc
      :class-card: sd-border-1

      Advanced meta-agent state management
      
      .. code-block:: python

         from haive.core.schema import MetaStateSchema
         
         meta_state = MetaStateSchema.from_agent(
             agent=my_agent
         )

.. admonition:: Schema Modules
   :class: dropdown

   .. autosummary::
      :toctree: 
      :template: custom-module-template.rst
      :recursive:
      
      haive.core.schema.state_schema
      haive.core.schema.prebuilt
      haive.core.schema.composer
      haive.core.schema.field_registry
      haive.core.schema.mixins

.. _graph-system:

Graph System 📊
~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **DynamicGraph** 🔄
      :link: core/graph/dynamic_graph/index
      :link-type: doc
      :class-card: sd-border-1

      Flexible graph builder for complex workflows
      
      .. code-block:: python

         from haive.core.graph import DynamicGraph
         
         graph = DynamicGraph()
         graph.add_node("process", node_func)
         graph.add_edge("start", "process")

   .. grid-item-card:: **StateGraph** 📈
      :link: core/graph/state_graph/index
      :link-type: doc
      :class-card: sd-border-1

      Stateful workflow orchestration
      
      .. code-block:: python

         from haive.core.graph import StateGraph
         
         workflow = StateGraph(MyState)
         workflow.add_node("agent", agent_node)

.. admonition:: Graph Modules
   :class: dropdown

   .. autosummary::
      :toctree: 
      :template: custom-module-template.rst
      :recursive:
      
      haive.core.graph.state_graph
      haive.core.graph.dynamic_graph
      haive.core.graph.node
      haive.core.graph.routers
      haive.core.graph.branches

.. _tools-system:

Tools System 🛠️
~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **BaseTool** 🔧
      :link: core/tools/base/index
      :link-type: doc
      :class-card: sd-border-1

      Interface for creating custom tools
      
      .. code-block:: python

         from haive.core.tools import BaseTool
         
         class MyTool(BaseTool):
             def __call__(self, input: str) -> str:
                 return f"Processed: {input}"

   .. grid-item-card:: **ToolRegistry** 📚
      :link: core/tools/registry/index
      :link-type: doc
      :class-card: sd-border-1

      Central registry for tool management
      
      .. code-block:: python

         from haive.core.tools import ToolRegistry
         
         registry = ToolRegistry()
         registry.register("calculator", calc_tool)

.. admonition:: Tools Modules
   :class: dropdown

   .. autosummary::
      :toctree: 
      :template: custom-module-template.rst
      :recursive:
      
      haive.core.tools.base
      haive.core.tools.registry
      haive.core.tools.calculator
      haive.core.tools.search

Supporting Systems 🔨
-------------------

.. tab-set::

   .. tab-item:: Persistence 💾

      .. grid:: 2
         :gutter: 2

         .. grid-item-card:: **Store Backends**
            :class-card: sd-bg-light

            - ``PostgresStore`` - PostgreSQL backend
            - ``RedisStore`` - Redis backend  
            - ``FileStore`` - File-based storage
            - ``MemoryStore`` - In-memory storage

         .. grid-item-card:: **Checkpointing**
            :class-card: sd-bg-light

            - ``Checkpointer`` - State snapshots
            - ``CheckpointManager`` - Recovery
            - ``VersionControl`` - History tracking

      .. autosummary::
         :toctree: 
         :template: custom-module-template.rst
         
         haive.core.persistence.store
         haive.core.persistence.handlers
         haive.core.persistence.memory

   .. tab-item:: Memory 🧩

      .. grid:: 2
         :gutter: 2

         .. grid-item-card:: **Conversation Memory**
            :class-card: sd-bg-light

            - ``ConversationBufferMemory``
            - ``ConversationSummaryMemory``
            - ``VectorStoreMemory``

         .. grid-item-card:: **Memory Backends**
            :class-card: sd-bg-light

            - ``ChromaMemory`` - Vector storage
            - ``RedisMemory`` - Key-value storage
            - ``FileMemory`` - File-based memory

      .. autosummary::
         :toctree: 
         :template: custom-module-template.rst
         
         haive.core.memory.conversation
         haive.core.memory.vector
         haive.core.memory.backends

   .. tab-item:: Common 🔗

      .. grid:: 2
         :gutter: 2

         .. grid-item-card:: **Mixins**
            :class-card: sd-bg-light

            - ``RecompileMixin`` - Dynamic rebuilding
            - ``ToolRouteMixin`` - Tool routing
            - ``StructuredOutputMixin`` - Output parsing

         .. grid-item-card:: **Utilities**
            :class-card: sd-bg-light

            - ``TypeUtils`` - Type checking
            - ``ImportUtils`` - Dynamic imports
            - ``ConfigUtils`` - Configuration

      .. autosummary::
         :toctree: 
         :template: custom-module-template.rst
         
         haive.core.common.mixins
         haive.core.common.types
         haive.core.common.utils

Class Index by Category 📖
------------------------

.. tab-set::

   .. tab-item:: Agents & Engines

      **Base Classes:**
      
      .. autosummary::
         :nosignatures:
         
         haive.core.engine.BaseAgent
         haive.core.engine.AugLLMConfig
         haive.core.engine.EngineMode
         haive.core.engine.ToolEngine

      **Providers:**
      
      .. autosummary::
         :nosignatures:
         
         haive.core.engine.providers.OpenAIProvider
         haive.core.engine.providers.AnthropicProvider
         haive.core.engine.providers.GoogleProvider
         haive.core.engine.providers.BedrockProvider

   .. tab-item:: Schemas & State

      **State Management:**
      
      .. autosummary::
         :nosignatures:
         
         haive.core.schema.StateSchema
         haive.core.schema.MetaStateSchema
         haive.core.schema.MessagesState
         haive.core.schema.AgentState

      **Composers:**
      
      .. autosummary::
         :nosignatures:
         
         haive.core.schema.SchemaComposer
         haive.core.schema.FieldRegistry
         haive.core.schema.DynamicSchema

   .. tab-item:: Graphs & Nodes

      **Graph Types:**
      
      .. autosummary::
         :nosignatures:
         
         haive.core.graph.StateGraph
         haive.core.graph.DynamicGraph
         haive.core.graph.MessageGraph

      **Nodes:**
      
      .. autosummary::
         :nosignatures:
         
         haive.core.graph.GraphNode
         haive.core.graph.ValidationNode
         haive.core.graph.ToolNode
         haive.core.graph.AgentNode

Complete Module Tree 🌳
--------------------

.. autoapi-nested::
   :nested-full:

Search & Indices 🔍
-----------------

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: **🔤 General Index**
      :link: ../genindex.html
      :link-type: url

      Alphabetical index of all classes, functions, and attributes

   .. grid-item-card:: **📦 Module Index**
      :link: ../py-modindex.html
      :link-type: url

      Quick access to all modules in haive-core

   .. grid-item-card:: **🔍 Search**
      :link: ../search.html
      :link-type: url

      Search the entire documentation