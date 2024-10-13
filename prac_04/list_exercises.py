"""
CP1404 Practical 4
list_exercises.py

"""
number = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
def get_number():
    for i in range(5):
        value = int(input("Number: "))
        number.append(value)

def check_username(username):
    if username in usernames:
        return "Access granted"
    else:
        return "Access denied"

def main():
    get_number()
    print(f"The first number is {number[0]}.")
    print(f"The last number is {number[-1]}.")
    print(f"The smallest number is {min(number)}.")
    print(f"The largest number is {max(number)}.")
    print(f"The average number is {sum(number)/5}.")
    username = input("Enter username: ")
    print(check_username(username))



main()