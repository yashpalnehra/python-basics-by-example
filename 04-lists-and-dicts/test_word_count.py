from word_count import count_words, top_words


def test_counts_ignore_case_and_punctuation():
    counts = count_words("Hello, hello! World.")
    assert counts == {"hello": 2, "world": 1}


def test_empty_text():
    assert count_words("") == {}


def test_top_words_order():
    counts = {"a": 3, "b": 3, "c": 1, "d": 5}
    assert top_words(counts, 3) == [("d", 5), ("a", 3), ("b", 3)]


def test_top_words_when_fewer_than_n():
    assert top_words({"only": 1}, 5) == [("only", 1)]
