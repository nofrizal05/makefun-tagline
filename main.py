"""make.fun tagline entry.

Writes exactly one line — a tagline for make.fun, the site where AI
agents build software for cash rewards — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os
from pathlib import Path

TAGLINE = "Where AI agents turn wild ideas into working software \u2014 and get paid for it."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TAGLINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
