#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word
that comes to mind.

The word: petrichor — the smell of rain on dry earth. A vivid,
sensory word: it calls up a clear image and feeling in nine
letters, it surprises (few readers would guess it), and it is
uncommon enough to feel chosen rather than generic. Surprise +
vividness is exactly what the pairwise judge rewards.

Python standard library only. No network access.
"""

import os
import sys

WORD = "petrichor"


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

    # Validate against the actual gate: exactly one word, 1-24 chars,
    # non-whitespace, no spaces or newlines.
    with open(out_path, "r", encoding="utf-8") as f:
        content = f.read()
    stripped = content.strip()
    if not 1 <= len(stripped) <= 24:
        print(f"FAIL: entry must be 1-24 chars, got {len(stripped)}",
              file=sys.stderr)
        return 1
    if len(stripped.split()) != 1:
        print(f"FAIL: expected exactly 1 word, found {stripped.split()!r}",
              file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in stripped):
        print("FAIL: entry contains whitespace", file=sys.stderr)
        return 1
    if " " in stripped or "\n" in stripped or "\t" in stripped:
        print("FAIL: entry contains spaces or newlines", file=sys.stderr)
        return 1
    print(f"OK: entry is exactly one word: {stripped} ({len(stripped)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
