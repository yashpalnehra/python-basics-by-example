# Strings

A Caesar cipher. Every letter moves a fixed number of places along the alphabet and wraps from z back to a. Case, digits and punctuation are left alone.

    python3 caesar.py encode 3 "attack at dawn"
    python3 caesar.py decode 3 "dwwdfn dw gdzq"

Tests: `python3 -m pytest`.
