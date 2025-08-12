#!/usr/bin/env python3
"""Fix all relative imports to use absolute haive.games imports."""

import os
import re
from pathlib import Path


def fix_imports_in_file(file_path):
    """Fix imports in a single file."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Fix patterns
        patterns = [
            # Fix relative imports that should be absolute
            (r"^from games\.", "from haive.games."),
            (r"^from agent\.", "from haive.games.core.agent."),
            (r"^from base\.", "from haive.games.base."),
            (r"^from monopoly\.", "from haive.games.monopoly."),
            (r"^from framework\.", "from haive.games.framework."),
            (r"^from core\.", "from haive.games.core."),
            # Fix engine imports (should be haive.core.engine)
            (r"from haive\.games\.engine\.", "from haive.core.engine."),
            (r"from \.engine\.", "from haive.core.engine."),
            # Fix graph imports (should be haive.core.graph)
            (r"from haive\.games\.graph\.", "from haive.core.graph."),
            (r"from \.graph\.", "from haive.core.graph."),
            # Fix relative imports starting with dot
            (r"^from \.([a-zA-Z_]+) ", r"from haive.games.\1 "),
            (r"^from \.\.([a-zA-Z_]+) ", r"from haive.games.\1 "),
            # Fix haive.core.agent imports (should be haive.games.core.agent)
            (
                r"from haive\.core\.agent\.player_agent ",
                "from haive.games.core.agent.player_agent ",
            ),
            (
                r"from haive\.core\.agent\.generic_player_agent ",
                "from haive.games.core.agent.generic_player_agent ",
            ),
        ]

        # Apply fixes line by line
        lines = content.split("\n")
        new_lines = []

        for line in lines:
            new_line = line
            for pattern, replacement in patterns:
                if re.match(pattern, line.strip()):
                    # Preserve indentation
                    indent = len(line) - len(line.lstrip())
                    new_line = " " * indent + re.sub(pattern, replacement, line.strip())
                    break
            new_lines.append(new_line)

        content = "\n".join(new_lines)

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Fix all imports in haive-games."""
    games_dir = Path("src/haive/games")

    fixed_count = 0

    for root, dirs, files in os.walk(games_dir):
        # Skip __pycache__
        dirs[:] = [d for d in dirs if d != "__pycache__"]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                if fix_imports_in_file(file_path):
                    fixed_count += 1
                    print(f"Fixed: {file_path}")

    print(f"\nFixed {fixed_count} files")

    # Test chess import
    print("\nTesting chess import...")
    try:
        import subprocess

        result = subprocess.run(
            [
                "python",
                "-c",
                "from haive.games.chess.agent import ChessAgent; print('SUCCESS: Chess import working!')",
            ],
            capture_output=True,
            text=True,
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    main()
