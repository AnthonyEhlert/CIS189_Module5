"""
Program: Basic_For_Loops_Ehlert.py
Author: Tony Ehlert
Last date modified: 2/8/2023

The purpose of this program is to use a for loop to first print a list of floating point numbers,
then print a list of of odd number from 99-33 inclusive
The input is a list of floating point numbers
The output is a print out of the floating point numbers list and a print out the odd numbers between 99-33 inclusive
"""
# creation of list of floating point numbers
float_list = [10.1, 20.2, 30.3, 40.4, 50.5, 60.6, 70.7, 80.8, 90.9]

# for loop to print all elements in list
for float_number in float_list:
    print(float_number)

# for loop to print odd numbers in descending order starting from 99 and ending with 33 (inclusive)
for number in range(99, 32, -1):
    if (number%2 != 1):
        continue
    print(number)
