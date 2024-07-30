FILEPATH = "todos.txt"


def get_todos():
    with open(FILEPATH, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todo):
    with open(FILEPATH, "w") as file:
        for item in todo:
            file.write(item)
