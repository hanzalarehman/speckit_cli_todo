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
    created_at: datetime