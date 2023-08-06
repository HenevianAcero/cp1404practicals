"""
CP1404 Practical 09
silver_service_taxi_test.py
Estimated time: 15 mins
Actual time:
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    taxi.get_fare()

main()