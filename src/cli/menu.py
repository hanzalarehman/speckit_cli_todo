"""
Menu and input handling for the CLI todo application.
"""
from typing import List, Optional
from src.models.task import Task, TaskStatus
from src.cli.operations import (
    add_task, list_tasks, update_task, delete_task, 
    mark_complete, mark_incomplete
)


def get_task_text() -> str:
    """
    Get task text with validation.
    
    Returns:
        The validated task text
        
    Raises:
        ValueError: If the input is empty after stripping whitespace
    """
    while True:
        text = input("Enter task: ").strip()
        if not text:
            print("Task cannot be empty. Please enter some text.")
            continue
        return text


def get_task_id(prompt: str = "Enter task ID: ") -> int:
    """
    Get and validate task ID from user.
    
    Args:
        prompt: The prompt to display to the user
        
    Returns:
        The validated task ID
        
    Raises:
        ValueError: If the input is not a positive integer
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Task ID cannot be empty")
            task_id = int(user_input)
            if task_id <= 0:
                print("ID must be a positive number.")
                continue
            return task_id
        except ValueError as e:
            if "Task ID cannot be empty" in str(e):
                raise e
            print("Please enter a valid number.")


def get_menu_choice(prompt: str, valid_choices: List[str]) -> str:
    """
    Get validated menu choice from user.
    
    Args:
        prompt: The prompt to display to the user
        valid_choices: List of valid choices
        
    Returns:
        The validated choice
    """
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter: {', '.join(valid_choices)}")


def display_tasks():
    """Display all tasks in a formatted list."""
    all_tasks = list_tasks()
    
    if not all_tasks:
        print("\nYour task list is empty.")
        return
    
    print("\n--- TASK LIST ---")
    for task in all_tasks:
        status_symbol = "✓" if task.status == TaskStatus.COMPLETED else "○"
        print(f"{task.id}. [{status_symbol}] {task.text}")
    print("-----------------")


def add_task_menu():
    """Handle the add task menu option."""
    try:
        text = get_task_text()
        task = add_task(text)
        print(f"Task added successfully with ID {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def update_task_menu():
    """Handle the update task menu option."""
    try:
        task_id = get_task_id("Enter task ID to update: ")
        text = get_task_text()
        updated_task = update_task(task_id, text)
        print(f"Task {updated_task.id} updated successfully")
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task_menu():
    """Handle the delete task menu option."""
    try:
        task_id = get_task_id("Enter task ID to delete: ")
        deleted_task = delete_task(task_id)
        print(f"Task {deleted_task.id} deleted successfully")
    except KeyError as e:
        print(f"Error: {e}")


def mark_complete_menu():
    """Handle the mark complete menu option."""
    try:
        task_id = get_task_id("Enter task ID to mark complete: ")
        completed_task = mark_complete(task_id)
        print(f"Task {completed_task.id} marked as complete")
    except KeyError as e:
        print(f"Error: {e}")


def mark_incomplete_menu():
    """Handle the mark incomplete menu option."""
    try:
        task_id = get_task_id("Enter task ID to mark incomplete: ")
        incomplete_task = mark_incomplete(task_id)
        print(f"Task {incomplete_task.id} marked as incomplete")
    except KeyError as e:
        print(f"Error: {e}")


def display_menu():
    """Display the main menu options."""
    print("\n=== TODO APPLICATION ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Mark Incomplete")
    print("7. Exit")
    print()


def get_user_choice():
    """Get the user's menu choice."""
    return get_menu_choice("Enter choice (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])