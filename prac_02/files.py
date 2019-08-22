# Program 1
output_file = open("name.txt", 'w')
name = input('Please enter your name: ')
output_file.write(name)
output_file.close()

# Program 2
input_file = open("name.txt", 'r')
name = input_file.read()
input_file.close()
print('Your name is', name)

# Program 3
input_file = open("numbers.txt", 'r')
number_one = int(input_file.readline())
number_two = int(input_file.readline())
input_file.close()
print(number_one + number_two)

# Program 3 Extension
input_file = open('numbers.txt', 'r')
total = 0
for line in input_file:
    number = int(line)
    total += number
input_file.close()
print(total)
