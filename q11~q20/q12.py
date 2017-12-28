#!/usr/bin/python
# coding: utf-8
from math import floor, sqrt


# コメントは後日
def q12():
    a_num = 0
    counter = 1

    while True:
        divisors = []
        a_num += counter
        for n in range(1, int(floor(sqrt(a_num) + 1))):
            if a_num % n == 0:
                divisors.append(n)
        rest_divisors = [a_num / x for x in divisors]
        for r in rest_divisors:
            if r not in divisors:
                divisors.append(r)
        if len(divisors) > 500:
            break
        counter += 1

    print a_num


q12()
