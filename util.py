# coding: utf-8
# よく使う関数をモジュールとしてまとめています。
from math import sqrt
from collections import deque


def create_wheel(maximum):
    primes = [2, 3, 5]
    step = [6, 4, 2, 4, 2, 4, 6, 2]

    wheel = []
    a_number = 1
    while a_number < maximum:
        for n in step:
            a_number += n
            if a_number > maximum:
                break
            wheel.append(a_number)
    return primes + wheel


def sieve_prime(*wheel):
    prime_numbers = []
    wheel = deque(wheel)
    while wheel[0] < sqrt(wheel[-1]):
        head = wheel.popleft()
        wheel = deque(filter(lambda p: p % head != 0, wheel))
        prime_numbers.append(head)
    prime_numbers += list(wheel)

    return prime_numbers


def find_primes(maximum):
    wheel = create_wheel(maximum)
    return sieve_prime(*wheel)
