Configuration Guide
===================

This guide covers all configuration options available in haive-core.

Engine Configuration
--------------------

AugLLMConfig Options
~~~~~~~~~~~~~~~~~~~~

The AugLLMConfig class provides comprehensive configuration for LLM engines:

.. code-block:: python

   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Full configuration example
   config = AugLLMConfig(
       # Model selection
       model="gpt-4",  # or "claude-3", "gemini-pro", etc.
       
       # Temperature and sampling
       temperature=0.7,  # 0.0 (deterministic) to 2.0 (creative)
       top_p=0.9,  # Nucleus sampling
       max_tokens=1000,  # Maximum response length
       
       # System configuration
       system_message="You are a helpful assistant",
       
       # Tools and functions
       tools=["calculator", "web_search"],  # Tool names or instances
       tool_choice="auto",  # "auto", "none", or specific tool
       
       # Structured output
       structured_output_model=MyPydanticModel,  # For typed responses
       
       # Advanced options
       streaming=True,  # Enable streaming responses
       retry_config={"max_retries": 3, "backoff": 2.0},
       timeout=30.0,  # Request timeout in seconds
       
       # Provider-specific options
       api_key="your-api-key",  # Or use environment variable
       base_url="https://api.openai.com/v1",  # Custom endpoints
   )

Model Providers
~~~~~~~~~~~~~~~

Configure different LLM providers:

**OpenAI**:

.. code-block:: python

   config = AugLLMConfig(
       model="gpt-4",
       api_key=os.getenv("OPENAI_API_KEY"),
       organization=os.getenv("OPENAI_ORG_ID"),
   )

**Anthropic**:

.. code-block:: python

   config = AugLLMConfig(
       model="claude-3-opus",
       api_key=os.getenv("ANTHROPIC_API_KEY"),
   )

**Google Vertex AI**:

.. code-block:: python

   config = AugLLMConfig(
       model="gemini-pro",
       project_id="your-project-id",
       location="us-central1",
   )

**Azure OpenAI**:

.. code-block:: python

   config = AugLLMConfig(
       model="gpt-4",
       api_key=os.getenv("AZURE_OPENAI_API_KEY"),
       base_url="https://your-resource.openai.azure.com/",
       api_version="2024-02-01",
   )

State Configuration
-------------------

Custom State Schemas
~~~~~~~~~~~~~~~~~~~~

Define custom states with validation:

.. code-block:: python

   from haive.core.schema.state_schema import StateSchema
   from pydantic import Field, validator
   from typing import List, Dict, Optional
   
   class AgentState(StateSchema):
       # Basic fields
       messages: List[Dict] = Field(
           default_factory=list,
           description="Conversation history"
       )
       
       # Typed fields
       user_id: str = Field(..., description="User identifier")
       session_id: Optional[str] = Field(None, description="Session ID")
       
       # Complex fields
       context: Dict[str, Any] = Field(
           default_factory=dict,
           description="Additional context"
       )
       
       # Validation
       @validator("user_id")
       def validate_user_id(cls, v):
           if not v.strip():
               raise ValueError("User ID cannot be empty")
           return v
       
       # Custom methods
       def add_message(self, role: str, content: str):
           self.messages.append({
               "role": role,
               "content": content,
               "timestamp": datetime.now()
           })

State Persistence
~~~~~~~~~~~~~~~~~

Configure state persistence:

.. code-block:: python

   from haive.core.persistence import PersistenceConfig
   
   # File-based persistence
   persistence = PersistenceConfig(
       backend="file",
       path="./agent_states",
       format="json"
   )
   
   # PostgreSQL persistence
   persistence = PersistenceConfig(
       backend="postgres",
       connection_string="postgresql://user:pass@localhost/haive",
       table_name="agent_states"
   )
   
   # Redis persistence
   persistence = PersistenceConfig(
       backend="redis",
       host="localhost",
       port=6379,
       db=0
   )

Vector Store Configuration
--------------------------

