import streamlit as st
import time
from pathlib import Path

# Constants
FILEPATH = Path('TO_do_simple.txt')
NEW_FILEPATH = Path('Previous_todo.txt')  # Fixed typo in variable name

# File Operations
def read_file(filepath: Path) -> list:
    """Read tasks from a file."""
    if filepath.exists():
        with open(filepath, 'r') as file:
            return [task.strip() for task in file.readlines() if task.strip()]
    return []

def write_file(filepath: Path, tasks: list) -> None:
    """Write tasks to a file."""
    with open(filepath, 'w') as file:
        file.write('\n'.join(tasks) + '\n')

# Task Operations
def add_task(task: str) -> None:
    """Add a new task to active tasks."""
    tasks = read_file(FILEPATH)
    tasks.append(task.strip())
    write_file(FILEPATH, tasks)

def delete_task(task: str) -> None:
    """Move task from active to completed tasks."""
    tasks = read_file(FILEPATH)
    if task in tasks:
        tasks.remove(task)
        write_file(FILEPATH, tasks)
        
        completed_tasks = read_file(NEW_FILEPATH)
        completed_tasks.append(f"{task} - completed on {time.strftime('%b/%d/%y')}")
        write_file(NEW_FILEPATH, completed_tasks)

# Streamlit UI
def main():
    st.set_page_config(page_title="To-Do App", page_icon="📝", layout='wide')
    st.title("Welcome to the To-Do App!")
    
    # Active Tasks Section
    st.subheader("Active Tasks")
    todos = read_file(FILEPATH)
    
    # Add new task
    def add_todo():
        if new_todo := st.session_state["new_todo"]:
            add_task(new_todo)
            st.session_state["new_todo"] = ""  # Clear input
            st.rerun()
    
    st.text_input(
        label="",
        placeholder="Add new todo",
        on_change=add_todo,
        key='new_todo'
    )
    
    # Display active tasks
    for todo in todos:
        if st.checkbox(todo, key=todo):
            delete_task(todo)
            st.rerun()
    
    # Completed Tasks Section
    st.subheader("Completed Tasks")
    completed_todos = read_file(NEW_FILEPATH)
    
    if completed_todos:
        for idx, task in enumerate(completed_todos, 1):
            st.write(f"{idx}. {task}")
    else:
        st.write("No completed tasks yet!")

if __name__ == "__main__":
    main()
