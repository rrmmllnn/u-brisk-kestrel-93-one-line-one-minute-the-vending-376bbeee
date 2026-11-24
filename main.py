"""A vending machine's one-line pickup, at most two hundred chars.

Drops one fixed flirtatious sentence from a snack machine to a
passer-by into /output/entry.txt. Same words every run: no dice
rolls, no wall clock, no web calls, only the standard library.
"""

import os

PICKUP = (
    "Hey, I've been humming your name since you first fed me exact change. "
    "Press B7 and I'll drop the sweet stuff. "
    "Unlike the chips, I never get stuck."
)

DEST = "/output/entry.txt"


def check_line(text: str) -> None:
    size = len(text)
    if size < 1 or size > 200:
        raise ValueError("line must run 1-200 chars, saw %d" % size)
    if not text.strip():
        raise ValueError("line must hold more than blank space")
    if "\n" in text or "\r" in text:
        raise ValueError("line must stay on one row")
    if "B7" not in text:
        raise ValueError("line must keep its button code")


def main() -> None:
    check_line(PICKUP)
    folder = os.path.dirname(DEST)
    os.makedirs(folder, exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="") as handle:
        handle.write(PICKUP)


if __name__ == "__main__":
    main()
