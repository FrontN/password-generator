import random
import string
import os
import time

def clear_screen():
    """
    Clears the screen by running the appropriate command for the current operating system.

    On Windows systems, this function runs the "cls" command to clear the screen.
    On all other systems, this function runs the "clear" command to clear the screen.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_int(prompt):
    """
    Continuously prompts the user for input until a valid integer is entered.
    Parameters:
    prompt (str): The message to display to the user when prompting for input.
    Returns:
    int: The valid integer entered by the user.
    """
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_input(prompt, valid_options):
    """
    Continuously prompts the user for input until a valid option is entered.
    Parameters:
    prompt (str): The message to display to the user when prompting for input.
    valid_options (list): A list of valid options that the user can enter.
    Returns:
    str: The valid option entered by the user.
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please enter a valid option.")

def main():
    """
    Main entry point for the PyPassword Generator program.

    This program clears the screen and then prompts the user for input on how many letters, numbers, and symbols they would like in their password.
    It then generates a password based on the user's input and prints it to the screen.
    The user is then given the option to generate another password or to quit the program.

    :return: None
    """
    clear_screen()
    lettere = list(string.ascii_letters)
    numeri = list(string.digits)
    simboli = list(string.punctuation)

    print("Welcome to the PyPassword Generator!")
    time.sleep(1.5)
    while True:
        clear_screen()
        NumlettereScelte = get_valid_int("How many letters would you like in your password?\n")
        clear_screen()
        NumnumeriScelti = get_valid_int("How many numbers would you like?\n")
        clear_screen()
        NumsimboliScelti= get_valid_int("How many symbols would you like?\n")

        formula = lambda x,y : random.choices(x, k=y)

        somma = formula(lettere, NumlettereScelte) + formula(numeri, NumnumeriScelti) + formula(simboli, NumsimboliScelti)
        random.shuffle(somma)
        password = "".join(somma)
        clear_screen()
        print("Your password is".center(40, "*"))
        print(password.center(40))
        print("*"*40)

        if get_valid_input("Do you want to generate another password? (yes/no):", ["yes", "no", "y", "n"]).startswith("n"):
            break

if __name__ == "__main__":
    main()
