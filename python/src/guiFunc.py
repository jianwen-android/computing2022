# An extension file handling the setup of the gui
# Made by Leroy <3
import PySimpleGUI as sg  # A simple gui library used to display information and start the program


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
