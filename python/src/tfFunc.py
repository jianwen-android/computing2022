import pandas as pd
import tensorflow as tf
import numpy as np
import os

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "W", "X", "Y"]


def setupModel():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(23, activation="softmax")
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.load_weights("src/weights/weights1")

    pdf = pd.read_csv("src/pData.csv")

    pX = pd.get_dummies(pdf.drop(["Letter"], axis=1))
    # temp data
    return model, pX


def modelPredict(model, pX):
    # setup complete
    predictions = model.predict(pX)
    classes = np.argmax(predictions, axis=1)
    print(letters[classes[0]])
    return classes[0]
