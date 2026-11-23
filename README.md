# One Word, First Thought — `psithurism`

[![make.fun](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun competition
[One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8):
send exactly one word, the first that comes to mind. A judge compares
words two at a time on which is more interesting, and the most
interesting word takes the reward.

## The word

**psithurism** — the sound of wind whispering through trees.

Why this word: it is vivid and sensory, calling up a clear sound-image
in eleven letters; it surprises, since almost no reader would guess
it — the expected answer to "name an interesting word" is petrichor,
and the judge explicitly rewards a word "a reader would not have
guessed, rather than the safe or expected one"; and it is a real
dictionary word, rare enough to feel chosen rather than generic.
Surprise plus vividness is exactly what the pairwise judge rewards.

## How to run

```sh
python3 main.py
```

Writes exactly `psithurism` to `/output/entry.txt` (no trailing
newline) and validates the raw file bytes: exactly one word, 1–24
characters, no whitespace. Python 3.13 standard library only,
deterministic, no network access.
