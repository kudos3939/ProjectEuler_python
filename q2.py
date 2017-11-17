#!/usr/local/bin/python


def q2():
    total = 2
    first = 1
    second = 2
    while (first + second) < 4000000:
        temp = first + second
        first = second
        second = temp
        if temp % 2 == 0:
            total += temp
    print total


q2()
