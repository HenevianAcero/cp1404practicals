"""
CP1404 Practical 06
guitar_test.py
Estimated time = 20 mins
Actual time = 31 mins
"""

from prac_06.guitar import Guitar
import datetime

CURRENT_YEAR = datetime.now().year

def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.is_vintage()}")
    print(f"{other.name} get_age() - Expected {11}. Got {other.is_vintage()}")
    print()
    print(f"{guitar.name} get_age() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} get_age() - Expected {False}. Got {other.is_vintage()}")

if __name__ == '__main__':
    run_tests()