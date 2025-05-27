"""
# TODO
- Mark which ones work or dont wokr
- Add examples to the README
- Add more games
- Add more examples to the examples folder
- Add more tests
"""

"""Haive Games package."""

import logging

# Configure logging - disable verbose output from base modules
logging.getLogger("haive.core.models.llm.base").setLevel(logging.ERROR)
logging.getLogger("haive.core.engine.aug_llm").setLevel(logging.ERROR)
logging.getLogger("openai").setLevel(logging.ERROR)
logging.getLogger("langchain").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Optional: Set up your own logger with appropriate level
games_logger = logging.getLogger("haive.games")
games_logger.setLevel(logging.INFO)  # Show important info from games module

# You can add your imports and other initialization here
