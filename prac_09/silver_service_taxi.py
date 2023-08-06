"""
CP1404 Practical 09
silver_service_taxi.py
Estimated time: 15 mins
Actual time: 20 mins
"""

from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi)
    flagfall = 4.5
    def __init__(self, name, fuel, fanciness)
    super().__init__(name, fuel)
    self.fanciness = fanciness
    self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} with flagfall of ${self.flagfall:2f}"

    def get_fare(self):
        get_fare = self.fanciness * Taxi.drive(distance)
        return self.flagfall + get_fare
