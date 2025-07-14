"""Debug test for LLM factory issues."""

import sys
from pathlib import Path

# Add packages to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_basic_imports():
    """Test basic imports work."""
    print("Testing basic imports...")

    try:
        from haive.core.models.llm.model_registry import ModelRegistry, model_registry

        print(f"✓ Imported ModelRegistry: {ModelRegistry}")
        print(f"✓ Imported model_registry: {model_registry}")
        print(f"  Type: {type(model_registry)}")
        print(
            f"  Has parse_model_string: {hasattr(model_registry, 'parse_model_string')}"
        )

        # Try calling parse_model_string
        try:
            result = model_registry.parse_model_string("gpt-4")
            print(f"✓ parse_model_string('gpt-4') returned: {result}")
        except Exception as e:
            print(f"✗ Error calling parse_model_string: {e}")
            print(f"  Error type: {type(e)}")

        # Try to understand the model_registry object
        print("\nInspecting model_registry:")
        print(
            f"  Dir: {[x for x in dir(model_registry) if not x.startswith('_')][:10]}"
        )

    except Exception as e:
        print(f"✗ Import error: {e}")
        return False

    print("\nTesting factory import...")
    try:
        from haive.core.models.llm.factory import create_llm_config

        print(f"✓ Imported create_llm_config: {create_llm_config}")

        # Try creating a config
        try:
            config = create_llm_config("gpt-4")
            print(f"✓ Created config: {config}")
        except Exception as e:
            print(f"✗ Error creating config: {e}")
            print(f"  Error type: {type(e)}")
            import traceback

            traceback.print_exc()

    except Exception as e:
        print(f"✗ Factory import error: {e}")
        return False

    return True


if __name__ == "__main__":
    test_basic_imports()
