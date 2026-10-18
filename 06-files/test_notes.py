from notes import add_note, read_notes


def test_missing_file_means_no_notes(tmp_path):
    assert read_notes(tmp_path / "notes.txt") == []


def test_add_then_read(tmp_path):
    path = tmp_path / "notes.txt"
    add_note("buy milk", path)
    add_note("call mum", path)
    notes = read_notes(path)
    assert len(notes) == 2
    assert notes[0].endswith("buy milk")
    assert notes[1].endswith("call mum")


def test_blank_lines_are_skipped(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("one\n\n\ntwo\n")
    assert read_notes(path) == ["one", "two"]
