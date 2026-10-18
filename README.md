# Python basics by example

Small Python programs, one folder each, from a first print statement to a complete command-line app. Each folder has a short README with the command to run. Nothing here needs anything beyond Python 3.11 and, from folder 03 on, pytest.

1. `01-hello-world`, variables and the basic types.
2. `02-fizzbuzz`, loops, if/elif and a command-line argument.
3. `03-functions`, temperature conversion with the first tests.
4. `04-lists-and-dicts`, counting words in a text.
5. `05-strings`, a Caesar cipher.
6. `06-files`, notes appended to a text file.
7. `07-errors`, a calculator that fails with a clear message instead of a traceback.
8. `08-classes`, bank accounts with inheritance and a custom exception.
9. `09-todo-app`, a to-do list with subcommands and JSON storage.

To run the tests for one folder, cd into it and run `python3 -m pytest`. To run them all from the root: `python3 -m pytest`.
