# An extension file handling the setup of the arduino and reading data off it
# pass arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) into functions
# Made by Jian Wen <3
import time
import re
import serial


def arduinoSetup(arduino) -> bool:  # Run once before program starts
    arduino.reset_input_buffer()
    arduino.flush()
    time.sleep(1.5)
    #  Gives buffer time to allow the serial port to be ready
    return True


def readData(arduino) -> str:  # Returns data read from arduino as a string
    string = ""
    arduino.reset_input_buffer()
    line = arduino.readline()   # read a byte string
    string = line.decode().strip()  # convert the byte string to a unicode string
    while not bool(re.match("\d{1,4},\d{1,4},\d{1,4},\d{1,4},\d{1,4}", string)):
        arduino.reset_input_buffer()
        time.sleep(1)
        line = arduino.readline()   # read a byte string
        string = line.decode().strip()  # convert the byte string to a unicode string
    return string

# arduino = serial.Serial(port="/dev/cu.usbserial-A9SOCXWK", baudrate=9600, timeout=float(0))
# arduinoSetup(arduino)

# while True:
#     datas = readData(arduino)
#     print(datas)
    
 