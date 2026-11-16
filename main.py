"""ai-excited-01 entry: write the chalk-dragon image to the output directory.

The repository holds the finished image as entry.png. This program copies
it, byte for byte, to <output>/entry.png, where <output> is the directory
named by MAKEFUN_OUTPUT_DIR when that variable is set and /output
otherwise (the sandbox layout). Copying a stored file is what makes the
two grading runs produce identical bytes.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def source_image() -> Path:
    """The image stored beside this file, wherever the program is run from."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def output_path() -> Path:
    """Where the judge's copy goes: MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / IMAGE_NAME


def main() -> None:
    src = source_image()
    if not src.is_file():
        raise SystemExit(f"stored image is missing: {src}")
    dst = output_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    with src.open("rb") as fin, dst.open("wb") as fout:
        shutil.copyfileobj(fin, fout, length=256 * 1024)
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
