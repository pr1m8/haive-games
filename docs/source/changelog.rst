Changelog
=========

This page tracks changes to haive-games using both manual entries and Git history.

Release Notes
-------------

.. changelog::
   :towncrier: ../../
   :towncrier-skip-if-empty:

Recent Documentation Updates
----------------------------

.. git_changelog::
   :revisions: 10
   :rev-list-extra: --first-parent

**How to Use This Page:**

- **Release Notes**: Structured changelog entries for each version
- **Recent Changes**: Git-based documentation updates  
- **Manual Entries**: Important changes added via towncrier fragments
- **Commit History**: Automatic tracking of all documentation changes

**Adding Changelog Entries:**

To add a changelog entry for this package:

.. code-block:: bash

   # From the package directory
   poetry run towncrier create <issue>.<type>.md --content "Description of change"
   
   # Types: feature, bugfix, improvement, deprecation, breaking, security, performance, docs, dev, misc

This ensures both structured release notes and detailed commit history are available for tracking changes.
