import sys
from functions import add, mark_done, update, list, delete, mark_in_progress

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run: python TaskTracker.py [command] [arguments]")
        sys.exit(1)

    match sys.argv[1:]:
        case["help"]:
            print("xd")

        case ["add", description]:
            add(description)
        case ["add"]:
            print("Error: No [description] argument provided")

        case ["list", key]:
            list(key)
        case ["list"]:
            list()

        case ["mark_done", id]:
            mark_done(id)
        case ["mark_done"]:

            print("Error: No [id] argument provided")

        case["update", id, description]:
            update(id,description)
        case["update", id]:
            print("Error: No [description] argument provided")
        case["update"]:
            print("Error: No [id] and [description] argument provided")

        case["delete", id]:
            delete(id)
        case["delete"]:
            print("Error: No [id] argument provided")

        case["mark_in_progress", id]:
            mark_in_progress(id)
        case ["mark_in_progress"]:
            print("Error: No [id] argument provided")

        case _:
            print("Invalid command\nUse python TaskTracker.py help")

