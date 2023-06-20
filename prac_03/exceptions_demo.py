"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When an incorrect value is given
2. When will a ZeroDivisionError occur? When a number is being divided by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError? A conditional statement can be added to check the denominator before performing the operation
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")