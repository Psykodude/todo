import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)




st.title("My Todo Appp")
st.subheader("This is my to do app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="add/edit Todo", placeholder="", on_change=add_todo, key='new_todo')