"""
Program that asks the user for a positive number and then outputs the
approximated square root of the number. Use Newton's method to find the
square root, with epsilon = 0.01. (Epsilon is the allowed error, plus or
minus, when you square your calculated square root and compare it to
your original number.)
"""

rounds = 1
negative = False


def ask_for_number():
    """Asks user for a positive number"""
    number = None
    while True:
        try:
            number = int(input("Please provide a nuumber: "))
            return number
        except:
            print("Silly human, that's not a number, let alone a positive one!")
            pass


def newtons_method(num, guess=None):
    """Calculates the square root of a number."""
    if guess is None:
        guess = 20

    if num < 0:
        global negative
        negative = True
        num = abs(num)

    new_guess = .5*(num/guess+guess)

    if new_guess == guess:
        if negative is True:
            print("The square root of -{} is {}i.".format(num, guess))
        else:
            print("The square root of {} is {}.".format(num, guess))
    else:
        global rounds
        print("Iteration # {}".format(rounds))
        rounds += 1
        newtons_method(num, new_guess)

newtons_method(num=ask_for_number())
