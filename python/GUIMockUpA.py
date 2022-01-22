import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

buttonCol = [[sg.Button(button_text="Start", key="_START_")],
             [sg.Button(button_text="Stop", key="_STOP_")],
             [sg.Button(button_text="Calibrate", key="_CALIBRATE_")],
             ]
col2 = [[sg.Image()]
        ]
layout = [  [sg.Column(buttonCol, element_justification='c')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
