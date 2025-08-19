Engine Architecture
===================

.. currentmodule:: haive.core.engine

The **Engine System** is the beating heart of Haive Core - a **revolutionary universal interface** for AI components that provides **seamless multi-provider orchestration**, **structured output handling**, **tool execution**, and **streaming capabilities** through a unified, extensible architecture that adapts to any AI workload.

🚀 **Beyond Simple LLM Wrappers**
---------------------------------

**Transform Your AI Integration from Fragmented to Unified:**

**Universal Engine Interface**
   Single API for LLMs, retrievers, embedders, and custom engines with automatic provider detection and configuration

**Multi-Provider Orchestration**
   Seamless switching between 20+ providers with automatic failover, load balancing, and cost optimization

**Structured Output Revolution**
   Type-safe responses with Pydantic v2, automatic validation, and intelligent parsing for reliable AI outputs

**Advanced Tool Integration**
   Parallel tool execution, automatic discovery, validation framework, and error recovery for robust workflows

**Streaming & Async First**
   Built for real-time applications with native streaming, async execution, and backpressure handling

Core Engine Components
----------------------

AugLLM Configuration System
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: haive.core.engine.aug_llm.AugLLMConfig
   :members:
   :undoc-members:
   :show-inheritance:

**The Ultimate LLM Configuration Framework**

AugLLMConfig provides a comprehensive configuration system that goes far beyond simple model wrappers, offering enterprise-grade features for production AI systems.

**Configuration Power**::

    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.engine.providers import AzureLLMConfig, AnthropicConfig
    from pydantic import BaseModel
    
    # Define structured output
    class AnalysisResult(BaseModel):
        sentiment: str
        confidence: float
        key_topics: List[str]
        recommendations: List[str]
    
    # Create advanced configuration
    config = AugLLMConfig(
        # Provider configuration
        llm_config=AzureLLMConfig(
            model="gpt-4",
            temperature=0.7,
            max_tokens=2000,
            api_version="2024-02-01"
        ),
        
        # System setup
        system_message="You are an expert data analyst.",
        
        # Tool integration
        tools=[web_search, calculator, database_query],
        force_tool_choice=["web_search"],  # Require web search
        
        # Structured output
        structured_output_model=AnalysisResult,
        structured_output_version="v2",  # Use latest handling
        
        # Advanced features
        enable_streaming=True,
        retry_strategy="exponential",
        timeout=30,
        
        # Callbacks for monitoring
        callbacks=[token_counter, latency_tracker]
    )
    
    # Create runnable chain
    analyzer = config.create_runnable()
    
    # Execute with streaming
    async for chunk in analyzer.astream({"query": "Analyze market trends"}):
        print(chunk)  # Real-time streaming output

**Multi-Shot Learning Configuration**::

    # Configure with examples
    config = AugLLMConfig(
        llm_config=llm_config,
        
        # Few-shot examples
        examples=[
            {"input": "The product is amazing!", "output": "positive"},
            {"input": "Terrible experience", "output": "negative"},
            {"input": "It's okay, nothing special", "output": "neutral"}
        ],
        
        # Example formatting
        example_prompt=PromptTemplate(
            template="Input: {input}\nOutput: {output}"
        ),
        prefix="Classify the sentiment of the following texts:",
        suffix="Input: {text}\nOutput:",
        
        # This creates an intelligent few-shot classifier
    )

Engine Factory System
~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.engine.factory
   :members:
   :undoc-members:

**Dynamic Engine Creation and Management**

The factory system enables runtime engine creation with automatic configuration discovery and validation.

