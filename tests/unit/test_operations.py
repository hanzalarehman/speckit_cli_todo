import unittest
from datetime import datetime
from src.models.task import Task, TaskStatus
from src.cli.storage import tasks, next_id


class TestOperations(unittest.TestCase):
    def setUp(self):
        """Reset storage before each test."""
        tasks.clear()
        # Note: We can't easily reset next_id in this test setup

    def test_add_task_creates_task_with_pending_status(self):
        """Test that add_task creates a task with pending status."""
        from src.cli.operations import add_task
        
        task_text = "New task"
        result = add_task(task_text)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.text, task_text)
        self.assertEqual(result.status, TaskStatus.PENDING)
        self.assertIn(result.id, tasks)
        self.assertEqual(tasks[result.id].text, task_text)

    def test_add_task_rejects_empty_text(self):
        """Test that add_task rejects empty text."""
        from src.cli.operations import add_task
        
        with self.assertRaises(ValueError):
            add_task("")
        
        with self.assertRaises(ValueError):
            add_task("   ")  # whitespace-only text

    def test_add_task_assigns_unique_id(self):
        """Test that add_task assigns unique IDs."""
        from src.cli.operations import add_task
        
        task1 = add_task("First task")
        task2 = add_task("Second task")
        
        self.assertNotEqual(task1.id, task2.id)
        self.assertEqual(task2.id, task1.id + 1)  # Assuming sequential IDs

    def test_view_tasks_returns_all_tasks(self):
        """Test that view_tasks returns all tasks."""
        from src.cli.operations import add_task, list_tasks
        
        task1 = add_task("First task")
        task2 = add_task("Second task")
        
        all_tasks = list_tasks()
        
        self.assertEqual(len(all_tasks), 2)
        self.assertIn(task1, all_tasks)
        self.assertIn(task2, all_tasks)

    def test_view_tasks_shows_empty_message_when_no_tasks(self):
        """Test that view_tasks shows empty message when no tasks."""
        from src.cli.operations import list_tasks
        
        all_tasks = list_tasks()
        
        self.assertEqual(len(all_tasks), 0)

    def test_update_task_changes_text(self):
        """Test that update_task changes text."""
        from src.cli.operations import add_task, update_task
        
        original_task = add_task("Original task")
        updated_task = update_task(original_task.id, "Updated task")
        
        self.assertEqual(updated_task.text, "Updated task")
        self.assertEqual(tasks[original_task.id].text, "Updated task")

    def test_update_task_rejects_empty_text(self):
        """Test that update_task rejects empty text."""
        from src.cli.operations import add_task, update_task
        
        task = add_task("Original task")
        
        with self.assertRaises(ValueError):
            update_task(task.id, "")
        
        with self.assertRaises(ValueError):
            update_task(task.id, "   ")  # whitespace-only text

    def test_update_task_raises_error_for_non_existent_id(self):
        """Test that update_task raises error for non-existent ID."""
        from src.cli.operations import update_task
        
        with self.assertRaises(KeyError):
            update_task(999, "New text")

    def test_delete_task_removes_task(self):
        """Test that delete_task removes task."""
        from src.cli.operations import add_task, delete_task, list_tasks
        
        task = add_task("Task to delete")
        self.assertIn(task.id, tasks)
        
        deleted_task = delete_task(task.id)
        
        self.assertEqual(deleted_task, task)
        self.assertNotIn(task.id, tasks)
        
        remaining_tasks = list_tasks()
        self.assertNotIn(task, remaining_tasks)

    def test_delete_task_raises_error_for_non_existent_id(self):
        """Test that delete_task raises error for non-existent ID."""
        from src.cli.operations import delete_task
        
        with self.assertRaises(KeyError):
            delete_task(999)

    def test_mark_complete_changes_status_to_completed(self):
        """Test that mark_complete changes status to completed."""
        from src.cli.operations import add_task, mark_complete
        
        task = add_task("Pending task")
        self.assertEqual(task.status, TaskStatus.PENDING)
        
        completed_task = mark_complete(task.id)
        
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)
        self.assertEqual(tasks[task.id].status, TaskStatus.COMPLETED)

    def test_mark_complete_is_idempotent(self):
        """Test that mark_complete is idempotent."""
        from src.cli.operations import add_task, mark_complete
        
        task = add_task("Completed task")
        mark_complete(task.id)  # First call
        completed_task = mark_complete(task.id)  # Second call
        
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)

    def test_mark_incomplete_changes_status_to_pending(self):
        """Test that mark_incomplete changes status to pending."""
        from src.cli.operations import add_task, mark_complete, mark_incomplete
        
        task = add_task("Task to complete")
        completed_task = mark_complete(task.id)
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)
        
        incomplete_task = mark_incomplete(task.id)
        
        self.assertEqual(incomplete_task.status, TaskStatus.PENDING)
        self.assertEqual(tasks[task.id].status, TaskStatus.PENDING)

    def test_mark_incomplete_is_idempotent(self):
        """Test that mark_incomplete is idempotent."""
        from src.cli.operations import add_task, mark_incomplete
        
        task = add_task("Pending task")
        incomplete_task = mark_incomplete(task.id)  # This should have no effect since it's already pending
        
        self.assertEqual(incomplete_task.status, TaskStatus.PENDING)


if __name__ == '__main__':
    unittest.main()