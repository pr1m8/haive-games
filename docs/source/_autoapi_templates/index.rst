📚 **API Documentation**
==========================

.. grid:: 1
   :gutter: 3
   :margin: 3

   .. grid-item-card:: :octicon:`package` Complete API Reference
      :class-card: sd-border-0 sd-shadow-lg sd-bg-primary sd-text-white
      :class-title: sd-text-center sd-font-weight-bold
      
      Comprehensive documentation for all modules, classes, and functions.
      Organized by logical structure with modern, searchable interface.

.. grid:: 1 2 2 3
   :gutter: 2
   :margin: 2

   .. grid-item-card:: :octicon:`package` **Modules**
      :class-card: sd-border-0 sd-shadow-sm
      :class-title: sd-text-center sd-font-weight-bold

      Browse packages and modules

   .. grid-item-card:: :octicon:`search` **Search**
      :class-card: sd-border-0 sd-shadow-sm
      :class-title: sd-text-center sd-font-weight-bold

      Find specific functions or classes

   .. grid-item-card:: :octicon:`code` **Examples**
      :class-card: sd-border-0 sd-shadow-sm
      :class-title: sd-text-center sd-font-weight-bold

      Usage patterns and code examples

📦 Module Navigation
====================

Click any module name below to jump directly to its documentation:

.. toctree::
   :maxdepth: 2
   :titlesonly:

   mcp/index

🎯 Getting Started
==================

.. tab-set::

   .. tab-item:: Basic Usage
      :class-label: sd-text-primary

      .. code-block:: python
         :caption: Import and Use

         # Import the package
         {% if pages %}
         import {{ pages[0].name.split('.')[0] }}
         {% endif %}

         # Use the APIs
         # Documentation for each module is linked above

   .. tab-item:: Type Hints
      :class-label: sd-text-secondary

      All APIs include comprehensive type hints for full IDE support.
      Enable type checking with ``mypy`` for complete type safety.

   .. tab-item:: Source Code
      :class-label: sd-text-info

      :octicon:`mark-github` All source code is available with direct links from each API page.

.. admonition:: 💡 Navigation Tips
   :class: tip

   - **Search**: Use the search box at the top to find specific functions or classes
   - **Browse**: Click modules in the list above for organized browsing
   - **Mobile**: All documentation is fully responsive and mobile-friendly

.. raw:: html

   <hr style="margin: 2rem 0; border: none; border-top: 2px solid var(--color-brand-primary);">
   <div style="text-align: center; color: var(--color-foreground-muted); font-size: 0.85rem;">
   <p>📖 Generated with <a href="https://github.com/readthedocs/sphinx-autoapi">sphinx-autoapi</a> and enhanced with modern design</p>
   </div>