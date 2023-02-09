"""
Program: Debugging_Assignment.py
Author: Tony Ehlert
Last date modified: 2/9/2023

The purpose of this program is print to a number starting with one and ending with the
number entered in the call to the function

The input is number inserted in a call to the function
The output is a print out of the numbers counting up by one to the number entered in the function call
"""


def print_to_number(number):
    """Prints to the number value passed in, beginning at 1
    :param number: ending number
    """
    for counter in range(1, number):
        print(counter)


if __name__ == "__main__":
    print_to_number(5)
