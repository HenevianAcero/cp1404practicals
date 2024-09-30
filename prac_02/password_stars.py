
def main():
    length_of_password = 8
    password = get_password()
    while len(password) <= length_of_password:
        print("Invalid password!")
        password = input("Please enter a password: ")
    print_password(password)


def print_password(password):
    print(len(password) * "*")


def get_password():
    password = input("Please enter a password: ")
    return password


main()
