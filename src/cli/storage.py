"""
In-memory storage for tasks.
"""
from typing import Dict
from src.models.task import Task

# Global in-memory storage
tasks: Dict[int, Task] = {}  # id -> Task mapping
next_id: int = 1  # Counter for next task ID