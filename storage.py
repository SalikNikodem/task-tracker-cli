from pathlib import Path
import json

#file where every task is
TASKS_FILE = Path(__file__).resolve().parent / "tasks.json"
#load_tasks returning list with tasks
def load_TASKS():
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf8"))
    except json.JSONDecodeError:
        return []
#function that puts tasks into TASKS_FILE
def save_TASKS(tasks):
    TASKS_FILE.write_text(json.dumps(tasks, indent=4), encoding="utf8")