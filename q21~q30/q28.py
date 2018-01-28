#!/usr/local/bin/python3


def q28(limit):
    gap = 2
    total = 1
    num = 1
    while gap < limit:
        for n in range(4):
            num += gap
            total += num
        gap += 2
    print(total)


q28(1001)
