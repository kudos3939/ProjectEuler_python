#!/usr/bin/python
# coding: utf-8


def q20():
    factorial = 1

    for i in range(100, 0, -1):
        factorial *= i

    print reduce(lambda a, b: int(a) + int(b), str(factorial))


q20()
