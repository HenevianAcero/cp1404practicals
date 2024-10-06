"""
CP1404 - Practical 3
exceptions_demo.py

Answer the following questions:
1. When will a ValueError occur? When the input is not the correct value.
2. When will a ZeroDivisionError occur? When a value is divided by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, add a conditional statement to check that the denominator is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by 0!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
