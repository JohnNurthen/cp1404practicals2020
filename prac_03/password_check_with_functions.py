'''John Nurthen'''
MIN_LENGTH = 3


def main():
    password = get_password()
    print_password_as_stars(password)


def get_password():
    password = input('Please enter your Password: ')
    while len(password) < MIN_LENGTH:
        print('Password must be between 3 and 10 characters')
        password = input('Please enter a valid Password: ')
    return password


def print_password_as_stars(password):
    print('*' * len(password))


main()
