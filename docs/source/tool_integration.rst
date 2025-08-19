Tool Integration
================

.. currentmodule:: haive.core.tools

The **Tool Integration System** is a game-changing framework for AI capabilities - a **revolutionary tool orchestration platform** that provides **type-safe tool creation**, **automatic discovery**, **parallel execution**, **validation frameworks**, and **intelligent error recovery** to give your AI agents real-world superpowers.

🛠️ **Beyond Simple Function Calling**
--------------------------------------

**Transform Your AI from Thinker to Doer:**

**Type-Safe Tool Creation**
   Build tools with full type hints, automatic validation, and rich metadata for reliable AI execution

**Automatic Tool Discovery**
   Scan codebases to automatically find and register tools, with capability detection and categorization

**Parallel Tool Execution**
   Execute multiple independent tools simultaneously with intelligent resource management

**Validation & Error Recovery**
   Comprehensive input/output validation with automatic retry logic and graceful error handling

**Tool Composition Framework**
   Build complex tools from simple primitives with chainable, reusable components

Core Tool Components
--------------------

Tool Creation System
~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.tools.creation
   :members:
   :undoc-members:

**Revolutionary Tool Definition**

The tool creation system provides multiple approaches for defining tools, from simple decorators to complex class-based implementations.

**Decorator-Based Tools**::

    from haive.core.tools import tool
    from typing import Annotated, List, Dict, Optional
    import aiohttp
    
    @tool
    def calculate_compound_interest(
        principal: Annotated[float, "Initial investment amount"],
        rate: Annotated[float, "Annual interest rate (as decimal)"],
        time: Annotated[int, "Investment period in years"],
        compounds_per_year: Annotated[int, "Number of times interest compounds per year"] = 12
    ) -> Annotated[Dict[str, float], "Investment growth details"]:
        """Calculate compound interest with detailed breakdown.
        
        This tool calculates compound interest and provides a comprehensive
        analysis of investment growth over time.
        """
        amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
        interest_earned = amount - principal
        
        return {
            "final_amount": round(amount, 2),
            "interest_earned": round(interest_earned, 2),
            "effective_rate": round((amount/principal) ** (1/time) - 1, 4),
            "total_return": round(interest_earned / principal, 4)
        }
    
    @tool
    async def web_search(
        query: Annotated[str, "Search query"],
        max_results: Annotated[int, "Maximum number of results"] = 10,
        search_type: Annotated[str, "Type of search: web, news, images"] = "web"
    ) -> Annotated[List[Dict[str, str]], "Search results with title, url, snippet"]:
        """Perform web search with multiple search engines.
        
        Aggregates results from multiple search providers for comprehensive coverage.
        """
        async with aiohttp.ClientSession() as session:
            # Search implementation
            results = await multi_engine_search(session, query, max_results)
            
            return [
                {
                    "title": result.title,
                    "url": result.url,
                    "snippet": result.snippet,
                    "source": result.source
                }
                for result in results
            ]

**Class-Based Tools**::

    from haive.core.tools import BaseTool, ToolResult
    from pydantic import BaseModel, Field
    
    class DatabaseQueryTool(BaseTool):
        """Advanced database query tool with connection pooling."""
        
        name = "database_query"
        description = "Execute SQL queries with automatic connection management"
        
        class InputSchema(BaseModel):
            query: str = Field(description="SQL query to execute")
            database: str = Field(description="Target database name")
            timeout: Optional[int] = Field(default=30, description="Query timeout")
            
        class OutputSchema(BaseModel):
            results: List[Dict[str, Any]] = Field(description="Query results")
            row_count: int = Field(description="Number of rows returned")
            execution_time: float = Field(description="Query execution time")
            
        def __init__(self, connection_pool):
            self.pool = connection_pool
            
        async def _arun(self, query: str, database: str, timeout: int = 30) -> Dict:
            """Execute query with connection from pool."""
            async with self.pool.acquire() as conn:
                start_time = time.time()
                
                # Execute with timeout
                results = await asyncio.wait_for(
                    conn.fetch(query),
                    timeout=timeout
                )
                
                execution_time = time.time() - start_time
                
                return {
                    "results": [dict(row) for row in results],
                    "row_count": len(results),
                    "execution_time": execution_time
                }
        
        def _run(self, *args, **kwargs):
            """Synchronous version."""
            return asyncio.run(self._arun(*args, **kwargs))

