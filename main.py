import PySimpleGUI as sg
from math_game import MathGame

"""
Simple Math Game

This program allows the user to play a simple math game with four modes:
Addition, Subtraction, Multiplication, and Division.

Dependencies:
    PySimpleGUI: GUI library for creating the user interface.
    math_game.py (contains the MathGame class).

Classes:
    MathGame: Handles the logic for the math game.

Functions:
    main(): Launches the main window and handles user interactions.
    level_window(): Displays the level selection window and returns the chosen level.
    game_window(mode): Initializes and starts a game session with the specified mode.

Usage:
    Run this scrit to launch the game interface.
    Select a mode to start playing.
    The game provides the option  to choose between two difficulty levels: Easy and Hard.

Author: Cezary Tubacki
Date: September 2023
"""


def main():
    """
    Function to launch the main window and handle user interactions.
    """
    # Setting the GUI theme
    sg.theme("Reddit")
    # Setting the title of the main window.
    title_main = "Simple Math Game"
    # Layout of the main window:
    layout_main = [
        [sg.Button("ADDITION")],
        [sg.Button("SUBTRACTION")],
        [sg.Button("MULTIPLICATION")],
        [sg.Button("DIVISION")],
        [sg.Button("EXIT")],
    ]
    # Creates the main window.
    window_main = sg.Window(title_main, layout_main)

    # Main game window
    while True:
        event, _ = window_main.read()
        if event in (sg.WIN_CLOSED, "EXIT"):
            break
        if event == "ADDITION":  # starts addition game
            game_window("+")
        if event == "SUBTRACTION":  # starts subtraction game
            game_window("-")
        if event == "MULTIPLICATION":  # starts multiplication game
            game_window("*")
        if event == "DIVISION":  # starts division game
            game_window("/")


def level_window():
    """
    Function to display the level selection window and return the chosen level.
    """
    # Setting the title of the level window.
    title_level = "Select level"

    # Layout for level window
    layout_level = [
        [sg.Text("Please select difficulty:")],
        [
            sg.Radio("Easy", "LEVEL", key="easy", default=True),
            sg.Radio("Hard", "LEVEL", key="hard"),
        ],
        [sg.Button("Submit"), sg.Button("Back")],
    ]
    # Creates level window:
    window_level = sg.Window(title_level, layout_level)
    while True:
        event, values = window_level.read()
        if event in (sg.WIN_CLOSED, "Back"):
            window_level.close()
            break
        if event == "Submit":
            if values["easy"]:
                window_level.close()
                return "easy"
            elif values["hard"]:
                window_level.close()
                return "hard"


def game_window(mode):
    """
    Funtion to initialize and start a game session with the specified mode.

    Parameters:
        mode(str): The operation mode for the game.
    """
    # Creates an instance of MathGame class.
    game = MathGame(mode=mode, level=level_window())
    if game.level == "hard":
        game.set_level("hard")  # Sets the difficulty level to "hard" if selected.
    # Starts the game session
    game.math_game_window()


if __name__ == "__main__":
    main()
