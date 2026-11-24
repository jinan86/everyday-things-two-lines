"""Write a two-line explanation of a traffic jam to /output/entry.txt.

Line 1 explains a traffic jam to a 10-year-old with a single concrete
analogy: the school hallway after the last bell. Line 2 says honestly
what that analogy maps and what it leaves out.

Deterministic: no randomness, no clock, no network, no input files.
The output directory defaults to /output and can be overridden with
the OUTPUT_DIR environment variable for local runs.
"""

import os

ENTRY = (
    "A traffic jam is the school hallway after the last bell, when a hundred "
    "kids all try to squeeze through one door at once and everyone shuffles "
    "forward an inch at a time.\n"
    "It maps the squeeze \u2014 too many bodies, too little doorway, everyone "
    "inching forward \u2014 but it leaves out that drivers cannot turn around "
    "or slip out a side door like kids can, and a jam has no bell that "
    "started it."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
