# Triple Cripple Uncripplers

A team of Sec 4s from the **School of Science and Technology, Singapore**.

## Hardware

#TODO: Add STL

## Arduino code

### Arduino code for sending data to computer

[Left hand](/arduino/left.ino) | [Right hand](/arduino/right.ino)[^1].

## Explanation

```Arduino
#define pinkie A4
void loop() {
    Serial.print(analogRead(pinkie));
    Serial.print(", ");
    delay(1000);
}
```

Declares variable pinkie and assigns it the the analog pin A4, then prints the value of the pin every second

## Python

[requirements](requirements.txt)

## Machine Learning

@Zafyree3

## Python GUI

@Leroy-Hong fat

## Instructions

1. Build translator glove
2. Upload Arduino code to the nano to the respective hand using the [Arduino IDE](https://www.arduino.cc/en/software)
3. \(python stuff yall need to explain here)

[^1]: Not used in the final prototype.
