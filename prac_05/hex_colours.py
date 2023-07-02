# hex_colours
# create a dictionary containing the name of colour and its hexadecimal colour code
# print user input (case-independent)

COLOUR_TO_CODE = {"Amethyst": "#9966cc", "GhostWhite": "#f8f8ff", "GOGreen": "#00ab66",
                  "Ginger": "#b06500", "AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a",
                  "BrightLilac": "#d891ef", "BrightUbe": "#d19fe8", "Bronze": "#cd7f32",
                  "Celeste": "#b2ffff"}
print(COLOUR_TO_CODE)


state_colour = input("Enter a colour: ").lower()
while state_colour != "":
    if state_colour in COLOUR_TO_CODE:
        print(f"{COLOUR_TO_CODE.get(state_colour)}")
    else:
        print("Invalid colour")
    state_colour = input("Enter a colour: ").lower()