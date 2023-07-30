"""
CP1404 Practical 07
project_management.py
Estimated time: 1 hr
Actual time: 25 mins
"""
from prac_07.project import Project

MENU = """
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate new project
(Q)uit 
"""
import datetime
date_string = input("Date (d/m/yyyy: ")
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

def main():
    print(MENU)
    choice = input(">>> ").upper()
    get_project()
    while choice != "Q":
        if choice == "L":
        elif choice == "S":
        elif choice == "D":
        elif choice == "F":
        elif choice == "A":
        elif choice == "U":
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")

def get_project():
    projects = []
    in_file = open("projects.txt, r")
    for line in in_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split()
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        projects.append(parts)
    input_file.close()

main()