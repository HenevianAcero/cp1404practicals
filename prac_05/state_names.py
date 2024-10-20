"""
CP1404 Practical 5
state_names.py

"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        try:
            print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Short state is invalid")
    state_code = input("Enter short state: ").upper()

