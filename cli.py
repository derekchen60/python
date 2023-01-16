#change
import functions
while True:
    user_input = input("Type add or show or edit or complete or exit: ")

    if user_input.startswith(('add','new')):
        if len(user_input) > 3 and user_input.startswith(('add', 'new')):

            modified_user_input = user_input[4:]
            todos = functions.get_todos()

            todos.append(modified_user_input + "\n")

            functions.write_todos()
        else:
            todo = input("Enter a todo: ")

            todos = functions.get_todos()

            todos.append(todo + "\n")

            functions.write_todos()

    elif user_input.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            print(f"{index+1}.{item}")

    elif user_input.startswith('edit'):
        try:
            if len(user_input) > 4 and user_input.startswith('edit'):
                todos = functions.get_todos()

                choice = int(user_input[5:])
                edit = input("Type new string: ")
                todos[choice - 1] = edit + "\n"

                functions.write_todos()
            else:
                todos = functions.get_todos()

                choice = int(input("Enter choice: "))
                edit = input("Type new string: ")
                todos[choice - 1] = edit + "\n"

                functions.write_todos()

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_input.startswith('complete'):
        user_input = int(input("Number of the todo to complete: "))

        todos = functions.get_todos()

        functions.write_todos()

    elif user_input.startswith('exit'):
        break

    else:
        print("Command not valid")