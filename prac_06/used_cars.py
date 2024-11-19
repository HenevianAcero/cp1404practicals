"""
CP1404 Practical 6
used_cars.py

"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(f"{limo.name} has fuel: {limo.fuel}")



main()