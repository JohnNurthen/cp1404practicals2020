import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 25

def main():
    quick_picks = int(input("How many quick picks would you like?: "))
    while quick_picks <= 0:
        print("Please enter a valid number: ")
        quick_picks = int(input("How many quick picks would you like?: "))
    for i in range(quick_picks):
        numbers = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN,MAX)
            while number in numbers:
                number = random.randint(MIN,MAX)
            numbers.append(number)
        print(numbers)

main()
