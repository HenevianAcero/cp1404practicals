"""
CP1404 Practical 09
band.py
Estimated time: 10 mins
Actual time: 6 mins
"""

from musician import Musician
from guitar import Guitar
class Band():
    band_name = "Extreme"
    def __init__(self, musician, guitar):
        self.musician = Musician.name(musician)
        self.guitar = Guitar.self(guitar)

    def __str__(self):
        return f"{self.musician} is playing {self.guitar}"