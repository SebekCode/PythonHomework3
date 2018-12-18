#!/usr/bin/env python3


def enter_a_name():
    user_name = input("Please enter your name: ")
    my_name = "Sebastian"

    if user_name == my_name:
        print("Hello {}! Your name is same as mine.".format(user_name))
    else:
        print("Hello {}! You're welcome.".format(user_name))


enter_a_name()
