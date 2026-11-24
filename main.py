"""A Day of One-Line Pitches — entry program.

Writes a single one-sentence pitch (at most 240 characters) that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun, to /output/entry.txt, the path the
grader reads.

Local testing: set ENTRY_OUTPUT to a local path so the run does not
touch the shared /output directory, e.g.
    ENTRY_OUTPUT=output/entry.txt python3 main.py

Standard library only, deterministic, no network, no file reads.
"""

import os
from pathlib import Path

LINE = (
    "Tell an AI agent on make.fun your app idea the way you'd tell a "
    "friend, and it will build the first version for you \u2014 no code, "
    "no setup, and if you don't like it, you've lost nothing but a "
    "conversation."
)


def main() -> None:
    # Gate guard: one line, 1-240 characters, not only whitespace.
    assert "\n" not in LINE and 1 <= len(LINE) <= 240 and LINE.strip(), (
        "entry line violates the 1-240 character single-line gate"
    )
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the one line, nothing else.
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
