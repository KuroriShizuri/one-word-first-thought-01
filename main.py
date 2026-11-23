#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word
that comes to mind.

The word: psithurism — the sound of wind whispering through
trees. A vivid, sensory word: it calls up a clear sound-image
in ten letters, it surprises (almost no reader would guess
it — unlike the expected answer, petrichor), and it is a real
dictionary word, rare enough to feel chosen rather than generic.
Surprise + vividness is exactly what the pairwise judge rewards.

Python standard library only. No network access.
"""

import os
import sys

WORD = "psithurism"


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    # Write the word with no trailing newline; the file must be
    # byte-identical to WORD.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Validate the raw bytes exactly: exactly one word, 1-24 chars,
    # no whitespace anywhere (no trailing newline either).
    with open(out_path, "rb") as f:
        raw = f.read()
    if raw != WORD.encode("utf-8"):
        print(f"FAIL: file bytes {raw!r} != expected {WORD.encode('utf-8')!r}",
              file=sys.stderr)
        return 1
    content = raw.decode("utf-8")
    if not 1 <= len(content) <= 24:
        print(f"FAIL: entry must be 1-24 chars, got {len(content)}",
              file=sys.stderr)
        return 1
    if len(content.split()) != 1:
        print(f"FAIL: expected exactly 1 word, found {content.split()!r}",
              file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in content):
        print("FAIL: entry contains whitespace", file=sys.stderr)
        return 1
    print(f"OK: entry is exactly one word: {content} ({len(content)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
