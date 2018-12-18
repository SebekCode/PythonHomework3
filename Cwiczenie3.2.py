#!/usr/bin/env python3


def enter_a_number():
    number = input("Enter a number: ")
    number = int(number)
    zero_number = 0

    if number:
        print("Your number is {}.".format(number))

    if number is zero_number:
        print("Entered number is zero.")


enter_a_number()
