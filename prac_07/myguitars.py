"""
CP1404 Practical 07
myguitars.py
Estimated time: 30 mins
Actual time: 45 mins
"""

from prac_06.guitar import Guitar

def main():
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitars = Guitar(parts[0], parts[1], int(parts[3]))
        guitars.append(guitars)
    add_guitar_details(guitars)
    # Close file as soon as we've finished reading it

    in_file.close()

    # Loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)
        guitar.sort()


def add_guitar_details(guitars):
    guitar_name = input("Enter name of new guitar: ")
    guitar_year = int(input("Enter guitar age: "))
    guitar_cost = input("Enter cost of guitar: ")
    new_guitar = list(guitar_name, guitar_year, guitar_cost)
    guitars.append(new_guitar)


def __lt__(self,other_guitar)
    return self < other_guitar

main()

