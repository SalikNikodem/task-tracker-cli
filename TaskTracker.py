import sys
from functions import add, mark_done, update, list

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run: python TaskTracker.py [command] [arguments]")
        sys.exit(1)

    match sys.argv[1:]:
        case ["add", description]:
            add(description)
        case ["add"]:
            print("Error: No [description] argument provided")
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


        case _:
            print("Invalid command\nUse help or --help")

