import functions
import PySimpleGUI as Sg

Sg.theme("green")

label = Sg.Text("Type in a To-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add", mouseover_colors="Green", tooltip="Add todo")
list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(44, 10))
edit_button = Sg.Button("Edit", mouseover_colors="Grey", tooltip="Edit todo")
complete_button = Sg.Button("Complete", mouseover_colors="Grey", tooltip="Remove todo")
exit_button = Sg.Button("Exit", mouseover_colors="Red")

window = Sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            if new_todo == "":
                Sg.popup("Please type a todo.", font=("Helvetica", 10))
                continue
            if new_todo.endswith("\n") is False:
                new_todo = values['todo'] + "\n"
            if new_todo in todos:
                Sg.popup("Todo already exists!", font=("Helvetica", 10))
                continue
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                edit_todo = values['todos'][0]
                new_todo = values['todo']
                if new_todo.endswith("\n") is False:
                    new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item first!",
                         font=("Helvetica", 10))
        case "todos":
            window['todo'].update(value=values['todos'][0].strip("\n"))
        case "Complete":
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                Sg.popup("Please select an item first!",
                         font=("Helvetica", 10))
        case "Exit":
            break
        case Sg.WIN_CLOSED:
            break

window.close()
