
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("The last number is: {}".format(numbers[-1]))
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))
print("The total of the numbers is: {}".format(sum(numbers)))
print("The number of numbers is: {}".format(len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter your username: ")
if name in usernames:
    print("Access Granted")
else:
    print("Access Denied")