"""
CP1404 Practical 09
unreliable_car.py
Estimated time: 20 mins
Actual time: 19 mins
"""
from random import randint
from prac_09.car import Car

class UnreliableCar:

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        rand_value = randint(1,100)
        if rand_value >= self.reliability:
            distance = 0
        distance_travelled = super().drive(distance)
        return distance_travelled