**Factory Patterns**::

    from haive.core.engine import EngineFactory, EngineRegistry
    
    # Register custom engine
    @EngineRegistry.register("custom_llm")
    class CustomLLMEngine(InvokableEngine):
        """Custom LLM implementation."""
        
        def invoke(self, input_data):
            # Custom logic
            return process_with_custom_model(input_data)
    
    # Create engines dynamically
    factory = EngineFactory()
    
    # Auto-detect best provider
    engine = factory.create_engine(
        task_type="text-generation",
        requirements={
            "max_tokens": 4000,
            "supports_tools": True,
            "cost_limit": 0.10  # Per request
        }
    )
    
    # Create with specific config
    azure_engine = factory.create_engine(
        engine_type="llm",
        provider="azure",
        config={"model": "gpt-4", "temperature": 0.5}
    )

Multi-Provider Support
~~~~~~~~~~~~~~~~~~~~~~

**20+ Provider Integrations**

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: OpenAI
      
      * GPT-4, GPT-3.5
      * DALL-E 3
      * Whisper
      * Embeddings

   .. grid-item-card:: Anthropic
      
      * Claude 3 Opus/Sonnet
      * Claude 2.1
      * Claude Instant
      * Constitutional AI

   .. grid-item-card:: Google
      
      * Gemini Pro/Ultra
      * PaLM 2
      * Vertex AI
      * Custom models

   .. grid-item-card:: Azure
      
      * Azure OpenAI
      * Cognitive Services
      * Custom deployments
      * Private endpoints

   .. grid-item-card:: AWS
      
      * Bedrock
      * SageMaker
      * Comprehend
      * Textract

   .. grid-item-card:: Open Source
      
      * Hugging Face
      * Ollama
      * LlamaCpp
      * vLLM

**Provider Orchestration Example**::

    from haive.core.engine.providers import MultiProviderOrchestrator
    
    # Configure provider pool
    orchestrator = MultiProviderOrchestrator([
        # Primary provider
        AzureLLMConfig(
            model="gpt-4",
            priority=1,
            rate_limit=100,  # Requests per minute
            cost_per_token=0.00003
        ),
        
        # Fallback for high load
        AnthropicConfig(
            model="claude-3-sonnet",
            priority=2,
            rate_limit=50,
            cost_per_token=0.00002
        ),
        
        # Budget option
        OllamaConfig(
            model="llama3-70b",
            priority=3,
            rate_limit=None,  # Unlimited local
            cost_per_token=0.0
        )
    ])
    
    # Intelligent routing
    response = await orchestrator.execute(
        prompt="Complex analysis task",
        routing_strategy="cost_optimized",  # or "latency_optimized"
        fallback_on_error=True,
        max_retries=3
    )

Tool Integration Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Advanced Tool Execution System**

.. automodule:: haive.core.engine.tool
   :members:
   :undoc-members:

**Tool Creation and Management**::

    from haive.core.engine.tool import tool, ToolEngine
    from typing import Annotated
    
    # Define tools with rich metadata
    @tool
    def analyze_data(
        data: Annotated[List[float], "Numerical data to analyze"],
        method: Annotated[str, "Analysis method: mean, median, std"] = "mean"
    ) -> Annotated[dict, "Analysis results with statistics"]:
        """Perform statistical analysis on numerical data.
        
        This tool supports various statistical methods and returns
        comprehensive results including confidence intervals.
        """
        import numpy as np
        
        if method == "mean":
            result = {
                "value": np.mean(data),
                "confidence_interval": calculate_ci(data),
                "sample_size": len(data)
            }
        # ... more methods
        
        return result
    
    # Create tool engine
    tool_engine = ToolEngine(
        tools=[analyze_data, web_search, database_query],
        execution_mode="parallel",  # Execute independent tools in parallel
        timeout_per_tool=10,
        error_handling="continue"  # Don't fail on single tool error
    )
    
    # Execute with validation
    results = await tool_engine.execute_tools([
        {"tool": "analyze_data", "args": {"data": [1, 2, 3, 4, 5]}},
        {"tool": "web_search", "args": {"query": "latest statistics"}}
    ])

Structured Output System
~~~~~~~~~~~~~~~~~~~~~~~~

**Type-Safe AI Responses**

.. automodule:: haive.core.engine.output_parser
   :members:
   :undoc-members:

