"""The Meeting That Should Have Been One Line — make.fun entry (v1).

This program writes the entry's one sentence to entry.txt inside the
output directory (MAKEFUN_OUTPUT_DIR, default /output). Stdlib only.
The line is validated before writing: exactly one line, 1-200
characters, no tabs, ending with sentence punctuation. The write is
verified by reading the file back and comparing it with the line.
"""

import os

LINE = (
    "The budget was approved on Tuesday, the client said no on "
    "Wednesday, and this meeting is Thursday pretending neither of "
    "those things happened."
)


def main() -> None:
    line = LINE
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert "\t" not in line, "entry must not contain tabs"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line[-1] in ".!?", "entry must end with sentence punctuation"
    # One sentence, standing alone: the decision is already made on
    # Tuesday and Wednesday, so Thursday's meeting has nothing left
    # to decide — the line itself replaces the meeting.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == line, "read-back mismatch"
    print(f"wrote {len(line.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
