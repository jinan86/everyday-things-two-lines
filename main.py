#!/usr/bin/env python3
"""Write the two-line Everyday Things entry to entry.txt.

The entry explains a traffic jam to a 10-year-old through a school
hallway analogy, then says honestly what the analogy maps and where
it stops. The text is fixed: this program's only job is to reproduce
it byte for byte, every run, with no input from the outside world.
"""

import os
from pathlib import Path

# First line: the analogy itself, one vivid sentence.
FIRST_LINE = (
    "A traffic jam is the school hallway after the last bell, "
    "when a hundred kids all try to squeeze through one door at once "
    "and everyone shuffles forward an inch at a time."
)

# Second line: what the analogy covers, and what it leaves out.
SECOND_LINE = (
    "It maps the squeeze \u2014 too many bodies, too little doorway, "
    "everyone inching forward \u2014 but it leaves out that drivers "
    "cannot turn around or slip out a side door like kids can, "
    "and a jam has no bell that started it."
)


def build_entry() -> str:
    """Join the two lines with a single newline, no trailing newline."""
    return FIRST_LINE + "\n" + SECOND_LINE


def check_entry(text: str) -> None:
    """Refuse to write anything that is not exactly two lines, 1-400 chars.

    The gate only accepts UTF-8 text of 1 to 400 characters that is not
    only whitespace, and this entry is defined as precisely two lines,
    so fail loudly here instead of shipping a broken file.
    """
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly 2 lines, got {len(lines)}")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip("\n"):
        raise ValueError("entry must not start or end with a newline")


def output_path() -> Path:
    """Where entry.txt goes: /output by default, OUTPUT_DIR overrides."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main() -> None:
    text = build_entry()
    check_entry(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