Tool Discovery & Registry
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.tools.discovery
   :members:
   :undoc-members:

**Automatic Tool Detection**

The discovery system can automatically find and catalog tools across your codebase.

**Tool Discovery Patterns**::

    from haive.core.tools.discovery import ToolDiscovery, ToolRegistry
    
    # Initialize discovery system
    discovery = ToolDiscovery(
        scan_paths=["./tools", "./plugins", "./extensions"],
        include_patterns=["*_tool.py", "*_tools.py"],
        exclude_patterns=["test_*", "*_test.py"]
    )
    
    # Discover all tools
    discovered_tools = discovery.discover_all()
    print(f"Found {len(discovered_tools)} tools")
    
    # Discover with filters
    api_tools = discovery.discover_by_category("api")
    async_tools = discovery.discover_by_capability("async")
    validated_tools = discovery.discover_validated()  # Tools with schemas
    
    # Register discovered tools
    registry = ToolRegistry()
    for tool in discovered_tools:
        registry.register(tool)
    
    # Query registry
    calculation_tools = registry.query(
        category="calculation",
        capabilities=["numeric"],
        has_async=True
    )
    
    # Get tool by name with validation
    calc_tool = registry.get_tool(
        "calculate_compound_interest",
        validate_inputs=True
    )

Tool Execution Engine
~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.tools.execution
   :members:
   :undoc-members:

**Intelligent Tool Orchestration**

The execution engine handles complex tool orchestration scenarios with parallelism, dependencies, and error handling.

**Advanced Execution Patterns**::

    from haive.core.tools.execution import (
        ToolExecutor, ExecutionPlan,
        ParallelExecutor, ChainedExecutor
    )
    
    # Create execution engine
    executor = ToolExecutor(
        max_parallel=10,
        timeout_default=30,
        retry_policy={
            "max_attempts": 3,
            "backoff": "exponential",
            "retry_on": [TimeoutError, ConnectionError]
        }
    )
    
    # Define execution plan
    plan = ExecutionPlan()
    
    # Add tools with dependencies
    plan.add_tool("search", web_search, args={"query": "AI news"})
    plan.add_tool("analyze", sentiment_analysis, depends_on=["search"])
    plan.add_tool("summarize", summarizer, depends_on=["analyze"])
    
    # Parallel tools
    plan.add_parallel_tools([
        ("weather", get_weather, {"city": "London"}),
        ("news", get_news, {"topic": "technology"}),
        ("stocks", get_stocks, {"symbols": ["AAPL", "GOOGL"]})
    ])
    
    # Execute plan
    results = await executor.execute_plan(plan)
    
    # Chain execution with data flow
    chain = ChainedExecutor()
    chain.add_step(web_search, {"query": "quantum computing"})
    chain.add_step(extract_entities)  # Uses previous output
    chain.add_step(enhance_with_knowledge)  # Enhances entities
    chain.add_step(generate_report)  # Final report
    
    report = await chain.execute()

Tool Validation Framework
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.tools.validation
   :members:
   :undoc-members:

**Comprehensive Validation System**

Ensure tool reliability with multi-layer validation for inputs, outputs, and execution constraints.

