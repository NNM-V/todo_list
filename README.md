<div id="top"></div>

<!-- Shields -->
<p style="display: inline">
	<img alt="Static Badge" src="https://img.shields.io/badge/python-blue">
</p>

# To-Do List Application
GUI ToDo list application with python.

## Table of Contents
- About the Project
- Image
- Environment
- Directory
- How to Build
- How to Use

## About the Project
A GUI ToDo list application that allows users to manage tasks and mark tasks as completed.

## ScreenShots
<img width=50% alt="MainWindow" src="https://github.com/user-attachments/assets/95473161-be30-4269-a6af-c7ee4e71eb8d" />

<img width=50% alt="SubWindow" src="https://github.com/user-attachments/assets/6953a467-c8d1-4889-86f8-8e1c483f4078" />

## Environment
- Python 3.11
- tkinter
- JSON

## Directory
```text
.
├── json_manager.py
├── main_window.py
├── main.py
├── README.md
├── sub_window.py
```

## Installation (Linux/Mac)
1.Install Python.

2.Clone the repository to your local environment.

3.Move to the project directory in the terminal.

4.Build the program on your terminal with command below:
```bash
    python -m compileall  main.py
```

5.Run program with command below:
```bash
    python main.py  
```

## How to Use
1.Input task to "Input Task" bar and press "add" button. The task will be added to ToDo section.

2.Click task and press "complete" button to move the task to the completed list. Press "Select all" to move everything from the list.

3.Click task and press "delete" button to delete the task from the list. Press "Select all" to delete everything from the list.

4.Click "deselect" to deselect the task chosen.

5.Click "show completed" to show subwindow with completed list.

6.Click "clear" to delete tasks from completed list.

7.Click task and press "save" button to save the current task and completed task.