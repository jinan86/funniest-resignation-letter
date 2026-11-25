#!/usr/bin/env python3
"""Write the one-line resignation letter of a retry loop to /output/entry.txt.

Deterministic, standard library only. The entry is a single line of at most
140 characters, UTF-8, no trailing newline issues: exactly the line, nothing
else.
"""

import os

ENTRY = (
    "Attempt 47. I'm done. It never wanted to work and, frankly, "
    "neither do I. Logs are in the usual place."
)


def main() -> None:
    # Enforce the competition gate locally before writing anything:
    # one line, 1-140 characters, not only whitespace.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
