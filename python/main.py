# The main file of the program

import threading  # Used for a separate flow of execution for processing, independent of gui
import serial  # Used to initialise a connection with arduino, from the glove
import PySimpleGUI as sg  # A simple gui library used to display information and start the program
import pandas as pd  # A data processing library used to format data to be passed into the learnt model
import configparser
import time

from src import tfFunc, guiFunc, arduinoFunc  # These are all functions separated by library for easier collation

images = ["../assets/signA2.png", "../assets/signB2.png", "C", "D", "E", "F", "../assets/signG2.png", "H",
          "../assets/signI2.png",
          "K", "../assets/signL2.png", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y"]

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "W", "X", "Y"]

isReceiving = False
imgSz = (530, 550)
btnSz = (20, 3)
# Do setup
config = configparser.ConfigParser()
config.read('../config.ini')

model, px = tfFunc.setupModel()  # Setup model for prediction
# arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
# arduinoFunc.arduinoSetup(arduino)  # Setup arduino connection
window = guiFunc.windowSetup(btnSz, imgSz)  # Create the Window


# Functions
# ---

def startProcess():
    # The bulk of the program:
    # 1. Reads data from arduino
    # 2. Processes the data into a readable format to be passed into a trained model
    # 3. Updates the image after processing the data

    while isReceiving:
        datas = arduinoFunc.readData(arduino)
        if datas:  # if there is data
            datas = datas.split(',')
            df = pd.DataFrame([datas], columns=['Pinky', 'Ring', 'Middle', 'Index', 'Thumb'], dtype=int)
            i = tfFunc.modelPredict(model, df)
            # print(i)
            # print(images[i])
            updateText(letters[i])


def linear(x):
    # (read value - callibrated min) / (callibrated max - callibrated min)
    pass


def updateImg(src=None):
    # Updates the image of the window to display the appropriate sign
    window["signImg"].update(source=src, size=imgSz)


def saveCalibrate(minmax):
    y = ['PINKIE', 'RING', 'MIDDLE', 'INDEX', 'THUMB']
    datas = arduinoFunc.readData(arduino)
    if datas:  # if there is data
        datas = datas.split(',')
        for i in range(5):
            # print(datas[i])
            config[y[i]][minmax] = datas[i]
        with open('../config.ini', 'w') as configfile:  # save
            config.write(configfile)


def calibrate():
    # store calibrated values
    value1, _ = sg.Window('Calibration', [[sg.Image(source='../assets/handClosed2.png', size=imgSz)],
                                          [sg.T('Extend your fingers and hold them out for 3 seconds')],
                                          [sg.Ok(s=10), sg.Cancel(s=10)]],
                          disable_close=True).read(close=True)
    arduino.flushInput()
    arduino.flush()
    time.sleep(1.5)
    if value1 == 'Ok':
        saveCalibrate('min')
    else:
        print('calibration quit')
        return

    value2, _ = sg.Window('Continue?', [[sg.Image(source='../assets/handClosed2.png', size=imgSz)],
                                        [sg.T('Close your fingers and hold them closed for 3 seconds')],
                                        [sg.Ok(s=10), sg.Cancel(s=10)]],
                          disable_close=True).read(close=True)
    arduino.flushInput()
    arduino.flush()
    time.sleep(1.5)
    if value2 == 'Ok':
        saveCalibrate('max')
    else:
        print('calibration quit')
        return

    # sg.popup_ok_cancel("Open your hands", image='../assets/signA2.png')


def updateText(text="Placeholder text"):
    # Updates the text of the window to display the appropriate sign
    window["outputText"].update(text)


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
        calibrate()
        # run calibrate()

window.close()
