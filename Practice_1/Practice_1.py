"""

Age calculator

Take input from the user
    1. Take age or year of birth, Detect accordingly
    and predict when will they would be 100 years old.

    Don't use any type of modules like datetime and dateUtils.
    they can then optionally provide a year and program should be able to tell the age as per the error
    all sorts of error should be handled

    You are not yet born
    you seem to be the oldest person alive
    all the error handling

"""

import enum

current_year = 2022
minimum_year = (current_year - 100)


class input_types(enum.Enum):
    YEAR = 1
    AGE = 2


def main_method():
    try:
        user_input, input_type = take_input()
        perform_action(user_input, input_type)
    except Exception as e:
        print(f"{e}")


def take_input():
    user_input = input("Enter user year or age: ")
    input_type = input_types.YEAR if len(user_input) > 3 else input_types.AGE

    valid_input(user_input, input_type)

    return user_input, input_type


def valid_input(user_input, input_type):

    if int(user_input) <= 0:
        raise Exception("You are not yet born")

    if not user_input.isnumeric():
        raise TypeError("Only numbers are allowed.")

    if input_type is input_types.AGE:
        if len(user_input) >= 3:
            raise Exception("You seems to be the oldest person alive. Can't proceed.")

    if input_type is input_types.YEAR:
        if int(user_input) <= minimum_year:
            raise Exception("You seems to be the oldest person alive. Can't proceed")

    return True


def perform_action(user_input, input_type):
    user_input = int(user_input)
    if input_type == input_types.AGE:
        result = (current_year - user_input) + 100
        print(f"You will be of 100 years on {result} year")
    else:
        result = user_input + 100
        print(f"You will be of 100 years on {result} year")


if __name__ == "__main__":
    main_method()
