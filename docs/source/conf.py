"""Sphinx configuration for haive-mcp documentation."""

import os
import sys

from sphinx.application import Sphinx

# Path setup
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
project = "haive-games"
copyright = "2025, Haive Team"
author = "Haive Team"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "autoapi.extension",  # Must be first
    "sphinx.ext.autodoc", 
    "sphinx.ext.autosummary",  # Add autosummary for detailed docs
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_codeautolink",  # Automatic GitHub source links
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx.ext.graphviz",
    "myst_parser",  # Parse README.md files
]

# AutoAPI Configuration
autoapi_dirs = ["../../src/haive"]
autoapi_type = "python"
autoapi_add_toctree_entry = True
autoapi_keep_files = True  # Keep generated files like haive-mcp
autoapi_root = "autoapi"
autoapi_include_inheritance_diagram = False
# autoapi_template_dir = "_templates/autoapi"  # Use custom templates
autoapi_options = [
    "members",
    "show-inheritance",
    "show-module-summary",
]

# CRITICAL: Use module-level pages for hierarchical organization
autoapi_own_page_level = "module"  # Module-level pages like haive-mcp
autoapi_member_order = "groupwise"
autoapi_generate_api_docs = True

# Skip problematic patterns  
autoapi_ignore = ["**/test_*.py", "**/tests/*", "**/*_test.py"]

# Enable both AutoAPI and autosummary to work together
autoapi_python_class_content = "both"  # Include both class and __init__ docstrings
autoapi_python_use_implicit_namespaces = True

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# Furo theme configuration - Enhanced purple theme
html_theme_options = {
    "navigation_with_keys": True,
    "show_nav_level": 3,
    "collapse_navigation": False,
    "sidebar_hide_name": False, 
    "navigation_depth": 4,
    "show_toc_level": 3,
    "light_css_variables": {
        "color-brand-primary": "#8b5cf6",
        "color-brand-content": "#7c3aed",
        "color-sidebar-background": "#faf5ff",
        "color-sidebar-background-border": "#e9d5ff", 
    },
    "dark_css_variables": {
        "color-brand-primary": "#a78bfa",
        "color-brand-content": "#c084fc",
        "color-background-primary": "#0f0019",  # Very dark purple
        "color-background-secondary": "#1a0033",  # Dark purple
        "color-background-hover": "#2d0059",  # Purple hover
        "color-background-border": "#4c1d95",  # Purple border
        "color-sidebar-background": "#14001f",  # Darker purple sidebar
        "color-sidebar-background-border": "#4c1d95",
        "color-sidebar-link-text": "#e9d5ff",
        "color-sidebar-link-text--top-level": "#f3e8ff",
        "color-sidebar-item-background--hover": "#2d0059",
        "color-sidebar-item-expander-background--hover": "#4c1d95",
        "color-content-foreground": "#ffffff",
        "color-code-background": "#1e0936",  # Dark purple code bg
    },
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# Autodoc settings to work with AutoAPI
autodoc_typehints = "description"
autodoc_member_order = "groupwise"
autodoc_default_options = {
    "members": True,
    "member-order": "groupwise", 
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__"
}

# Intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# -- Purple Theme Configuration ----------------------------------------------
# Syntax highlighting - use purple-friendly themes
pygments_style = "default"  # Better for light mode with our custom CSS
pygments_dark_style = "monokai"  # Good for dark mode

# AutoAPI configuration for prominent API Reference
# Already configured above - removed duplicates
autoapi_toctree_caption = "🔍 API Reference"
autoapi_toctree_first = True  # Put at top!

# Graphviz configuration for beautiful diagrams
graphviz_output_format = "svg"
graphviz_dot_args = [
    "-Kdot",
    "-Tsvg",
    "-Gfontname=Inter",
    "-Nfontname=Inter",
    "-Efontname=Inter",
    "-Gbgcolor=transparent",
    "-Gpad=0.5",
    "-Grankdir=TB",
    "-Gnodesep=0.7",
    "-Granksep=0.8",
    "-Gsplines=true",
]

# CSS files in correct order - purple theme loads last to override
# Simplified - using Furo's built-in theme (no CSS overrides needed)
# The dark_css_variables above already provide the purple theme

# Autosummary settings for detailed API docs
autosummary_generate = True
autosummary_generate_overwrite = True
autosummary_imported_members = True

# Code autolink configuration for GitHub links
codeautolink_concat_default = True
codeautolink_global_preface = "https://github.com/pr1m8/haive-games"

# MyST parser configuration for README.md files
source_suffix = {
    ".rst": None,
    ".md": "myst_parser",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Include README.md files in documentation
myst_heading_anchors = 3
myst_title_to_header = True
