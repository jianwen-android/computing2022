# Triple Cripple Uncripplers

A team of Sec 4s from the **School of Science and Technology, Singapore**.

# Table of Contents

- [Triple Cripple Uncripplers](#triple-cripple-uncripplers)
- [Table of Contents](#table-of-contents)
  - [Instructions](#instructions)
    - [Glove](#glove)
      - [Reels](#reels)
        - [Flex sensor](#flex-sensor)
      - [Arduino](#arduino)
      - [Putting it all together](#putting-it-all-together)
    - [Setting up the environment](#setting-up-the-environment)
  - [Hardware](#hardware)
    - [3D Printed Parts](#3d-printed-parts)
    - [Wiring](#wiring)
  - [Arduino](#arduino-1)
    - [Explanation](#explanation)
  - [Python](#python)
    - [Tensorflow (Training the model)](#tensorflow-training-the-model)
      - [Importing Libraries](#importing-libraries)
      - [Dealing With Spreadsheet](#dealing-with-spreadsheet)
      - [Preprocessing Data](#preprocessing-data)
      - [Getting Model](#getting-model)
      - [Training Model](#training-model)
      - [Evaluate the Model](#evaluate-the-model)
      - [Saving Model](#saving-model)
    - [Tensorflow (Predicting with the model)](#tensorflow-predicting-with-the-model)
      - [Load the model with weights](#load-the-model-with-weights)
      - [Predicting with the model](#predicting-with-the-model)
      - [Colaboratory of code](#colaboratory-of-code)
    - [configparser](#configparser)
    - [pysimplegui](#pysimplegui)
- [Limitations](#limitations)
  - [Possible improvements](#possible-improvements)
- [Thanks to](#thanks-to)


![Team Image](/assets/IMG_6436.png)

_Image of the team *Triple Cripple Uncrippler*_

_(From left to right, top to bottom) Leroy Hong (S401), Jian Wen (S402), Irman Zafyree (S401)_

## Instructions

### Glove

#### Reels

1. For each hand, print:

   1. 5 [End caps](hardware/stl/Prot3_EndCap.STL)[^endcap]
   2. 14 [Guide nodes](hardware/stl/Prot3_EndCap.STL)[^nodes]
   3. 5 [Holders](hardware/stl/Prot3.1_Holder.STL)
   4. 5 [Tensioners](hardware/stl/Prot3.1_Tensioner.STL)
   5. 5 [Spool holders](hardware/stl/Prot3.1R2_EasySpool.STL)
   6. 5 [Spool covers](hardware/stl/Prot3.1_SpoolCover_Taller.STL)

2. Prepare 5 badge reels by removing their outer plastic casing, and extracting the string + metal spool spring

   ![Anatomy of a badge reel](/hardware/anatomy-badge-reel.png)

   _Taken from [EID badges](https://www.eidbadges.com/anatomy-reels)_

3. Prepare each reel by inserting a potentiometer knob side up into the bottom of the tensioner and screwing it in place with the provided nut
   1. Then insert the etched end of the spool spring into the hole on the side of the tensioner, turn and coil the spring into the tensioner
   2. Slot the spring into the slit of the potentiometer to hold it in place
4. Tie a knot on one end of the string and slot it through the bottom hole of the spool holder
   1. Insert the spool holder onto the knob of the potentiometer
   2. Ensure that the potentiometer will spring back into place when you turn the spool holder clockwise
5. Thread the other end of the string into the spool cover
   1. Turn it clockwise to coil in the extra string until the string is of a suitable length to suit your finger
   2. We recommend leaving extra length as the string will be tied to the endcap and you can simply cut off the excess when you are done
   3. Once you are done, push the covers down onto the tensioner and holder. They should click into place
6. Insert the completed module (Tensioner + Spool holder + Spool cover) onto the holders. They should click into place.
7. Wear the gloves and put on the customized endcaps to each of the fingers
   1. Straighten your fingers against a flat surface and tie the ends of the string to the endcaps, ensuring that the reels are not pulled

##### Flex sensor

Alternatively, you can use bend sensors to measure the bend of a finger, this method will be more accurate, less bulky and easier to wear but will require more time and effort to create if you don't choose to buy the sensors.

Instructions on how to make them:

[Instructables](https://www.instructables.com/How-to-Make-FLEX-Sensor-at-Home-DIY-Flex-Sensor/)

[Arduino Forums](https://create.arduino.cc/projecthub/Shahirnasar/simple-homemade-flex-sensor-ff54f0)

#### Arduino

1. Solder 5V and GND to the first and last pin of the potentiometers from the top (these can be shared between the 5 fingers on each hand)
2. Solder a wire connecting the middle pin (analogue pin) of the potentiometer to the corresponding pin on the Arduino
3. Refer to [Wiring](README.md#wiring)

#### Putting it all together

1. Glue the completed reels to the back of your gloves such that they are side by side and correspond to each of your fingers
   1. Glue the guide nodes to the first 2 phalange or section of your finger on the back of your gloves
2. Trim the pins of the Arduino to make sure that they don't stand out, using a flush cutter
3. Depending on the material of your glove, either:
   1. Hot glue the Arduino Nano onto the glove (ensure that the pins of the Arduino are electrically isolated)
   2. Tape the Nano onto the glove

### Setting up the environment

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

5. Install Python (version 3.10.x will do)
   1. Ensure that the installation comes with the latest version of tkinter
6. Install the [requirements](requirements.txt) for this project using

   ```shell
   pip install -r requirements.txt
   ```

   1. Run the code using `python3 main.py`

## Hardware

### 3D Printed Parts

Taken from [lucidVR](https://github.com/LucidVR/lucidgloves/tree/44050f3c9a5da6cbe2278d66de1696ce95ae12e5) at commit **44050f3**

### Wiring

In order to measure the values of the potentiometers when we bend our fingers, we need to connect the wipers (middle pin) of the potentiometer to the Arduino in this fashion:

| Pin | Arduino |
| :-: | :-----: |
| A0  |  thumb  |
| A1  |  index  |
| A2  | middle  |
| A3  |  ring   |
| A4  | pinkie  |

![Schematic](hardware/electronics/image.png)[^schematic]

## Arduino

[Code](/arduino/nano/nano.ino)[^right].

### Explanation

```c
#define pinkie A4
void loop() {
    Serial.print(analogRead(pinkie));
    Serial.print(",");
    delay(1000);
}
```

_Declares variable pinkie and assigns it the the analog pin A4, then prints the value of the pin every second_

## Python

### Tensorflow (Training the model)

#### Importing Libraries

```Python
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import tensorflow as tf
import csv
import numpy as np
from google.colab import auth
import gspread
from oauth2client.client import GoogleCredentials
```

_These are all the libraries we used to train the model_

#### Dealing With Spreadsheet

```Python
auth.authenticate_user() # Auth to allow access to the spread sheet
gc = gspread.authorize(GoogleCredentials.get_application_default())
worksheet = gc.open("Spoof Data").worksheet('Sheet4') # Opening the spreadsheet and downloading as CSV
rows = worksheet.get_all_values()
pd.DataFrame.from_records(rows).to_csv("data.csv",index=False,header=False)
```

_These lines are to get the data from the google sheet and saves it as a csv to be used later_

#### Preprocessing Data

```Python
df = pd.read_csv("data.csv") # Reading the CSV
X = pd.get_dummies(df.drop(["Letter"],axis=1)) # Remove letter as that outcome
letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q",
            "S","T","U","W","X","Y"] # List of the doable alphabets in order, some letters like j and z requires movement, r,
Y = df["Letter"].apply(lambda x: letters.index(x)) # Mapping ints to the letters
```

_Sets up the data to be used for the training of the model_

#### Getting Model

```Python
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.3) # Split the data to be used for training and then testing
model = tf.keras.models.Sequential([ # Create a neural network with a these following layers:
                                    tf.keras.layers.Dense(5, activation="relu"), # Input layers with 5 nodes
                                    tf.keras.layers.Dense(64, activation="relu"), # Hidden layers of 64 nodes
                                    tf.keras.layers.Dense(32, activation="relu"), # Hidden layers of 32 nodes
                                    tf.keras.layers.Dense(len(letters), activation="softmax") # Output layers with node equal to number of alphabet
])
model.compile( # Configures the model for training
              optimizer='adam', # Optimizer that implements the Adam algorithm
              loss='sparse_categorical_crossentropy', # Use this crossentropy loss function when there are two or more label classes.
              metrics=['accuracy'] # Calculates how often predictions equal labels
)
```

_Prepare the model that we want to train_

#### Training Model

```Python
model.fit(X_train, Y_train, epochs=200) # Trains the model 200 times using our training data
```

_Our model learns from the data and changes the weights according to how the model was prepared earlier_

#### Evaluate the Model

```Python
model.evaluate(X_test, Y_test) # Tests the model with the test data to see how accurate the prediction is
```

_We see how well our model is able to predict and change the configuration if the accuracy is too low (i.e < 70%)_

#### Saving Model

```Python
model.save_weights('./weights/weights1')
```

_Saves the weights of the model into a folder to be used to predict data later_

### Tensorflow (Predicting with the model)

#### Load the model with weights

```Python
model = tf.keras.models.Sequential([ # Configures the layers to be the same as how it is trains in order to use the weights
                                    tf.keras.layers.Dense(5, activation="relu"),
                                    tf.keras.layers.Dense(64, activation="relu"),
                                    tf.keras.layers.Dense(32, activation="relu"),
                                    tf.keras.layers.Dense(len(letters), activation="softmax")
])
model.compile( # We also configure the compliations the same
              optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
)
model.load_weights('./weights/weights1') # Load the weights into the model
```

_This is how we set up and load the weights into the model to be_

#### Predicting with the model

```Python
pDf = pd.read_csv("pData.csv") # Loads the data to be predicted
pX = pd.get_dummies(pDf.drop(["Letter"],axis=1)) # Removed the letter column as that is what we are predicting
predictions = model.predict(pX) # Uses the model to predict the letter of the data
classes = np.argmax(predictions, axis = 1) # We take the highest values from the predictions array
letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q",
            "R","S","T","U","W","X","Y"]
print(letters[classes[0]]) # Use the highest value to determine which latter was predicted
```

_The is how we use the model to predict letter of data_

#### Colaboratory of code

[Link for the colaboratory code can be found here](https://colab.research.google.com/drive/1Sa6vwZDiKaWeS2yP_VQGnIof6uECQ_Ln?usp=sharing)

---

### configparser

```Python
import configparser  # A default(?) library used to read off ini files
```

```Python
config = configparser.ConfigParser()  # Setup configparser to read config.ini
config.read("../config.ini")  # Read config.ini
```

_Creates an object that contains values from config.ini_

```Python
imgSz = (int(config["IMAGESIZE"]["x"]), int(config["IMAGESIZE"]["y"]))
btnSz = (int(config["BUTTONSIZE"]["x"]), int(config["BUTTONSIZE"]["y"]))
padding = (int(config["PADDING"]["x"]), int(config["PADDING"]["y"]))

arduino = serial.Serial(port=config["SERIAL"]["port"], baudrate=int(config["SERIAL"]["baudrate"]), timeout=float(config["SERIAL"]["timeout"]),)
```

_Accesses the variables in the config object for prior setup._

### pysimplegui

```Python
import PySimpleGUI as sg  # A simple gui library used to display information and start the program
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

1. Letters
   1. Letters like z and j require you to move your hand, which is not possible to track in the current prototype
   2. Letters like r, v and u only differ in pointing towards different directions, which is not possibel to track in the current prototype
2. Words
   1. Most if not all nouns and verbs require you to move or rotate your hand, which is not possible to track in the current prototype
3. Connectivity
   1. Right now the glove is limited to being connected to the computer via USB
   2. This means that you can only wear the glove around the computer, and you would need a cable connected
4. Consistency
   1. Not all badge reels are made equal, some are extremely rusty while some are extremely springy
   2. This means that the consistency and the force needed to bend a finger may vary from finger to finger
   3. It also meant that finding springs that can meet our threshold of springing back fast enough is difficult

## Possible improvements

1. Add an IMU to the glove to track the orientation of and movement from the glove
   1. This would allow us to overcome the challenge of not being able to translate certain letters and words
2. Use bend sensors to track the bending of the fingers
   1. This would eliminate the need for potentiometers, making our gloves less bulky and easier to carry around
   2. This would also eliminate the need for endcaps and guide nodes, giving the gloves more comfortability
3. Add a battery as a power source and bluetooth module
   1. With Bluetooth modules connected to the Arduino, we would be able to implement wireless features to the glove

# Thanks to

[lucidVR](https://github.com/LucidVR/lucidgloves) for the STL files and how to use badge reels to measure finger movements

The teachers for giving us advice and guidance throughout the duration of the project:

1. Ms Tang
2. Mr Pang
3. Mr Samuel Lee

[^right]: Right hand is not used in the prototype.
[^endcap]: Need to be sized to fit each individual finger (Use 3D modelling software like Fusion360)
[^nodes]: Number can be adjusted according to how many you need, however at the minimum you will need 9 and we reccommend 14
[^schematic]: Wire the first and second pin directly to 5V and the analog pins if youre using flex sensors
