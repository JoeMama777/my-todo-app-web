import streamlit as st
import todo_functions

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    todo_functions.write_current_list(todos)

todos = todo_functions.get_numbered_task_list()


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todo_functions.write_current_list(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add new todo", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

print("Hello ")

st.session_state