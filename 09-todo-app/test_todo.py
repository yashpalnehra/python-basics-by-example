import json

import pytest

import storage
import todo


@pytest.fixture
def todo_file(tmp_path):
    return tmp_path / "todo.json"


def run(todo_file, *args):
    todo.run(["--file", str(todo_file), *args])


def tasks_in(todo_file):
    return storage.load(todo_file)["tasks"]


def test_add_and_list(todo_file, capsys):
    run(todo_file, "add", "buy", "milk")
    run(todo_file, "add", "walk the dog")
    run(todo_file, "list")
    out = capsys.readouterr().out
    assert "buy milk" in out
    assert "walk the dog" in out
    assert [t["id"] for t in tasks_in(todo_file)] == [1, 2]


def test_done_hides_task_unless_all(todo_file, capsys):
    run(todo_file, "add", "a")
    run(todo_file, "add", "b")
    run(todo_file, "done", "1")
    capsys.readouterr()

    run(todo_file, "list")
    assert capsys.readouterr().out.splitlines() == ["[ ]   2  b"]

    run(todo_file, "list", "--all")
    assert "[x]   1  a" in capsys.readouterr().out


def test_remove(todo_file):
    run(todo_file, "add", "a")
    run(todo_file, "add", "b")
    run(todo_file, "remove", "1")
    assert [t["text"] for t in tasks_in(todo_file)] == ["b"]


def test_ids_are_not_reused(todo_file):
    run(todo_file, "add", "a")
    run(todo_file, "add", "b")
    run(todo_file, "remove", "2")
    run(todo_file, "add", "c")
    assert [t["id"] for t in tasks_in(todo_file)] == [1, 3]


def test_unknown_id(todo_file):
    with pytest.raises(LookupError):
        run(todo_file, "done", "42")


def test_empty_list_message(todo_file, capsys):
    run(todo_file, "list")
    assert capsys.readouterr().out.strip() == "nothing to do"


def test_broken_file(todo_file):
    todo_file.write_text("{not json")
    with pytest.raises(ValueError, match="not valid JSON"):
        run(todo_file, "list")


def test_wrong_shape(todo_file):
    todo_file.write_text("[1, 2, 3]")
    with pytest.raises(ValueError, match="does not look like"):
        run(todo_file, "list")


def test_save_writes_readable_json(todo_file):
    storage.save(
        todo_file, {"next_id": 2, "tasks": [{"id": 1, "text": "a", "done": False}]}
    )
    assert json.loads(todo_file.read_text())["tasks"][0]["text"] == "a"
    assert not todo_file.with_suffix(".tmp").exists()
