:mod:`haive.core.models.vectorstore`
=====================================

.. currentmodule:: haive.core.models.vectorstore

.. admonition:: Quick Links
   :class: tip

   * :class:`VectorStoreConfig` - Main configuration class
   * :class:`VectorStoreProvider` - Supported providers enum
   * :ref:`Examples <vectorstore-examples>` - Usage examples
   * :doc:`Related: Embeddings <../embeddings/index>` - Embedding configurations

.. contents:: Module Contents
   :local:
   :depth: 2

Overview
--------

This module provides comprehensive abstractions and implementations for working with 
vector stores in the Haive framework. Vector stores are specialized databases optimized 
for storing and retrieving high-dimensional vectors, typically used for similarity 
search in RAG (Retrieval-Augmented Generation) applications.

.. note::
   
   Vector stores enable efficient semantic search by storing document embeddings and 
   providing fast similarity-based retrieval. They are essential components for building 
   RAG systems, recommendation engines, and other applications that require similarity 
   search over large document collections.

Supported Providers
-------------------

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: Open Source
      
      * **Chroma** - Local and server modes
      * **FAISS** - Facebook AI Similarity Search
      * **Weaviate** - Vector search engine
      * **Qdrant** - Similarity search engine
      * **Milvus** - Distributed vector database

   .. grid-item-card:: Cloud Services
      
      * **Pinecone** - Managed vector database
      * **Supabase** - PostgreSQL + pgvector
      * **MongoDB Atlas** - Vector search
      * **OpenSearch** - Elasticsearch-based
      * **Redis** - Vector search capabilities

   .. grid-item-card:: Specialized
      
      * **LanceDB** - Serverless vector DB
      * **Marqo** - Tensor search engine
      * **Zilliz** - Cloud-native Milvus

Quick Start
-----------

.. tab-set::

   .. tab-item:: Local Development

      .. code-block:: python

         from haive.core.models.vectorstore import VectorStoreConfig, VectorStoreProvider

         # Configure a local vector store
         config = VectorStoreConfig(
             provider=VectorStoreProvider.Chroma,
             collection_name="documents",
             persist_directory="./chroma_db"
         )

         # Create and use the vector store
         vectorstore = config.instantiate()
         vectorstore.add_texts(["Document content"], metadatas=[{"source": "doc1"}])
         results = vectorstore.similarity_search("query text", k=5)

   .. tab-item:: Cloud Production

      .. code-block:: python

         # Configure for production with Pinecone
         config = VectorStoreConfig(
             provider=VectorStoreProvider.Pinecone,
             api_key_env_var="PINECONE_API_KEY",
             environment="us-west1-gcp",
             index_name="production-index"
         )

         # Create with custom embeddings
         from haive.core.models.embeddings import OpenAIEmbeddingConfig
         
         embedding_config = OpenAIEmbeddingConfig(model="text-embedding-3-small")
         config.embedding_model = embedding_config

   .. tab-item:: From Documents

      .. code-block:: python

         from haive.core.models.vectorstore import VectorStoreConfig
         from langchain_core.documents import Document

         # Create documents
         docs = [
             Document(page_content="Content 1", metadata={"source": "file1.txt"}),
             Document(page_content="Content 2", metadata={"source": "file2.txt"})
         ]

         # Create vector store from documents
         vs_config = VectorStoreConfig.create_vs_config_from_documents(
             documents=docs,
             vector_store_provider=VectorStoreProvider.Chroma
         )

API Reference
-------------

Configuration Classes
~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: custom-class-template.rst

   VectorStoreConfig
   VectorStoreProvider

