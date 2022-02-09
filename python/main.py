# The main file of the program

import threading  # Used for a separate flow of execution for processing, independent of gui
import serial  # Used to initialise a connection with arduino, from the glove
import PySimpleGUI as sg  # A simple gui library used to display information and start the program
import pandas as pd  # A data processing library used to format data to be passed into the learnt model
import configparser  # A default(?) library used to read off ini files
import time  # A default library for delaying certain portions of the code

from src import (
    tfFunc,
    guiFunc,
    arduinoFunc,
)  # These are all functions separated by library for easier collation

images = [
    "../assets/signA2.png",
    "../assets/signB2.png",
    "C",
    "D",
    "E",
    "F",
    "../assets/signG2.png",
    "H",
    "../assets/signI2.png",
    "K",
    "../assets/signL2.png",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "W",
    "X",
    "Y",
]

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "W",
    "X",
    "Y",
]

# Do setup
config = configparser.ConfigParser()  # Setup configparser to read config.ini
config.read("../config.ini")  # Read config.ini

isReceiving = False
imgSz = (int(config["IMAGESIZE"]["x"]), int(config["IMAGESIZE"]["y"]))
btnSz = (int(config["BUTTONSIZE"]["x"]), int(config["BUTTONSIZE"]["y"]))
padding = (int(config["PADDING"]["x"]), int(config["PADDING"]["y"]))

model, px = tfFunc.setupModel()  # Setup model for prediction
arduino = serial.Serial(port=config["SERIAL"]["port"],baudrate=int(config["SERIAL"]["baudrate"]),timeout=float(config["SERIAL"]["timeout"]),)
arduinoFunc.arduinoSetup(arduino)  # Setup arduino connection
window = guiFunc.windowSetup(btnSz, imgSz, padding)  # Create the Window


# Functions
# ---


def startProcess() -> None:
    # The bulk of the program:
    # 1. Reads data from arduino
    # 2. Processes the data into a readable format to be passed into a trained model
    # 3. Updates the image after processing the data

    while isReceiving:
        datas = arduinoFunc.readData(arduino)
        if datas:  # if there is data
            datas = datas.split(",")
            pdatas = linear(datas)
            df = pd.DataFrame(
                [pdatas],
                columns=["Pinky", "Ring", "Middle", "Index", "Thumb"],
                dtype=int,
            )  # Format data into a table for predicting
            i = tfFunc.modelPredict(model, df)  # Pass read values into model
            # print(i,images[i])
            updateText(letters[i])


def linear(datas) -> list:
    # dis ting the normalisation i tink
    y = ["PINKIE", "RING", "MIDDLE", "INDEX", "THUMB"]
    processedDatas = []
    for i in range(0, 5):
        processedData = (datas[i] - config[y[i]]['min']) / (config[y[i]]['max'] - config[y[i]]['min'])
        processedDatas.append(processedData)
        # (read value - calibrated min) / (calibrated max - callibrated min)
    return processedDatas


def saveCalibrate(minmax) -> None:
    y = ["PINKIE", "RING", "MIDDLE", "INDEX", "THUMB"]
    datas = arduinoFunc.readData(arduino)  # Store read data at one instance
    if datas:  # If there is data
        datas = datas.split(",")
        for i in range(5):
            # print(datas[i])
            config[y[i]][minmax] = datas[i]  # Store data in the correct category for each data
        with open(
                "../config.ini", "w"
        ) as configfile:  # Save read data into the config.ini
            config.write(configfile)  # This data will be used in the linear function


def calibrate() -> None:
    # Stores calibrated values
    value1, _ = sg.Window(
        "Calibration",
        [
            [sg.Image(source="../assets/handClosed2.png", size=imgSz)],
            [sg.T("Extend your fingers and hold them out for 3 seconds")],
            [sg.Ok(s=10), sg.Cancel(s=10)],
        ],
        disable_close=True,
    ).read(close=True)
    # Create a window containing instructions
    arduino.reset_input_buffer()  # Clear the buffer
    time.sleep(1.5)  # Delay to minimise chance of no read value
    if value1 == "Ok":  # If button clicked on window is Ok
        saveCalibrate("min")  # Save values that is being read in the point of time
    else:
        print("calibration quit")
        return

    value2, _ = sg.Window(
        "Calibration",
        [
            [sg.Image(source="../assets/handClosed2.png", size=imgSz)],
            [sg.T("Close your fingers into a fist and hold them closed for 3 seconds")],
            [sg.Ok(s=10), sg.Cancel(s=10)],
        ],
        disable_close=True,
    ).read(close=True)
    # Create a window containing instructions
    arduino.flushInput()  # arduino.readall() if this doesnt work
    arduino.flush()  # Clears serial monitor
    time.sleep(1.5)  # Delay to minimise chance of no read value
    if value2 == "Ok":  # If button clicked on window is Ok
        saveCalibrate("max")  # Save values that is being read in the point of time
    else:
        print("calibration quit")


def updateText(text="Placeholder text") -> None:
    # Updates the text of the window to display the appropriate sign
    window["outputText"].update(text)


def updateImg(src=None) -> None:
    # Updates the image of the window to display the appropriate sign
    window["signImg"].update(source=src, size=imgSz)


# Program loop
# ---

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    t1 = threading.Thread(
        target=startProcess, args=()
    )  # Creates a separate thread from the window for processing
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    elif event == "_START_":  # When the start button is clicked:
        print("Start")
        isReceiving = True  # Allow the thread to loop
        t1.start()  # Start the thread

    elif event == "_STOP_":  # When the stop button is clicked:
        print("Stop")
        isReceiving = (
            False  # Stops the thread from looping, effectively stopping the thread
        )

    elif event == "_CALIBRATE_":  # When the calibrate button is clicked:
        print("Calibrate")
        if not isReceiving:
            calibrate()
        else:
            sg.popup("Please stop the program before calibration")
        # run calibrate()

window.close()
