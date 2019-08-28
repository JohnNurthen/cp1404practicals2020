"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    if 100 < score or score < 0:
        return 'Invalid score'
    elif score < 50:
        return 'Bad'
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
