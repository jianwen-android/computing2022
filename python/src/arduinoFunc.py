import time


# pass arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) into functions
def arduinoSetup(arduino):
    arduino.flushInput()
    arduino.flush()
    time.sleep(1.5)
    return True


def readData(arduino):
    try:
        ser_bytes = arduino.readline()
        decoded_bytes = (ser_bytes[:len(ser_bytes) - 2].decode("utf-8"))
        if decoded_bytes:
            return decoded_bytes
        else:
            return None
    except:
        return None
