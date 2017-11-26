#!/usr/bin/python
# coding: utf-8


def q14():
    longest_chain = []
    for n in range(1, 1000000):
        chain = []
        while n != 1:
            chain.append(n)
            if n % 2 == 0:
                n /= 2
            else:
                n = n * 3 + 1
        chain.append(n)

        if len(chain) > len(longest_chain):
            longest_chain = chain

    print longest_chain


q14()
