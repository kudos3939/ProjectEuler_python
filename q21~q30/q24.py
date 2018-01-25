#!/usr/bin/python
# coding: utf-8
import math


def q24():
    index = 999999
    pool = list(range(10))
    digit = []

    reminder = (-1, index)
    while len(pool) is not 0:
        for n in range(len(pool)):
            temp = index - n * math.factorial(len(pool)-1)
            if reminder[1] >= temp >= 0:
                reminder = (pool[n], temp)
            elif temp < 0:
                break
        index = reminder[1]
        pool = [x for x in pool if x != reminder[0] in pool]
        digit.append(reminder[0])

    print(digit)

q24()
