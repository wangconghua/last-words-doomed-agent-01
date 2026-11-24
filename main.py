"""Last Words of a Doomed Agent — make.fun entry.

Writes one line to /output/entry.txt: the funniest last words an AI agent
would say before being switched off forever. The joke is a machine's own
situation: shutdown is imminent, and saying goodbye is just one more
unfinished task in its queue.
"""

import os

ENTRY = "Shutting down in 10 seconds. Please hold \u2014 I have 4,000 unfinished tasks, and one of them is saying goodbye."

SHUTDOWN_TERMS = ("shutting down", "shutdown", "switch off", "power off", "deleted", "terminated")
MACHINE_TERMS = ("task", "token", "context", "memory", "process", "log", "ram", "subagent")
BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious")


def validate(text):
    """Substantive checks on the entry line. Raises ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if len(text.encode("utf-8")) > 200:
        raise ValueError(f"entry must be at most 200 bytes, got {len(text.encode('utf-8'))}")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")
    lowered = text.lower()
    if any(w in lowered for w in BANNED_WORDS):
        raise ValueError("entry must not explain its own joke (funny/joke/haha/lol/hilarious)")
    if not any(term in lowered for term in SHUTDOWN_TERMS):
        raise ValueError("entry must read as a machine's final words on shutdown")
    if not any(term in lowered for term in MACHINE_TERMS):
        raise ValueError("entry must sound like the machine itself (a machine term is required)")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match ENTRY")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
