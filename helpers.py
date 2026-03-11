from datetime import datetime
#fast function to return time
def today():
    return datetime.now().strftime("%Y-%m-%d %H:%M")
#decorator validating id to make sure it is a number
def validate_id(func):
    def wrapper(id, *args, **kwargs):
        try:
            new_id = int(id)
        except ValueError:
            print(f"Error: Please provide valid ID number")
            return

        return func(new_id, *args, **kwargs)
    return wrapper


#help string
help = """Run the application using the following commands:
-Add a new task
python TaskTracker.py add "Buy groceries"
-List all tasks
python TaskTracker.py list
-List tasks by status
python TaskTracker.py list done
python TaskTracker.py list in-progress
-Update a task
python TaskTracker.py update 1 "Buy groceries and milk"
-Delete a task
python TaskTracker.py delete 1
-Mark task as done
python TaskTracker.py mark_done 1
-Mark task as 'in progress'
python TaskTracker.py mark_in_progress 1"""