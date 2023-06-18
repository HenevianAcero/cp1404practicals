
def main():
    '''Returns password as stars while checking that it has more than the minimum number of characters'''
    length_of_password = 8
    password = get_password(length_of_password)
    password_stars(password)


def password_stars(password):
    print(len(password) * "*")


def get_password(length_of_password):
    password = input("Please enter a password: ")
    while len(password) <= length_of_password:
        print("Invalid password!")
        password = input("Please enter a password: ")
    return password


main()