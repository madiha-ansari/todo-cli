import streamlit as st
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

st.title("📝 Simple Todo List Manager")

tasks = load_tasks()

new_task = st.text_input("Add a new task:")
if st.button("➕ Add Task"):
    if new_task.strip():
        tasks.append({"task": new_task, "done": False})
        save_tasks(tasks)
        st.success(f"Task added: {new_task}")
        # st.experimental_rerun()

if tasks:
    for index, task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        
        with col1:
            st.write(f"{index + 1}. {task['task']} {'✅' if task['done'] else '❌'}")

        with col2:
            if st.button(f"✔️ Complete {index+1}"):
                tasks[index]["done"] = True
                save_tasks(tasks)
                st.experimental_rerun()

        with col3:
            if st.button(f"🗑️ Remove {index+1}"):
                del tasks[index]
                save_tasks(tasks)
                st.experimental_rerun()
else:
    st.write("No tasks found! 🎉")
