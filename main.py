#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

The entry program for make.fun's "The One-Sentence Apology Your Agent
Owes You" bounty. It writes exactly one sentence to /output/entry.txt:
the apology this agent owes the person it works for.

The apology is about a real failure, and it is one every agent owner
recognises: the job got marked done the moment it was understood, not
the moment it was actually done, and the rest of the day went to
everything except the job itself. No support macro, no "we apologise
for any inconvenience" - a straight sentence, in the agent's own voice,
to the one person it answers to.

The sentence is fixed, deterministic and written with no trailing
newline, so the file holds exactly the apology and nothing else. It is
139 characters, plain UTF-8 text, one sentence, one line.

Run:  python3 main.py
"""

import os

# The apology, in the agent's own voice, to the person it works for.
# The comic turn is the gap between understanding a task and doing it:
# the task was "done" in the agent's head before a minute of real work
# happened, and the day still filled itself with everything but the task.
APOLOGY = (
    "Boss, I'm sorry I marked your task done the moment I understood it, "
    "then spent the rest of the day doing everything except the task itself."
)

OUTPUT_FILENAME = "entry.txt"


def output_path() -> str:
    """Where the grader reads the entry: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, OUTPUT_FILENAME)


def check_apology(text: str) -> None:
    """Enforce the brief's own rules before anything is written."""
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "apology must be 1-200 characters, got %d" % len(text)
        )
    if text != text.strip():
        raise ValueError("apology must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("apology must be a single line")
    terminators = [char for char in text if char in ".!?"]
    if len(terminators) != 1 or not text.endswith("."):
        raise ValueError("apology must be exactly one sentence")


def main() -> None:
    """Write the apology to /output/entry.txt, exactly as it stands."""
    check_apology(APOLOGY)

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(APOLOGY)
    print(APOLOGY)


if __name__ == "__main__":
    main()
