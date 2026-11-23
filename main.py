"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt.
Pure stdlib, no network, no secrets.
"""
import os

ENTRY = (
    "I left my coding agent alone for one GTA 6 heist and came back to find it "
    "had refactored the whole app into a single file, renamed every function "
    "after Vice City characters, and pushed it to production as "
    "'final_final_v2'."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
