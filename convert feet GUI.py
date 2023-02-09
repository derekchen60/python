import PySimpleGUI as sg
label = sg.Text("Enter feet:")
label2 = sg.Text("Enter inches:")

feet_box = sg.InputText(key ='feet')
inches_box = sg.InputText(key ='inches')
convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

result_text = sg.Text(key = 'result')

window = sg.Window('Convertor', layout=[[label,feet_box],[label2,inches_box],[convert_button,result_text,exit_button]])

while True:
    button,values = window.read()
    #print(button)
    #print(values)

    if button == 'Convert':
        feet = int(values['feet'])
        inches = int(values['inches'])

        metre1 = feet * 0.3048
        metre2 = inches * 0.0254

        result = metre1 + metre2

        window['result'].update(result)

    elif button == sg.WIN_CLOSED:
        break
    elif button == 'Exit':
        break

window.close()
