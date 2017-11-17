#!/usr/bin/python


def q5():
    max_number = 20
    prime_numbers = find_primes(max_number)
    smallest_multiple = 1

    for p in prime_numbers:
        biggest_power = p
        while biggest_power * p < max_number:
            biggest_power *= p
        smallest_multiple *= biggest_power
    print smallest_multiple


def find_primes(max_number):
    prime_numbers = []
    for x in range(2, max_number):
        temp_arary = [x % p for p in prime_numbers]
        if 0 not in temp_arary:
            prime_numbers.append(x)
    return prime_numbers


q5()
