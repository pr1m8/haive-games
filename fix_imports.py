#!/usr/bin/env python3
"""Fix broken relative imports in monopoly package."""

import os
import re

# Fix all import patterns in monopoly package
monopoly_dir = "src/haive/games/monopoly"

# Define replacement patterns
patterns = [
    (
        r"from \.engine\.agent\.agent import",
        "from haive.core.engine.agent.agent import",
    ),
    (
        r"from \.engine\.agent\.config import",
        "from haive.core.engine.agent.config import",
    ),
    (r"from \.engine\.aug_llm import", "from haive.core.engine.aug_llm import"),
    (r"from \.monopoly\.models import", "from haive.games.monopoly.models import"),
    (r"from \.monopoly\.state import", "from haive.games.monopoly.state import"),
    (r"from \.monopoly\.utils import", "from haive.games.monopoly.utils import"),
    (r"from \.monopoly\.config import", "from haive.games.monopoly.config import"),
    (
        r"from \.monopoly\.generic_engines import",
        "from haive.games.monopoly.generic_engines import",
    ),
    (
        r"from \.monopoly\.main_agent import",
        "from haive.games.monopoly.main_agent import",
    ),
    (r"from \.config\.runnable import", "from haive.core.config.runnable import"),
]

# Process all Python files
fixed_files = []
for root, _dirs, files in os.walk(monopoly_dir):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath) as f:
                    content = f.read()

                original_content = content
                for old_pattern, new_pattern in patterns:
                    content = re.sub(old_pattern, new_pattern, content)

                if content != original_content:
                    with open(filepath, "w") as f:
                        f.write(content)
                    fixed_files.append(filepath)
                    print(f"Fixed imports in: {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Import fixing complete! Fixed {len(fixed_files)} files.")
