#!/usr/bin/python


def q1():
    maximum = 1000
    result = 0
    for x in range(0, maximum):
        if x % 3 == 0 or x % 5 == 0:
            result += x

    print result


q1()
