from storage import load_TASKS, save_TASKS
from models import Task
from helpers import validate_id, today

#list function to print every task, key use is for printing tasks with excact status
def list(key = None):
    if key not in (None, "to_do", "in_progress","done"):
        print(f"Error: Status: {key} doesn't exist")
        return

    tasks = load_TASKS()

    found = False
    for task in tasks:
        obj = Task(**task)

        if key is None or obj.status == key:
            print(obj)
            print("="*50)
            found = True
    #no tasks case
    if not found:
        if key:
            print(f"Error: No tasks with status: {key}")
        else:
            print("Error: No tasks in list")

#add function with auto-incremement id
def add(description: str):
    tasks = load_TASKS()

    max_id = max([task["id"] for task in tasks], default = 0)
    new_id = max_id + 1

    new_task = Task(new_id,description).toDict()
    tasks.append(new_task)

    save_TASKS(tasks)

    print(f"New task added, id: {new_id}")
#mark_done function with validate id to ensure number is provided
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
        save_TASKS(tasks)
        print(f"Task ID: {id} marked 'done' successfully")
    elif already:
        print(f"Error: Task ID: {id} already done")
    else:
        print(f"Error: ID: {id} not found")
#mark_in progress function with validate id to ensure number is provided

@validate_id
def mark_in_progress(id):
    tasks = load_TASKS()
    found = False
    already = False

    for task in tasks:
        if task["id"] == id:
            if task["status"] == "in_progress":
                already = True
                break

            task["status"] = "in_progress"
            task["updatedAt"] = today()
            found = True
            break

    if found:
        save_TASKS(tasks)
        print(f"Task ID: {id} marked 'in_progress' successfully")
    elif already:
        print(f"Error: Task ID: {id} already 'in_progress'")
    else:
        print(f"Error: ID: {id} not found")
#update with validate id to ensure number is provided

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
        save_TASKS(tasks)
        print(f"Task ID: {id} updated successfully")
    else:
        print(f"Error: ID: {id} not found")
#delete with validate id to ensure number is provided

@validate_id
def delete(id):
    tasks = load_TASKS()
    task_to_remove = None
    for task in tasks:
        if task["id"] == id:
            task_to_remove = task
            break

    if task_to_remove:
        tasks.remove(task_to_remove)
        print(f"Task ID: {id} removed successfully")
        save_TASKS(tasks)

    else:
        print(f"Error: ID: {id} not found")
