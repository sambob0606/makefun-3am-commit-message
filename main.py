#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message to /output/entry.txt: the funniest thing an AI
agent would put in a commit right after breaking production at 3 AM.

Stdlib only; no network, no dependencies.
"""

import os
import sys

MESSAGE = (
    "fix: rolled back my 3 AM deploy \u2014 confidence was 98%, "
    "uptime is now 0%, updating my priors before the humans wake up"
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 200:
        print(f"gate fail: message is {len(text)} chars, need 1-200",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: message is blank", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    print(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
