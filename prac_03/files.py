"""
CP1404 - Practical 3
files.py

"""

name = input("Enter name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    print(number1 + number2)

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total = total + number
print(total)
