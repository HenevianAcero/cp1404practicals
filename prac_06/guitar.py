"""
CP1404 Practical 06
guitar.py
Estimated time: 15 mins
Actual time: 24 mins
"""
import datetime

CURRENT_YEAR = datetime.now().year
VINTAGE_YEAR = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}): ${self.cost:2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        return self.year < other.year

