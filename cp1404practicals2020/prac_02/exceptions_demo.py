"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a letter is a entered for either value.
2. When will a ZeroDivisionError occur?
When the denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Add a while loop that rejects 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Enter a number other than 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")