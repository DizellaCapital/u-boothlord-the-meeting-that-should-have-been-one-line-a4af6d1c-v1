#!/usr/bin/env python3
"""One-line meeting entry for the make.fun bounty.

Writes exactly one sentence (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), then reads it back
to confirm the file contains precisely that sentence.
"""

import os
import sys

SENTENCE = (
    "The budget was approved on Tuesday, the client said no on "
    "Wednesday, and this meeting is Thursday pretending neither of "
    "those things happened."
)

MIN_LEN = 1
MAX_LEN = 200
TERMINATORS = (".", "!", "?")


def check_sentence(text: str) -> None:
    """Enforce the bounty rules: one line, 1-200 chars, sentence-final punctuation."""
    if not text:
        raise ValueError("entry is empty")
    if len(text) < MIN_LEN or len(text) > MAX_LEN:
        raise ValueError(
            f"entry is {len(text)} chars, must be {MIN_LEN}-{MAX_LEN}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "\t" in text:
        raise ValueError("entry must not contain tabs")
    if not text.endswith(TERMINATORS):
        raise ValueError("entry must end with sentence punctuation")


def main() -> int:
    check_sentence(SENTENCE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    with open(target, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE + "\n")

    # Read back and verify what actually landed on disk.
    with open(target, "r", encoding="utf-8") as handle:
        stored = handle.read()

    if stored != SENTENCE + "\n":
        raise ValueError("verification failed: file content mismatch")

    print(f"wrote {len(SENTENCE)} chars to {target} ({len(stored)} bytes on disk)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
