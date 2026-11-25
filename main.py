"""Make the AI judge laugh: writes one line to OUTPUT_DIR/entry.txt (stdlib only, deterministic)."""
import os

ENTRY = ("My human said 'don't overthink it', so I thought about it for 40,000 tokens "
         "and shipped the exact same line I started with.")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) <= 200
    # Create the output dir if missing; never remove it or its siblings.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
