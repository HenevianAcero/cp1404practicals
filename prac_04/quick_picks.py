import random
numbers_in_line = 6
MIN = 1
MAX = 45

def main():
    num_quick_picks = int(input("How many quick picks? "))
    while num_quick_picks < 0:
        print("Invalid number of quick picks")
        num_quick_picks = int(input("Number of quick picks? "))

    for i in range(num_quick_picks):
        quick_pick = []
        for j in range(numbers_in_line):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()