# An extension file handling the setup of the arduino and reading data off it
# pass arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) into functions
# Made by Jian Wen <3
import time


def arduinoSetup(arduino) -> bool:  # Run once before program starts
    arduino.reset_input_buffer()
    arduino.flush()
    time.sleep(1.5)
    #  Gives buffer time to allow the serial port to be ready
    return True


def readData(arduino) -> str:  # Returns data read from arduino as a string
    try:
        ser_bytes = arduino.readline()  # Read line printed by arduino
        arduino.reset_input_buffer()
        decoded_bytes = ser_bytes[: len(ser_bytes) - 2].decode(
            "utf-8"
        )  # Perform a decode using utf-8
        if decoded_bytes:  # If there is data read
            return decoded_bytes
        else:  # If there is NO data read
            return None
    except:
        return None
