
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 101, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

n = int(input("Number of stars: "))
star = "*"
i = n * star
print(i)

for i in range(n):
    i = (i + 1) * star
    print(i)