**Validation Patterns**::

    from haive.core.tools.validation import (
        ToolValidator, ValidationRule,
        create_validator, compose_validators
    )
    
    # Create custom validators
    @create_validator
    def validate_sql_query(query: str) -> bool:
        """Validate SQL query safety."""
        forbidden = ["DROP", "DELETE", "TRUNCATE", "ALTER"]
        query_upper = query.upper()
        
        for keyword in forbidden:
            if keyword in query_upper:
                raise ValueError(f"Forbidden SQL keyword: {keyword}")
        
        return True
    
    @create_validator
    def validate_url(url: str) -> bool:
        """Validate URL format and accessibility."""
        from urllib.parse import urlparse
        
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            raise ValueError("Invalid URL format")
            
        if parsed.scheme not in ["http", "https"]:
            raise ValueError("Only HTTP(S) URLs allowed")
            
        return True
    
    # Compose validators
    api_validator = compose_validators([
        validate_url,
        validate_rate_limit,
        validate_api_key
    ])
    
    # Apply to tools
    @tool(validators=[validate_sql_query])
    def execute_query(query: str) -> List[Dict]:
        """Execute validated SQL query."""
        # Query execution
        pass
    
    # Runtime validation
    validator = ToolValidator()
    
    # Validate tool definition
    validation_result = validator.validate_tool_definition(
        my_tool,
        checks=[
            "has_description",
            "has_type_hints",
            "has_return_type",
            "has_examples"
        ]
    )
    
    # Validate execution context
    context_valid = validator.validate_execution_context({
        "tool": my_tool,
        "inputs": {"query": "SELECT * FROM users"},
        "timeout": 30,
        "memory_limit": "1GB"
    })

Tool Composition
~~~~~~~~~~~~~~~~

**Building Complex Tools from Primitives**

.. automodule:: haive.core.tools.composition
   :members:
   :undoc-members:

**Compositional Tool Patterns**::

    from haive.core.tools.composition import (
        ToolComposer, CompositeTool,
        ToolPipeline, ToolRouter
    )
    
    # Compose tools into pipelines
    research_pipeline = ToolPipeline([
        ("search", web_search),
        ("extract", extract_key_points),
        ("verify", fact_checker),
        ("summarize", create_summary)
    ])
    
    # Use as single tool
    research_tool = research_pipeline.as_tool(
        name="research_assistant",
        description="Comprehensive research tool"
    )
    
    # Conditional tool routing
    router = ToolRouter()
    
    router.add_route(
        condition=lambda x: x.get("type") == "calculation",
        tool=calculator
    )
    router.add_route(
        condition=lambda x: x.get("type") == "search",
        tool=web_search
    )
    router.add_route(
        condition=lambda x: x.get("type") == "analysis",
        tool=data_analyzer
    )
    
    # Use router as tool
    smart_tool = router.as_tool(
        name="smart_assistant",
        description="Routes to appropriate tool based on request type"
    )
    
    # Create composite tool with shared state
    class ResearchAssistant(CompositeTool):
        """Advanced research assistant combining multiple tools."""
        
        tools = [
            web_search,
            arxiv_search,
            semantic_scholar,
            pdf_extractor,
            summarizer
        ]
        
        def __init__(self):
            super().__init__()
            self.knowledge_base = []
            
        async def execute(self, query: str) -> Dict:
            """Execute comprehensive research."""
            # Search phase
            search_results = await self.parallel_execute([
                (web_search, {"query": query}),
                (arxiv_search, {"query": query}),
                (semantic_scholar, {"query": query})
            ])
            
            # Extract phase
            documents = []
            for result in search_results:
                if result.get("pdf_url"):
                    content = await pdf_extractor(result["pdf_url"])
                    documents.append(content)
            
            # Summarize phase
            summary = await summarizer({
                "documents": documents,
                "query": query
            })
            
            # Update knowledge base
            self.knowledge_base.extend(documents)
            
            return {
                "summary": summary,
                "sources": search_results,
                "documents_processed": len(documents)
            }

Performance & Optimization
--------------------------

Tool Performance Metrics
~~~~~~~~~~~~~~~~~~~~~~~~

**Lightning-Fast Tool Execution**

* **Invocation Overhead**: < 1ms per tool call
* **Parallel Execution**: Up to 100 concurrent tools
* **Validation Time**: < 0.5ms per parameter
* **Registry Lookup**: O(1) with 10,000+ tools
* **Memory Usage**: < 10KB per tool definition

