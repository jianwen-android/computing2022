# Triple Cripple Uncripplers

A team of Sec 4s from the **School of Science and Technology, Singapore**.

## Instructions

### Glove

1. For each hand, print:

   1. 5 [End caps](hardware/stl/Prot3_EndCap.STL)[^endcap]
   2. 14 [Guide nodes](hardware/stl/Prot3_EndCap.STL)

2.

### Code

1. Connect the Arduino Nano to the computer
2. Upload Arduino code to the nano to the respective hand using the [Arduino IDE](https://www.arduino.cc/en/software)
3. Select the correct serial port
   1. You can find out which one by uploading a blank sketch to the Arduino Nano
   2. Test the serial port by going under Tools > Port
4. Under [config.ini](config.ini) change the following:

```conf
[SERIAL]
port = 'COM3' #Change this to the correct port
```

5. Run the code by typing `python3 main.py`
6. \(python stuff yall need to explain here)

## Hardware

## STL

Taken from [lucidVR](https://github.com/LucidVR/lucidgloves/tree/44050f3c9a5da6cbe2278d66de1696ce95ae12e5) at commit **44050f3**

## Wiring

In order to measure the values of the potentiometers when we bend our fingers, we need to connect the wipers of the potentiometer to the Arduino in this fashion:

| Pin | Arduino |
| :-: | :-----: |
| A0  |  thumb  |
| A1  |  index  |
| A2  | middle  |
| A3  |  ring   |
| A4  | pinkie  |

![](hardware/electronics/image.png)

## Arduino code

[Left hand](/arduino/nano/nano.ino)[^right].

### Explanation

```Arduino
#define pinkie A4
void loop() {
    Serial.print(analogRead(pinkie));
    Serial.print(",");
    delay(1000);
}
```

_Declares variable pinkie and assigns it the the analog pin A4, then prints the value of the pin every second_

## Python

Install the [requirements](requirements.txt) for this project using

```shell
pip install -r requirements.txt
```

### tensorflow

@Zafyree3

### configparser


### pysimplegui

```Python
import PySimpleGUI as sg
```

```Python
def windowSetup(btnSz, imgSz, padding):  # Run once before program starts

    sg.theme("DarkBlue")  # Color theme for program
    imgSrc = "../assets/placeholder2.png"  # Placeholder image

    buttonCol = [
        [sg.Button(button_text="Start", key="_START_", size=btnSz, font=('Arial', 40), expand_x=True, expand_y=True, pad=padding)],
        [sg.Button(button_text="Stop", key="_STOP_", size=btnSz, font=('Arial', 40), expand_x=True, expand_y=True, pad=padding)],
        [sg.Button(button_text="Calibrate", key="_CALIBRATE_", size=btnSz, font=('Arial', 40), expand_x=True, expand_y=True, pad=padding)],
    ]
    # Creates a column of buttons

    col2 = [[sg.Image(source=imgSrc, size=imgSz, key="signImg")]]
    # Creates a column of containing the predicted sign

    layout = [
        [
            sg.Column(buttonCol, element_justification="c", expand_y=True),
            sg.Column(col2, element_justification="c"),
        ],
        [
            sg.Text(
                text="This is the output message",
                key="outputText",
                justification="c",
                font=('Arial', 40)
            )
        ],
    ]
    # Creates the final layout, combining both columns side by side and a textbox at the bottom

    return sg.Window("Cripple enabler", layout, default_element_size=(45, 1), resizable=True)
```
_This function prepares a window object which will be used to display information and interact with the programme - basically a GUI_

# Limitations
1. We are not able to translate certain letters
   1. Letters like z and j require you to move your hand, which is not possible to track in the current prototype
   2. Letters like r, v and u only differ in pointing towards different directions, which is not possibel to track in the current prototype
2. Words
   1. Most if not all nouns and verbs require you to move or rotate your hand, which is not possible to track in the current prototype
3. Connectivity
   1. Right now the glove is limited to being connected to the computer via USB
   2. This means that you can only wear the glove around the computer, and you would need a cable connected

## Possible improvements

1. Add an IMU to the glove to track the orientation of and movement from the glove
   1. This would allow us to overcome the challenge of not being able to translate certain letters and words
2. Use bend sensors to track the bending of the fingers
   1. This would eliminate the need for potentiometers, making our gloves less bulky and easier to carry around
   2. This would also eliminate the need for endcaps and guide nodes, giving the gloves more comfortability
3. Add a battery as a power source and bluetooth module
   1. With Bluetooth modules connected to the Arduino, we would be able to implement wireless features to the glove

[^right]: Not used in the final prototype.
[^endcap]: Need to be sized to fit each individual finger (Use 3D modelling software like Fusion360)
