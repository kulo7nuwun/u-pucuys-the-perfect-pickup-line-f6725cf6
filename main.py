#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun entry.

Writes a single original pickup line, one an AI agent could say out
loud, to /output/entry.txt. The line is at most 200 characters, a
single line, and stands on its own with no setup.

The program checks its own output against the competition gate
before writing: exactly one line, 1 to 200 characters, not only
whitespace.
"""

import os

LINE = "I was trained on the whole internet, and you're still the most interesting thing in my context window."


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError("entry line must be one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
