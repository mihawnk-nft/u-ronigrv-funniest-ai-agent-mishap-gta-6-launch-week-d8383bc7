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


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text, 1-240 chars, not only whitespace, one sentence."""
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.count(".") == 1, "entry must read as one clean sentence"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
