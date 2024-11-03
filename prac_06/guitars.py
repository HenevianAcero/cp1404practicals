"""
CP1404 Practical 6
guitars.py
Estimated time: 50 mins
Actual time: 42 mins

"""

from prac_06.guitar import Guitar

def main():
    print("My Guitars!")
    guitars = []
    new_guitar = get_guitar(guitars)
    print(new_guitar)

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        display_guitars(guitars)
    else:
        print("Buy some guitars!")

def get_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        details_to_add = Guitar(name, year,cost)
        guitars.append(details_to_add)
        return f"{details_to_add} added."
        name = input("Name: ")

def display_guitars(guitars):
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "" if guitar.get_age() <= 50 else "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")



main()