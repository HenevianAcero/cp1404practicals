"""
CP1404 - Practical 2
score_menu.py

"""
MENU = """(G)et a valid score - must be 0-100 inclusive
(P)rint result
(S)how stars
(Q)uit"""

def check_valid_score(score):
    if score >= 0 and score <= 100:
        return "valid"
    else:
        return "invalid"

def get_valid_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def convert_valid_score_as_stars(score):
    return score * "*"

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            check_valid_score(score)
            print(f"Score is {check_valid_score(score)}.")
        elif choice == "P":
            get_valid_score_status(score)
            print(get_valid_score_status(score))
        elif choice == "S":
            convert_valid_score_as_stars(score)
            print(convert_valid_score_as_stars(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")

main()