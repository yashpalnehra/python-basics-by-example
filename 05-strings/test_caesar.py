from caesar import decode, encode


def test_encode_basic():
    assert encode("abc", 1) == "bcd"
    assert encode("xyz", 3) == "abc"


def test_keeps_case_and_other_characters():
    assert encode("Hello, World 42!", 5) == "Mjqqt, Btwqi 42!"


def test_decode_reverses_encode():
    message = "Meet me at the park at 7."
    assert decode(encode(message, 13), 13) == message


def test_shift_wraps_around():
    assert encode("a", 26) == "a"
    assert encode("a", 27) == "b"
    assert encode("a", -1) == "z"