**Performance Optimization**::

    from haive.core.tools.optimization import (
        ToolOptimizer, CachedTool,
        BatchedTool, ProfiledTool
    )
    
    # Cache deterministic tools
    @CachedTool(ttl=3600, max_size=1000)
    @tool
    def expensive_calculation(params: Dict) -> float:
        """Expensive calculation cached for 1 hour."""
        # Complex computation
        return result
    
    # Batch API calls
    @BatchedTool(batch_size=100, delay=0.1)
    @tool
    async def api_lookup(item_id: str) -> Dict:
        """Batched API calls for efficiency."""
        # Individual calls batched automatically
        return await api.get_item(item_id)
    
    # Profile tool performance
    @ProfiledTool(metrics=["latency", "memory", "cpu"])
    @tool
    def data_processor(data: List[Dict]) -> Dict:
        """Profiled data processing tool."""
        # Processing logic
        return results
    
    # Get profiling data
    metrics = data_processor.get_metrics()
    print(f"Average latency: {metrics.avg_latency}ms")
    print(f"Memory usage: {metrics.memory_usage}MB")

Tool Monitoring
~~~~~~~~~~~~~~~

**Real-Time Tool Analytics**::

    from haive.core.tools.monitoring import ToolMonitor, AlertManager
    
    # Initialize monitoring
    monitor = ToolMonitor(
        export_interval=60,  # Export metrics every minute
        retention_days=30
    )
    
    # Track all tool executions
    monitor.track_all_tools()
    
    # Set up alerts
    alerts = AlertManager()
    
    alerts.add_rule(
        name="high_error_rate",
        condition=lambda m: m.error_rate > 0.1,
        action=send_alert_email
    )
    
    alerts.add_rule(
        name="slow_tool",
        condition=lambda m: m.p95_latency > 5000,  # 5 seconds
        action=log_performance_issue
    )
    
    # Dashboard data
    dashboard_data = monitor.get_dashboard_data()

Advanced Patterns
-----------------

Stateful Tools
~~~~~~~~~~~~~~

**Tools with Persistent State**::

    from haive.core.tools import StatefulTool, ToolState
    
    class ConversationTool(StatefulTool):
        """Tool that maintains conversation context."""
        
        def __init__(self):
            super().__init__()
            self.state = ToolState()
            self.state.conversation_history = []
            self.state.user_preferences = {}
            
        async def _arun(self, message: str, user_id: str) -> str:
            """Process message with context."""
            # Load user context
            user_context = self.state.user_preferences.get(user_id, {})
            
            # Add to history
            self.state.conversation_history.append({
                "user_id": user_id,
                "message": message,
                "timestamp": datetime.now()
            })
            
            # Generate contextual response
            response = await self.generate_response(
                message,
                context=user_context,
                history=self.get_user_history(user_id)
            )
            
            # Update preferences based on interaction
            self.update_preferences(user_id, message, response)
            
            return response
        
        def save_state(self, path: str):
            """Persist tool state."""
            self.state.save(path)
            
        def load_state(self, path: str):
            """Restore tool state."""
            self.state = ToolState.load(path)

Tool Versioning
~~~~~~~~~~~~~~~

**Managing Tool Evolution**::

    from haive.core.tools.versioning import VersionedTool, migrate_tool
    
    @VersionedTool(version="2.0.0")
    @tool
    def enhanced_calculator(
        expression: str,
        variables: Optional[Dict[str, float]] = None,
        precision: int = 2
    ) -> Dict[str, Any]:
        """Enhanced calculator with variables support."""
        # New implementation
        pass
    
    # Migration from old version
    @migrate_tool(from_version="1.0.0", to_version="2.0.0")
    def migrate_calculator_inputs(old_inputs: Dict) -> Dict:
        """Migrate inputs from v1 to v2."""
        return {
            "expression": old_inputs["formula"],
            "variables": {},  # New feature
            "precision": 2    # New feature with default
        }
    
    # Version-aware execution
    result = await enhanced_calculator.execute(
        inputs={"formula": "2 + 2"},  # Old format
        input_version="1.0.0"  # Automatic migration
    )

Enterprise Features
-------------------

**Production-Ready Tool Management**

* **Tool Governance**: Approval workflows for tool deployment
* **Access Control**: Fine-grained permissions per tool
* **Audit Logging**: Complete execution history with inputs/outputs
* **Cost Tracking**: Monitor and limit tool execution costs
* **SLA Management**: Define and monitor tool performance SLAs

See Also
--------

* :doc:`engine_architecture` - Integrate tools with engines
* :doc:`graph_workflows` - Use tools in workflows
* :doc:`patterns` - Advanced tool patterns
* :doc:`examples` - Real-world tool examples