#!/usr/bin/env python3
"""
This program checks to see if a users input pin is valid or not
"""


def valid_input(userpin):
    """
    Checks if an input PIN Number is valid or invalid
    Args:
        userpin: the userpin the user enters
    Returns:
        False or True depending on the userpin
    """
    pin = "1234"

    if userpin == pin:
        print("Your PIN is correct")
        return True
    elif len(userpin) != 4:
        print("Invalid PIN length. Correct format is: <9876>")
        return False
    elif userpin.isdigit() is False:
        print("Invalid PIN character. Correct format is: <9876>")
        return False
    elif userpin != pin:
        print("Your PIN is incorrect")
        return False


def main():
    """
    Tests the module
    Checks invalid input up to 3 times
    """
    for i in range(3):
        i += 1
        userpin = input("Please enter your PIN: ")
        returnvalue = valid_input(userpin)
        if returnvalue is True:
            exit(0)
        if i == 3:
            print("Your bank card is blocked")
            exit(2)


if __name__ == "__main__":
    main()
    exit(0)
