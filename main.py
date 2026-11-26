"""Last Text at One Percent: the final text a dying phone sends at 1% battery.

The joke turns on two things every phone owner knows: a phone can sit at 1%
for hours, and the cruellest way to spend its last breath is opening maps —
the one app that needs the phone alive to get its owner home. The phone does
not beg for a charger; it is insulted by how its final moments were spent,
and it says so in lowercase, the way a real text reads.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the same
bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = (
    "i held 1% for three hours like a champ and you spend my last breath "
    "opening maps. MAPS. good luck getting home, genius."
)

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
