#!/usr/bin/env python3
"""
This program checks to see if a users input pin is valid or not
"""


RETURNS = []


def valid_input(userpin, pin):
    """
    Checks if an input PIN Number is valid or invalid
    """
    # Check to see if userpin length is 4 characters long
    if len(userpin) != 4:
        print("Invalid PIN length. Correct format is: <9876>")

    # Check to see if userpin input contains letters
    bad = False
    for num in userpin:
        if num.isdigit() is False:
            bad = True
            break
    if bad:
        print("Invalid PIN character. Correct format is: <9876>")

    # Check to see if userpin is correct or incorrect
    if userpin == pin:
        print("Your PIN is correct")
        return True
    elif userpin != pin:
        print("Your PIN is incorrect")
        return False


def main():
    """
    Test your module
    """
    pin = "1234"
    userpin = input("Please enter your PIN: ")
    returnvalue = valid_input(userpin, pin)
    if returnvalue is False:
        RETURNS.append(False)
        if len(RETURNS) == 3:
            print("Your account is locked")
            exit(1)
        main()


if __name__ == "__main__":
    main()
    exit(0)
