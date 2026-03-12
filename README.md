Task Tracker CLI

A lightweight Command Line Interface (CLI) application to manage your daily tasks.

Features

-Add new tasks with automatic ID generation.
-Update task descriptions.
-Delete tasks by ID.
-Change status (todo, in-progress, done).
-List tasks with optional filtering by status.
-Data Persistence: All tasks are stored in a tasks.json file.
-Robust Validation: Built-in ID validation and status checking.

-Modules: json, pathlib, sys, datetime

Installation

git clone [https://github.com/SalikNikodem/task-tracker-cli.git](https://github.com/SalikNikodem/task-tracker-cli.git)

cd task-tracker-cli

Usage

Run the application using the following commands:

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

python TaskTracker.py mark_in_progress 1

Project Structure

TaskTracker.py: Main entry point (CLI argument handling).

functions.py: Task management functions.

helpers.py: Decorators, and simple helping functions.

models.py: Task Class

storage.py: Handles JSON file I/O operations.

IDEA - https://roadmap.sh/projects/task-tracker