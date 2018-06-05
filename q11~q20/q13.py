#!/usr/bin/python
# coding: utf-8


# コメントは後日〜
def q13():
    f = open("../etc/q13_number", "r")
    numbers = f.read().split()

    result = reduce(lambda a, b: str_sum(a, b), numbers)

    print result[:10]


def one_str_sum(first, second, carry):
    result = int(first) + int(second)
    if carry:
        result += 1
    result = str(result)
    if len(result) == 2:
        return result[1], True
    else:
        return result, False


def str_sum(first, second):
    result = ''
    first = list(first)
    second = list(second)
    carry = False
    while len(first) and len(second) != 0:
        one_str, carry = one_str_sum(first.pop(), second.pop(), carry)
        result = one_str + result

    while len(first) != 0:
        one_str, carry = one_str_sum(first.pop(), '0', carry)
        result = one_str + result
    while len(second) != 0:
        one_str, carry = one_str_sum('0', second.pop(), carry)
        result = one_str + result
    if carry:
        result = '1' + result
    return result


q13()
