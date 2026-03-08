from pathlib import Path
import json


TASKS_FILE = Path(__file__).resolve().parent / "tasks.json"

def load_TASKS():
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf8"))
    except json.JSONDecodeError:
        return []