"""
CP1404 Practical 5
hex_colours.py

"""

COLOUR_TO_CODE = {"amber": "#ffbf00", "amethyst": "#9966cc", "baby pink": "#f4c2c2", "blue bell": "#a2a2d0",
                  "canary": "#ffff99", "cardinal": "#c41e3a", "dandelion": "#f0e130", "dutch white": "#efdfbb",
                  "ebony": "#555d50", "emerald": "#50c878"}
print(COLOUR_TO_CODE)

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(f"The hexadecimal code for {colour_name} is {COLOUR_TO_CODE.get(colour_name)}")
    else:
        print("Invalid color name")
    colour_name = input("Enter colour name: ")
