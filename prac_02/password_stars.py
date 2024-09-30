
length_of_password = 8
password = input("Please enter a password: ")
while len(password) <= length_of_password:
    print("Invalid password!")
    password = input("Please enter a password: ")
print(len(password) * "*")