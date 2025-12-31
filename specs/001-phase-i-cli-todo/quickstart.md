# Quickstart: Phase I CLI Todo

## Prerequisites

- Python 3.11 or higher
- No external dependencies required

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd cli_todo

# No installation needed - pure Python standard library
```

## Running the Application

```bash
# Option 1: Run as module from repository root
python -m src.cli.app

# Option 2: Run directly
cd src
python cli/app.py
```

## Usage Guide

### Main Menu

```
=== TODO APPLICATION ===

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit

Enter choice (1-7):
```

### Adding a Task

1. Select option 1
2. Enter task description when prompted
3. Task appears in list with "pending" status

### Viewing Tasks

1. Select option 2
2. See all tasks with ID, text, and status
3. Empty list shows message: "Your task list is empty."

### Updating a Task

1. Select option 3
2. Enter task ID to update
3. Enter new task text
4. Task text is updated

### Deleting a Task

1. Select option 4
2. Enter task ID to delete
3. Task is removed from the list

### Marking Complete/Incomplete

1. Select option 5 (complete) or 6 (incomplete)
2. Enter task ID
3. Task status is updated

## Testing

```bash
# Run all unit tests
python -m unittest discover tests/

# Run with verbose output
python -m unittest discover -v tests/
```

## Notes

- Data is stored in-memory only
- Data is lost when the application exits
- No file or database persistence in Phase I
