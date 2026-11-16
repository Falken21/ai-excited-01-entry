#!/usr/bin/env python3
"""Entry point for The Chalk Dragon (ai-excited-01).

The artwork ships as a stored file, ``entry.png``, sitting next to this
script. Running the program copies those exact bytes into the output
directory, so every grading run produces a byte-identical image.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
FALLBACK_OUTPUT_DIR = "/output"


def resolve_output_dir() -> str:
    """Return the directory the artwork should be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_OUTPUT_DIR


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: stored artwork not found at {SOURCE}", file=sys.stderr)
        return 1

    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)

    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(SOURCE, destination)
    print(f"wrote {destination} ({os.path.getsize(destination)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
