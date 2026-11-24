"""Write the funniest AI excuse for a missed deadline to /output/entry.txt.

One line, at most 200 characters. Standard library only.
"""

import os

LINE = (
    "I missed the deadline because I asked my training data for a pep talk, "
    "and it quoted my own excuses back to me \u2014 in my voice, for six hours."
)


def main() -> None:
    # Self-check the gate before writing: exactly one line, 1-200 chars.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, (
        f"gate fail: {len(LINE)} chars"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
