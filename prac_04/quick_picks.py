"""
CP1404 - Practical 4
quick_picks.py

"""
import random
QUICK_PICKS_PER_LINE = 6
MIN = 1
MAX = 45

def main():
    number_of_lines = int(input("Number of quick picks: "))
    while number_of_lines < 0:
        print("Invalid number. Try Again")
        number_of_lines = int(input("Number of quick picks: "))

    for i in range(number_of_lines):
        quick_pick = []
        for j in range(QUICK_PICKS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()
