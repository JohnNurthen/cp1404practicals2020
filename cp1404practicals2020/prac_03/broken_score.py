"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(calculate_mark(score))
    score = random.randint(0, 101)
    print(score)
    print(calculate_mark(score))


def calculate_mark(score):
    if 100 < score or score < 0:
        return"Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()