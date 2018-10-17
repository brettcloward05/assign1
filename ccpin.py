#!/usr/bin/env python3
"""
This program checks to see if a users pin is valid or not
"""


PIN = "1234"


def valid_input(userpin):
    """
    checks for valid input
    """
    if userpin == PIN:
        print("Your PIN is correct")
        return True

    if len(userpin) != 4:
        print("Invalid PIN length. Correct format is: <9876>")

    bad = False
    for c in userpin:
        if c.isdigit() == False:
            bad = True
            break
    if bad:
        print("Invalid PIN character. Correct format is: <9876>")

def main():
    """
    Test your module
    """
    userpin = input("Please enter your PIN: ")
    r = valid_input(userpin)
    timesincorrect = 0
    if r == False:
        timesincorrect += 1



    #pass


if __name__ == "__main__":
    main()
    exit(0)
