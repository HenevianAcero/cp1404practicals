"""
CP1404 Practical 9
unreliable_car_test.py

"""

from prac_09.unreliable_car import UnreliableCar
def main():
    good_car = UnreliableCar("Good Car", 100, 85)
    bad_car = UnreliableCar("Bad Car", 100, 5)

    for i in range(1, 10):
        print(f"Driving {i}km")
        print(f"{good_car.name:10} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:10} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)


main()