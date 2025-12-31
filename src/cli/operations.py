"""
Task operations for the CLI todo application.
"""
from datetime import datetime
from typing import List, Optional
from src.models.task import Task, TaskStatus
from src.cli.storage import tasks, next_id


def add_task(text: str) -> Task:
    """
    Add a new task with the given text.
    
    Args:
        text: The text of the task to add
        
    Returns:
        The created Task object
        
    Raises:
        ValueError: If the text is empty or contains only whitespace
    """
    global next_id
    
    if not text or not text.strip():
        raise ValueError("Task text cannot be empty or contain only whitespace")
    
    task = Task(
        id=next_id,
        text=text.strip(),
        status=TaskStatus.PENDING,
        created_at=datetime.now()
    )
    
    tasks[next_id] = task
    next_id += 1
    
    return task


def list_tasks() -> List[Task]:
    """
    Return a list of all tasks, sorted by ID.
    
    Returns:
        List of all Task objects, sorted by ID
    """
    return sorted(tasks.values(), key=lambda t: t.id)


def update_task(task_id: int, new_text: str) -> Task:
    """
    Update the text of an existing task.
    
    Args:
        task_id: The ID of the task to update
        new_text: The new text for the task
        
    Returns:
        The updated Task object
        
    Raises:
        KeyError: If no task exists with the given ID
        ValueError: If the new text is empty or contains only whitespace
    """
    if not new_text or not new_text.strip():
        raise ValueError("Task text cannot be empty or contain only whitespace")
    
    if task_id not in tasks:
        raise KeyError(f"Task with ID {task_id} does not exist")
    
    task = tasks[task_id]
    updated_task = Task(
        id=task.id,
        text=new_text.strip(),
        status=task.status,
        created_at=task.created_at
    )
    
    tasks[task_id] = updated_task
    return updated_task


def delete_task(task_id: int) -> Task:
    """
    Delete a task by its ID.
    
    Args:
        task_id: The ID of the task to delete
        
    Returns:
        The deleted Task object
        
    Raises:
        KeyError: If no task exists with the given ID
    """
    if task_id not in tasks:
        raise KeyError(f"Task with ID {task_id} does not exist")
    
    return tasks.pop(task_id)


def mark_complete(task_id: int) -> Task:
    """
    Mark a task as complete.
    
    Args:
        task_id: The ID of the task to mark complete
        
    Returns:
        The updated Task object
        
    Raises:
        KeyError: If no task exists with the given ID
    """
    if task_id not in tasks:
        raise KeyError(f"Task with ID {task_id} does not exist")
    
    task = tasks[task_id]
    completed_task = Task(
        id=task.id,
        text=task.text,
        status=TaskStatus.COMPLETED,
        created_at=task.created_at
    )
    
    tasks[task_id] = completed_task
    return completed_task


def mark_incomplete(task_id: int) -> Task:
    """
    Mark a task as incomplete (pending).
    
    Args:
        task_id: The ID of the task to mark incomplete
        
    Returns:
        The updated Task object
        
    Raises:
        KeyError: If no task exists with the given ID
    """
    if task_id not in tasks:
        raise KeyError(f"Task with ID {task_id} does not exist")
    
    task = tasks[task_id]
    incomplete_task = Task(
        id=task.id,
        text=task.text,
        status=TaskStatus.PENDING,
        created_at=task.created_at
    )
    
    tasks[task_id] = incomplete_task
    return incomplete_task