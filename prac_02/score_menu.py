
def main():
    Menu = '''(G)et valid score
     (P)rint result
     (S)how stars
     (Q)uit'''
    print(Menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = random_number()
            print(score)
        elif choice == "P":
            result(score)
        elif choice == "S":
            score_as_stars = stars(score)
            print(score_as_stars)
        print(Menu)
        choice = input(">>> ").upper()
    print("Farewell")


def stars(score):
    score_as_stars = (score * "*")
    return score_as_stars


def result(score):
    if score < 50:
        print("Bad")
    elif score >= 50 and score < 90:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Invalid score")


def random_number():
    import random
    score = random.randint(1, 100)
    return score


main()