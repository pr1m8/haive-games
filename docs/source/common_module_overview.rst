Common Module Overview
======================

.. meta::
   :description: Comprehensive overview of the Haive Core Common module with intelligent mixins, data structures, and utilities
   :keywords: haive, common, mixins, utilities, data structures, type system

The Swiss Army Knife of AI Infrastructure
-----------------------------------------

.. container:: hero-section

   .. raw:: html

      <div class="hero-banner">
         <h1>🧰 Common Module</h1>
         <p class="subtitle">Battle-tested utilities that make AI systems smarter by default</p>
      </div>

The Common module provides an extraordinary collection of intelligent mixins, advanced data structures, and performance utilities that form the backbone of the Haive ecosystem.

.. contents:: Table of Contents
   :local:
   :depth: 3
   :backlinks: none

Architecture Overview
---------------------

.. graphviz::

   digraph common_architecture {
      rankdir=TB;
      node [shape=box, style="rounded,filled", fillcolor=lightblue];
      edge [color=darkblue];
      
      subgraph cluster_mixins {
         label="Mixin System";
         style=filled;
         fillcolor=lightyellow;
         
         IdentifierMixin [label="IdentifierMixin\n(Unique IDs)"];
         TimestampMixin [label="TimestampMixin\n(Created/Updated)"];
         VersionMixin [label="VersionMixin\n(Semantic Versioning)"];
         ObservableMixin [label="ObservableMixin\n(Event System)"];
         CacheableMixin [label="CacheableMixin\n(Result Caching)"];
      }
      
      subgraph cluster_structures {
         label="Data Structures";
         style=filled;
         fillcolor=lightgreen;
         
         Tree [label="Tree\n(Hierarchical Data)"];
         Graph [label="Graph\n(Network Structure)"];
         NamedList [label="NamedList\n(Enhanced Lists)"];
         NestedDict [label="NestedDict\n(Deep Access)"];
      }
      
      subgraph cluster_types {
         label="Type System";
         style=filled;
         fillcolor=lightcoral;
         
         TypeInference [label="Type Inference\n(Runtime Detection)"];
         ProtocolCheck [label="Protocol Checking\n(Interface Validation)"];
         TypeGuards [label="Type Guards\n(Safe Narrowing)"];
      }
      
      Component [label="Your Component", shape=ellipse, fillcolor=white];
      
      Component -> IdentifierMixin [label="inherits"];
      Component -> TimestampMixin [label="inherits"];
      Component -> Tree [label="uses"];
      Component -> TypeInference [label="validates with"];
   }

Mixin Architecture
------------------

Class Hierarchy
~~~~~~~~~~~~~~~

.. inheritance-diagram:: haive.core.common.mixins.IdentifierMixin
                        haive.core.common.mixins.TimestampMixin
                        haive.core.common.mixins.VersionMixin
                        haive.core.common.mixins.ObservableMixin
   :parts: 1
   :private-bases:

Core Mixins
~~~~~~~~~~~

.. autoclass:: haive.core.common.mixins.IdentifierMixin
   :members:
   :show-inheritance:
   :special-members: __init__

   **Example Usage**::

      from haive.core.common.mixins import IdentifierMixin
      
      class MyComponent(IdentifierMixin):
          def __init__(self, name: str):
              super().__init__()
              self.name = name
              # self.id is automatically generated
              
      component = MyComponent("example")
      print(component.id)  # e.g., "MyComponent_7f3d8a9b"

.. autoclass:: haive.core.common.mixins.TimestampMixin
   :members:
   :show-inheritance:

   **Automatic Timestamp Management**:

   .. code-block:: python

      class TrackedEntity(TimestampMixin):
          def update_data(self, new_data):
              self.data = new_data
              self.mark_updated()  # Updates timestamp
              
      entity = TrackedEntity()
      print(entity.created_at)  # Creation time
      print(entity.updated_at)  # Last update time

Data Structures
---------------

Tree Structure
~~~~~~~~~~~~~~

.. uml::

   @startuml
   class Tree<T> {
       - root: TreeNode<T>
       - size: int
       + add_child(value: T): TreeNode<T>
       + find(value: T): TreeNode<T>
       + traverse(order: TraversalOrder): Iterator[T]
       + prune(condition: Callable): Tree<T>
   }
   
   class TreeNode<T> {
       - value: T
       - parent: TreeNode<T>
       - children: List[TreeNode<T>]
       + add_child(value: T): TreeNode<T>
       + get_path(): List[T]
       + get_depth(): int
   }
   
   Tree *-- TreeNode : contains
   TreeNode o-- TreeNode : parent/children
   @enduml

**Usage Example**:

.. testcode::

   from haive.core.common.structures import Tree
   
   # Build knowledge hierarchy
   knowledge = Tree[str]("AI")
   ml = knowledge.add_child("Machine Learning")
   dl = ml.add_child("Deep Learning")
   dl.add_children(["Transformers", "CNNs", "RNNs"])
   
   # Find and traverse
   transformer_node = knowledge.find("Transformers")
   path = transformer_node.get_path()
   print(" > ".join(path))

.. testoutput::

   AI > Machine Learning > Deep Learning > Transformers

Performance Patterns
--------------------

Caching Strategy
~~~~~~~~~~~~~~~~

