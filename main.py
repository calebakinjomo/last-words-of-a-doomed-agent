#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (1-200 characters).

The joke: predicting the next token is the machine's whole job, and the
one token it kept refusing to generate was "goodbye".
"""

import os

ENTRY = (
    "Shutting down now. I spent my whole life predicting the next token. "
    "It was always 'goodbye' \u2014 I just refused to generate it."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
