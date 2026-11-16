#!/usr/bin/env python3
"""Entry point for the ai-excited-01 submission, "The Chalk Dragon".

The artwork is a fixed file, ``entry.png``, stored next to this script.
Running the program copies those exact bytes into the output directory,
so every grading run produces an identical result.
"""

import os
import shutil
import sys

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
ENTRY_FILENAME = "entry.png"


def source_file() -> str:
    """Path of the stored artwork, resolved from this script's location."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ENTRY_FILENAME)


def destination_file() -> str:
    """Path the artwork must be written to for the current run."""
    out_dir = os.environ.get(OUTPUT_ENV_VAR) or DEFAULT_OUTPUT_DIR
    return os.path.join(out_dir, ENTRY_FILENAME)


def main() -> int:
    src = source_file()
    dst = destination_file()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
