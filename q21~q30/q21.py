#!/usr/bin/python
# coding: utf-8
from util import find_primes


def q21():
    exception = find_primes(10000)
    total = 0
    for num in range(1, 10000):
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
    result = 0
    for n in range(1, num):
        if num % n is 0:
            result += n
    return result


q21()
