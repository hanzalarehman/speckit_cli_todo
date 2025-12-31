"""
Main application entry point for the CLI todo application.
"""
from src.cli.menu import (
    display_menu, get_user_choice, display_tasks, 
    add_task_menu, update_task_menu, delete_task_menu,
    mark_complete_menu, mark_incomplete_menu
)


def main():
    """Main application loop."""
    print("Welcome to the CLI Todo Application!")
    
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            if choice == "1":
                add_task_menu()
            elif choice == "2":
                display_tasks()
            elif choice == "3":
                update_task_menu()
            elif choice == "4":
                delete_task_menu()
            elif choice == "5":
                mark_complete_menu()
            elif choice == "6":
                mark_incomplete_menu()
            elif choice == "7":
                print("Thank you for using the CLI Todo Application. Goodbye!")
                break
            else:
                # This shouldn't happen due to validation in get_user_choice
                print("Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()