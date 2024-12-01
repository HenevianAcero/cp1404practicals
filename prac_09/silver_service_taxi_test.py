"""
CP1404 Practical 9
silver_service_taxi_test.py

"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"${taxi.get_fare()}")  # prints rounded value

main()