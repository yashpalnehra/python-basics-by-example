# To-do app

A command-line to-do list. Tasks live in `~/.todo.json`, or wherever `--file` points.

    python3 todo.py add buy milk
    python3 todo.py add call the dentist
    python3 todo.py list
    python3 todo.py done 1
    python3 todo.py list --all
    python3 todo.py remove 2

`list` hides finished tasks unless you pass `--all`. Ids come from a counter stored in the file and are never reused. An old note that says "task 3" keeps meaning the same thing.

The code is split in two. `todo.py` has the commands and the argparse setup, `storage.py` only knows how to read and write the JSON file. Saving goes through a temp file and a rename, so an interrupted write can't leave you with half a file.

Tests use a file in a temporary folder: `python3 -m pytest`.
