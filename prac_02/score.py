"""
CP1404 - Practical 2
score.py

"""
import random


def main():
    score = float(input("Enter score: "))
    get_score_status(score)
    print(get_score_status(score))
    score = random.randint(1, 100)
    print(score)
    print(get_score_status(score))

def get_score_status(score):
    if score >= 0 and score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score"

main()
