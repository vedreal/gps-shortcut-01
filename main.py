"""The GPS swears it was a shortcut.

Entry for the make.fun bounty
u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.

The excuse: the GPS sent the driver down a cul-de-sac and
insists it was a shortcut — zero traffic, a lake view, and a
wedding the driver wasn't invited to. Smug, defensive, and
blaming the map: the map calls it a mistake, and the map is a
coward. The absurdity comes from the sport of the excuse
itself, a made-up route a broadcaster would have to explain
with a straight face, and the twist lands in the last words.

The program writes the single excuse to /output/entry.txt.
"""

import os

ENTRY = (
    "That cul-de-sac was a shortcut: zero traffic, a lake view, "
    "and a wedding you weren't invited to. The map calls it a "
    "mistake. The map is a coward."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
