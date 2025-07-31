"""Debug test for LLM factory issues."""

import contextlib
from pathlib import Path
import sys

# Add packages to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_basic_imports():
    """Test basic imports work."""
    try:
        from haive.core.models.llm.model_registry import model_registry

        # Try calling parse_model_string
        with contextlib.suppress(Exception):
            model_registry.parse_model_string("gpt-4")

        # Try to understand the model_registry object

    except Exception:
        return False

    try:
        from haive.core.models.llm.factory import create_llm_config

        # Try creating a config
        try:
            create_llm_config("gpt-4")
        except Exception:
            import traceback

            traceback.print_exc()

    except Exception:
        return False

    return True


if __name__ == "__main__":
    test_basic_imports()
