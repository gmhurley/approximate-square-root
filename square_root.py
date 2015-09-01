"""
Program that asks the user for a positive number and then outputs the
approximated square root of the number. Use Newton's method to find the
square root, with epsilon = 0.01. (Epsilon is the allowed error, plus or
minus, when you square your calculated square root and compare it to
your original number.)
"""


def ask_for_number():
    """Asks user for a positive number"""
    number = '0'
    while True:
        number = raw_input("Please provide a positive nuumber: ")
        if number.isdigit() and int(number) > 0:
            return number


def newtons_method(number):
    pass

ask_for_number()
