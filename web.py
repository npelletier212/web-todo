import streamlit as st
from Modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo.title())
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This page is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a To-Do: ", placeholder="Add a new To-Do...",
              on_change=add_todo, key='new_todo')
