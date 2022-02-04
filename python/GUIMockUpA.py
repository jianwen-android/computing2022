import PySimpleGUI as sg
import threading
import time

#Do setup
images = ["../assets/signA2.png", "../assets/signB2.png", "../assets/signG2.png", "../assets/signI2.png",
          "../assets/signL2.png"]
isReceiving = False

# All the stuff inside your window.

def retrieveData():
    # retrieveData
    print('wenis')
    count = 0
    while isReceiving:
        print('in loop')
        time.sleep(1)
        count += 1
        updateImg(images[count % 4])


def updateImg(src=None):
    window["signImg"].update(source=src, size=imgSz)


def updateText(text="Placeholder text"):
    window["outputText"].update(text)


sg.theme('DarkBrown4')
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
    t1 = threading.Thread(target=retrieveData, args=())
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    elif event == "_START_":
        print("Start")
        isReceiving = True
        t1.start()
        # run start()

    elif event == "_STOP_":
        print("Stop")
        # run stop()
        isReceiving = False

    elif event == "_CALIBRATE_":
        print("Calibrate")
        # run calibrate()

window.close()
