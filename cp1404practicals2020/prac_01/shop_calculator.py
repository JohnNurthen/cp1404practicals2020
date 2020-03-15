total = 0
number_of_items = int(input("Please enter the number of items: "))

while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Please enter the number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total += price_of_item

if total > 100:
    total = total * 0.9

if number_of_items > 1:
    print("Total price for", number_of_items, "items is $", total, sep=" ")
else:
    print("Total price for 1 item is $", total, sep=" ")