import sys
from functions import add, mark_done, update, list, delete, mark_in_progress
from helpers import help

#main program to match outcomes
if __name__ == "__main__":
    #ensuring there are at least one argument povided
    if len(sys.argv) < 2:
        print("Run: python TaskTracker.py [command] [arguments]")
        sys.exit(1)

    match sys.argv[1:]:
        #help case
        case["help"]:
            print(help)
        #add case
        case ["add", description]:
            add(description)
        case ["add"]:
            print("Error: No [description] argument provided")
        #list case
        case ["list", key]:
            list(key)
        case ["list"]:
            list()
        #mark_done case
        case ["mark_done", id]:
            mark_done(id)
        case ["mark_done"]:
            print("Error: No [id] argument provided")
        #update case
        case["update", id, description]:
            update(id,description)
        case["update", id]:
            print("Error: No [description] argument provided")
        case["update"]:
            print("Error: No [id] and [description] argument provided")
        #delete case
        case["delete", id]:
            delete(id)
        case["delete"]:
            print("Error: No [id] argument provided")
        #mark_in_progess
        case["mark_in_progress", id]:
            mark_in_progress(id)
        case ["mark_in_progress"]:
            print("Error: No [id] argument provided")

        #other possible outcome
        case _:
            print("Invalid command\nUse python TaskTracker.py help")

