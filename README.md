# python-task-manager
Practical Software Engineering Final Project

Project Requirements:
1. Python Task Manager Application:
    - The application should allow users to manage daily tasks with the following functionality:
        - Add New Task: Users can add tasks with a title, description, and a due date. Each task should be assigned a unique ID.
        - View All Tasks: Display all tasks in a structured format. Separate tasks into pending and completed categories.
        - Mark Task as Complete: Provide a feature that allows users to mark tasks as completed by referencing the task's unique ID.
        - Delete Task: Users can delete tasks by their unique ID.
        - Save and Load Tasks: All tasks should be saved to a JSON file and loaded when the program starts.
        - Search Tasks: Add a function to search tasks by keywords or due date.
    - The program should have a command-line interface (CLI) for user interaction. The CLI should include:
        - A menu that displays available options (e.g., add task, view tasks, mark as complete, delete task, search tasks, exit).
        - Input validation to ensure proper task entry (e.g., no empty titles or invalid dates).