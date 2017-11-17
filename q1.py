#!/usr/bin/python


def q1():
    maximum = 1000
    three_five = []
    for x in range(0, maximum):
        if x % 3 == 0 or x % 5 == 0:
            three_five.append(x)

    sum = 0
    for x in three_five:
        sum += x

    print sum


q1()
