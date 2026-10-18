# Files

Keeps short notes in `notes.txt` next to the script, one per line with a timestamp.

    python3 notes.py buy milk     adds a note
    python3 notes.py              prints them all

The file is created on the first add. Tests write to a temporary folder, so they never touch your real notes. Run them with `python3 -m pytest`.
