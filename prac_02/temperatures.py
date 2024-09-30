"""
CP1404 - Practical 2
temperatures.py
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """convert_celsius_to_fahrenheit"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            celsius_to_fahrenheit(celsius)
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            """convert_fahrenheit_to_celsius"""
            fahrenheit = float(input("Fahrenheit: "))
            fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {fahrenheit_to_celsius(fahrenheit): .2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
