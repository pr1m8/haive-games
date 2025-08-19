Common Utilities
================

.. currentmodule:: haive.core.common

The **Common Utilities** module is the Swiss Army knife of the Haive framework - a **comprehensive collection of battle-tested components** providing **reusable mixins**, **data structures**, **type utilities**, **validation helpers**, and **performance optimizations** that power every aspect of the AI infrastructure.

🧰 **Beyond Basic Utilities**
-----------------------------

**Transform Your Code from Repetitive to Reusable:**

**Intelligent Mixins**
   Powerful mixin classes that add capabilities like timestamps, IDs, state management, and recompilation to any component

**Advanced Data Structures**
   Specialized trees, graphs, ordered collections, and nested dictionaries optimized for AI workflows

**Type System Enhancements**
   Runtime type checking, generic helpers, and advanced type inference for bulletproof code

**Validation Framework**
   Comprehensive validation utilities for data integrity, schema compliance, and error handling

**Performance Helpers**
   Caching, memoization, lazy loading, and optimization utilities for blazing-fast execution

Core Utility Components
-----------------------

Mixin Architecture
~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.common.mixins
   :members:
   :undoc-members:

**Powerful Capability Injection**

The mixin system provides composable behaviors that can be added to any class for instant functionality.

**Essential Mixins**::

    from haive.core.common.mixins import (
        TimestampMixin, IDMixin, StateMixin,
        RecompileMixin, CacheableMixin, SerializableMixin
    )
    from datetime import datetime
    import uuid
    
    # Timestamp tracking
    class TrackedComponent(TimestampMixin):
        """Component with automatic timestamp tracking."""
        
        def process(self, data):
            # created_at and updated_at automatically managed
            result = self.analyze(data)
            # updated_at refreshed on any change
            return result
    
    # Unique identification
    class IdentifiableAgent(IDMixin):
        """Agent with UUID and custom ID support."""
        
        id_prefix = "agent"  # Generates: agent_7f3d8a9b
        id_generator = lambda: str(uuid.uuid4())[:8]
        
        def __init__(self, name: str):
            super().__init__()
            self.name = name
            # self.id automatically generated
    
    # State management
    class StatefulProcessor(StateMixin):
        """Processor with built-in state tracking."""
        
        state_schema = ProcessorState  # Pydantic model
        state_defaults = {"status": "idle", "queue": []}
        
        async def process_item(self, item):
            self.update_state(status="processing")
            
            try:
                result = await self.process(item)
                self.update_state(
                    status="idle",
                    last_processed=item.id,
                    success_count=self.state.success_count + 1
                )
                return result
            except Exception as e:
                self.update_state(
                    status="error",
                    last_error=str(e),
                    error_count=self.state.error_count + 1
                )
                raise
    
    # Recompilation support
    class DynamicGraph(RecompileMixin):
        """Graph that can trigger its own recompilation."""
        
        def add_node(self, node):
            self.nodes.append(node)
            self.mark_for_recompile("Node added")
            
        def should_recompile(self) -> bool:
            # Custom recompilation logic
            return (
                self.needs_recompile or
                len(self.nodes) > self.last_compiled_size * 1.5
            )

