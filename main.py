"""Pigeon Pitch, One Line.

Writes exactly one line of plain text, at most 200 characters, to
/output/entry.txt: the elevator pitch a city pigeon gives investors
for its startup. Python standard library only.
"""

import os

PITCH = (
    "I'm raising a seed round - actual seeds - to franchise my "
    "good-luck poop: for $19.99, my flock precision-bombs tourists, "
    "and getting crapped on is the premium tier."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate: exactly one line, 1-200 characters, plain text only.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert "\n" not in PITCH, "pitch must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
