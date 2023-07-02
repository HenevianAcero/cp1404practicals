
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    categorise_result(score)
    import random
    score = random.randint(1,100)
    print(score)
    categorise_result(score)


def categorise_result(score):
    if score >= 0 and score <= 100:
        if score < 50:
            print("Bad")
        elif score >= 50 and score < 90:
            print("Passable")
        elif score >= 90:
            print("Excellent")
    else:
        print("Invalid score")


main()