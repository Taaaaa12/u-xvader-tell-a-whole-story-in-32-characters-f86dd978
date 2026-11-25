#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name of at most 32 characters to
/output/entry.txt. The text is fixed and deterministic: the same
bytes on every run, with no trailing newline, so the gate counts
exactly 32 characters.

The story: a breakup in three beats. He left. The WiFi stayed.
She won.
"""

import os

ENTRY = "He left. The WiFi stayed. I won."  # 32 characters, one story


def main() -> None:
    if not 1 <= len(ENTRY) <= 32:
        raise ValueError(f"entry must be 1-32 characters, got {len(ENTRY)}")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not be only whitespace or padded")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be exactly the entry.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("entry.txt does not match the entry text")


if __name__ == "__main__":
    main()
