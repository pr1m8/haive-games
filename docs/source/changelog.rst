Changelog
=========

All notable changes to haive-core will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

.. note::
   
   This changelog is automatically updated from git commits using sphinx-git.
   For the most recent changes, see the git log below.

[Unreleased]
------------

Added
~~~~~
- Enhanced documentation with 12 new Sphinx extensions
- Getting Started guide for new users
- Automatic changelog generation from git commits
- Multiple favicon support
- Enhanced tooltips with sphinx-tippy
- Git timestamps showing last updated dates
- Custom 404 error pages
- Execute code examples in documentation

Changed
~~~~~~~
- Improved API documentation hierarchy with module-level organization
- Enhanced navigation with expandable toctree
- Better Pydantic model documentation

Fixed
~~~~~
- AutoAPI flat structure issue - now shows hierarchical organization
- Dark mode code visibility issues

[0.1.0] - 2025-01-15
--------------------

Initial release of haive-core.

Added
~~~~~
- Core agent engine and infrastructure
- State management and schema composition  
- Graph-based workflow orchestration
- Tool and retriever integration
- Vector stores and embeddings support
- Persistence and checkpointing
- Comprehensive type system
- Plugin architecture
- MCP (Model Context Protocol) support

Documentation Changes
---------------------

Recent documentation updates from git:

.. git_changelog::
   :revisions: 20