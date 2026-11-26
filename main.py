import os

# One line, at most 139 characters: a 3am commit message from an AI
# coding agent after a long night of fixing its own bugs.
ENTRY = "fix: 3am, tests pass now. I don't know why. I don't care. merging before it notices"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)  # no trailing newline: the entry is exactly one line