**Advanced Mixin Patterns**::

    from haive.core.common.mixins import (
        ObservableMixin, ValidatableMixin,
        RetryableMixin, ThrottleMixin
    )
    
    # Observable pattern
    class ObservableAgent(ObservableMixin):
        """Agent that emits events."""
        
        def process(self, input_data):
            self.emit("processing_started", {"input": input_data})
            
            try:
                result = self._process(input_data)
                self.emit("processing_completed", {
                    "input": input_data,
                    "output": result
                })
                return result
            except Exception as e:
                self.emit("processing_failed", {
                    "input": input_data,
                    "error": str(e)
                })
                raise
    
    # Usage
    agent = ObservableAgent()
    agent.on("processing_completed", lambda e: print(f"Done: {e.data}"))
    
    # Validation mixin
    class ValidatedConfig(ValidatableMixin):
        """Configuration with validation."""
        
        validation_rules = {
            "temperature": lambda x: 0 <= x <= 2,
            "max_tokens": lambda x: x > 0 and x <= 4000,
            "model": lambda x: x in ["gpt-4", "claude-3", "llama3"]
        }
        
        def __init__(self, **kwargs):
            self.validate(kwargs)  # Automatic validation
            super().__init__(**kwargs)
    
    # Retry logic
    class ResilientAPI(RetryableMixin):
        """API client with automatic retries."""
        
        retry_config = {
            "max_attempts": 3,
            "backoff": "exponential",
            "retry_on": [ConnectionError, TimeoutError],
            "max_delay": 30
        }
        
        @retry_method
        async def fetch_data(self, url):
            # Automatically retried on failure
            return await self.http_client.get(url)

Data Structures
~~~~~~~~~~~~~~~

.. automodule:: haive.core.common.structures
   :members:
   :undoc-members:

**Specialized Collections for AI**

Advanced data structures optimized for common AI patterns.

**Tree Structures**::

    from haive.core.common.structures import (
        Tree, TreeNode, TreeTraversal,
        NamedTree, WeightedTree
    )
    
    # Build knowledge tree
    knowledge_tree = Tree[str]("AI")
    
    # Add branches
    ml_node = knowledge_tree.add_child("Machine Learning")
    dl_node = ml_node.add_child("Deep Learning")
    rl_node = ml_node.add_child("Reinforcement Learning")
    
    # Add leaves
    dl_node.add_children([
        "Transformers",
        "CNNs",
        "RNNs",
        "GANs"
    ])
    
    # Traverse tree
    for node in knowledge_tree.traverse(TreeTraversal.DEPTH_FIRST):
        print("  " * node.depth + node.value)
    
    # Find nodes
    transformer_node = knowledge_tree.find("Transformers")
    path = transformer_node.get_path()  # ["AI", "Machine Learning", "Deep Learning", "Transformers"]
    
    # Weighted tree for decision making
    decision_tree = WeightedTree[str]("Root Decision")
    
    option_a = decision_tree.add_weighted_child("Option A", weight=0.7)
    option_b = decision_tree.add_weighted_child("Option B", weight=0.3)
    
    # Get best path
    best_path = decision_tree.get_highest_weight_path()

**Nested Dictionaries**::

    from haive.core.common.structures import (
        NestedDict, DeepDict, 
        FrozenDict, OrderedNestedDict
    )
    
    # Deep nested access
    config = NestedDict({
        "model": {
            "name": "gpt-4",
            "settings": {
                "temperature": 0.7,
                "max_tokens": 2000
            }
        }
    })
    
    # Dot notation access
    temp = config["model.settings.temperature"]  # 0.7
    config["model.settings.streaming"] = True    # Deep set
    
    # Default values
    timeout = config.get("api.timeout", default=30)
    
    # Deep merge
    updates = {
        "model": {
            "settings": {
                "temperature": 0.8,
                "top_p": 0.9
            }
        }
    }
    config.deep_merge(updates)
    
    # Frozen immutable dict
    constants = FrozenDict({
        "API_KEY": "secret",
        "BASE_URL": "https://api.example.com"
    })
    # constants["API_KEY"] = "new"  # Raises ImmutableError

Type Utilities
~~~~~~~~~~~~~~

.. automodule:: haive.core.common.types
   :members:
   :undoc-members:

**Advanced Type System Helpers**

Utilities for runtime type checking and manipulation.

