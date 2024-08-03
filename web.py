import streamlit as st
import functions

st.title("Todo App")
st.subheader("This could be a good todo app fr")
st.write("This app is to increase your productivity")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo..")
