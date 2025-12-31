import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.models.task import Task, TaskStatus
from src.cli.menu import display_tasks


class TestMenu(unittest.TestCase):
    @patch('src.cli.menu.list_tasks')
    def test_display_tasks_shows_empty_message_when_no_tasks(self, mock_list_tasks):
        """Test that display_tasks shows empty message when no tasks."""
        mock_list_tasks.return_value = []
        
        # Capture the print output
        with patch('builtins.print') as mock_print:
            display_tasks()
            mock_print.assert_called_with("\nYour task list is empty.")
    
    @patch('src.cli.menu.list_tasks')
    def test_display_tasks_shows_tasks_when_tasks_exist(self, mock_list_tasks):
        """Test that display_tasks shows tasks when tasks exist."""
        task = Task(
            id=1,
            text="Sample task",
            status=TaskStatus.PENDING,
            created_at=datetime.now()
        )
        mock_list_tasks.return_value = [task]
        
        # Capture the print output
        with patch('builtins.print') as mock_print:
            display_tasks()
            # Check that the task was displayed with the correct format
            # We expect at least the header and the task to be printed
            self.assertTrue(any("1. [○] Sample task" in str(call) for call in mock_print.call_args_list))

    @patch('src.cli.menu.get_task_text')
    @patch('src.cli.menu.add_task')
    def test_add_task_menu_calls_add_task_and_prints_success(self, mock_add_task, mock_get_task_text):
        """Test that add_task_menu calls add_task and prints success message."""
        from src.cli.menu import add_task_menu
        mock_get_task_text.return_value = "New test task"
        mock_add_task.return_value = Task(id=1, text="New test task", status=TaskStatus.PENDING, created_at=datetime.now())

        with patch('builtins.print') as mock_print:
            add_task_menu()
            mock_add_task.assert_called_once_with("New test task")
            mock_print.assert_called_with("Task added successfully with ID 1")

    @patch('src.cli.menu.get_task_id')
    @patch('src.cli.menu.get_task_text')
    @patch('src.cli.menu.update_task')
    def test_update_task_menu_calls_update_task_and_prints_success(self, mock_update_task, mock_get_task_text, mock_get_task_id):
        """Test that update_task_menu calls update_task and prints success message."""
        from src.cli.menu import update_task_menu
        mock_get_task_id.return_value = 1
        mock_get_task_text.return_value = "Updated test task"
        mock_update_task.return_value = Task(id=1, text="Updated test task", status=TaskStatus.PENDING, created_at=datetime.now())

        with patch('builtins.print') as mock_print:
            update_task_menu()
            mock_update_task.assert_called_once_with(1, "Updated test task")
            mock_print.assert_called_with("Task 1 updated successfully")

    @patch('src.cli.menu.get_task_id')
    @patch('src.cli.menu.delete_task')
    def test_delete_task_menu_calls_delete_task_and_prints_success(self, mock_delete_task, mock_get_task_id):
        """Test that delete_task_menu calls delete_task and prints success message."""
        from src.cli.menu import delete_task_menu
        mock_get_task_id.return_value = 1
        mock_delete_task.return_value = Task(id=1, text="Task to delete", status=TaskStatus.PENDING, created_at=datetime.now())

        with patch('builtins.print') as mock_print:
            delete_task_menu()
            mock_delete_task.assert_called_once_with(1)
            mock_print.assert_called_with("Task 1 deleted successfully")

    @patch('src.cli.menu.get_task_id')
    @patch('src.cli.menu.mark_complete')
    def test_mark_complete_menu_calls_mark_complete_and_prints_success(self, mock_mark_complete, mock_get_task_id):
        """Test that mark_complete_menu calls mark_complete and prints success message."""
        from src.cli.menu import mark_complete_menu
        mock_get_task_id.return_value = 1
        mock_mark_complete.return_value = Task(id=1, text="Task to complete", status=TaskStatus.COMPLETED, created_at=datetime.now())

        with patch('builtins.print') as mock_print:
            mark_complete_menu()
            mock_mark_complete.assert_called_once_with(1)
            mock_print.assert_called_with("Task 1 marked as complete")

    @patch('src.cli.menu.get_task_id')
    @patch('src.cli.menu.mark_incomplete')
    def test_mark_incomplete_menu_calls_mark_incomplete_and_prints_success(self, mock_mark_incomplete, mock_get_task_id):
        """Test that mark_incomplete_menu calls mark_incomplete and prints success message."""
        from src.cli.menu import mark_incomplete_menu
        mock_get_task_id.return_value = 1
        mock_mark_incomplete.return_value = Task(id=1, text="Task to mark incomplete", status=TaskStatus.PENDING, created_at=datetime.now())

        with patch('builtins.print') as mock_print:
            mark_incomplete_menu()
            mock_mark_incomplete.assert_called_once_with(1)
            mock_print.assert_called_with("Task 1 marked as incomplete")

    @patch('builtins.input', side_effect=['invalid', '1'])
    @patch('builtins.print')
    def test_get_menu_choice_validates_input(self, mock_print, mock_input):
        """Test that get_menu_choice validates user input."""
        from src.cli.menu import get_menu_choice
        valid_choices = ['1', '2']
        prompt = "Enter choice: "
        choice = get_menu_choice(prompt, valid_choices)
        self.assertEqual(choice, '1')
        mock_print.assert_called_with(f"Invalid choice. Please enter: {', '.join(valid_choices)}")

    @patch('src.cli.menu.get_task_id', side_effect=KeyError("Task with ID 999 not found"))
    @patch('builtins.print')
    def test_update_task_menu_handles_key_error(self, mock_print, mock_get_task_id):
        """Test that update_task_menu handles KeyError and prints an error message."""
        from src.cli.menu import update_task_menu
        update_task_menu()
        mock_print.assert_called_with("Error: 'Task with ID 999 not found'")


if __name__ == '__main__':
    unittest.main()