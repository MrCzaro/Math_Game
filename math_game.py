from random import randint
import PySimpleGUI as sg


class MathGame:
    """
    A class for a math game.
    The game can be played in diffrent modes such as addition, subtraction,
    multiplication, and division.

    Dependencies:
    PySimpleGUI: GUI library for creating the user interface.

    Parameters:
        mode (str): The operation mode of the game.
        level (str, optional): The difficulty level of the game. Default is "easy".
        max_num (int, optional): The maximum number used in the game. Default is 50.
        games (int, optional): The number of games to play. Default is 20.

    Methods:
        set_level(level):
            Sets the difficulty level of the game.

        generate_numbers():
            Generates random numbers based on the chose mode.

        check_answer(answer, num1, num2):
            Checks if the provided answer is correct.

        math_game_window():
            Starts a GUI-based math game session using PySimpleGUI.

    """

    def __init__(self, mode, level="easy", max_num=50, games=20):
        self.mode = mode
        self.level = level
        self.games = games
        self.correct_answer = 0
        self.counter = 1
        self.max_num = max_num

    def set_level(self, level):
        """
        Sets the difficulty level of the game.

        Parameters:
            level (str): The difficulty level ("easy" - default or "hard").
        """
        self.level = level
        if self.level == "hard":
            self.games = 50
            self.max_num = 100

    def generate_numbers(self):
        """
        Generates two random numbers based on the chosen mode.

        Returns:
            tuple: A tuple containing two random numbers.
        """
        if self.mode == "+":
            while True:
                num1 = randint(1, self.max_num)
                num2 = randint(1, self.max_num)
                if (num1 + num2) <= self.max_num:
                    break
        elif self.mode == "-":
            while True:
                num1 = randint(1, self.max_num)
                num2 = randint(1, self.max_num)
                if num1 > num2:
                    break
        elif self.mode == "/":
            while True:
                num1 = randint(1, self.max_num)
                num2 = randint(1, 10)
                if (num1 > num2) and (num1 % num2 == 0) and ((num1 / num2) <= 10):
                    break
        elif self.mode == "*":
            num1 = randint(1, 10)
            num2 = randint(1, 10)
        return num1, num2

    def check_answer(self, answer, num1, num2):
        """
        Checks if the provided answer is correct.

        Parameters:
            answer (int): The user's answer.
            num1 (int): The rist random number.
            num2 (int): The second random number.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        if self.mode == "+":
            return answer == (num1 + num2)
        elif self.mode == "-":
            return answer == (num1 - num2)
        elif self.mode == "/":
            return answer == (num1 / num2)
        elif self.mode == "*":
            return answer == (num1 * num2)

    def math_game_window(self):
        """
        Starts a GUI-based math game session using PySimpleGUI.
        """
        # Define operation modes for the game
        modes = {
            "+": "Addition",
            "-": "Subtraction",
            "*": "Multiplication",
            "/": "Division",
        }
        game_type = modes[self.mode]
        title = f"{game_type} Math Game!"
        num1, num2 = self.generate_numbers()  # Generate numbers before the loop
        # Game layout
        layout = [
            [sg.Text(f"Correct Answers: 0/{self.games}", key="correct_answer")],
            [
                sg.Text(
                    f"Question {self.counter}: {num1} {self.mode} {num2} = ",
                    key="question",
                )
            ],
            [sg.InputText(key="answer")],
            [sg.Button("Submit"), sg.Button("Exit")],
        ]

        window = sg.Window(title, layout) # Create the game window

        for _ in range(self.games):
            event, values = window.read()
            if event in [sg.WIN_CLOSED, "Exit"]:
                window.close()
                break
            if event == "Submit":
                try:
                    answer = int(values["answer"])
                    if self.check_answer(answer, num1, num2):
                        self.correct_answer += 1
                    self.counter += 1
                    num1, num2 = self.generate_numbers()
                    window["correct_answer"].update(
                        f"Correct Answer: {self.correct_answer}/{self.games}"
                    )
                    window["question"].update(
                        f"Question {self.counter}: {num1} {self.mode} {num2} = "
                    )
                    window["answer"].update("")

                except ValueError:
                    sg.popup_error("Incorrect input! Please enter a valid number.")
        sg.popup(f"Your score: {self.correct_answer}/{self.games}")
        window.close()
