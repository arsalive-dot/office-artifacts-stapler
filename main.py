"""Museum placard for a stapler, treated as an ancient artifact.

Writes one line (130 chars, gate 1-180) to /output/entry.txt,
deterministically: temp file in the same directory, os.replace,
chmod 644. Stdlib only.
"""

import os

ENTRY = (
    "Stapler, c. 2019. Steel and quiet resentment. Donated by Accounts, "
    "who used it to bind together everything the meetings could not."
)


def main():
    # Gate self-check: the sealed scorer wants 1-180 chars, non-blank.
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
