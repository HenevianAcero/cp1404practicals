"""
CP1404 Practical 7
myguitars.py
Estimated time: 30 mins
Actual time: 25 mins
"""

from prac_07.guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is: Name,Year,Cost
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        guitars = Guitar(parts)
        # Add the language to the list
        guitars.append(Guitar)
        guitars.sort()
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)


main()


