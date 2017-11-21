#!/usr/bin/python
# coding: utf-8
from util import find_primes


def q10():
    prime_numbers = find_primes(2000000)

    print reduce(lambda a, b: a + b, prime_numbers)


q10()