.. autoclass:: VectorStoreConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:
   :special-members: __init__

   .. autopydantic_model:: VectorStoreConfig
      :model-show-json: True
      :model-show-field-summary: True
      :model-show-validator-members: True

   .. rubric:: Configuration Examples

   **Local Vector Store**:

   .. code-block:: python

      config = VectorStoreConfig(
          provider=VectorStoreProvider.Chroma,
          persist_directory="./local_db",
          collection_name="my_documents"
      )

   **Cloud Vector Store with Authentication**:

   .. code-block:: python

      config = VectorStoreConfig(
          provider=VectorStoreProvider.Pinecone,
          api_key_env_var="PINECONE_API_KEY",
          environment="us-west1-gcp",
          index_name="production",
          vector_store_kwargs={
              "metric": "cosine",
              "dimension": 1536
          }
      )

.. autoclass:: VectorStoreProvider
   :members:
   :undoc-members:
   :show-inheritance:

   .. rubric:: Available Providers

   .. list-table::
      :header-rows: 1
      :widths: 20 20 60

      * - Provider
        - Type
        - Best For
      * - :attr:`~VectorStoreProvider.Chroma`
        - Open Source
        - Local development, prototyping
      * - :attr:`~VectorStoreProvider.Pinecone`
        - Cloud Service
        - Production, managed infrastructure
      * - :attr:`~VectorStoreProvider.FAISS`
        - Local/Memory
        - High-performance similarity search
      * - :attr:`~VectorStoreProvider.Weaviate`
        - Open Source
        - GraphQL queries, hybrid search

Functions
~~~~~~~~~

.. autofunction:: add_document

Architecture
------------

.. mermaid::

   graph LR
       A[Documents] --> B[Embeddings]
       B --> C[Vector Store]
       C --> D[Similarity Search]
       D --> E[Retrieved Documents]
       
       subgraph "Vector Store Types"
           F[Local/File-based]
           G[Cloud Services]
           H[In-Memory]
       end

Performance Considerations
--------------------------

.. admonition:: Optimization Tips
   :class: important

   * **Index Type**: Different providers support different index types (HNSW, IVF, etc.)
   * **Batch Operations**: Use batch operations for better performance when adding many documents
   * **Connection Pooling**: Configured automatically for cloud providers
   * **Caching**: In-memory caching for frequently accessed embeddings

.. warning::

   Large-scale deployments should consider:
   
   * Index size limitations
   * Query latency requirements
   * Cost per query/storage
   * Data persistence needs

.. _vectorstore-examples:

Extended Examples
-----------------

RAG Pipeline Example
~~~~~~~~~~~~~~~~~~~~

.. exec_code::
  :hide_code:

  # Example of a complete RAG pipeline
  from haive.core.models.vectorstore import VectorStoreConfig, VectorStoreProvider
  from haive.core.engine.retriever import create_retriever
  from langchain_core.documents import Document
  
  # Create sample documents for the example
  sample_docs = [
      Document(page_content="This is a sample document about AI.", metadata={"source": "example"}),
      Document(page_content="Vector stores enable semantic search.", metadata={"source": "example"})
  ]
  
  # Setup vector store with sample documents
  config = VectorStoreConfig(
      provider=VectorStoreProvider.InMemory,  # Use InMemory to avoid external dependencies
      collection_name="knowledge_base",
      documents=sample_docs
  )
  
  # Create retriever
  retriever = config.create_retriever()
  
  print("RAG pipeline configured successfully!")

Migration Between Providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Migrate from one provider to another
   def migrate_vectorstore(source_config, target_config):
       """Migrate documents between vector stores."""
       # Extract from source
       source_vs = source_config.instantiate()
       docs = source_vs.similarity_search("", k=1000)  # Get all
       
       # Load into target
       target_vs = target_config.instantiate()
       target_vs.add_documents(docs)
       
       return target_vs

See Also
--------

* :doc:`/autoapi/haive/core/engine/retriever/index` - Retriever configurations
* :doc:`/autoapi/haive/core/models/embeddings/index` - Embedding models
* :doc:`/autoapi/haive/core/engine/document/index` - Document processing
* `LangChain Vector Stores <https://python.langchain.com/docs/modules/data_connection/vectorstores/>`_ - External documentation

.. toctree::
   :hidden:
   :maxdepth: 1

   base