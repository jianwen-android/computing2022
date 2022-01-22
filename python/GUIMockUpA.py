import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color

images = ["../assets/signL2.png", "../assets/signA2.png", "../assets/signB2.png", "../assets/signG2.png"]
count = 0


# All the stuff inside your window.

def updateImg(src=None):
    window["signImg"].update(source=images[count % 4], size=imgSz)


btnSz = (20, 3)
imgSz = (530, 550)
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

# Create the Window
window = sg.Window('Cripple enabler', layout, default_element_size=(45, 1))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    elif event == "_START_":
        print("Start")
        # run start()
        count += 1
        updateImg()
    elif event == "_STOP_":
        print("Stop")
        # run stop()
    elif event == "_CALIBRATE_":
        print("Calibrate")
        # run calibrate()

window.close()
