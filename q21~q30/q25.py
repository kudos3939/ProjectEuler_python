#!/usr/bin/python


def q25():
    index = 2
    one = 1
    two = 1
    num = 0
    while len(str(num)) < 1000:
        num = one + two
        index += 1
        one = two
        two = num

    print(index)

q25()