# 📝 Python Task Manager

A simple command-line task management application built with Python.  
Supports adding, viewing, searching, and managing tasks with persistent storage using a JSON file.


## 📦 Features

1. ➕ Add Task
    - Add a new task with a title, description, and due date (format: YYYY-MM-DD)
    - Each task gets a unique ID

2. 📋 View All Tasks
    - Tasks are shown in two sections: Pending and Completed

3. ✅ Mark Task as Completed
    - Input the task ID to mark as done

4. 🗑️ Delete Task
    - Remove any task by entering its ID

5. 💾 Save & Load Automatically
    - All tasks are saved to a tasks.json file and loaded every time you run the program

6. 🔍 Search Tasks
    - Search by keyword in title/description or by due date

## ⚙️ Installation

Clone this repository
```bash
git clone https://github.com/Supakorn-suri/python-task-manager.git
cd python-task-manager
```
## ▶️ How to Run
You can run the program either in the terminal or through Visual Studio Code.
```bash
python3 task_manager.py
```
If your system uses python instead of python3, use:
```bash
python task_manager.py
```

## 💡 Sample Usage
If the program runs successfully, you will see a menu like this in the terminal.
Simply type the number of the option you want to use.
```bash
--------------------------------------------
📌 Menu
1. Add a new task
2. View all tasks
3. Mark task as completed
4. Delete a task
5. Search tasks
6. Exit
Select an option (1–6):
```

📁 Example File
```bash
tasks.example.json
```