Available Providers
~~~~~~~~~~~~~~~~~~~

Configure different vector store backends:

**Chroma**:

.. code-block:: python

   from haive.core.engine.vectorstore import VectorStoreConfig
   
   vector_config = VectorStoreConfig(
       provider="chroma",
       collection_name="documents",
       persist_directory="./chroma_data",
       embedding_model="text-embedding-ada-002"
   )

**Pinecone**:

.. code-block:: python

   vector_config = VectorStoreConfig(
       provider="pinecone",
       api_key=os.getenv("PINECONE_API_KEY"),
       environment="us-east-1",
       index_name="haive-docs",
       embedding_model="text-embedding-ada-002"
   )

**FAISS**:

.. code-block:: python

   vector_config = VectorStoreConfig(
       provider="faiss",
       index_path="./faiss_index",
       embedding_model="sentence-transformers/all-MiniLM-L6-v2"
   )

**PostgreSQL with pgvector**:

.. code-block:: python

   vector_config = VectorStoreConfig(
       provider="postgres",
       connection_string="postgresql://user:pass@localhost/haive",
       table_name="embeddings",
       embedding_model="text-embedding-ada-002"
   )

Embedding Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Configure embedding models:

.. code-block:: python

   from haive.core.engine.embedding import EmbeddingConfig
   
   # OpenAI embeddings
   embedding_config = EmbeddingConfig(
       provider="openai",
       model="text-embedding-ada-002",
       api_key=os.getenv("OPENAI_API_KEY")
   )
   
   # HuggingFace embeddings
   embedding_config = EmbeddingConfig(
       provider="huggingface",
       model="sentence-transformers/all-MiniLM-L6-v2",
       device="cuda"  # or "cpu"
   )
   
   # Cohere embeddings
   embedding_config = EmbeddingConfig(
       provider="cohere",
       model="embed-english-v3.0",
       api_key=os.getenv("COHERE_API_KEY")
   )

Tool Configuration
------------------

Tool Registration
~~~~~~~~~~~~~~~~~

Register and configure tools:

.. code-block:: python

   from langchain_core.tools import tool
   from haive.core.engine.tool import ToolConfig
   
   # Simple tool
   @tool
   def calculator(expression: str) -> str:
       """Calculate mathematical expressions."""
       return str(eval(expression))
   
   # Tool with configuration
   tool_config = ToolConfig(
       name="web_search",
       description="Search the web for information",
       parameters={
           "max_results": 10,
           "safe_search": True
       },
       rate_limit={"calls": 100, "period": "hour"}
   )

Tool Permissions
~~~~~~~~~~~~~~~~

Control tool access:

.. code-block:: python

   from haive.core.engine.tool import ToolPermissions
   
   permissions = ToolPermissions(
       allowed_tools=["calculator", "web_search"],
       blocked_tools=["file_write", "shell_execute"],
       require_confirmation=["api_call", "database_query"],
       max_tool_calls=10  # Per conversation
   )

Graph Configuration
-------------------

Graph Builder Options
~~~~~~~~~~~~~~~~~~~~~

Configure workflow graphs:

.. code-block:: python

   from haive.core.graph import GraphConfig
   
   graph_config = GraphConfig(
       # Execution options
       max_iterations=10,  # Prevent infinite loops
       timeout=60.0,  # Overall timeout
       
       # Memory options
       checkpointing=True,  # Enable state checkpoints
       checkpoint_interval=5,  # Checkpoint every N steps
       
       # Debugging
       debug=True,  # Enable debug logging
       trace_execution=True,  # Detailed execution trace
       
       # Parallelization
       max_parallel_nodes=4,  # Concurrent node execution
       thread_pool_size=8
   )

Conditional Routing
~~~~~~~~~~~~~~~~~~~

Configure dynamic routing:

