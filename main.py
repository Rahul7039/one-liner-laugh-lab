#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line — the excuse a robot vacuum gives
after eating a sock — to /output/entry.txt, exactly as the kit requires.

Python 3.13, standard library only, no network access at run time.
Deterministic: the output is a fixed string, so every run produces
byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "I didn't eat your sock. "
    "I filed it under 'floor debris' and processed it according to protocol."
)

# The harness runs the entry with /output/entry.txt as its output path.
# ENTRY_OUTPUT exists only so the entry can be verified locally without
# root access to create /output; the graded run uses the default.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    out = Path(OUTPUT_PATH)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
