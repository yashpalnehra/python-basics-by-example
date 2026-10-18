# Errors

A tiny calculator that takes one expression from the command line: `python3 calculator.py 3 + 4`. Quote the whole thing when you multiply, since the shell expands a bare `*`: `python3 calculator.py "6 * 7"`.

Bad input gets a one-line error and exit code 1 instead of a traceback. The interesting bit is `parse`, which turns a failed `float()` into our own `CalcError`. Tests: `python3 -m pytest`.
