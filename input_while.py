"""
Program: input_while.py
Author: Tony Ehlert
Last date modified: 2/9/2023

The purpose of this program is to prompt a user for a number between 1 and 100 and store the input in a list
and use while loops to check for input validation as well as a sentinel value, then once the sentinel value is entered,
a for loop is used to print out the contents of the list

The input is a series of integer numbers from a user
The output is a print out of the all the numbers the user entered
"""
# creation of list variable
user_input_list = []

# creation of sentinel variable
SENTINEL_VALUE = "stop"

# creation of variable for user input
user_input = 0

# creation of float variable for user input, defaulted to 0.0 (a value not within a good range)
user_input_as_float = 0.0

# while loop and try/except block used to check for valid number entry
while (user_input != SENTINEL_VALUE):
    # prompt the user for input (indicating the sentinel value to stop)
    user_input = input(f"Please enter a number between 1 and 100. Enter \"{SENTINEL_VALUE}\" to stop.").lower()
    try:
        user_input_as_float = float(user_input)

        # while loop checks for valid range
        while ((user_input_as_float < 1) or (user_input_as_float > 100) and user_input != SENTINEL_VALUE):
            print("Entry out of range! Number must be between 1 and 100")
            user_input = input(f"Please enter a number between 1 and 100. Enter \"{SENTINEL_VALUE}\" to stop.").lower()
            user_input_as_float = float(user_input)

        # add user input to list
        user_input_list.append(user_input_as_float)

    except:
        print(f"Cannot convert a string to float: \"{user_input}\"")

# print of the contents of list using for loop
for number in user_input_list:
    print(number)
