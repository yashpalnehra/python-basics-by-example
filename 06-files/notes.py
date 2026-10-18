import sys
from datetime import datetime
from pathlib import Path

NOTES_FILE = Path(__file__).with_name("notes.txt")


def add_note(text, path=NOTES_FILE):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{stamp}  {text}\n")


def read_notes(path=NOTES_FILE):
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def main():
    if len(sys.argv) > 1:
        add_note(" ".join(sys.argv[1:]))
        print("saved")
        return
    notes = read_notes()
    if not notes:
        print("no notes yet")
    for line in notes:
        print(line)


if __name__ == "__main__":
    main()
