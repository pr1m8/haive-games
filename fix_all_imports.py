#!/usr/bin/env python3
"""Fix all import issues in haive-games systematically."""

import ast
import importlib.util
import os
import sys
from pathlib import Path


def get_actual_exports(module_path):
    """Get what a module actually exports."""
    try:
        spec = importlib.util.spec_from_file_location("temp_module", module_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules["temp_module"] = module
            spec.loader.exec_module(module)

            # Get all public names
            if hasattr(module, "__all__"):
                return set(module.__all__)
            else:
                # Get all non-private names
                return {
                    name
                    for name in dir(module)
                    if not name.startswith("_")
                    and not callable(getattr(module, name, None))
                    or name in ["main", "run", "setup", "create", "build"]
                }
    except Exception as e:
        print(f"Error loading {module_path}: {e}")
        return set()


def fix_init_file(init_file_path):
    """Fix an __init__.py file by removing invalid imports."""
    print(f"\n🔧 Fixing {init_file_path}")

    try:
        with open(init_file_path, "r") as f:
            content = f.read()

        tree = ast.parse(content)

        valid_imports = []
        all_exports = set()

        for node in tree.body:
            if isinstance(node, ast.ImportFrom) and node.module:
                if node.module.startswith("haive.games."):
                    # Convert to file path
                    module_parts = node.module.split(".")
                    if len(module_parts) >= 3:
                        relative_path = "/".join(module_parts[2:]) + ".py"
                        module_file = (
                            Path(init_file_path).parent.parent.parent
                            / "src/haive/games"
                            / relative_path
                        )

                        if module_file.exists():
                            actual_exports = get_actual_exports(module_file)

                            # Filter imports to valid ones
                            valid_names = []
                            for alias in node.names:
                                if alias.name in actual_exports:
                                    valid_names.append(alias.name)
                                    all_exports.add(alias.name)
                                else:
                                    print(
                                        f"  ❌ Removing: {alias.name} from {node.module}"
                                    )

                            if valid_names:
                                import_line = f"from {node.module} import " + ", ".join(
                                    sorted(valid_names)
                                )
                                valid_imports.append(import_line)
                        else:
                            print(f"  ⚠️  Module not found: {module_file}")
                else:
                    # Keep non-haive imports
                    if hasattr(node, "lineno"):
                        import_line = ast.get_source_segment(content, node)
                        if import_line:
                            valid_imports.append(import_line)

        # Create new content
        new_content = '"""Module exports."""\n\n'
        if valid_imports:
            new_content += "\n".join(valid_imports) + "\n\n"

        new_content += "__all__ = [\n"
        for name in sorted(all_exports):
            new_content += f'    "{name}",\n'
        new_content += "]\n"

        # Write back
        with open(init_file_path, "w") as f:
            f.write(new_content)

        print(f"  ✅ Fixed {len(all_exports)} exports")
        return True

    except Exception as e:
        print(f"  ❌ Error fixing {init_file_path}: {e}")
        return False


def main():
    """Fix all problematic __init__.py files."""
    print("🚀 Starting comprehensive import fix...")

    games_src = Path("src/haive/games")

    # Get all __init__.py files
    init_files = list(games_src.rglob("__init__.py"))

    print(f"📁 Found {len(init_files)} __init__.py files")

    # Sort by depth (fix deeper ones first)
    init_files.sort(key=lambda p: len(p.parts), reverse=True)

    fixed_count = 0
    for init_file in init_files:
        if fix_init_file(init_file):
            fixed_count += 1

    print(f"\n✅ Fixed {fixed_count}/{len(init_files)} files")

    # Test import
    print("\n🧪 Testing chess import...")
    try:
        import subprocess

        result = subprocess.run(
            [
                "poetry",
                "run",
                "python",
                "-c",
                "from haive.games.chess import *; print('✅ Chess imports working')",
            ],
            capture_output=True,
            text=True,
            cwd=os.getcwd(),
        )

        if result.returncode == 0:
            print("✅ Chess import test passed!")
        else:
            print("❌ Chess import test failed:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Test failed: {e}")


if __name__ == "__main__":
    main()
