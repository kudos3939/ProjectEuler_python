#!/usr/bin/python
# coding: utf-8
from util import find_primes
from math import floor, sqrt


def q21():
    exception = find_primes(10000)
    total = 0
    for num in range(2, 10000):
        if num in exception:
            continue
        ano_num = sum_of_proper_divisor(num)
        if sum_of_proper_divisor(ano_num) == num:
            if ano_num == num:
                continue
            total += num + ano_num
            exception.append(ano_num)
    print total


def sum_of_proper_divisor(num):
    divisors = set()
    for n in range(1, int(floor(sqrt(num) + 1))):
        if num % n == 0:
            divisors.add(n)
    rest_divisors = [num / x for x in divisors]
    for r in rest_divisors:
        if r not in divisors:
            divisors.add(r)
    divisors.remove(num)
    return sum(divisors)


q21()
