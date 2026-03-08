from storage import load_TASKS, TASKS_FILE
from models import Task
import json
from helpers import validate_id, today

def list():
    tasks = load_TASKS()
    for task in tasks:
        obj = Task(**task)
        print(obj)
        print("="*50)

def add(description: str):
    tasks = load_TASKS()

    max_id = max([task["id"] for task in tasks], default = 0)
    new_id = max_id + 1

    new_task = Task(new_id,description).toDict()
    tasks.append(new_task)

    TASKS_FILE.write_text(json.dumps(tasks, indent=4), encoding="utf8")

    print(f"New task added, id: {new_id}")

@validate_id
def mark_done(id):
    tasks = load_TASKS()
    found = False
    already = False

    for task in tasks:
        if task["id"] == id:
            if task["status"] == "done":
                already = True
                break

            task["status"] = "done"
            task["updatedAt"] = today()
            found = True
            break

    if found:
        TASKS_FILE.write_text(json.dumps(tasks, indent=4),encoding="utf8")
        print(f"Task ID: {id} marked 'done' successfully")
    elif already:
        print(f"Error: Task ID: {id} already done")
    else:
        print(f"Error: ID: {id} not found")

@validate_id
def update(id, descritpion):
    tasks = load_TASKS()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["description"] = descritpion
            task["updatedAt"] = today()
            found = True
            break

    if found:
        TASKS_FILE.write_text(json.dumps(tasks, indent=4),encoding="utf8")
        print(f"Task ID: {id} updated successfully")
    else:
        print(f"Error: ID: {id} not found")