.. code-block:: python

   from haive.core.graph.routers import ConditionalRouter
   
   router_config = ConditionalRouter(
       conditions={
           "needs_search": lambda state: "search" in state.user_query,
           "needs_calculation": lambda state: any(op in state.user_query for op in ["+", "-", "*", "/"]),
           "needs_clarification": lambda state: len(state.messages) < 2
       },
       default_route="process_general"
   )

Environment Variables
---------------------

Core Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~

haive-core recognizes these environment variables:

.. code-block:: bash

   # API Keys
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   GOOGLE_API_KEY=...
   COHERE_API_KEY=...
   
   # Model Defaults
   HAIVE_DEFAULT_MODEL=gpt-4
   HAIVE_DEFAULT_TEMPERATURE=0.7
   HAIVE_DEFAULT_MAX_TOKENS=1000
   
   # Vector Store
   PINECONE_API_KEY=...
   PINECONE_ENVIRONMENT=us-east-1
   WEAVIATE_URL=http://localhost:8080
   QDRANT_URL=http://localhost:6333
   
   # Database
   HAIVE_POSTGRES_URL=postgresql://user:pass@localhost/haive
   HAIVE_REDIS_URL=redis://localhost:6379
   
   # Debugging
   HAIVE_DEBUG=true
   HAIVE_LOG_LEVEL=DEBUG
   HAIVE_TRACE_EXECUTION=true

Loading Configuration
~~~~~~~~~~~~~~~~~~~~~

Load from environment files:

.. code-block:: python

   from haive.core.config import load_config
   
   # Load from .env file
   config = load_config(".env")
   
   # Load from YAML
   config = load_config("config.yaml")
   
   # Load from TOML
   config = load_config("config.toml")
   
   # Merge multiple sources
   config = load_config([".env", "config.yaml", "local.toml"])

Advanced Configuration
----------------------

Custom Providers
~~~~~~~~~~~~~~~~

Add custom LLM providers:

.. code-block:: python

   from haive.core.engine.base import BaseEngine
   
   class CustomLLMProvider(BaseEngine):
       def __init__(self, api_key: str, **kwargs):
           self.api_key = api_key
           super().__init__(**kwargs)
       
       def invoke(self, messages):
           # Custom implementation
           pass
   
   # Register provider
   from haive.core.registry import register_provider
   register_provider("custom_llm", CustomLLMProvider)

Plugin Configuration
~~~~~~~~~~~~~~~~~~~~

Configure plugins:

.. code-block:: python

   from haive.core.plugins import PluginConfig
   
   plugin_config = PluginConfig(
       enabled_plugins=["monitoring", "caching", "rate_limiting"],
       plugin_settings={
           "monitoring": {
               "endpoint": "http://localhost:9090",
               "interval": 60
           },
           "caching": {
               "backend": "redis",
               "ttl": 3600
           },
           "rate_limiting": {
               "max_requests": 1000,
               "window": "hour"
           }
       }
   )

Performance Tuning
~~~~~~~~~~~~~~~~~~

Optimize performance:

.. code-block:: python

   from haive.core.config import PerformanceConfig
   
   perf_config = PerformanceConfig(
       # Batching
       batch_size=10,
       batch_timeout=1.0,
       
       # Caching
       enable_cache=True,
       cache_ttl=3600,
       cache_size=1000,
       
       # Connection pooling
       connection_pool_size=20,
       connection_timeout=5.0,
       
       # Memory management
       max_memory_mb=1024,
       gc_interval=300
   )

Configuration Best Practices
----------------------------

1. **Use Environment Variables**: Keep sensitive data out of code
2. **Layer Configurations**: Base → Environment → Runtime
3. **Validate Early**: Check configuration at startup
4. **Document Defaults**: Make default behavior clear
5. **Version Configurations**: Track config changes
6. **Test Configurations**: Have test-specific configs
7. **Monitor Performance**: Log configuration impacts

Next Steps
----------

- Review :doc:`getting_started` for practical examples
- Check :doc:`concepts` for architectural overview
- See :doc:`API Reference <autoapi/haive/index>` for detailed options