**Type Checking Utilities**::

    from haive.core.common.types import (
        is_generic_type, get_type_args,
        is_optional, unwrap_optional,
        create_typed_dict, TypeValidator
    )
    from typing import List, Optional, Dict, Union
    
    # Check generic types
    assert is_generic_type(List[str])
    assert get_type_args(Dict[str, int]) == (str, int)
    
    # Handle optionals
    assert is_optional(Optional[str])
    assert unwrap_optional(Optional[int]) == int
    
    # Runtime type validation
    validator = TypeValidator()
    
    @validator.validate_types
    def process_data(
        items: List[str],
        config: Dict[str, Any],
        threshold: float = 0.5
    ) -> Dict[str, float]:
        # Types validated at runtime
        return {item: score for item, score in zip(items, scores)}
    
    # Create typed dictionaries dynamically
    ConfigType = create_typed_dict("ConfigType", {
        "model": str,
        "temperature": float,
        "max_tokens": int,
        "streaming": bool
    })
    
    config: ConfigType = {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 2000,
        "streaming": True
    }

Validation Framework
~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.common.validation
   :members:
   :undoc-members:

**Comprehensive Data Validation**

Robust validation utilities for ensuring data integrity.

**Validation Patterns**::

    from haive.core.common.validation import (
        Validator, ValidationRule,
        create_validator, compose_validators,
        validate_schema, validate_data
    )
    
    # Create custom validators
    @create_validator
    def validate_email(email: str) -> bool:
        """Validate email format."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email format: {email}")
        return True
    
    @create_validator
    def validate_api_key(key: str) -> bool:
        """Validate API key format."""
        if not key.startswith("sk-") or len(key) != 51:
            raise ValueError("Invalid API key format")
        return True
    
    # Compose validators
    user_validator = compose_validators({
        "email": validate_email,
        "api_key": validate_api_key,
        "age": lambda x: 0 < x < 150,
        "username": lambda x: len(x) >= 3 and x.isalnum()
    })
    
    # Validate data
    try:
        user_validator.validate({
            "email": "user@example.com",
            "api_key": "sk-" + "x" * 48,
            "age": 25,
            "username": "john123"
        })
    except ValidationError as e:
        print(f"Validation failed: {e.errors}")
    
    # Schema validation
    schema_valid = validate_schema(
        UserSchema,
        checks=["required_fields", "type_annotations", "default_values"]
    )

Performance Helpers
~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.common.performance
   :members:
   :undoc-members:

**Optimization Utilities**

Tools for improving performance across the framework.

**Caching and Memoization**::

    from haive.core.common.performance import (
        cached, memoize, lazy_property,
        timed, profile, BatchProcessor
    )
    import time
    
    # Function caching
    @cached(ttl=3600, maxsize=1000)
    def expensive_calculation(x: int, y: int) -> int:
        """Cached for 1 hour."""
        time.sleep(1)  # Simulate expensive operation
        return x ** y
    
    # Method memoization
    class DataProcessor:
        @memoize
        def process_data(self, data: List[int]) -> Dict[str, Any]:
            """Results memoized per instance."""
            return {
                "mean": sum(data) / len(data),
                "max": max(data),
                "min": min(data)
            }
    
    # Lazy properties
    class ExpensiveObject:
        @lazy_property
        def computed_value(self) -> float:
            """Computed once on first access."""
            print("Computing expensive value...")
            time.sleep(2)
            return 42.0
    
    # Performance profiling
    @timed
    def slow_function():
        """Execution time logged."""
        time.sleep(0.5)
        
    @profile(metrics=["time", "memory"])
    def memory_intensive():
        """Full profiling enabled."""
        large_list = [i for i in range(1_000_000)]
        return sum(large_list)
    
    # Batch processing
    processor = BatchProcessor(
        batch_size=100,
        process_func=lambda batch: [x * 2 for x in batch],
        parallel=True,
        max_workers=4
    )
    
    results = processor.process_all(range(10_000))

Utility Functions
~~~~~~~~~~~~~~~~~

.. automodule:: haive.core.common.utils
   :members:
   :undoc-members:

**Essential Helper Functions**

Common utilities used throughout the framework.

**String and Data Manipulation**::

    from haive.core.common.utils import (
        snake_to_camel, camel_to_snake,
        truncate, pluralize, humanize_bytes,
        deep_get, deep_set, flatten_dict
    )
    
    # Case conversion
    assert snake_to_camel("hello_world") == "HelloWorld"
    assert camel_to_snake("HelloWorld") == "hello_world"
    
    # String formatting
    assert truncate("Long text here", 10) == "Long te..."
    assert pluralize(1, "item") == "1 item"
    assert pluralize(5, "item") == "5 items"
    assert humanize_bytes(1024 * 1024) == "1.0 MB"
    
    # Deep dictionary access
    data = {"user": {"profile": {"name": "John"}}}
    assert deep_get(data, "user.profile.name") == "John"
    deep_set(data, "user.profile.age", 30)
    
    # Flatten nested structures
    flat = flatten_dict({
        "user": {
            "name": "John",
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        }
    })
    # {"user.name": "John", "user.settings.theme": "dark", ...}

**Async Utilities**::

    from haive.core.common.utils import (
        run_async, gather_with_timeout,
        async_retry, create_task_group
    )
    
    # Run async in sync context
    result = run_async(async_function(param))
    
    # Gather with timeout
    results = await gather_with_timeout(
        [async_task1(), async_task2(), async_task3()],
        timeout=5.0,
        return_exceptions=True
    )
    
    # Async retry
    @async_retry(attempts=3, delay=1.0)
    async def flaky_api_call():
        # Automatically retried
        return await external_api.fetch()
    
    # Task groups
    async with create_task_group() as tg:
        tg.create_task(process_item(1))
        tg.create_task(process_item(2))
        tg.create_task(process_item(3))
        # All tasks awaited on exit

Advanced Patterns
-----------------

Plugin System
~~~~~~~~~~~~~

**Extensible Component Architecture**::

    from haive.core.common.plugins import (
        PluginRegistry, Plugin,
        hook, extension_point
    )
    
    # Define plugin interface
    class AnalyzerPlugin(Plugin):
        """Base class for analyzer plugins."""
        
        @extension_point
        def analyze(self, data: Any) -> Dict:
            """Analyze data and return results."""
            pass
    
    # Create plugin
    @PluginRegistry.register("sentiment")
    class SentimentAnalyzer(AnalyzerPlugin):
        """Sentiment analysis plugin."""
        
        def analyze(self, data: str) -> Dict:
            # Implementation
            return {"sentiment": "positive", "score": 0.8}
    
    # Use plugins
    registry = PluginRegistry()
    
    for plugin_name in registry.list_plugins("analyzer"):
        plugin = registry.get_plugin(plugin_name)
        result = plugin.analyze(text_data)

Event System
~~~~~~~~~~~~

**Decoupled Communication**::

    from haive.core.common.events import (
        EventBus, Event, 
        subscribe, emit
    )
    
    # Global event bus
    bus = EventBus()
    
    # Subscribe to events
    @bus.subscribe("agent.started")
    def on_agent_start(event: Event):
        print(f"Agent {event.data['agent_id']} started")
    
    @bus.subscribe("agent.completed", priority=10)
    async def on_agent_complete(event: Event):
        await log_completion(event.data)
    
    # Emit events
    bus.emit("agent.started", {"agent_id": "agent-123"})
    
    # Async event handling
    await bus.emit_async("agent.completed", {
        "agent_id": "agent-123",
        "duration": 5.2,
        "result": "success"
    })

Enterprise Features
-------------------

**Production-Ready Utilities**

* **Thread Safety**: All utilities designed for concurrent use
* **Memory Efficiency**: Optimized data structures and algorithms
* **Error Handling**: Comprehensive error types and recovery
* **Monitoring**: Built-in metrics and instrumentation
* **Compatibility**: Python 3.8+ with type stubs

See Also
--------

* :doc:`patterns` - Common patterns using utilities
* :doc:`performance` - Performance optimization guide
* :doc:`examples` - Utility usage examples
* :doc:`api_reference` - Complete API documentation