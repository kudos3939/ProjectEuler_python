#!/usr/bin/python
# coding: utf-8


def q14():
    known_numbers = {}
    longest_chain = (0, 0)
    for n in range(1, 1000000):
        num = n
        chain = 1
        while n != 1:
            if n in known_numbers:
                chain += known_numbers[n] - 1
                break
            chain += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = n * 3 + 1

        if num not in known_numbers:
            known_numbers[num] = chain
        if chain > longest_chain[1]:
            longest_chain = (num, chain)

    print longest_chain


q14()
