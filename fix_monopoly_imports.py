#!/usr/bin/env python3
"""Fix remaining relative imports in monopoly package only."""

import os
import re

# Fix all import patterns in monopoly package
monopoly_dir = "src/haive/games/monopoly"

# Define replacement patterns specific to monopoly
patterns = [
    # Core/engine imports
    (r"from \.models\.llm\.base import", "from haive.core.models.llm.base import"),
    (
        r"from \.schema\.prebuilt\.messages_state import",
        "from haive.core.schema.prebuilt.messages_state import",
    ),
    (
        r"from \.core\.agent\.player_agent import",
        "from haive.core.agent.player_agent import",
    ),
    (
        r"from \.core\.agent\.generic_player_agent import",
        "from haive.core.agent.generic_player_agent import",
    ),
    # Monopoly-specific imports
    (
        r"from \.monopoly\.game_agent import",
        "from haive.games.monopoly.game_agent import",
    ),
    (
        r"from \.monopoly\.player_agent import",
        "from haive.games.monopoly.player_agent import",
    ),
    (r"from \.monopoly\.ui_fixed import", "from haive.games.monopoly.ui_fixed import"),
    (
        r"from \.monopoly\.integration import",
        "from haive.games.monopoly.integration import",
    ),
]

# Process all Python files
fixed_files = []
for root, dirs, files in os.walk(monopoly_dir):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r") as f:
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

print(f"\nMonopoly import fixing complete! Fixed {len(fixed_files)} files.")
