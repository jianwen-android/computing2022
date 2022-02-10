# An extension file handling the setup of a trained model and predicting signs from it

import pandas as pd  # Used for data formatting to be passed into model
import tensorflow as tf  # Used to load the model given trained weights
import numpy as np  # Used to do math or something
import os  # Used for permissions I think...

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
    "S",
    "T",
    "U",
    "W",
    "X",
    "Y",
]


def setupModel():  # Run once before program starts
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Gives tf perms i think

    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(5, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(len(letters), activation="softmax")
    ])
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    # The infrastructure of the model

    model.load_weights("src/weights/weights1")
    # Load the weights derived from training model

    pdf = pd.read_csv("src/pData.csv")
    pX = pd.get_dummies(pdf.drop(["Letter"], axis=1))
    # Backup test data (not necessary when program is running)
    return model, pX


def modelPredict(model, pX) -> int:  # Predicts / processes data given the data from arduino
    predictions = model.predict(pX)  # Predict the sign given the data
    classes = np.argmax(predictions, axis=1)  # Takes the index of the highest value
    # print(letters[classes[0]])  # Was used in debugging
    return classes[0]