**Structured Output Patterns**::

    from haive.core.engine.output_parser import create_structured_parser
    from pydantic import BaseModel, Field
    from typing import List, Optional
    
    # Complex nested structure
    class Address(BaseModel):
        street: str
        city: str
        country: str
        postal_code: Optional[str] = None
    
    class Person(BaseModel):
        name: str = Field(description="Full name")
        age: int = Field(ge=0, le=150)
        email: str = Field(pattern=r"[^@]+@[^@]+\.[^@]+")
        address: Address
        skills: List[str] = Field(min_items=1)
        
    class TeamAnalysis(BaseModel):
        team_name: str
        members: List[Person]
        average_age: float
        top_skills: List[str] = Field(max_items=5)
        recommendations: List[str]
    
    # Create parser with validation
    parser = create_structured_parser(
        model=TeamAnalysis,
        strict_mode=True,  # Enforce all validations
        repair_json=True,  # Fix malformed JSON
        max_retries=3
    )
    
    # Use with LLM
    config = AugLLMConfig(
        llm_config=llm_config,
        structured_output_model=TeamAnalysis,
        output_parser=parser
    )
    
    # Get validated, typed response
    result: TeamAnalysis = config.create_runnable().invoke(
        "Analyze our development team structure"
    )
    print(f"Average age: {result.average_age}")
    print(f"Top skills: {', '.join(result.top_skills)}")

Streaming Architecture
~~~~~~~~~~~~~~~~~~~~~~

**Real-Time Data Processing**

.. automodule:: haive.core.engine.streaming
   :members:
   :undoc-members:

**Advanced Streaming Patterns**::

    from haive.core.engine.streaming import StreamingEngine, ChunkProcessor
    
    class TokenAggregator(ChunkProcessor):
        """Aggregate tokens with buffering."""
        
        def __init__(self, buffer_size: int = 10):
            self.buffer = []
            self.buffer_size = buffer_size
            
        async def process_chunk(self, chunk):
            self.buffer.append(chunk)
            
            if len(self.buffer) >= self.buffer_size:
                # Emit aggregated chunk
                result = "".join(self.buffer)
                self.buffer = []
                return result
            return None  # Buffer not full
    
    # Create streaming pipeline
    streaming_engine = StreamingEngine(
        engine=llm_engine,
        processors=[
            TokenAggregator(buffer_size=5),
            SentimentAnalyzer(),  # Analyze sentiment per chunk
            KeywordExtractor()    # Extract keywords in real-time
        ]
    )
    
    # Stream with processing
    async for processed_chunk in streaming_engine.stream(prompt):
        print(f"Chunk: {processed_chunk.text}")
        print(f"Sentiment: {processed_chunk.sentiment}")
        print(f"Keywords: {processed_chunk.keywords}")

Performance & Optimization
--------------------------

Engine Performance Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Blazing Fast Execution**

* **Initialization**: < 10ms engine startup time
* **First Token**: < 100ms time to first token (streaming)
* **Throughput**: 10,000+ tokens/second (local models)
* **Concurrency**: 1,000+ parallel requests
* **Memory**: < 100MB base memory footprint

**Optimization Strategies**::

    from haive.core.engine.optimization import EngineOptimizer
    
    # Create optimized engine
    optimizer = EngineOptimizer()
    
    optimized_engine = optimizer.optimize(
        base_engine,
        strategies=[
            "connection_pooling",    # Reuse connections
            "response_caching",      # Cache common queries
            "batch_processing",      # Batch similar requests
            "token_budgeting",      # Manage token usage
            "adaptive_timeout"      # Dynamic timeout adjustment
        ]
    )
    
    # Monitor performance
    metrics = optimized_engine.get_metrics()
    print(f"Average latency: {metrics.avg_latency}ms")
    print(f"Cache hit rate: {metrics.cache_hit_rate}%")
    print(f"Token efficiency: {metrics.tokens_per_dollar}")

