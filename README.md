# Task Manager CLI App 📝

This is a simple command-line application written in Python for managing your daily tasks.  
It uses a JSON file to store the tasks persistently.

https://roadmap.sh/projects/task-tracker

## Features

- Add a task
- List tasks
- Mark tasks as done
- Update a task
- Delete a task

## How It Works

- The app stores tasks in a `tasks.json` file.
- When the program runs, if the `tasks.json` file does **not** exist, it will be created automatically.
- If the file is empty, it will be initialized with an empty list.
- Any new task added will be saved into this JSON file.
- Tasks are saved with the following properties:
  - `id`: a unique number for each task
  - `title`: the task description
  - `done`: whether the task is completed or not

## Usage

Just run the Python script:

```bash
python main.py


