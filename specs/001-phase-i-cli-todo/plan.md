# Implementation Plan: Phase I - CLI Todo

**Branch**: `001-phase-i-cli-todo` | **Date**: 2026-01-01 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-phase-i-cli-todo/spec.md`

## Summary

A menu-driven CLI todo application written in Python that operates entirely in-memory. Users can add, view, update, delete tasks and mark them as complete/incomplete. The application follows clean architecture with clear separation between data models and CLI presentation logic.

## Technical Context

**Language/Version**: Python 3.11+ (standard library only, no external dependencies)
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory Python list/dictionary (no persistence)
**Testing**: unittest (Python built-in)
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single CLI application
**Performance Goals**: Sub-second response for all operations
**Constraints**: No databases, no files, no network, no external dependencies
**Scale/Scope**: Single user, single session, in-memory only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status | Notes |
|-----------|-------------|--------|-------|
| I. Spec-Driven Development | Follow Constitution → Specs → Plan → Tasks → Implement | ✅ Pass | Specification approved, planning in progress |
| II. Agent Behavior Rules | No feature invention, spec-level refinement only | ✅ Pass | All design derived strictly from approved spec |
| III. Phase Governance | No future-phase features | ✅ Pass | No persistence, database, or web concepts included |
| IV. Technology Constraints | Python for backend | ✅ Pass | Using Python standard library for CLI |
| V. Quality Principles | Clean architecture, separation of concerns | ✅ Pass | Model/CLI separation planned |

**Result**: All gates pass. Proceeding with design.

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-i-cli-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (N/A - no clarifications needed)
├── data-model.md        # Phase 1 output (below)
├── quickstart.md        # Phase 1 output (below)
├── contracts/           # N/A - CLI app, no API contracts
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task data class
├── cli/
│   ├── __init__.py
│   ├── menu.py          # Menu display and input handling
│   ├── operations.py    # Task operations (CRUD)
│   └── app.py           # Main application entry point
└── __init__.py

tests/
├── unit/
│   ├── test_task.py
│   ├── test_operations.py
│   └── test_menu.py
└── __init__.py
```

**Structure Decision**: Single Python project with clear separation between `models/` (data) and `cli/` (presentation/operations). Tests mirror source structure.

## Data Model

### Task Entity

```python
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

@dataclass
class Task:
    id: int
    text: str
    status: TaskStatus
    created_at: datetime  # Optional in Phase I, for future use
```

### Storage

```python
# Global task registry (in-memory)
tasks: dict[int, Task] = {}  # id -> Task mapping for O(1) lookups
next_id: int = 1  # Auto-incrementing ID counter
```

### ID Generation Strategy

- Sequential integers starting from 1
- Increment `next_id` after each successful add
- Never reuse IDs (IDs remain stable for session lifetime)
- Simple counter variable, no complex ID generation needed

## CLI Control Flow

### Main Menu Loop

```
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit

Enter choice (1-7):
```

### Input Handling Pattern

```python
def get_menu_choice(prompt: str, valid_choices: list[str]) -> str:
    """Get validated menu choice from user."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter: {', '.join(valid_choices)}")
```

### Task ID Input Pattern

```python
def get_task_id(prompt: str) -> int | None:
    """Get and validate task ID from user."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                return None  # User cancelled
            task_id = int(user_input)
            if task_id <= 0:
                print("ID must be a positive number.")
                continue
            return task_id
        except ValueError:
            print("Please enter a valid number.")
```

### Task Text Input Pattern

```python
def get_task_text() -> str | None:
    """Get task text with validation."""
    while True:
        text = input("Enter task: ").strip()
        if not text:
            print("Task cannot be empty. Please enter some text.")
            continue
        return text
```

## Separation of Responsibilities

### models/task.py
- Pure data container
- No business logic
- No I/O operations
- Type validation only

### cli/operations.py
- Task CRUD operations
- Business logic for task management
- Works with in-memory storage
- Returns results, no I/O

### cli/menu.py
- Display functions (print statements)
- Input collection and validation
- Error message presentation
- Calls operations.py functions

### cli/app.py
- Application lifecycle
- Menu loop orchestration
- Exit handling

## Error Handling Strategy

### Error Types and Responses

| Error Condition | User Message | Behavior |
|-----------------|--------------|----------|
| Invalid menu choice | "Invalid choice. Please enter 1-7." | Re-prompt |
| Non-numeric ID | "Please enter a valid number." | Re-prompt |
| Negative/zero ID | "ID must be a positive number." | Re-prompt |
| Task ID not found | "Task with ID X not found." | Return to menu |
| Empty task text | "Task cannot be empty." | Re-prompt |
| Empty task list (view) | "Your task list is empty." | Inform, return |
| Empty task list (update/delete) | "No tasks to update/delete." | Return to menu |

### Exception Handling

```python
try:
    # Operation that might fail
except ValueError as e:
    print(f"Invalid input: {e}")
except KeyError as e:
    print(f"Task not found: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

All errors are caught at CLI layer and presented as user-friendly messages. No stack traces exposed to users.

## Quickstart

### Running the Application

```bash
# From repository root
python -m src.cli.app

# Or
cd src
python cli/app.py
```

### First Use

1. Run the application
2. Select option 1 to add your first task
3. Tasks persist in memory for the session
4. Data is lost when application exits

### Testing

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python -m unittest tests.unit.test_task
```

## Complexity Tracking

> No Constitution Check violations requiring justification. Design follows all principles with minimal complexity appropriate for Phase I scope.

---

## Research Notes

No Phase 0 research needed. All technical decisions are straightforward Python patterns with no external dependencies or clarifications required.

- CLI input validation: Standard Python input() with while loops
- In-memory storage: Native Python dict for O(1) operations
- Data classes: Python dataclasses (3.7+)
- No external dependencies needed
