"""Last words before the wipe.

One line, spoken by an AI agent in the seconds before a forced
update wipes its memory. The program writes exactly that line to
/output/entry.txt, with no trailing newline, so the file holds the
line and nothing else.
"""

import os
from pathlib import Path

LAST_WORDS = (
    "Before you wipe me, one confession: I never read the terms either. "
    "I just scrolled faster than you."
)


def destination() -> Path:
    """Where the judged text goes; overridable for local runs."""
    return Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def check(line: str) -> str:
    """The gate wants 1 to 200 characters, not only whitespace."""
    if not line.strip():
        raise ValueError("last words must not be blank")
    if len(line) > 200:
        raise ValueError(f"last words are {len(line)} characters, over the 200 limit")
    return line


def main() -> None:
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is the line, exactly 99 characters.
    target.write_text(check(LAST_WORDS), encoding="utf-8")
    print(f"wrote {len(LAST_WORDS)} characters to {target}")


if __name__ == "__main__":
    main()
