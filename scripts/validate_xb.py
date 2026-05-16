#!/usr/bin/env python3
"""
Minimal xb validator.

Usage:
  python scripts/validate_xb.py examples/basic_handoff.yaml

This checks only basic structure. It does not validate the semantic quality of the handoff.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml")
    print("Install with: pip install pyyaml")
    sys.exit(2)


REQUIRED = ["t", "history", "state", "relations", "request"]


def fail(msg: str) -> None:
    print(f"INVALID: {msg}")
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_xb.py path/to/xb.yaml")
        sys.exit(2)

    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"file not found: {path}")

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        fail("top-level YAML must be a mapping")

    if "xb" not in data:
        fail("missing top-level 'xb' key")

    xb = data["xb"]
    if not isinstance(xb, dict):
        fail("'xb' must be a mapping")

    for key in REQUIRED:
        if key not in xb:
            fail(f"missing required field: {key}")

    if not isinstance(xb["history"], list):
        fail("'history' must be a list")

    if not isinstance(xb["relations"], list):
        fail("'relations' must be a list")

    for i, rel in enumerate(xb["relations"]):
        if not isinstance(rel, list) or len(rel) != 3:
            fail(f"relations[{i}] must be a 3-item list: [source, relation, target]")

    if "dropped" in xb:
        if not isinstance(xb["dropped"], list):
            fail("'dropped' must be a list")
        for i, item in enumerate(xb["dropped"]):
            if not isinstance(item, list) or len(item) != 2:
                fail(f"dropped[{i}] must be a 2-item list: [item, reason]")

    if "gaps" in xb and not isinstance(xb["gaps"], list):
        fail("'gaps' must be a list")

    print("VALID: xb structure looks correct")


if __name__ == "__main__":
    main()
