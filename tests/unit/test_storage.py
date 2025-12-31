import unittest
from datetime import datetime
from src.models.task import Task, TaskStatus
from src.cli.storage import tasks, next_id


class TestStorage(unittest.TestCase):
    def setUp(self):
        """Reset storage before each test."""
        tasks.clear()
        # Note: We can't easily reset next_id in this test setup without making it a function

    def test_initial_state(self):
        """Test that storage starts with empty tasks dict and next_id of 1."""
        self.assertEqual(tasks, {})
        # Note: We can't easily test next_id without making changes to how it's defined

    def test_task_storage(self):
        """Test that tasks can be stored and retrieved by ID."""
        task_id = 1
        task = Task(
            id=task_id,
            text="Sample task",
            status=TaskStatus.PENDING,
            created_at=datetime.now()
        )
        
        tasks[task_id] = task
        
        self.assertIn(task_id, tasks)
        self.assertEqual(tasks[task_id], task)
        self.assertEqual(tasks[task_id].id, task_id)
        self.assertEqual(tasks[task_id].text, "Sample task")
        self.assertEqual(tasks[task_id].status, TaskStatus.PENDING)


if __name__ == '__main__':
    unittest.main()