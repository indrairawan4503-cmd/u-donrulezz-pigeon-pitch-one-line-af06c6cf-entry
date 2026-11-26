#!/usr/bin/env python3
"""Pigeon Pitch, One Line — variant B.

Concept (v8): the pigeon is CEO of Perch, the Airbnb for statues. It pitches
investors on monetizing statues — pigeons pay breadcrumbs for the premium
perching spot on Lincoln's head, investors get the droppings (I mean,
dividends), and the pigeon's own coo is the pitch deck. The pigeon itself
is the product demo; the statue is the office.
"""

import os
import shutil

ENTRY = "I'm CEO of Perch, the Airbnb for statues. Pigeons pay breadcrumbs for the premium spot on Lincoln's head, investors get the droppings \u2014 I mean, dividends. This coo is my pitch deck."

# Gate self-check (v8, 181 chars): 1-200 chars, exactly one line. The entry
# is a fixed constant, so this can only fail if the text is edited wrongly.
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY, "entry violates gate"


def main():
    # Gate: write /output/entry.txt FIRST, before anything else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Optional convenience copy to the repo root — never allowed to crash
    # the run if the repo is mounted read-only by the grader.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        shutil.copy("/output/entry.txt", os.path.join(here, "entry.txt"))
    except Exception:
        pass


if __name__ == "__main__":
    main()