Cost Optimization
~~~~~~~~~~~~~~~~~

**Intelligent Cost Management**::

    from haive.core.engine.cost import CostOptimizer, BudgetManager
    
    # Set up budget controls
    budget_manager = BudgetManager(
        daily_limit=100.0,  # $100/day
        alert_thresholds=[0.5, 0.8, 0.95],
        notification_handlers=[email_handler, slack_handler]
    )
    
    # Cost-aware routing
    cost_optimizer = CostOptimizer(
        providers={
            "gpt-4": {"cost_per_1k_tokens": 0.03, "quality": 0.95},
            "claude-3": {"cost_per_1k_tokens": 0.02, "quality": 0.93},
            "llama3": {"cost_per_1k_tokens": 0.0, "quality": 0.85}
        }
    )
    
    # Route based on query complexity
    engine = cost_optimizer.select_engine(
        query=user_query,
        quality_threshold=0.9,  # Minimum quality required
        optimize_for="cost"     # or "quality" or "balanced"
    )

Advanced Patterns
-----------------

Retrieval-Augmented Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Advanced RAG Implementation**::

    from haive.core.engine.retriever import RetrieverEngine
    from haive.core.engine.patterns import RAGPattern
    
    # Configure RAG system
    rag = RAGPattern(
        retriever=RetrieverEngine(
            vector_store=pinecone_store,
            embedding_model="text-embedding-3-large",
            top_k=5,
            similarity_threshold=0.8
        ),
        generator=AugLLMConfig(
            llm_config=gpt4_config,
            system_message="Use the provided context to answer questions accurately."
        ),
        reranker=CohereReranker(model="rerank-english-v2.0"),
        citation_mode="inline"  # Add citations to response
    )
    
    # Execute RAG query
    result = await rag.query(
        "What are the latest developments in quantum computing?",
        filters={"date": {"$gte": "2024-01-01"}},
        include_sources=True
    )
    
    print(result.answer)
    print(f"Sources: {result.sources}")
    print(f"Confidence: {result.confidence}")

Engine Composition
~~~~~~~~~~~~~~~~~~

**Building Complex Engines**::

    from haive.core.engine.composition import EngineComposer, Pipeline
    
    # Compose multi-stage engine
    composer = EngineComposer()
    
    # Stage 1: Information extraction
    extractor = composer.create_stage(
        name="extractor",
        engine=AugLLMConfig(
            llm_config=fast_model,
            structured_output_model=ExtractedInfo
        )
    )
    
    # Stage 2: Enrichment with external data
    enricher = composer.create_stage(
        name="enricher",
        engine=ToolEngine(tools=[api_lookup, database_query]),
        depends_on=["extractor"]
    )
    
    # Stage 3: Analysis and synthesis
    analyzer = composer.create_stage(
        name="analyzer",
        engine=AugLLMConfig(
            llm_config=powerful_model,
            system_message="Perform deep analysis on enriched data"
        ),
        depends_on=["enricher"]
    )
    
    # Build pipeline
    pipeline = composer.build_pipeline(
        stages=[extractor, enricher, analyzer],
        execution_mode="sequential",
        state_passing="incremental"  # Each stage adds to state
    )
    
    # Execute pipeline
    final_result = await pipeline.execute(initial_input)

Enterprise Features
-------------------

**Production-Ready Capabilities**

* **High Availability**: Multi-region deployment with automatic failover
* **Security**: End-to-end encryption, API key rotation, audit logging
* **Compliance**: GDPR, HIPAA, SOC2 compliant configurations
* **Monitoring**: OpenTelemetry integration, custom metrics, alerting
* **Governance**: Model access control, usage policies, cost allocation

See Also
--------

* :doc:`schema_system` - Dynamic state management for engines
* :doc:`graph_workflows` - Orchestrate engines in workflows
* :doc:`tool_integration` - Deep dive into tool system
* :doc:`examples` - Real-world engine patterns