"""
CP1404 - Practical 1
broken_score.py

Broken program to determine score status
"""

score = float(input("Enter score: "))
if score >= 0 and score <= 100:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
else:
    print("Invalid score")
