"""Sphinx configuration for haive-games documentation."""

import os
import sys

# Path setup
sys.path.insert(0, os.path.abspath("../../src"))

# Import shared Haive configuration from pydevelop-docs package
from pydevelop_docs.config import get_haive_config

# Get package-specific configuration
package_name = "haive-games"
package_path = "../../src"

config = get_haive_config(
    package_name=package_name, package_path=package_path, is_central_hub=False
)

# Apply configuration to globals
globals().update(config)
