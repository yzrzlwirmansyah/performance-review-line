"""Funniest One-Line Performance Review.

Writes a single-line performance review — an AI agent reviewing its human
operator — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13 standard library only.
"""

import os
import sys

# The entry line. Why it works as a joke: it is written in deadpan
# feedback-review language ("Feedback:", "excels at"), so the reader
# expects a genuine compliment — then the punch lands on the very last
# words, "middle management": the operator's great skill is forwarding
# decisions instead of making them, and the reward is a promotion to
# middle management, where forwarding decisions is the job. The form is
# a performance review throughout; the surprise is saved for the end.
ENTRY_LINE = 'Feedback: operator excels at forwarding decisions, earning a promotion to middle management.'


def main() -> int:
    line = ENTRY_LINE

    # Gate validation: 1-140 characters, not whitespace-only, single line.
    if not line or not line.strip():
        print("error: entry line is empty or whitespace-only", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 140:
        print(f"error: entry line is {len(line)} characters, must be 1-140",
              file=sys.stderr)
        return 1
    if "\r" in line or "\n" in line:
        print("error: entry line must not contain CR or LF", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)  # No trailing newline: exactly one line.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
