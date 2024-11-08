def read_positive_int_for_choice(ask: str) -> int:
    """Asks how many books  you own and returns int, then it looks if its negative, if it does it ask again."""
    while True:
        question = input(ask)  # This takes the variable from "ask" and puts it into an input.
        try:
            question = int(question)  # Turns the value of question from "String" to integer
            if 1 <= question < 4:  # if greater than 0 or = to = return it to "number"
                return question
            elif question < 1 or question > 3:  # if less than 0, print it following.
                print("Not an option..")
        except ValueError:
            print("PLEASE USE PROPER NUMBERS")  # For Errors


def read_positive_int_for_module(ask: str) -> int:
    """Asks how many books  you own and returns int, then it looks if its negative, if it does it ask again."""
    while True:
        question = input(ask)  # This takes the variable from "ask" and puts it into an input.
        try:
            question = int(question)  # Turns the value of question from "String" to integer
            if 1 <= question <= 2:  # if greater than 0 or = to = return it to "number"
                return question
            elif question < 1 or question > 2:  # if less than 0, print it following.
                print("Not options represented..")
        except ValueError:
            print("PLEASE USE PROPER NUMBERS")  # For Errors


def read_positive_int_in_range(ask: str, min, max) -> int:
    """Asks how many books  you own and returns int, then it looks if its negative, if it does it ask again."""
    while True:
        question = input(ask)  # This takes the variable from "ask" and puts it into an input.
        try:
            question = int(question)  # Turns the value of question from "String" to integer
            if min <= question <= max:  # if greater than 0 or = to = return it to "number"
                return question
            else:  # if less than 0, print it following.
                print("Not options represented..")
        except ValueError:
            print("PLEASE USE PROPER NUMBERS")  # For Errors

def read_positive_float(ask: str) -> float:
    """Asks how many books  you own and returns int, then it looks if its negative, if it does it ask again."""
    while True:
        question = input(ask)  # This takes the variable from "ask" and puts it into an input.
        try:
            question = float(question)  # Turns the value of question from "String" to integer
            if question >= 0:  # if greater than 0 or = to = return it to "number"
                return question
            elif question < 0:  # if less than 0, print it following.
                print(" It cannot be negative")
        except ValueError:
            print("Whole numbers only please.")  # For Errors


def read_procentage_float(ask: str) -> float:
    """Asks how many books  you own and returns int, then it looks if its negative, if it does it ask again."""
    while True:
        question = input(ask)  # This takes the variable from "ask" and puts it into an input.
        try:
            question = float(question)  # Turns the value of question from "String" to integer
            if 100 >= question >= 0:  # if greater than 0 or = to = return it to "number"
                return question
            elif question < 0:  # if less than 0, print it following.
                print(" It cannot be negative")
        except ValueError:
            print("Whole numbers only please.")  # For Errors


def read_procentage_int(ask: str) -> int:
    """Asks how many books  you own and returns int, then it looks if its negative, if it does it ask again."""
    while True:
        question = input(ask)  # This takes the variable from "ask" and puts it into an input.
        try:
            question = int(question)  # Turns the value of question from "String" to integer
            if 100 >= question >= 0:  # if greater than 0 or = to = return it to "number"
                return question
            elif question < 0:  # if less than 0, print it following.
                print(" It cannot be negative")
        except ValueError:
            print("Whole numbers only please.")  # For Errors


def multiple_prompts():
    """Multiple Questions that can be asked"""
    number_of_books = read_positive_int("How many books do you own?")
    age = read_positive_int("What age are you?")
    number_of_students = read_positive_int("How many students took the exam?")


if __name__ == '__main__':
    multiple_prompts()
