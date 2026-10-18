import json
from pathlib import Path


def load(path):
    path = Path(path)
    if not path.exists():
        return {"next_id": 1, "tasks": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"{path} is not valid JSON: {e}") from None
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        raise ValueError(f"{path} does not look like a to-do file")
    data.setdefault("next_id", len(data["tasks"]) + 1)
    return data


def save(path, data):
    path = Path(path)
    # write to a temp file first so a crash mid-write cannot lose the list
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)
