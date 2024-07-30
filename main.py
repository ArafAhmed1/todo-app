import functions
import time
now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todos = functions.get_todos()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        functions.write_todos(todos)
        print(f"\"{todo[:-1]}\" has been added to your to-do list!")
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        if len(todos) == 0:
            print("Nothing to show!")
        else:
            print("To-do list:")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1}. {item}")
    elif user_action.startswith("complete"):
        todos = functions.get_todos()
        if user_action == "complete":
            print("You have to mention the number of to-do you have completed.")
            continue
        try:
            number = int(user_action[9:])
            if number > len(todos):
                print("please enter a valid number")
                continue
            completed = todos[number-1]
            todos.pop(number-1)
            functions.write_todos(todos)
            print(f"\"{completed[:-1]}\" has been removed from your to-do list!")
        except ValueError:
            print("Please enter a number followed by \"completed\"")
    elif user_action.startswith("edit"):
        todos = functions.get_todos()
        if user_action == "edit":
            print("You have to mention the number of to-do you want to edit.")
            continue
        try:
            number = int(user_action[5:])
            if number > len(todos):
                print("Please enter a valid number")
                continue
            new = input("What do you want the to-do to edit to? ") + "\n"
            todos[number-1] = new
            functions.write_todos(todos)
            print(f"Edit successful!")
        except ValueError:
            print("Please enter a number followed by \"edit\"")
    elif user_action == "exit":
        break
    else:
        print("Invalid command.")
