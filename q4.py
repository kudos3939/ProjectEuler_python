#!/usr/bin/python


def q4():
    palindrome = 0

    for first in range(1, 1000):
        for second in range(1, 1000):
            a_number = first * second
            if is_palindrome(a_number) and a_number > palindrome:
                palindrome = a_number
    print palindrome


def is_palindrome(a_number):
    num_str = str(a_number)
    reversed_num = num_str[::-1]
    if num_str == reversed_num:
        return True
    else:
        return False


q4()
