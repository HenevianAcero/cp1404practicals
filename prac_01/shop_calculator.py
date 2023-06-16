
discount_rate = 0.1
total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: $"))
    total = total + price
if total >= 100:
    total = total - (total * discount_rate)
print(f"Total price of {number_of_items} items is ${total: .2f}")
