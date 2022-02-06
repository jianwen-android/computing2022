import PySimpleGUI as sg


def windowSetup(btnSz, imgSz):
    sg.theme('DarkBrown4')
    imgSrc = "../assets/placeholder2.png"

    buttonCol = [[sg.Button(button_text="Start", key="_START_", size=btnSz)],
                 [sg.Button(button_text="Stop", key="_STOP_", size=btnSz)],
                 [sg.Button(button_text="Calibrate", key="_CALIBRATE_", size=btnSz)],
                 ]

    col2 = [[sg.Image(source=imgSrc, size=imgSz, key="signImg")]
            ]

    layout = [[sg.Column(buttonCol, element_justification='c'), sg.Column(col2, element_justification="center")],
              [sg.Text(text="This is the output message", key="outputText", justification="center")]
              ]
    return sg.Window('Cripple enabler', layout, default_element_size=(45, 1))
