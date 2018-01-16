#!/user/bin/python
# coding: utf-8
from util import find_primes
from math import floor, sqrt


def q23():
    exception = set(find_primes(28123))
    abundant_numbers = []
    for num in range(2, 28123):
        if num in exception:
            continue
        divisors = set()
        for n in range(1, int(floor(sqrt(num) + 1))):
            if num % n == 0:
                divisors.add(n)
        rest_divisors = [num / x for x in divisors]
        for r in rest_divisors:
            if r not in divisors:
                divisors.add(r)
        divisors.remove(num)
        total = sum(divisors)
        if total > num:
            abundant_numbers.append(num)

    numbers = set(range(1, 28124))
    sum_of_a_numbers = set()
    for num in abundant_numbers:
        for ano_num in abundant_numbers:
            temp = num + ano_num
            if temp > 28123:
                break
            if temp not in sum_of_a_numbers:
                sum_of_a_numbers.add(temp)
        abundant_numbers = [n for n in abundant_numbers if not n == num]

    print sum(numbers - sum_of_a_numbers)


q23()
