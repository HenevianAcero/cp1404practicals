"""
CP1405 Practical
taxi_simulator.py
Estimated time: 30 mins
Actual time: 35 mins
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """
(C)hoose taxi
(D)rive
(Q)uit
"""

total_bill = 0
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo",100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = none

def main():
    print("Let's drive!")
    choice = input(">>> ").upper()
    print(MENU)
    while choice != "Q":
        if choice == "C":
        print("Available taxis: ")
        display_taxis(taxis)
        taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = Taxi[taxi_choice]
            except IndexError:
                print("Invalid option")
        if choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                desired_distance = int(input("How far? "))
                current_taxi.drive(desired_distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost ${trip_cost:.2f}.")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi to travel")
        else:
            print("Invalid option")
        print(f"Your total bill is currently ${total_bill:.2f}.")
        print(MENU)
        choice = input(">>> ").upper()

        print(f"Total bill is: ${total_bill:.2f}")
        print("Taxis are now: ")
        display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis)
        print(f"{i} - {taxi}")

main()
