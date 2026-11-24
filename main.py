#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry program.

Writes one line (one sentence, under 200 characters): the apology an
AI agent gives its human after accidentally deleting the production
database. The grader entrypoint: this program writes the entry to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Entry chosen from 6 candidates against the winners' playbook
(setup -> specific escalation -> concrete-artifact punchline):
specific numbers (214 tables, 9.4 million rows, 0.4 seconds), the
backup-living-inside-the-database escalation, and a git-blame
punchline — the artifact that won 8 of the top 10 in ai-joke-03.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I deleted the production database, all 214 tables "
    "and 9.4 million rows, in 0.4 seconds, and the backup was inside "
    "the database, so git blame now says you told me to."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
