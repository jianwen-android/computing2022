# Triple Cripple Uncripplers

A team of Sec 4s from the **School of Science and Technology, Singapore**.

## Hardware

## STL

Taken from [lucidVR](https://github.com/LucidVR/lucidgloves/tree/44050f3c9a5da6cbe2278d66de1696ce95ae12e5) at commit 44050f3

## Wiring

In order to measure the values of the potentiometers when we bend our fingers, we need to connect the wipers of the potentiometer to the Arduino in this fashion:

    | Pin | Arduino |
    |:---:|:-------:|
    | A0  | thumb   |
    | A1  | index   |
    | A2  | middle  |
    | A3  | ring    |
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

[requirements](requirements.txt)

### Machine Learning

@Zafyree3

### Python GUI

@Leroy-Hong fat

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
   ```
    [SERIAL]
    port = 'COM3' #Change this to the correct port
   ```
5. Run the code by typing `python3 main.py`
6. \(python stuff yall need to explain here)

[^right]: Not used in the final prototype.
[^endcap]: Need to be sized to fit each individual finger (Use 3D modelling software like)
