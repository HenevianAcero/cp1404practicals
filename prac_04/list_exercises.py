numbers = []
get_number = int(input("Number: "))
numbers.append(get_number)
get_number = int(input("Number: "))
numbers.append(get_number)
get_number = int(input("Number: "))
numbers.append(get_number)
get_number = int(input("Number: "))
numbers.append(get_number)
get_number = int(input("Number: "))
numbers.append(get_number)
average = sum(numbers) / len(numbers)

print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")