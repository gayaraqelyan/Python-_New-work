'''x = int(input("Enter the number"))
if x % 5 == 0:
    print("divides 5")
if x % 7 == 0:
    print("divides 7")
if x % 7 == 0 and x % 5 == 0:
    print("divides 5 and 7")
else:
    print("bye")

-----------------------------------------------------------------------------------------
x = input("Enter the word  ")
str_length = len(x)
if str_length < 10:
    print(str_length, "short word")
if str_length == 10:
    print(str_length, "too short long")
else:
    print(str_length, "long word")

--------------------------------------------------------------------------------------
user_string = input("Enter the word:  ")
string_count = user_string.lower().count("a")
print(f"The number is 'a' characters:  {string_count}")
---------------------------------------------------------------------------------------
List_of_numbers = [1, 12, 3, 14, 5, 16]
print(f"This is number summery: {sum(List_of_numbers)}")
------------------------------------------------------------------------------------------
def List_of_numbers(name):
    sum = 0
    for i in name:
        sum += i
    return sum


print(f"This is number summery: {List_of_numbers([1, 12, 3, 14, 5, 16])}")
---------------------------------------------------------------------------------------------

def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform calculation based on the operation
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected.")


# Run the calculator
calculator()

----------------------------------------------------------------------------------------------
import calendar

year = int(input("Enter the year:  "))
month = int(input("Enter the month: "))

print("\n", calendar.month(year, month))

----------------------------------------------------------------------------------------------
import calendar

year = int(input("Enter the year: "))

print("\n", calendar.calendar(year))
----------------------------------------------------------------------------------------

import math
from math import factorial

num = int(input("Enter the number"))
if num < 0:
    print("not")
else:
    print(f"{num}is {math.factorial(num)}")

-------------------------------------------------------------------------------------------
def factorial(n):
    if n < 0:
        return "Factorial is not defined of negative number."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

----------------------------------------------------------------------------------------------
num = int(input("Enter the number: "))
print(f"The factorial of {num},is {factorial(num)}")


----------------------------------------------------------------------------------------------

def middle_three_chars(string):
    if len(string) < 3:
        return "String is too short to extract middle three characters."
    if len(string) % 2 == 0:
        return "String length must be odd to extract the middle three characters."

    middle_index = len(string) // 2
    return string[middle_index - 1:middle_index + 2]


user_string = input("Enter the word: ")
result = middle_three_chars(user_string)
print(f"The middle three characters are:{result}")


----------------------------------------------------------------------------------------------
def str_length(string):
    if len(string) < 3:
        return string  # Leave the string unchanged if length is less than 3
    if string.endswith("ing"):
        return string + "iy"
    else:
        return string + "ing"


user_str = input("Enter the word: ")
result = str_length(user_str)
print(f"Resulting string: {result}")
'''
