# Data Model: Phase I - CLI Todo

## Task Entity

### Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | int | positive, unique, auto-increment | Unique identifier for the task |
| `text` | str | non-empty, trimmed (max length TBD) | Task description |
| `status` | TaskStatus | enum: pending/completed | Current state of the task |
| `created_at` | datetime | auto-set on creation | Timestamp of task creation |

### TaskStatus Enum

```python
class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
```

## Storage Structure

```python
# Global in-memory storage
tasks: dict[int, Task] = {}  # id -> Task mapping
next_id: int = 1  # Counter for next task ID
```

## Validation Rules

### Task Creation
- `id`: Assigned automatically (1-based counter)
- `text`: Must be non-empty after stripping whitespace
- `status`: Defaults to PENDING
- `created_at`: Auto-generated with current datetime

### Task Update
- `id`: Must exist in tasks dictionary
- `text`: Must be non-empty after stripping whitespace

### State Transitions

```
PENDING <--> COMPLETED
```

Both directions are allowed:
- Mark Complete: PENDING → COMPLETED
- Mark Incomplete: COMPLETED → PENDING

Idempotent operations allowed:
- Marking complete when already complete: no change
- Marking incomplete when already pending: no change
