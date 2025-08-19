Installation Guide
==================

This guide covers different ways to install haive-core and manage dependencies.

Requirements
------------

- Python 3.10 or higher
- pip or Poetry package manager
- Git (for development installation)

Basic Installation
------------------

Using pip
~~~~~~~~~

The simplest way to install haive-core:

.. code-block:: bash

   pip install haive-core

Using Poetry (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~

For better dependency management:

.. code-block:: bash

   poetry add haive-core

Install with Extras
-------------------

haive-core includes optional dependencies for different features:

All Features
~~~~~~~~~~~~

.. code-block:: bash

   # With pip
   pip install "haive-core[all]"
   
   # With Poetry
   poetry add "haive-core[all]"

Specific Features
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Vector stores only
   pip install "haive-core[vectorstores]"
   
   # Embeddings support
   pip install "haive-core[embeddings]"
   
   # Popular LLM providers
   pip install "haive-core[popular-llms]"
   
   # Multiple features
   pip install "haive-core[vectorstores,embeddings]"

Development Installation
------------------------

To contribute to haive-core or use the latest development version:

Clone the Repository
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/haive-ai/haive.git
   cd haive/packages/haive-core

Install with Poetry
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install all dependencies including dev tools
   poetry install --all-extras
   
   # Activate the virtual environment
   poetry shell

Install with pip
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install in editable mode
   pip install -e ".[all]"

Dependency Groups
-----------------

haive-core organizes dependencies into logical groups:

LLM Providers
~~~~~~~~~~~~~

- **popular-llms**: OpenAI, Anthropic, Google
- **all-llms**: All supported LLM providers
- **azure**: Azure OpenAI integration
- **bedrock**: AWS Bedrock support

Vector Stores
~~~~~~~~~~~~~

- **popular-vectorstores**: Chroma, Pinecone, FAISS
- **all-vectorstores**: All supported vector stores
- **postgres**: PostgreSQL vector support
- **elasticsearch**: Elasticsearch integration

Embeddings
~~~~~~~~~~

- **popular-embeddings**: OpenAI, HuggingFace
- **all-embeddings**: All embedding providers

Tools & Integrations
~~~~~~~~~~~~~~~~~~~~

- **tools**: Common tool integrations
- **mcp**: Model Context Protocol support
- **persistence**: Database persistence

Verifying Installation
----------------------

After installation, verify everything is working:

.. code-block:: python

   # Test basic import
   from haive.core import __version__
   print(f"haive-core version: {__version__}")
   
   # Test core components
   from haive.core.engine.aug_llm import AugLLMConfig
   from haive.core.schema.state_schema import StateSchema
   
   # Create a simple config
   config = AugLLMConfig()
   print("✓ Core components imported successfully")

Environment Variables
---------------------

haive-core uses environment variables for configuration:

.. code-block:: bash

   # LLM API Keys
   export OPENAI_API_KEY="your-api-key"
   export ANTHROPIC_API_KEY="your-api-key"
   export GOOGLE_API_KEY="your-api-key"
   
   # Vector Store Configuration
   export PINECONE_API_KEY="your-api-key"
   export PINECONE_ENVIRONMENT="your-environment"
   
   # Optional: Default model
   export HAIVE_DEFAULT_MODEL="gpt-4"

Using .env Files
~~~~~~~~~~~~~~~~

Create a `.env` file in your project root:

.. code-block:: text

   # .env
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   HAIVE_DEFAULT_MODEL=gpt-4

Load it in your code:

.. code-block:: python

   from dotenv import load_dotenv
   load_dotenv()

Troubleshooting
---------------

Common Installation Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

**ImportError: No module named 'haive'**

- Ensure you've activated your virtual environment
- Check installation: `pip show haive-core`

**Dependency Conflicts**

- Use Poetry for better dependency resolution
- Create a fresh virtual environment

**Missing Optional Dependencies**

- Install the appropriate extras group
- Example: `pip install "haive-core[vectorstores]"`

Platform-Specific Notes
~~~~~~~~~~~~~~~~~~~~~~~

**Windows**

- Use `python -m pip` instead of `pip` if needed
- Activate venv with `venv\Scripts\activate`

**macOS**

- May need to install Xcode Command Line Tools
- Use `python3` if `python` points to Python 2

**Linux**

- May need to install python3-dev package
- Use system package manager for system dependencies

Next Steps
----------

- Continue with the :doc:`getting_started` guide
- Explore the :doc:`API Reference <autoapi/haive/index>`
- Check out example projects in the repository