
total_price = 0

number_of_items = int(input("Enter Number of Items: "))
while number_of_items <= 0:
    print('Invalid number of items!')
    number_of_items = int(input("Enter Number of Items: "))

for i in range(number_of_items):
    price_of_item = float(input("Enter Price of item: $"))
    total_price = total_price + price_of_item

if total_price >= 100:
    total_price = total_price * .9

print('Total price for ', number_of_items, 'items is: $', total_price)
