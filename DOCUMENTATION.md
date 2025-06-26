# Haive Games Documentation Guide

This guide explains how to maintain and enhance documentation for the haive-games package, including Google-style docstrings, module-level README files, and Sphinx integration.

## Documentation Tools

### Automatic Docstring Generator

The `add_docstrings.py` script in the `scripts` directory automatically adds Google-style docstrings to Python modules, classes, and functions. It intelligently generates documentation based on naming conventions and context.

#### Usage:

```bash
# Add docstrings to all files
cd /home/will/Projects/haive/backend/haive/packages/haive-games
python scripts/add_docstrings.py

# Add docstrings to a specific module
python scripts/add_docstrings.py --path src/haive/games/chess

# Test what would be changed without modifying files
python scripts/add_docstrings.py --dry-run
```

### Documentation Templates

Templates for consistent documentation are available in the `scripts/templates` directory:

- `README_TEMPLATE.md` - Template for module-level README files
- `MODULE_DOCSTRING_TEMPLATE.txt` - Template for module-level docstrings

## Documentation Standards

All documentation in the haive-games package follows Google-style docstring formatting:

### Module-level Docstrings

```python
"""Module name and brief description.

This module provides [functionality description].

Example:
    >>> from haive.games.module_name import ClassName
    >>> instance = ClassName()
    >>> result = instance.method()

Typical usage:
    - Step 1 description
    - Step 2 description
"""
```

### Class Docstrings

```python
class ClassName:
    """Brief description of the class.

    Detailed description of the class's purpose and functionality.

    Attributes:
        attr1 (type): Description of attribute 1.
        attr2 (type): Description of attribute 2.

    Example:
        >>> instance = ClassName()
        >>> instance.method()
    """
```

### Method/Function Docstrings

```python
def function_name(param1, param2=default):
    """Brief description of the function.

    Args:
        param1 (type): Description of parameter 1.
        param2 (type, optional): Description of parameter 2. Defaults to default.

    Returns:
        type: Description of the return value.

    Raises:
        Exception: Description of when this exception is raised.

    Example:
        >>> result = function_name("value", param2=42)
    """
```

### Pydantic Models

```python
class ModelName(BaseModel):
    """Brief description of the model.

    Attributes:
        field1 (type): Description of field 1.
        field2 (type): Description of field 2.
    """
    field1: type = Field(..., description="Description of field 1")
    field2: type = Field(default, description="Description of field 2")
```

## Module README Files

Each game module should have a README.md file in its directory explaining:

1. Overview of the game implementation
2. Key features
3. Components (models, agents, state managers)
4. Usage examples
5. Game rules and strategy (where applicable)
6. Customization options
7. Integration with the Haive framework

The `add_docstrings.py` script can automatically generate these README files based on module content.

## Building Documentation

Documentation is built using Sphinx via the noxfile.py in the project root:

```bash
# From the project root
nox -s docs

# For live documentation editing with auto-reload
nox -s docs-live

# For checking documentation without building
nox -s docs-check
```

## Documentation Architecture

The Haive documentation is organized as follows:

- **Project Root README**: High-level overview of the entire project
- **Package READMEs**: Overview of each package (like haive-games)
- **Module READMEs**: Detailed documentation for each game module
- **API Documentation**: Generated from docstrings using Sphinx
- **Guides and Tutorials**: Located in the docs/source directory

## Best Practices

1. **Be Consistent**: Follow the established documentation patterns
2. **Include Examples**: Every component should include usage examples
3. **Document Edge Cases**: Note any limitations or special considerations
4. **Keep Updated**: Update documentation when code changes
5. **Use Templates**: Start from templates rather than creating from scratch
6. **Run Documentation Checks**: Use `nox -s docs-check` to verify documentation

## Contributing to Documentation

When adding new games or features:

1. Ensure all modules, classes and functions have docstrings
2. Create a README.md file for each game module
3. Add usage examples for key components
4. Update the appropriate sections in the Sphinx documentation

For major changes, also update the main README.md file and relevant guide documents.
