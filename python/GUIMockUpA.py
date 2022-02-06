# The main file of the program

import threading  # Used for a separate flow of execution for processing, independent of gui
import serial  # Used to initialise a connection with arduino, from the glove
import PySimpleGUI as sg  # A simple gui library used to display information and start the program
import pandas as pd  # A data processing library used to format data to be passed into the learnt model

from src import tfFunc, guiFunc, arduinoFunc  # These are all functions separated by library for easier collation

# Do setup
model, px = tfFunc.setupModel()  # Setup model for prediction
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
arduinoFunc.arduinoSetup(arduino)  # Setup arduino connection

images = ["../assets/signA2.png", "../assets/signB2.png", "C", "D", "E", "F", "../assets/signG2.png", "H",
          "../assets/signI2.png",
          "K", "../assets/signL2.png", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y"]
'''
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "W", "X", "Y"]'''
isReceiving = False
imgSz = (530, 550)
btnSz = (20, 3)


# Functions
# ---

def startProcess():
    # The bulk of the program:
    # 1. Reads data from arduino
    # 2. Processes the data into a readable format to be passed into a trained model
    # 3. Updates the image after processing the data

    while isReceiving:
        x = arduinoFunc.readData(arduino)
        if x:  # if there is data
            x = x.split(',')
            df = pd.DataFrame([x], columns=['Pinky', 'Ring', 'Middle', 'Index', 'Thumb'], dtype=float)
            i = tfFunc.modelPredict(model, df)
            updateImg(images[i])


def updateImg(src=None):
    # Updates the image of the window to display the appropriate sign
    window["signImg"].update(source=src, size=imgSz)


def updateText(text="Placeholder text"):
    # Updates the text of the window to display the appropriate sign
    window["outputText"].update(text)


window = guiFunc.windowSetup(btnSz, imgSz)
# Create the Window


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    t1 = threading.Thread(target=startProcess, args=())  # Creates a separate thread from the window for processing
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    elif event == "_START_":  # When the start button is clicked:
        print("Start")
        isReceiving = True  # Allow the thread to loop
        t1.start()  # Start the thread

    elif event == "_STOP_":  # When the stop button is clicked:
        print("Stop")
        isReceiving = False  # Stops the thread from looping, effectively stopping the thread

    elif event == "_CALIBRATE_":  # When the calibrate button is clicked:
        print("Calibrate")
        # run calibrate()

window.close()
