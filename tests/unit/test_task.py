import unittest
from datetime import datetime
from src.models.task import Task, TaskStatus


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        """Test that a Task can be created with required fields."""
        task_id = 1
        task_text = "Sample task"
        task_status = TaskStatus.PENDING
        created_at = datetime.now()
        
        task = Task(
            id=task_id,
            text=task_text,
            status=task_status,
            created_at=created_at
        )
        
        self.assertEqual(task.id, task_id)
        self.assertEqual(task.text, task_text)
        self.assertEqual(task.status, task_status)
        self.assertEqual(task.created_at, created_at)

    def test_task_equality(self):
        """Test that tasks with same attributes are considered equal."""
        created_at = datetime.now()
        
        task1 = Task(
            id=1,
            text="Sample task",
            status=TaskStatus.PENDING,
            created_at=created_at
        )
        
        task2 = Task(
            id=1,
            text="Sample task",
            status=TaskStatus.PENDING,
            created_at=created_at
        )
        
        self.assertEqual(task1, task2)


if __name__ == '__main__':
    unittest.main()