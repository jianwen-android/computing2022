import time


# pass arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) into functions
def arduinoSetup(arduino):
    time.sleep(3)
    while True:
        x = arduino.read()
        try:
            x.decode("utf8")
        except:
            return True


def readData(arduino):
    byteList = []
    while True:
        x = arduino.read().decode("utf8")
        byteList.append(x)
        try:
            byteList[-1]
        except:
            continue

        if byteList[-1] == "\n":
            data = ''.join(byteList[0:-1])
            return data
