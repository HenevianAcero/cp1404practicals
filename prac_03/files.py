
name = input("Enter name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
content = file.readline()
print(f"Your name is {content}.")

numbers = open("numbers.txt", "r")
values = numbers.readline()
for line in enumerate(values):
    total = int(line)
    print(total)
    numbers.close()

numbers = open("numbers.txt", "r")
values = numbers.readline()
for line in values:
    sum = values.readline[1] + next()
    print(sum)