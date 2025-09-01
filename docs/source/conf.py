# Configuration file for haive-games documentation
import os
import sys
from pathlib import Path

# Add package to path
sys.path.insert(0, os.path.abspath('../../src'))

# Project information
project = 'haive-games'
copyright = '2025, Haive Team'
author = 'Haive Team'
release = '0.1.0'

# Extensions
extensions = [
    'autoapi.extension',       # Must be first for API documentation
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx.ext.githubpages',
    'sphinxcontrib.mermaid',   # Keep mermaid support for game diagrams
    'myst_parser',             # Keep MyST for markdown support
]

# AutoAPI Configuration - Consistent across all packages
autoapi_dirs = ['../../src']
autoapi_type = 'python'
autoapi_root = 'autoapi'  # Use consistent directory name
autoapi_add_toctree_entry = True
autoapi_keep_files = False  # Don't keep files to avoid stale references
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members',
]

# Fix for hierarchical API structure
autoapi_member_order = 'groupwise'
autoapi_own_page_level = 'class'  # Create pages at class level for better navigation
autoapi_python_class_content = 'both'  # Show both class and __init__ docstrings
autoapi_include_inheritance_diagrams = True  # Show inheritance diagrams

# Theme Configuration
html_theme = 'furo'
html_static_path = ['_static']

# CSS files
html_css_files = [
    "purple-theme.css",
]

# Theme options - Consistent navigation and colors
html_theme_options = {
    # Navigation settings
    "navigation_depth": 6,  # Show 6 levels of navigation for better API visibility
    "collapse_navigation": False,  # Keep navigation expanded
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
    "show_nav_level": 1,  # Show navigation from first level
    "navigation_with_keys": True,  # Keep from original
    "announcement": "🎮 <b>haive-games</b> - Multi-agent game framework for the Haive ecosystem",
    
    # Light mode colors
    "light_css_variables": {
        "color-brand-primary": "#1e40af",
        "color-brand-content": "#1e3a8a",
    },
    
    # Dark mode colors (black/blue theme)
    "dark_css_variables": {
        "color-background-primary": "#000612",
        "color-background-secondary": "#0a1428",
        "color-background-hover": "#1e293b",
        "color-brand-primary": "#60a5fa",
        "color-brand-content": "#93bbfc",
        "color-sidebar-background": "#0a1428",
        "color-sidebar-background-border": "#1e3a8a",
    },
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'haive-core': ('https://docs.haive.ai/packages/haive-core/', None),
    'haive-agents': ('https://docs.haive.ai/packages/haive-agents/', None),
}

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Add package-specific sidebar
html_sidebars = {
    '**': [
        'sidebar/brand.html',
        'sidebar/search.html',
        'sidebar/scroll-start.html',
        'sidebar/navigation.html',
        'sidebar/ethical-ads.html',
        'sidebar/scroll-end.html',
        'sidebar/variant-selector.html',
    ]
}

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {%.+%} {%.+%}"
copybutton_prompt_is_regexp = True

# MyST Parser settings (keeping from original)
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
]
myst_heading_anchors = 3

# Mermaid settings (keeping from original for game diagrams)
mermaid_output_format = "svg"
mermaid_theme = "default"

# HTML title configuration
html_title = "haive-games"
html_short_title = "haive-games"

# Template paths
templates_path = ["_templates"]

# Exclude patterns
exclude_patterns = []