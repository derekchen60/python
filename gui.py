import PySimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

sg.theme("Black")

label_clock = sg.Text('', key = 'clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo",key ='todo')
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", 
tooltip = "Add Todo", key="Add")                       
list_box = sg.Listbox(values = functions.get_todos(), key = 'todos', enable_events = True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App', layout=[[label_clock],[label,input_box,add_button],[list_box,edit_button,complete_button],[exit_button]], font=('Helvetica', 20))

#Different keys are declared, input_box has the key of "todo" while the list_box has the key of "todos"
#We split the output of window.read() into 2 seperate variables, the event and the values. The 'event' variable
#will contain the action that was done and the 'values' variable will contain a dictionary of both the input_box
#and the list_box. Below are dictionaries of 'values'.

#Output of values when adding a new todo: {'todo': 'asdasd', 'todos': ['\n']}
#Output of values when selecting in list_box: {'todo': '', 'todos': ['test2\n']}

#We can then specify the specific key that we are looking for inside of values. For example
#when we are doing (values['todo']) we are looking for the text being entered in the
#input_box.

while True:
    #When applying a timeout, the loop runs every 10 seconds rather than
    #executing only when user does something
    event,values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = (values['todo']) + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)

        window['todos'].update(values=todos)

    elif event == "Edit":
        try: 
        #The reason why we use values['todos'][0] is because the output is: {'todo': '', 'todos': ['test2\n']}
        #We need to remove the the list from the ['test2\n'] since it's a list inside a dictionary to make it usable
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)

            todos[index] = new_todo + "\n"
            functions.write_todos(todos)

        #Allow the window to update in real time using "mother" window box
        #Updates the "values" which holds 
            window['todos'].update(values=todos)
        except IndexError:
            sg.Popup("Please select a todo")
    elif event == "Complete":
        todos = functions.get_todos()
        #Todo_index = todos.index(values['todos'])
        todos.remove(values['todos'][0])
        functions.write_todos(todos)

        #Update List box to remove todo item
        window['todos'].update(values=todos)
        #Update Input box to remove todo item 
        window['todo'].update(value='')

    #Update the input_box with the values from the list
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == 'Exit' or event == sg.WIN_CLOSED:
        break

window.close()

