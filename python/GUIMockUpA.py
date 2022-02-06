import threading
import time
import serial
import PySimpleGUI as sg

from src import tfFunc, guiFunc, arduinoFunc

# Do setup
model, px = tfFunc.setupModel()
# arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
# tfFunc.modelPredict(model,px)

images = ["../assets/signA2.png", "../assets/signB2.png", "C", "D", "E", "F", "../assets/signG2.png", "H",
          "../assets/signI2.png",
          "K", "../assets/signL2.png", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y"]
'''
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "W", "X", "Y"]'''
isReceiving = False
imgSz = (530, 550)
btnSz = (20, 3)


# All the stuff inside your window.

def retrieveData():
    # retrieveData
    # i = tfFunc.modelPredict(model, arduinoFunc.readData(arduino))
    while isReceiving:
        i = tfFunc.modelPredict(model, px)
        updateImg(images[i])

    '''print('wenis')
    count = 0
    while isReceiving:
        print('in loop')
        time.sleep(1)
        count += 1
        updateImg(images[count % 5])'''


def updateImg(src=None):
    window["signImg"].update(source=src, size=imgSz)


def updateText(text="Placeholder text"):
    window["outputText"].update(text)


# Create the Window
window = guiFunc.windowSetup(btnSz, imgSz)

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
