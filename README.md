# Todo List

This is a practice project for implementing a Todo List web application using Django. The application allows users to manage tasks with support for tagging, sorting, and status toggling.

## Project Overview

The Todo List application includes the following features:

- **Task Management**: Create, update, and delete tasks.
- **Tagging**: Assign and view tags associated with tasks.
- **Sorting**: View tasks ordered by completion status and creation date.
- **Task Status Toggle**: Change task status between "complete" and "not done."

## Models

### Task

Each task has the following fields:

- **content**: Description of the task.
- **datetime**: Timestamp when the task was created.
- **deadline**: Optional deadline for the task.
- **done**: Boolean field indicating if the task is complete or not.
- **tags**: Many-to-many relationship with tags.

### Tag

A tag includes:

- **name**: The name of the tag.

A tag can be associated with multiple tasks, and a task can have multiple tags.

## Installation

### Prerequisites

- Python 3.13 or higher
- Django 5.1.3# todo_list

## Skrinshots

TODO list

![Todo list](https://github.com/Viacheslav417865/todo_list/blob/dev/todolist/tasks/templates/static/skrinshot/Todo%20list.png?raw=true)


Tags

![Tags](https://github.com/Viacheslav417865/todo_list/blob/dev/todolist/tasks/templates/static/skrinshot/Tags.png)


