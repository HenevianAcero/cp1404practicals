"""
CP1404 Practical 6
guitar_test.py
Estimated time: 20 mins
Actual time: 18 mins

"""
from prac_06.guitar import Guitar

def run_tests():
    name = "Gibson L-5"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{guitar} get_age() - Expected 102. Got {guitar.get_age()}.")
    print(f"{other} get_age() - Expected 11. Got {other.get_age()}.")
    print(f"{guitar} is_vintage() - Expected True. Got {guitar.is_vintage()}.")
    print(f"{other} is_vintage() - Expected False. Got {other.is_vintage()}.")

run_tests()
