"""
CP1404 Practical 9
band.py

"""

from musician import Musician
from guitar import Guitar
class Band:
    def __init__(self, musician, guitar):
        self.musician = Musician(musician)
        self.guitar = Guitar(guitar)

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.musician} is playing: ({self.guitar})"
