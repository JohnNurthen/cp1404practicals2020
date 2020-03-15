OUTPUT_FILE = "name.txt"

user_name = input("Enter your name: ")
out_file = open(OUTPUT_FILE, "w")
out_file.close()
print(user_name, file=out_file)

read_file = open(OUTPUT_FILE, "r")
name = read_file.read().strip()
read_file.close()
print("Your name is {}".format(name))

numbers_file = "numbers.txt"
in_file = open(numbers_file, "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open(numbers_file, "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)


