"""
CP1404 Practical 09
unreliable_car_test.py
Estimated time: 20 mins
Actual time: 24 mins
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    good_car = UnreliableCar("Reliable", 100, 80)
    bad_car = UnreliableCar("Unreliable", 100, 10)

    for i in range (1, 15):
        print(f"Driving {i}km")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)

main()