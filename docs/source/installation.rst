Installation Guide
==================

This guide covers different ways to install haive-games and manage dependencies.

Requirements
------------

- Python 3.10 or higher
- pip or Poetry package manager
- Git (for development installation)

Basic Installation
------------------

Using pip
~~~~~~~~~

The simplest way to install haive-games:

.. code-block:: bash

   pip install haive-games

Using Poetry (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~

For better dependency management:

.. code-block:: bash

   poetry add haive-games

Install with Extras
-------------------

haive-games includes optional dependencies for different features:

All Features
~~~~~~~~~~~~

.. code-block:: bash

   # With pip
   pip install "haive-games[all]"
   
   # With Poetry
   poetry add "haive-games[all]"

Specific Features
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Analytics and metrics
   pip install "haive-games[analytics]"
   
   # Tournament system
   pip install "haive-games[tournament]"
   
   # AI provider support
   pip install "haive-games[ai-providers]"
   
   # Multiple features
   pip install "haive-games[analytics,tournament]"

Development Installation
------------------------

To contribute to haive-games or use the latest development version:

Clone the Repository
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/haive-ai/haive.git
   cd haive/packages/haive-games

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

haive-games organizes dependencies into logical groups:

Game Categories
~~~~~~~~~~~~~~~

- **board-games**: Chess, Go, Checkers, Reversi
- **card-games**: Poker, Blackjack, UNO
- **social-games**: Among Us, Mafia, Clue
- **puzzle-games**: Sudoku, Wordle, Mastermind

AI & Analytics
~~~~~~~~~~~~~~

- **ai-providers**: OpenAI, Anthropic, Google AI support
- **analytics**: Performance metrics and analysis
- **tournament**: Tournament system and rankings
- **research**: Research data collection tools

Integrations
~~~~~~~~~~~~

- **visualization**: Game state visualization
- **persistence**: Game state persistence
- **multiplayer**: Multi-player game support

Verifying Installation
----------------------

After installation, verify everything is working:

.. code-block:: python

   # Test basic import
   from haive.core import __version__
   print(f"haive-games version: {__version__}")
   
   # Test game components
   from haive.games.chess import ChessAgent
   from haive.games.poker import PokerAgent
   from haive.core.engine.aug_llm import AugLLMConfig
   
   # Create a simple agent
   config = AugLLMConfig()
   chess_ai = ChessAgent(name="TestBot", engine=config)
   print("✓ Game components imported successfully")

Environment Variables
---------------------

haive-games uses environment variables for configuration:

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
- Check installation: `pip show haive-games`

**Dependency Conflicts**

- Use Poetry for better dependency resolution
- Create a fresh virtual environment

**Missing Optional Dependencies**

- Install the appropriate extras group
- Example: `pip install "haive-games[tournament]"`

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