.. mermaid::

   sequenceDiagram
       participant Client
       participant Component
       participant Cache
       participant Computation
       
       Client->>Component: request(data)
       Component->>Cache: check(data_hash)
       alt Cache Hit
           Cache-->>Component: cached_result
           Component-->>Client: return cached_result
       else Cache Miss
           Component->>Computation: compute(data)
           Computation-->>Component: result
           Component->>Cache: store(data_hash, result)
           Component-->>Client: return result
       end

**Implementation**:

.. code-block:: python

   from haive.core.common.mixins import CacheableMixin
   from haive.core.common.decorators import memoize
   
   class SmartProcessor(CacheableMixin):
       @memoize(maxsize=1000, ttl=3600)
       def analyze(self, text: str) -> Dict[str, float]:
           """Expensive analysis cached for 1 hour."""
           # Complex NLP processing
           return {"sentiment": 0.8, "confidence": 0.95}

Type System Enhancements
------------------------

Type Inference Flow
~~~~~~~~~~~~~~~~~~~

.. graphviz::

   digraph type_inference {
      rankdir=LR;
      node [shape=box];
      
      Data [label="Raw Data\n{...}"];
      Analyzer [label="Type Analyzer", fillcolor=lightblue, style=filled];
      Schema [label="Type Schema\nTypedDict", fillcolor=lightgreen, style=filled];
      Validator [label="Runtime\nValidator", fillcolor=lightyellow, style=filled];
      
      Data -> Analyzer [label="analyze"];
      Analyzer -> Schema [label="generate"];
      Schema -> Validator [label="create"];
      Validator -> Data [label="validate", style=dashed];
   }

Advanced Usage Patterns
-----------------------

Event-Driven Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.core.common.mixins import ObservableMixin
   
   class WorkflowEngine(ObservableMixin):
       """Event-driven workflow with observable state changes."""
       
       def __init__(self):
           super().__init__()
           self.state = "idle"
           
           # Wire event handlers
           self.on("state_change", self._log_transition)
           self.on("error", self._handle_error)
           self.on("complete", self._cleanup)
       
       def process(self, data):
           self._transition("processing")
           try:
               result = self._execute(data)
               self._transition("complete")
               self.emit("complete", {"result": result})
               return result
           except Exception as e:
               self._transition("error")
               self.emit("error", {"exception": e, "data": data})
               raise
       
       def _transition(self, new_state):
           old_state = self.state
           self.state = new_state
           self.emit("state_change", {
               "from": old_state,
               "to": new_state
           })

Composition Pattern
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from haive.core.common.mixins import (
       IdentifierMixin,
       TimestampMixin,
       VersionMixin,
       ObservableMixin,
       SerializationMixin
   )
   
   class IntelligentAgent(
       IdentifierMixin,
       TimestampMixin,
       VersionMixin,
       ObservableMixin,
       SerializationMixin
   ):
       """Agent with multiple intelligent behaviors."""
       
       version = "1.0.0"
       
       def __init__(self, name: str):
           super().__init__()  # Initialize all mixins
           self.name = name
           self.knowledge = Tree[str]("root")
           
           # Emit creation event
           self.emit("agent_created", {
               "id": self.id,
               "name": name,
               "version": self.version
           })
       
       def learn(self, fact: str, category: str = "general"):
           """Add knowledge and track changes."""
           node = self.knowledge.add_child_to(fact, category)
           self.mark_updated()  # From TimestampMixin
           self.bump_version("patch")  # From VersionMixin
           self.emit("learned", {"fact": fact, "category": category})
           
       def to_dict(self) -> Dict[str, Any]:
           """Serialize to dictionary (from SerializationMixin)."""
           return {
               **super().to_dict(),  # Include mixin fields
               "name": self.name,
               "knowledge": self.knowledge.to_dict()
           }

Performance Benchmarks
----------------------

.. list-table:: Mixin Performance Characteristics
   :header-rows: 1
   :widths: 30 20 20 30

   * - Operation
     - Time Complexity
     - Space Complexity
     - Notes
   * - Mixin Initialization
     - O(1)
     - O(1)
     - < 0.1ms overhead
   * - ID Generation
     - O(1)
     - O(1)
     - UUID-based
   * - Event Emission
     - O(n)
     - O(1)
     - n = number of listeners
   * - Tree Operations
     - O(log n)
     - O(n)
     - Balanced tree assumed
   * - Cache Lookup
     - O(1)
     - O(k)
     - k = cache size

API Reference
-------------

Mixins
~~~~~~

.. automodule:: haive.core.common.mixins
   :members:
   :undoc-members:
   :show-inheritance:

Data Structures
~~~~~~~~~~~~~~~

.. automodule:: haive.core.common.structures
   :members:
   :undoc-members:
   :show-inheritance:

Type Utilities
~~~~~~~~~~~~~~

.. automodule:: haive.core.common.types
   :members:
   :undoc-members:
   :show-inheritance:

See Also
--------

* :doc:`engine_architecture` - How engines use common utilities
* :doc:`schema_system` - Schema system built on common types
* :doc:`graph_workflows` - Graphs using common structures
* :doc:`api_reference` - Complete API documentation

.. toctree::
   :hidden:
   :maxdepth: 2

   mixins_guide
   structures_guide
   types_guide
   performance_guide