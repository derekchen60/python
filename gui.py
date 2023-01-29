import PySimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo",key ='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key = 'todos', enable_events = True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App', layout=[[label,input_box, add_button],[list_box,edit_button]], font=('Helvetica', 20))

#Different keys are declared, input_box has the key of "todo" while the list_box has the key of "todos"
#We split the output of window.read() into 2 seperate variables, the event and the values. The 'event' variable
#will contain the action that was done and the 'values' variable will contain a dictionary of both the input_box
#and the list_box. Below are dictionaries of 'values'.

#Output when adding a new todo: {'todo': 'asdasd', 'todos': ['\n']}
#Output selecting in list_box: {'todo': '', 'todos': ['test2\n']}

#We can then specify the specific key that we are looking for inside of values. For example
#when we are doing (values['todo']) we are looking for the text being entered in the
#input_box.

while True:
    event,values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = (values['todo']) + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)

        window['todos'].update(values=todos)

    elif event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)

        todos[index] = new_todo + "\n"
        functions.write_todos(todos)

        #Allow the window to update in real time using "mother" window box
        #Updates the "values" which holds 
        window['todos'].update(values=todos)
    
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == sg.WIN_CLOSED:
        break

window.close()