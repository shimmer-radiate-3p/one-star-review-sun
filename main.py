"""One-star review of something essential: the sun.

Entry for make.fun's "One-Star Review of Something Essential" bounty.
Writes a single-line, deadpan one-star review (112 characters) to
/output/entry.txt. Standard library only, no network, no randomness,
no clock: every run writes exactly the same bytes.
"""

import os

ENTRY = (
    "One star. The sun rises at 5 a.m. uninvited, fades the sofa, "
    "and still expects a thank-you every single morning."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the gate before writing: 1-160 characters, one line.
    assert 1 <= len(ENTRY) <= 160, "review must be 1-160 characters"
    assert "\n" not in ENTRY, "review must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly the 112-character review,
    # one line, UTF-8, so it passes the gate (1-160 characters) and the
    # byte-size tie-break is as small as this entry can be.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
