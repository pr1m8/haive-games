#!/usr/bin/env python3
"""
Export poetry dependencies from pyproject.toml to requirements.txt for Sphinx documentation.

This script reads the pyproject.toml file and exports all dependencies (including dev/docs groups)
to a requirements.txt file that can be used by sphinx extensions like seed_intersphinx_mapping.
"""

import subprocess
import sys
from pathlib import Path


def export_requirements():
    """Export poetry dependencies to requirements.txt."""
    # Get the directory where this script is located
    docs_dir = Path(__file__).parent
    project_root = docs_dir.parent  # haive-core root

    # Output file in docs directory
    requirements_file = docs_dir / "requirements.txt"

    print(f"📦 Exporting dependencies from {project_root}/pyproject.toml")
    print(f"📝 Writing to {requirements_file}")

    try:
        # Export all dependencies including dev and docs groups
        # Using --without-hashes for cleaner output
        # Using --with-credentials false to avoid any auth issues
        cmd = [
            "poetry",
            "export",
            "-f",
            "requirements.txt",
            "--output",
            str(requirements_file),
            "--without-hashes",
            "--with",
            "dev",
            "--with",
            "docs",
            "--without-urls",
        ]

        # Run from the project root where pyproject.toml is located
        result = subprocess.run(
            cmd, cwd=str(project_root), capture_output=True, text=True
        )

        if result.returncode != 0:
            print(f"❌ Error exporting requirements: {result.stderr}")
            return False

        print(f"✅ Successfully exported dependencies to {requirements_file}")

        # Read and display summary
        with open(requirements_file, "r") as f:
            lines = f.readlines()
            print(f"📊 Exported {len(lines)} dependencies")

        # Also create a minimal requirements.txt in the parent directory if needed
        parent_requirements = project_root / "requirements.txt"
        if not parent_requirements.exists():
            print(f"📝 Creating minimal requirements.txt in {parent_requirements}")
            with open(parent_requirements, "w") as f:
                f.write("# Minimal requirements for haive-core\n")
                f.write("# Full dependencies are managed by Poetry\n")
                f.write("# This file is auto-generated for documentation builds\n\n")
                # Write just the main dependencies (no dev/docs)
                cmd_minimal = [
                    "poetry",
                    "export",
                    "-f",
                    "requirements.txt",
                    "--output",
                    str(parent_requirements),
                    "--without-hashes",
                    "--without-urls",
                    "--only",
                    "main",
                ]
                subprocess.run(cmd_minimal, cwd=str(project_root))
                print(f"✅ Created minimal requirements.txt")

        return True

    except FileNotFoundError:
        print("❌ Poetry not found. Please ensure Poetry is installed.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def update_sphinx_config():
    """Update Sphinx configuration to use the exported requirements."""
    docs_dir = Path(__file__).parent
    conf_py = docs_dir / "source" / "conf.py"

    print(f"\n🔧 Checking Sphinx configuration at {conf_py}")

    if conf_py.exists():
        print(
            "✅ Found conf.py - seed_intersphinx_mapping will now find requirements.txt"
        )
        print("💡 Make sure to re-enable seed_intersphinx_mapping extension in conf.py")
    else:
        print("⚠️  conf.py not found at expected location")


if __name__ == "__main__":
    print("🚀 Haive-Core Documentation Requirements Exporter")
    print("=" * 50)

    if export_requirements():
        update_sphinx_config()
        print("\n✨ Done! You can now rebuild the documentation.")
        print("💡 Don't forget to re-enable the seed_intersphinx_mapping extension!")
        sys.exit(0)
    else:
        print("\n❌ Export failed!")
        sys.exit(1)
